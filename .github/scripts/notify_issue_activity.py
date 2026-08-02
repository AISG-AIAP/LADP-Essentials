#!/usr/bin/env python3
"""Email the team about issue activity (opened / reopened / commented).

Driven by a GitHub Actions `issues` / `issue_comment` event. The event
payload fields are passed in as environment variables (never interpolated
into the shell command, to avoid script injection from issue/comment text):

    EVENT_KIND     opened | reopened | commented   (required)
    ISSUE_NUMBER   issue number
    ISSUE_TITLE    issue title
    ISSUE_URL      link to the issue or the specific comment
    ACTOR          github login of whoever triggered the event
    CONTENT_BODY   the issue body (opened/reopened) or comment text (commented)
    REPO           "owner/name", used in the subject/body

Also reads the SMTP_* / MAIL_* config used by _mailer.send_email().
"""

import html
import os
import sys

from _mailer import send_email, require_env

VERBS = {
    "opened": "opened a new issue",
    "reopened": "reopened an issue",
    "commented": "commented on an issue",
}


def build_message(kind, number, title, url, actor, repo, body):
    verb = VERBS[kind]
    subject = f"[{repo}] Issue #{number} {kind}: {title}"

    text_lines = [
        f"{actor} {verb} in {repo}.",
        "",
        f"Issue #{number}: {title}",
        f"Link: {url}",
    ]
    if body:
        text_lines += ["", "----------", body]
    text_lines += ["", "— Automated notification from the LADP-Essentials issue watcher."]
    text_body = "\n".join(text_lines)

    body_html = ""
    if body:
        # Escape user-supplied text and keep line breaks readable in HTML.
        body_html = (
            "<hr><p style='white-space:pre-wrap'>"
            f"{html.escape(body)}</p>"
        )
    html_body = (
        f"<p><strong>{html.escape(actor)}</strong> {verb} in {html.escape(repo)}.</p>"
        f"<p><strong>Issue #{number}:</strong> {html.escape(title)}<br>"
        f"<a href=\"{html.escape(url)}\">{html.escape(url)}</a></p>"
        f"{body_html}"
        "<p style='color:#888'>— Automated notification from the "
        "LADP-Essentials issue watcher.</p>"
    )
    return subject, text_body, html_body


def main():
    kind = require_env("EVENT_KIND")
    if kind not in VERBS:
        sys.exit(f"ERROR: unknown EVENT_KIND '{kind}' (expected one of {list(VERBS)}).")

    number = os.environ.get("ISSUE_NUMBER", "?")
    title = os.environ.get("ISSUE_TITLE", "(no title)")
    url = os.environ.get("ISSUE_URL", "")
    actor = os.environ.get("ACTOR", "someone")
    repo = os.environ.get("REPO", "LADP-Essentials")
    body = (os.environ.get("CONTENT_BODY") or "").strip()

    subject, text_body, html_body = build_message(
        kind, number, title, url, actor, repo, body
    )
    mail_to = send_email(subject, text_body, html_body)
    print(f"Sent issue notification (#{number}, {kind}) to {mail_to}.")


if __name__ == "__main__":
    main()
