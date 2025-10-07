<!DOCTYPE html>
<html>
<head>
    <title>System Health Visualization</title>
</head>
<body>
    <h1>🖥️ System Health Visualization 📊</h1>
    <p>Visualize your CPU, Memory, and Disk usage over time!</p>

    <h2>Features ✨</h2>
    <ul>
        <li>📂 Reads from <code>logs/health_log.txt</code></li>
        <li>📈 Plots CPU, Memory & Disk usage</li>
        <li>💾 Saves plot as <code>logs/usage_plot.png</code></li>
    </ul>

    <h2>Log Format 📝</h2>
    <pre>
timestamp,cpu=XX,mem=XX,disk=XX
    </pre>
    <p>Example:</p>
    <pre>
2025-10-07 10:00:00,cpu=25,mem=45,disk=60
    </pre>

    <h2>How to Run ▶️</h2>
    <ol>
        <li>Install matplotlib:
            <pre>pip install matplotlib</pre>
        </li>
        <li>Place your log file in <code>logs/health_log.txt</code></li>
        <li>Run the script:
            <pre>python your_script_name.py</pre>
        </li>
        <li>View your graph in <code>logs/usage_plot.png</code> 📊</li>
    </ol>

    <h2>License 🛡️</h2>
    <p>Open-source and free to use!</p>
</body>
</html>
