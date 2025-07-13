
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Chit Fund Tracker App!"

@app.route('/fund', methods=['POST'])
def handle_fund_selection():
    data = request.json
    return jsonify({
        "message": "Fund data received successfully!",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True)
