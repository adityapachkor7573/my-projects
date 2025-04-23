from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',  # Set your MySQL password here
        database='job_card'
    )

@app.route('/apply', methods=['POST'])
def apply():
    data = request.get_json()

    job_id = data.get('job_id')
    name = data.get('name')
    email = data.get('email')
    cover_letter = data.get('cover_letter')

    if not job_id or not name or not email or not cover_letter:
        return jsonify(success=False, message="All fields are required."), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Insert the application using job_id
        cursor.execute(
            "INSERT INTO applications (job_id, name, email, cover_letter) VALUES (%s, %s, %s, %s)",
            (job_id, name, email, cover_letter)
        )

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify(success=True, message="Application submitted successfully!"), 200

    except mysql.connector.Error as err:
        print("MySQL Error:", err)
        return jsonify(success=False, message="Database error: " + str(err)), 500

    except Exception as e:
        print("Error:", e)
        return jsonify(success=False, message="Unexpected error: " + str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
