# RESTful API

This project is a RESTful API built with Flask and Flask-SQLAlchemy to manage a simple database of drinks. The API allows users to create, read, update, and delete drink records, making it a basic yet powerful example of CRUD operations in a Python web application.

## Features

- **SQLite database integration** to store drinks.
- **CRUD operations** for managing drinks:
  - **GET**: Retrieve all drinks or a single drink by ID.
  - **POST**: Add a new drink.
  - **PUT**: Update an existing drink by ID.
  - **DELETE**: Remove a drink by ID.
- Basic setup with Flask and Flask-SQLAlchemy.

## Routes

1. **Index Route**
   - `GET /`
   - Returns a simple "Hello!" message to confirm the API is running.

2. **Retrieve All Drinks**
   - `GET /drinks`
   - Returns a JSON object containing all drinks in the database.

3. **Retrieve a Single Drink**
   - `GET /drinks/<id>`
   - Returns the details of a drink specified by its ID.

4. **Add a New Drink**
   - `POST /drinks`
   - Adds a new drink to the database.
   - Expects a JSON payload:
     ```json
     {
       "name": "Drink Name",
       "description": "Drink Description"
     }
     ```

5. **Update a Drink**
   - `PUT /drinks/<id>`
   - Updates the details of an existing drink by its ID.
   - Expects a JSON payload:
     ```json
     {
       "name": "Updated Drink Name",
       "description": "Updated Drink Description"
     }
     ```

6. **Delete a Drink**
   - `DELETE /drinks/<id>`
   - Deletes the drink specified by its ID.

## Setup Instructions

### Prerequisites
- Python
- Flask
- Flask-SQLAlchemy
- Postman (or any REST API client)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/KacperKolasa/restapi/tree/main
   cd restapi
   ```
2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```
5. Run the application:
   ```bash
   flask run
   ```
6. Access the API at http://127.0.0.1:5000.

## Using Postman

### Add a New Drink
1. Open Postman and create a new **POST** request.
2. Set the URL to `http://127.0.0.1:5000/drinks`.
3. Navigate to the **Body** tab, select **raw**, and set the format to **JSON**.
4. Add the following JSON payload:
   ```json
   {
     "name": "Cola",
     "description": "Sweet fizzy drink"
   }
   ```
5. Click **Send** to create the new drink.

### Retrieve All Drinks
1. Create a new **GET** request.
2. Set the URL to `http://127.0.0.1:5000/drinks`.
3. Click **Send** to retrieve all the drinks in the database.

### Update a Drink
1. Create a new **PUT** request.
2. Set the URL to `http://127.0.0.1:5000/drinks/<id>` (replace `<id>` with the ID of the drink you want to update).
3. Navigate to the **Body** tab, select **raw**, and set the format to **JSON**.
4. Add the following JSON payload:
   @json
   {
     "name": "Updated Drink Name",
     "description": "Updated Drink Description"
   }
   @
5. Click **Send** to update the drink.

### Delete a Drink
1. Create a new **DELETE** request.
2. Set the URL to `http://127.0.0.1:5000/drinks/<id>` (replace @<id>@ with the ID of the drink you want to delete).
3. Click **Send** to delete the drink.

