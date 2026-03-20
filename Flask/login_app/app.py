from flask import request, Response, url_for, session, redirect, Flask, render_template

app = Flask(__name__)
app.secretkey = 'secret'


### main home page (aka login page) directory
@app.route('/', methods = ['GET', 'POST'])
def login() : 

    username = request.form.get('username')
    password = request.form.get('password')

    print(f"{username} :: {password}")

    return render_template('login.html')

if __name__ == '__main__' : 
    app.run(debug = True)