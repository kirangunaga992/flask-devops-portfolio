from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Points to the new HTML file in the /templates folder
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is a simple check to practice handling 'POST' requests
        username = request.form.get('username')
        return f"<h1>Security Alert:</h1><p>Attempted login for user: {username}</p>"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)