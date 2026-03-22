from flask import request, Response, url_for, session, redirect, Flask, render_template

app = Flask(__name__)
app.secret_key = 'secret'


### main home page (login page) directory
@app.route('/', methods = ['GET', 'POST'])
def login() : 

    if request.method == 'POST' : 

        ### getting the username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')

        ### printing into the terminal to make sure that it's working
        print(f"{username} :: {password}")

        valid_users = {
            'utsav' : '123',
            'bob' : '123',
            'joe' : 'joe123'
        }

        if username in valid_users.keys() and password == valid_users[username]: 
            session['user'] = username ### store into the session
            return redirect(url_for('welcome'))

        else : 
            return render_template('login.html', error = 'Invalid credentials')

    return render_template('login.html')

### welcome page (after successful login)
@app.route('/welcome')
def welcome() : 

    if 'user' in session :
        return render_template('welcome.html', user = session['user'])

    else : 
        return redirect(url_for('login'))
    

### logout page
@app.route('/logout')
def logout() : 

    session.pop('user', None)
    return redirect(url_for('login'))
