import smtplib
from flask import Flask, render_template, request
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/portfolio/')
def about():
    return render_template('portfolio.html')


@app.route('/')
def load_index():
    return render_template('index.html')


@app.route('/send-email/', methods=["POST", "GET"])
def send_email():

    try:
        subject = request.form['Subject']
        email = request.form['email']
        message = MIMEText(request.form['message'])
        message['Subject'] = subject
        message['From'] = email
        message['To'] = email

        server = smtplib.SMTP('smtp.gmail.com', 465)
        sender_email = email
        receiver_email = "dalevdw3011@gmail.com"
        password = "dale30112000"

        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        return "Something wrong happened: " + e
    return render_template('email-success.html')


if __name__ == '__main__':
    app.run(debug=True)
