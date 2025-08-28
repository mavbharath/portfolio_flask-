from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthz', methods=['GET'])
def health_check():
    response = {
        "status": "ok",
        "message": "Service is healthy"
    }
    return jsonify(response), 200  # Returning JSON with status code 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
