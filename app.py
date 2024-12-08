from flask import Flask, request
app = Flask(__name__)  # Create a new Flask application instance
from flask_sqlalchemy import SQLAlchemy

# Configure the app to use SQLite as the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define a Drink model to represent drinks in the database
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    # Representation method to print out a drink object
    def __repr__(self):
        return(f"{self.name} - {self.description}")

# A simple route to test if the API is working
@app.route('/')
def index():
    return('Hello!')

# Route to display all drinks from the database
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()  # Query all drinks in the database
    output = []
    for drink in drinks:  # Loop through each drink and format it
        drink_data = {'name': drink.name,
                      'description': drink.description}
        output.append(drink_data)  # Add each drink to the output list
    return {"drinks": output}  # Return all drinks as a JSON response

# Route to get a single drink by its ID
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)  # Try to get the drink or return a 404 if it doesn't exist
    return {"name": drink.name, "description": drink.description}  # Return the drink details as JSON

# Route to add a new drink to the database
@app.route('/drinks', methods=['POST'])
def add_drink():
    # Create a new Drink object using data from the JSON request
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)  # Add the drink to the database session
    db.session.commit()  # Commit the session to save the drink
    return {'id': drink.id}

# Route to delete a drink by its ID
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)  # Try to get the drink
    if drink is None:
        return {"error": "not found"}  # Return an error if it doesn't exist
    db.session.delete(drink)  # Delete the drink
    db.session.commit()  # Commit the changes to the database
    return {"message": "drink deleted"}

# Route to update an existing drink by its ID
@app.route('/drinks/<id>', methods=['PUT'])
def edit_drink(id):
    drink = Drink.query.get(id)  # Try to get the drink
    if drink is None:
        return {"error": "not found"}  # Return an error if it doesn't exist
    # Update the drink's name and description from the JSON request
    drink.name = request.json['name']
    drink.description = request.json['description']
    db.session.commit()  # Save the changes
    return {"message": "drink edited"}
