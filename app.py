from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rohan Gunaga | DevOps Portfolio</title>
    <style>
        :root { --primary: #00ff88; --bg: #0f172a; --card: #1e293b; --text: #f8fafc; }
        body { font-family: 'Inter', sans-serif; background-color: var(--bg); color: var(--text); margin: 0; padding: 20px; line-height: 1.6; }
        .container { max-width: 800px; margin: auto; }
        header { text-align: center; padding: 50px 0; border-bottom: 1px solid #334155; }
        h1 { font-size: 2.5rem; color: var(--primary); margin-bottom: 10px; }
        .badge { background: #064e3b; color: var(--primary); padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; border: 1px solid var(--primary); }
        
        .section { margin: 40px 0; }
        .project-card { background: var(--card); padding: 20px; border-radius: 12px; border-left: 4px solid var(--primary); margin-bottom: 20px; transition: transform 0.2s; }
        .project-card:hover { transform: translateY(-5px); }
        .project-title { font-weight: bold; font-size: 1.2rem; color: var(--primary); }
        .tech-stack { font-family: monospace; font-size: 0.85rem; color: #94a3b8; margin-top: 10px; }
        
        footer { text-align: center; font-size: 0.8rem; color: #64748b; margin-top: 50px; padding: 20px; }
        .status-dot { height: 10px; width: 10px; background-color: var(--primary); border-radius: 50%; display: inline-block; margin-right: 5px; box-shadow: 0 0 8px var(--primary); }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Rohan Gunaga</h1>
            <p>Computer Science & Design Student @ Canara Engineering College</p>
            <span class="badge">6th Semester</span>
            <p><span class="status-dot"></span> System Status: <strong>Live on Cloud</strong></p>
        </header>

        <div class="section">
            <h2>🚀 Featured Projects</h2>
            
            <div class="project-card">
                <div class="project-title">Green Cloud Autonomous (Aura)</div>
                <p>AI-integrated cloud infrastructure project focused on maximizing energy efficiency and sustainable computing.</p>
                <div class="tech-stack">Stack: Python, AI/ML, Cloud Architecture</div>
            </div>

            <div class="project-card">
                <div class="project-title">Cybersecurity: Cowrie Honeypot</div>
                <p>Configured and deployed a honeypot system on Kali Linux to monitor and analyze brute-force attacks in real-time.</p>
                <div class="tech-stack">Stack: Kali Linux, Cowrie, Network Security</div>
            </div>

            <div class="project-card">
                <div class="project-title">Automated DevOps Pipeline</div>
                <p>This portfolio itself! Fully containerized and deployed using a CI/CD pipeline.</p>
                <div class="tech-stack">Stack: Docker, Flask, GitHub Actions, Render</div>
            </div>
        </div>

        <div class="section">
            <h2>🛠️ Technical Skills</h2>
            <p><strong>DevOps:</strong> Docker, CI/CD (GitHub Actions), Linux Administration</p>
            <p><strong>Development:</strong> MERN Stack, Python (Flask), Java, C</p>
        </div>

        <footer>
            <p>Ankola, Karnataka | 2023 - 2027</p>
            <p>Built with ❤️ and Automation</p>
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)