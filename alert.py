import psutil, smtplib, json

config = json.load(open("config.json"))
cpu_limit = config["cpu_limit"]
email_user, email_pass, email_to = config["email_user"], config["email_pass"], config["email_to"]

cpu = psutil.cpu_percent(interval=1)

if cpu > cpu_limit:
    msg = f"Subject: ⚠️ CPU Alert\n\nCPU usage = {cpu}% exceeded limit of {cpu_limit}%"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_user, email_pass)
        server.sendmail(email_user, email_to, msg)
