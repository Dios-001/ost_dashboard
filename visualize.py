import matplotlib.pyplot as plt

times, cpu, mem, disk = [], [], [], []

with open("logs/health_log.txt") as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) < 4:
            continue
        times.append(parts[0])
        cpu.append(float(parts[1].split('=')[1]))
        mem.append(float(parts[2].split('=')[1]))
        disk.append(float(parts[3].split('=')[1]))

plt.figure(figsize=(10,5))
plt.plot(cpu, label="CPU %")
plt.plot(mem, label="Memory %")
plt.plot(disk, label="Disk %")
plt.legend()
plt.title("System Health Trends")
plt.savefig("reports/usage_plot.png")
