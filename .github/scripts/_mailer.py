"""Shared SMTP email sender for the repo notification workflows.

Both notify_open_prs.py and notify_issue_activity.py use send_email().

Configuration comes from environment variables:
    SMTP_USERNAME   (required)  sending account, also the default From address
    SMTP_PASSWORD   (required)  app password for that account
    SMTP_HOST       (optional)  default: smtp.gmail.com
    SMTP_PORT       (optional)  default: 587 (STARTTLS)
    MAIL_TO         (optional)  default: ladp-team@aisingapore.org
    MAIL_FROM       (optional)  default: SMTP_USERNAME
"""

import os
import smtplib
import sys
from email.message import EmailMessage
from email.utils import formataddr, formatdate


def require_env(name):
    value = os.environ.get(name)
    if not value:
        sys.exit(f"ERROR: required environment variable {name} is not set.")
    return value


def send_email(subject, text_body, html_body=None):
    """Send an email via SMTP. Returns the recipient address on success."""
    username = require_env("SMTP_USERNAME")
    password = require_env("SMTP_PASSWORD")
    host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("SMTP_PORT", "587"))
    mail_to = os.environ.get("MAIL_TO", "ladp-team@aisingapore.org")
    mail_from = os.environ.get("MAIL_FROM", username)

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("LADP-Essentials notifier", mail_from))
    msg["To"] = mail_to
    msg["Date"] = formatdate(localtime=False)
    msg.set_content(text_body)
    if html_body:
        msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP(host, port, timeout=30) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

    return mail_to
