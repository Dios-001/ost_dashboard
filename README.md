# System Health Logger and Auto-Report Suite

This project monitors CPU, memory, disk, and network usage periodically, logs data, generates visual reports, and sends alerts when thresholds are exceeded.

## How to Run
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

### Contributors
- Abhishek Patawari
- Otniel Jhirad
- Dev Suresh Kartik
- Deepti Emmi
- Akshit Mathur
