import psutil, smtplib, json

config = json.load(open("config.json"))
cpu_limit = config["cpu_limit"]

cpu = psutil.cpu_percent(interval=1)
if cpu > cpu_limit:
    message = f"Subject: ⚠️ High CPU Alert!\n\nCPU usage = {cpu}% exceeded limit {cpu_limit}%"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(config["email_user"], config["email_pass"])
        server.sendmail(config["email_user"], config["email_to"], message)

