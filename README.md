# System Health Logger and Alert Automation Suite

A project that monitors system performance, automates alerts, visualizes data, and generates analytics — built using **Shell scripting**, **Python**, and **cron automation**.


> **Goal:** To design an end-to-end automated system that logs CPU, memory, and disk usage, sends alert notifications when thresholds are crossed, and provides real-time analytics and visualizations — all while demonstrating GitHub collaboration and scripting proficiency.


## Introduction

This project integrates multiple scripts working together:
- **monitor.sh** → Orchestrates execution and scheduling
- **logger.py** → Collects and logs system performance metrics
- **alert.py** → Sends email alerts when thresholds exceed limits
- **visualize.py** → Plots CPU, memory, and disk usage over time
- **analyzer.py** → Summarizes system health with performance statistics

All scripts are modular, easy to integrate, and run automatically using a cron job.



## Tech Stack

| Component    | Technology                         |
|--------------|-------------------------------------|
| Languages    | Python, Bash                        |
| Libraries    | `psutil`, `matplotlib`, `pandas`    |
| Automation   | Cron jobs                           |
| Platform     | Linux / Ubuntu                      |
| Collaboration| GitHub (branches, PRs, issues)      |


## Folder Structure

```
system-health-logger/
├── monitor.sh
├── logger.py
├── alert.py
├── visualize.py
├── analyzer.py
├── config.json
├── logs/
│   ├── health_log.txt
│   ├── summary.txt
│   └── usage_plot.png
├── README.md
└── .gitignore
```





##  Key Features

- **End-to-End Automation:** Fully scheduled execution through cron jobs.  
- **Email Alerting:** Real-time notifications for CPU spikes.  
- **Data Visualization:** Graphical representation of CPU, Memory, and Disk trends.  
- **System Analytics:** Generates average, peak, and health status summaries.  
 

##  Contributors

| Name | PRN | Role | GitHub | PRs |
|------|-----|------|--------|-----|
| **Abhishek Patawari** | 23070123006 | Shell Automation & Integration | [github.com/abhishekpatawari](https://github.com/abhishekpatawari) | #11, #12 |
| **Deepti Emmi** | 23070123024 | Logging Module & File Handling | [github.com/DeeptiEmmi](https://github.com/DeeptiEmmi) | #9, #16 |
| **Akshit Mathur** | 23070123048 | Alert System & Configuration | [github.com/AkshitMathur](https://github.com/AkshitMathur) | #10 |
| **Otniel Jhirad** | 23070123059 | Data Visualization & Testing | [github.com/0tniel](https://github.com/0tniel) | #8 |
| **Devkarthik Suresh** | 230701230XX | System Analyzer & Performance Summary | [github.com/DevkarthikSuresh](https://github.com/DevkarthikSuresh) | #19 #20 |



## Project Tracking

The entire project was completed through synchronized teamwork and continuous GitHub activity.  
Each member worked on an assigned branch, raised issues, committed code with descriptive messages, and merged through peer-reviewed pull requests.  



## Usage Instructions

### How to Run
```bash
chmod +x monitor.sh cleanup.sh
./monitor.sh
```

### Cron Setup
```bash
crontab -e
*/10 * * * * /home/$USER/system-health-logger/monitor.sh
```

### Git Commands Used
```bash
git init
git add .
git commit -m "initial commit"
git push origin main
```
## Sample Outputs

- **health_log.txt** — Raw data logs (timestamp, CPU, memory, disk usage)
- **summary.txt** — Health summary report (average/peak usage, status verdict)
- **usage_plot.png** — Graph showing trends over time

## Summary

This project showcases how scripting, monitoring, automation, and collaboration can come together to form a reliable and useful system performance tool. The modular approach, real-time analytics, and end-to-end automation make it suitable for both personal use and small-scale production systems.
