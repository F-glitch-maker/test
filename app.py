from __future__ import annotations

import os
from email.message import EmailMessage
from smtplib import SMTP

from flask import Flask, flash, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = os.environ.get("SECRET_KEY", "my-secret-key-change-this")

CONTACT_MESSAGES: list[dict[str, str]] = []


def send_email_notification(data: dict[str, str]) -> None:
    smtp_host = os.environ.get("SMTP_HOST")
    smtp_user = os.environ.get("SMTP_USER")
    smtp_password = os.environ.get("SMTP_PASSWORD")
    recipient = os.environ.get("CONTACT_EMAIL", "you@example.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))

    if not smtp_host or not smtp_user or not smtp_password:
        print("Email sending skipped: SMTP settings not configured.")
        return

    message = EmailMessage()
    message["Subject"] = f"New message from {data['name']}"
    message["From"] = smtp_user
    message["To"] = recipient
    message["Reply-To"] = data["email"]
    message.set_content(
        f"Name: {data['name']}\n"
        f"Email: {data['email']}\n"
        f"Phone: {data['phone'] or 'Not provided'}\n\n"
        f"Message:\n{data['message']}"
    )

    with SMTP(smtp_host, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_user, smtp_password)
        smtp.send_message(message)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in your name, email, and message.", "error")
            return render_template("index.html")

        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "message": message,
        }

        CONTACT_MESSAGES.append(data)
        send_email_notification(data)

        print(f"New contact received: {data}")
        flash("Thanks for your message. I will get back to you soon!", "success")

    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(debug=False, host="0.0.0.0", port=port)
