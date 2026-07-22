import os
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "online", "role": "System Anchor Platform"})

# --- DATA SCIENCE ANALYTICS ENDPOINTS ---

@app.route("/api/hotspots", methods=["GET"])
def get_hotspots():
    try:
        data_path = os.path.join(os.path.dirname(__file__), "data", "hotspots_layer.json")
        with open(data_path, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 404

@app.route("/api/network", methods=["GET"])
def get_network():
    try:
        data_path = os.path.join(os.path.dirname(__file__), "data", "extracted_network.json")
        with open(data_path, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 404

if __name__ == '__main__':
    port = int(os.environ.get("X_ZOHO_CATALYST_LISTEN_PORT", os.environ.get("PORT", 8080)))
    app.run(host="0.0.0.0", port=port)