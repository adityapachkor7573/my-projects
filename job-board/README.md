<!-- 
# Job Listings Application

## Overview
This project is a simple Job Listings web application built with HTML, CSS, JavaScript (frontend), and a Flask backend connected to a MySQL database. It allows users to view job listings, see detailed job information, and submit job applications.

## Project Structure
- `index.html`: Displays the list of available jobs.
- `job details.html`: Shows detailed information for a selected job.
- `apply.html`: Form for users to apply for a job.
- `app.py`: Flask backend API to handle job applications.
- MySQL Database: Stores job application data.

## Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask
- Database: MySQL
- CORS enabled for API requests.

## Setup Instructions

### Prerequisites
- Python 3.x installed
- MySQL server installed and running
- `mysql-connector-python` package installed (`pip install mysql-connector-python`)
- Flask installed (`pip install flask flask-cors`)

### Database Setup
1. Create a MySQL database named `job_card`.
2. Create a table named `applications` with the following structure:

```sql
CREATE TABLE applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  job_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  cover_letter TEXT NOT NULL,
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Running the Application
1. Update database credentials in `app.py` if needed.
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open `index.html` in a browser to view the frontend.

### Usage
- Browse jobs on the home page (`index.html`).
- Click "View Details" to see job details.
- Click "Apply Now" to submit an application.
- Applications are sent to the Flask backend and stored in the MySQL database.

## Notes
- Ensure the Flask server is running for the application form to submit successfully.
- The frontend and backend run separately; frontend uses static files, backend runs on `localhost:5000`.

## Author
Aditya Pachkor -->