from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Kubernetes 🚀"

@app.route('/health')   # ✅ ADD THIS
def health():
    return "OK", 200    # ✅ MUST return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)