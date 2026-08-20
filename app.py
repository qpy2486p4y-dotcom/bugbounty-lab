from flask import Flask, request, jsonify

app = Flask(__name__)

# Intentionally simple learning examples for a private security lab.
DEMO_API_KEY = "demo-key-not-a-real-secret"

@app.route("/")
def home():
    return """
    <h1>Bug Bounty Lab</h1>
    <p>This is my local Flask security-testing application.</p>
    <p>Try /api/info</p>
    """

@app.route("/api/info")
def info():
    return jsonify({
        "app": "Bug Bounty Lab",
        "version": "1.0",
        "environment": "training"
    })

@app.route("/api/search")
def search():
    query = request.args.get("q", "")
    return jsonify({
        "query": query,
        "message": f"You searched for: {query}"
    })

@app.route("/api/config")
def config():
    return jsonify({
        "demo_api_key": DEMO_API_KEY
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
