from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded user credentials for demonstration purposes
USER_CREDENTIALS = {'user1':'1234', 'Amulya Karwa':'amulya_karwa'}

@app.route('/')
def home():
    return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            return render_template('Welcome.html', username=username)
        else:
            return render_template('Error.html', username=username)
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS:
            return render_template('Error2.html', username=username)
        else:
            USER_CREDENTIALS[username] = password
            return render_template('Registered.html', username=username)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
