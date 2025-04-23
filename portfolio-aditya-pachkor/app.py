from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='portfolio_form'
    )

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify(success=False, error="All fields are required."), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify(success=True, message="Message sent successfully!"), 200
    
    except mysql.connector.Error as err:
        print("MySQL Error:", err)
        return jsonify(success=False, error="Database error: " + str(err)), 500
    except Exception as e:
        print("Error:", e)
        return jsonify(success=False, error="Unexpected error: " + str(e)), 500
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
