from flask import Flask, render_template
import os

app = Flask(__name__)

# Serve the index.html when the root URL is accessed
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the app runs on port 5000, which is default for Flask
    app.run(debug=True, host='0.0.0.0', port=5000)
