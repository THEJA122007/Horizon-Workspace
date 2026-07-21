import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "online", "role": "System Anchor Platform"})

if __name__ == '__main__':
    # AppSail passes the port via X_ZOHO_CATALYST_LISTEN_PORT or PORT
    port = int(os.environ.get("X_ZOHO_CATALYST_LISTEN_PORT", os.environ.get("PORT", 8080)))
    app.run(host="0.0.0.0", port=port)