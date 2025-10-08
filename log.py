import psutil, datetime, json, os

config = json.load(open("config.json"))
log_file = config["log_file"]

if not os.path.exists("logs"):
    os.makedirs("logs")

now = datetime.datetime.now()
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

with open(log_file, "a") as f:
    f.write(f"{now}, CPU={cpu}, MEM={mem}, DISK={disk}\n")
