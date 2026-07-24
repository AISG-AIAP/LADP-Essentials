#!/usr/bin/env python3
"""Email a summary of outstanding (open) pull requests.

Reads a JSON file produced by:
    gh pr list --state open --json number,title,author,createdAt,url

If there are no open PRs, prints a message and exits 0 without sending.
Otherwise sends a plain-text + HTML summary email via SMTP (Gmail by default).

Configuration comes from environment variables:
    SMTP_USERNAME   (required)  sending account, also used as the From address
    SMTP_PASSWORD   (required)  app password for that account
    SMTP_HOST       (optional)  default: smtp.gmail.com
    SMTP_PORT       (optional)  default: 587 (STARTTLS)
    MAIL_TO         (optional)  default: ladp-team@aisingapore.org
    MAIL_FROM       (optional)  default: SMTP_USERNAME
    REPO            (optional)  "owner/name", used only in the subject/body
"""

import json
import os
import smtplib
import sys
from datetime import datetime, timezone
from email.message import EmailMessage
from email.utils import formataddr, formatdate


def load_prs(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list in {path}, got {type(data).__name__}")
    return data


def days_open(created_at):
    """Whole days since the PR was opened. Returns None if unparseable."""
    if not created_at:
        return None
    try:
        # gh emits RFC3339 like 2026-07-24T02:15:30Z
        created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    except ValueError:
        return None
    return max(0, (datetime.now(timezone.utc) - created).days)


def author_login(pr):
    author = pr.get("author") or {}
    if isinstance(author, dict):
        return author.get("login") or author.get("name") or "unknown"
    return str(author)


def format_age(n):
    if n is None:
        return "age unknown"
    if n == 0:
        return "opened today"
    if n == 1:
        return "opened 1 day ago"
    return f"opened {n} days ago"


def build_bodies(prs, repo):
    where = f" in {repo}" if repo else ""
    header = f"{len(prs)} outstanding pull request(s){where}:"

    text_lines = [header, ""]
    html_items = []
    for pr in prs:
        num = pr.get("number", "?")
        title = pr.get("title", "(no title)")
        author = author_login(pr)
        age = format_age(days_open(pr.get("createdAt")))
        url = pr.get("url", "")
        text_lines.append(f"  #{num} — {title} (by {author}, {age})")
        text_lines.append(f"      {url}")
        html_items.append(
            "<li><strong>#{num}</strong> — {title}<br>"
            "<small>by {author}, {age}</small><br>"
            '<a href="{url}">{url}</a></li>'.format(
                num=num, title=title, author=author, age=age, url=url
            )
        )
    text_lines += ["", "— Automated notification from the LADP-Essentials PR watcher."]

    text_body = "\n".join(text_lines)
    html_body = (
        f"<p>{header}</p><ul>{''.join(html_items)}</ul>"
        "<p style='color:#888'>— Automated notification from the "
        "LADP-Essentials PR watcher.</p>"
    )
    return text_body, html_body


def require_env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(f"ERROR: required environment variable {name} is not set.")
    return value


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: notify_open_prs.py <prs.json>")

    prs = load_prs(sys.argv[1])
    if not prs:
        print("No open PRs — nothing to send.")
        return

    repo = os.environ.get("REPO", "")
    username = require_env("SMTP_USERNAME")
    password = require_env("SMTP_PASSWORD")
    host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("SMTP_PORT", "587"))
    mail_to = os.environ.get("MAIL_TO", "ladp-team@aisingapore.org")
    mail_from = os.environ.get("MAIL_FROM", username)

    text_body, html_body = build_bodies(prs, repo)

    msg = EmailMessage()
    subject_repo = repo or "LADP-Essentials"
    msg["Subject"] = f"[{subject_repo}] {len(prs)} outstanding pull request(s)"
    msg["From"] = formataddr(("LADP-Essentials PR watcher", mail_from))
    msg["To"] = mail_to
    msg["Date"] = formatdate(localtime=False)
    msg.set_content(text_body)
    msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP(host, port, timeout=30) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

    print(f"Sent notification for {len(prs)} open PR(s) to {mail_to}.")


if __name__ == "__main__":
    main()
