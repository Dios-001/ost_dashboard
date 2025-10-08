# 🖥️ System Health Logger

A simple Python script to **log system resource usage** (CPU, Memory, Disk) at regular intervals. This tool is useful for monitoring performance and serves as a base for further automation or alert systems.

---

## 📌 Features
- Logs CPU, memory, and disk usage
- Auto-creates `logs/` directory if not present
- Uses configurable file paths via `config.json`
- Timestamped entries for easy tracking

---

## 🛠️ Requirements
- Python 3.8+
- Install dependencies:
```bash
pip install psutil
