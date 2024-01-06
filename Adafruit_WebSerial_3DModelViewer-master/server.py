from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ws():
    return render_template('index.html')

app.run('0.0.0.0', 8080)