from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Azmeera sai teja"  
    username = os.getenv("USER", "codespace")
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    top_output = subprocess.getoutput("top -b -n 1 | head -15")

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
