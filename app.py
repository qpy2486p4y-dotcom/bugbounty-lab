from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bug Bounty Lab</h1>"

@app.route("/search")
def search():
    q = request.args.get("q", "")
    return f"<h1>Search</h1><p>You searched for: {q}</p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
