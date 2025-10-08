import psutil, datetime, json, os

config = json.load(open("config.json"))
log_file = config["log_file"]

os.makedirs("logs", exist_ok=True)

now = datetime.datetime.now()
cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

with open(log_file, "a") as f:
    f.write(f"{now}, CPU={cpu}, MEM={mem}, DISK={disk}, NET={net}\n")
