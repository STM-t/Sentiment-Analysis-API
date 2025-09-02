from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', 
                         message='Привет от Flask на Railway!',
                         environment=os.environ.get('ENVIRONMENT', 'development')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/status')
def status():
    return {
        'status': 'ok',
        'service': 'Flask App',
        'deployed': True,
        'environment': os.environ.get('ENVIRONMENT', 'development')
    }

if __name__ == '__main__':


