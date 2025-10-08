import pandas as pd
import matplotlib.pyplot as plt
import os

# Make sure logs folder exists
os.makedirs("logs", exist_ok=True)

# Read log file
data = []
try:
    with open("logs/health_log.txt") as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 4:
                cpu = float(parts[1].split('=')[1])
                mem = float(parts[2].split('=')[1])
                disk = float(parts[3].split('=')[1])
                data.append([cpu, mem, disk])
except FileNotFoundError:
    print(" No log file found at logs/health_log.txt")
    exit()

if not data:
    print(" No valid data found in log file.")
    exit()

df = pd.DataFrame(data, columns=["CPU", "Memory", "Disk"])

# Compute summary
avg_cpu = df["CPU"].mean()
peak_cpu = df["CPU"].max()
avg_mem = df["Memory"].mean()
peak_disk = df["Disk"].max()

summary = (
    "===== SYSTEM HEALTH SUMMARY =====\n"
    f"Average CPU Usage  : {avg_cpu:.2f}%\n"
    f"Peak CPU Usage     : {peak_cpu:.2f}%\n"
    f"Average Memory Use : {avg_mem:.2f}%\n"
    f"Peak Disk Usage    : {peak_disk:.2f}%\n"
)

# Print on screen
print(summary)

# Save to summary.txt
with open("logs/summary.txt", "w") as out:
    out.write(summary)

print(" Summary exported to logs/summary.txt")
