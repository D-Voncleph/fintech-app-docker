import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/test')
def get_test_data():
    # Read the DATABASE_URL from the environment variable we injected
    db_url = os.environ.get('DATABASE_URL')
    
    if not db_url:
        return jsonify(error="DATABASE_URL environment variable is not set."), 500

    try:
        # Try to connect to the database
        conn = psycopg2.connect(db_url)
        conn.close() # Close the connection immediately if successful
        
        # If connection is successful, return a success message
        return jsonify(message="Successfully connected to the Postgres database!")
    
    except Exception as e:
        # If connection fails, return an error message
        return jsonify(
            error="Failed to connect to the database.",
            details=str(e)
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
