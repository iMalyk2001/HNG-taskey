            FastAPI Student Management API Documentation
Overview
The FastAPI Student Management API is a web-based application for managing student records. It provides a set of RESTful endpoints for creating, retrieving, updating, and deleting student data. The API utilizes FastAPI, a modern Python web framework, along with SQLite for data storage.

Base URL
The base URL for accessing the API is:

``` https://hng-taskey2.onrender.com ```


                                    ENDPOINTS
1. Create a new person
  Endpoint: /api
  HTTP Method: POST
  Request Body: JSON object representing a student (Pydantic model Persons).
  Response: JSON object representing the created student.
  Description: Create a new student record in the database.
2. Get Student by ID
  Endpoint: /api/{userId}
  HTTP Method: GET
  Path Parameter: userId - The unique identifier of the student.
  Response: JSON object representing the student with the specified userId.
  Description: Retrieve a student's information by their unique ID.
3. Update Student
  Endpoint: /api/{userId}
  HTTP Method: PUT
  Path Parameter: userId - The unique identifier of the student to update.
  Request Body: JSON object representing the updated student data (Pydantic model Persons).
  Response: JSON object representing the updated student.
  Description: Update an existing student's information.
4. Delete Student
  Endpoint: /api/{userId}
  HTTP Method: DELETE
  Path Parameter: userId - The unique identifier of the student to delete.
  Response: JSON message confirming the student deletion.
  Description: Delete a student record from the database.

```
{
  "userId": 1,
  "name": "John Doe"
}
```
Id (integer): Unique identifier for the student.
name (string): Name of the student.
Usage
You can interact with the API using HTTP clients such as curl, Postman, or by making HTTP requests from your application. Make sure to set the appropriate HTTP headers (e.g., Content-Type: application/json) when sending requests.

Dependencies
The FastAPI Student Management API depends on the following external libraries and frameworks:

FastAPI: A modern Python web framework.
SQLAlchemy: An Object-Relational Mapping (ORM) library for database interaction.
Pydantic: A data validation and parsing library for data models.
SQLite: A lightweight, embedded database for storing student records.
Getting Started
Clone the project repository.
Install the required Python packages using pip install -r requirements.txt.
Run the FastAPI application using uvicorn main:app --host 0.0.0.0 --port 8000.
Feedback and Contributions
We welcome feedback, bug reports, and contributions from the community. If you encounter issues or have suggestions for improvements, please open an issue on the project's GitHub repository.

License
This project is open-source and licensed under the MIT License.

This documentation provides an overview of the FastAPI Student Management API, including its endpoints, data formats, and dependencies. Feel free to expand this documentation to include more detailed information about the API, its use cases, and additional features as your project evolves.




