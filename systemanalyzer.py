import pandas as pd
import matplotlib.pyplot as plt

# Read log file
data = []
with open("logs/health_log.txt") as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 4:
            cpu = float(parts[1].split('=')[1])
            mem = float(parts[2].split('=')[1])
            disk = float(parts[3].split('=')[1])
            data.append([cpu, mem, disk])

df = pd.DataFrame(data, columns=["CPU", "Memory", "Disk"])

# Compute summary
avg_cpu = df["CPU"].mean()
peak_cpu = df["CPU"].max()
avg_mem = df["Memory"].mean()
peak_disk = df["Disk"].max()

print("===== SYSTEM HEALTH SUMMARY =====")
print(f"Average CPU Usage  : {avg_cpu:.2f}%")
print(f"Peak CPU Usage     : {peak_cpu:.2f}%")
print(f"Average Memory Use : {avg_mem:.2f}%")
print(f"Peak Disk Usage    : {peak_disk:.2f}%")

