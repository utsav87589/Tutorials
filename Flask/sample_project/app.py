from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home() : 

    return render_template('index.html')


@app.route('/about')
def about() :

    return 'This is about page'

@app.route('/submit', methods = ['GET', 'POST'])
def submit() : 
    name = None
    error_message = None

    if request.method == 'POST' :
        name = request.form.get('username', '').strip()
        # print(f"user entered the name : {name}")

        if not name : 
            error_message = 'You did not entered any name!'
            name = None

    return render_template('submit.html', name = name, error = error_message)


if __name__ == '__main__' : 
    app.run(debug = True)