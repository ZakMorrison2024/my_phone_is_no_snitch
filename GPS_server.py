from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['POST'])
def receive_gps_data():
    data = request.json
    print(f"Received GPS Data: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
