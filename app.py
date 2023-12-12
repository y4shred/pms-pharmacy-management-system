from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy data for users, medicines, and inventory (replace with a database in a real-world scenario)
users = {}
medicines = {'Medicine1': 10, 'Medicine2': 20, 'Medicine3': 5}
inventory = {'Medicine1': 100, 'Medicine2': 200, 'Medicine3': 50}

@app.route('/')
def index():
    return render_template('index.html')

# Patient functionalities
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        users[username] = {}
        return redirect('/')
    return render_template('register.html')

@app.route('/search_medicine')
def search_medicine():
    return render_template('search_medicine.html', medicines=medicines)

@app.route('/request_medicine', methods=['GET', 'POST'])
def request_medicine():
    if request.method == 'POST':
        medicine_name = request.form['medicine_name']
        if medicine_name in medicines:
            return f"{medicine_name} requested successfully!"
        else:
            return f"{medicine_name} is not available."
    return render_template('request_medicine.html', medicines=medicines)

@app.route('/make_payment')
def make_payment():
    return render_template('make_payment.html')

# Pharmacist functionalities
@app.route('/pharmacist')
def pharmacist_dashboard():
    return render_template('pharmacist_dashboard.html')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        users[username] = {}
        return redirect('/pharmacist')
    return render_template('create_user.html')

@app.route('/modify_user')
def modify_user():
    return render_template('modify_user.html', users=users)

@app.route('/delete_user/<username>')
def delete_user(username):
    if username in users:
        del users[username]
    return redirect('/pharmacist')

@app.route('/check_medicine')
def check_medicine():
    return render_template('check_medicine.html', medicines=medicines, inventory=inventory)

@app.route('/generate_bill')
def generate_bill():
    return render_template('generate_bill.html', medicines=medicines)

@app.route('/dispense_medicine')
def dispense_medicine():
    return render_template('dispense_medicine.html')

if __name__ == '__main__':
    app.run(debug=True)
