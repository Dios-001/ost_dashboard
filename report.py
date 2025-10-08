from jinja2 import Template
import datetime, os

template_html = """
<html><head><title>System Report</title></head>
<body>
<h2>System Health Report - {{ date }}</h2>
<img src='usage_plot.png' width='600'><br>
<p>Latest Log Entries:</p>
<pre>{{ logs }}</pre>
</body></html>
"""

with open("logs/health_log.txt") as f:
    logs = ''.join(f.readlines()[-5:])

html = Template(template_html).render(date=datetime.datetime.now(), logs=logs)

os.makedirs("reports", exist_ok=True)
with open("reports/report.html", "w") as f:
    f.write(html)
