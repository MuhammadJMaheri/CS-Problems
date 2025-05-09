from flask import Flask
import os

app = Flask(__name__)

# Generate or retrieve a unique identifier for the instance
instance_id = os.getenv('INSTANCE_ID', os.uname().nodename)

@app.route('/')
def home():
    return f"Hello, World from Kubernetes! Instance ID: {instance_id}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
