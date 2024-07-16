from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cyber'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a database instance
db = SQLAlchemy(app)

# Define a model for your data
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result_data = db.Column(db.Text)
    E_value = db.Column(db.Integer)
    N_value = db.Column(db.Integer)
    P_value = db.Column(db.Integer)

# Input from the user
user_input_result_data = "133.1.213.1.157.244.1.220."  # Replace this with the actual user input

with app.app_context():
# Retrieve the entry from the Result table that matches the user input
    result_entry = Result.query.filter_by(result_data=user_input_result_data).first()

# Check if a matching entry is found
    if result_entry:
        e = result_entry.E_value
        n = result_entry.N_value
        phi = result_entry.P_value

        letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

        input_data1 = ""
        input_string = user_input_result_data
        numbers_list = [int(num) for num in input_string.split(".") if num]  # Filter out empty strings
    # Find the modular multiplicative inverse of e modulo phi
        d = pow(e, -1, phi)

        for val in numbers_list:
            PT = pow(val, d, n)
            for letter, number in letter_to_number.items():
                if number == PT:
                    input_data1 += letter

        print("The decrypted text is : ",input_data1)
    else:
        print(f"No entry found in the Result table for result_data: {user_input_result_data}")
