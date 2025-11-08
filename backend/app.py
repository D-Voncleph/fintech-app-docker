from flask import Flask, jsonify
app = Flask(__name__)

# This is your API endpoint
@app.route('/api/test')
def get_test_data():
    # Return some sample JSON
    return jsonify(message="Hello from the FinTech Backend!")

if __name__ == '__main__':
    # Run on 0.0.0.0 to be accessible outside the container
    app.run(host='0.0.0.0', port=5000)