from flask import Flask, render_template
import os

app = Flask(__name__)

# Serve the index.html when the root URL is accessed
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the app runs on the correct port set by Render
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
