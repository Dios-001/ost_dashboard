import matplotlib.pyplot as plt
from datetime import datetime

times, cpu, mem, disk = [], [], [], []

with open("logs/health_log.txt") as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 4:
            time_str = parts[0]
            try:
                time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                times.append(time_obj)
                cpu.append(float(parts[1].split('=')[1]))
                mem.append(float(parts[2].split('=')[1]))
                disk.append(float(parts[3].split('=')[1]))
            except:
                continue

plt.figure(figsize=(10, 5))
plt.plot(times, cpu, label='CPU (%)')
plt.plot(times, mem, label='Memory (%)')
plt.plot(times, disk, label='Disk (%)')

plt.xlabel('Time')
plt.ylabel('Usage (%)')
plt.title('System Health Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("logs/usage_plot.png")
print("✅ Graph saved as logs/usage_plot.png")
