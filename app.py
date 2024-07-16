import math
import time
import random
from flask import Flask, render_template, request
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
    E_value = db.Column(db.Integer)  # Add a column for e
    N_value = db.Column(db.Integer)
    P_value = db.Column(db.Integer)

@app.route('/')
def Encoder():
    return render_template('Encoder.html')

@app.route('/process', methods=['POST'])
def process():
    input_data1 = request.form['input_data1']
    input_data2 = request.form['input_data2']
    input_data3 = request.form['input_data3']

    # Your Python code processing input_data goes here
    letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
                    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    user_name = input_data1.lower()

    numeric_values = list()

    for letter in user_name:
        if letter.isalpha():  # Ignore non-alphabetic characters
            number = letter_to_number.get(letter, 0)
            numeric_values.append(number)

    n = int(input_data2) * int(input_data3)
    phi = (int(input_data2) - 1) * (int(input_data3) - 1) 
    input_data1 = ""
    for x in range(0,100) :
            temp = random.randint(1, phi)
            if math.gcd(phi,temp) == 1 :
                e = temp
                break
              
    for number in numeric_values :
        CT = (pow(number, e)) % n
        CT = str(CT)
        input_data1 = input_data1 + CT + "."

    result_data = f"{input_data1}"

    # Create a new Result object and add it to the database
    result_entry = Result(result_data=result_data, E_value=e, N_value=n, P_value = phi)

    # Create a Flask application context before interacting with the database
    with app.app_context():
        db.create_all()  # This should be called inside the application context
        db.session.add(result_entry)
        db.session.commit()
    
    return render_template('Encoder.html', result_data=result_data)

if __name__ == '__main__':
    app.run(debug=True)
