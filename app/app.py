from flask import Flask
app = Flask(__name__)

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return 'False'
    if number <= 3:
        return 'True'
    if number % 2 == 0 or number % 3 == 0:
        return 'False'
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return'False'
        i += 6
    return 'True'

@app.route('/is_prime/<int:number>', methods=['GET'])
def check_prime(number):
    return  is_prime(number)

if __name__ == '__main__':
    app.run(debug=True)
