# Contact Website

A simple Python + Flask website for a portfolio or personal business page with a contact form.

## Run it locally

1. Open a terminal in this folder.
2. Create a virtual environment if you want:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   python app.py
   ```
5. Open your browser to:
   ```text
   http://127.0.0.1:5000
   ```

## Email sending

The contact form works even without email setup. It saves the message in the terminal output and shows a success message.

To enable real email delivery, set these environment variables before running the app:

```bash
set SMTP_HOST=smtp.gmail.com
set SMTP_PORT=587
set SMTP_USER=your_email@gmail.com
set SMTP_PASSWORD=your_google_app_password
set CONTACT_EMAIL=your_business_email@example.com
set SECRET_KEY=your_secret_key
```

Notes:
- For Gmail, use a Google App Password, not your normal Gmail password.
- `SMTP_USER` should be the Gmail address that is sending the message.
- `CONTACT_EMAIL` is the inbox where the new messages should be received.

Then run the app again.

## Deploy to Render

1. Create a GitHub repository for this project.
2. Push these files to GitHub:
   - `app.py`
   - `requirements.txt`
   - `templates/`
   - `static/`
   - `.gitignore`
   - `Procfile`
   - `render.yaml`
   - `runtime.txt`
3. Go to https://render.com and sign in.
4. Click New -> Web Service.
5. Connect your GitHub repository.
6. Choose the repository and keep the default settings.
7. Render will run:
   ```bash
   pip install -r requirements.txt
   gunicorn app:app
   ```
8. Your site will get a public Render URL.
9. Add your environment variables in Render:
   ```bash
   SECRET_KEY=your_secret_key
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your_email@gmail.com
   SMTP_PASSWORD=your_google_app_password
   CONTACT_EMAIL=your_email@gmail.com
   ```
10. Save and deploy.

## Customize it

Edit the text in `templates/index.html` and change the brand name, email, phone, and services to match your business.
