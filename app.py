from flask import Flask, render_template
import os
from waitress import serve

app = Flask(__name__)

# Serve the index.html when the root URL is accessed
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # This block will only be executed if you run the script locally, and not in production
    if os.environ.get('FLASK_ENV') == 'production':
        # Use Waitress to serve the app in production
        serve(app, host='0.0.0.0', port=5000)
    else:
        # Only use Flask's built-in server during local development
        app.run(debug=True, host='0.0.0.0', port=5000)
