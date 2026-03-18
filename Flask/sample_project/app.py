from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() : 

    return 'Switching to the flask mid project lol!'


@app.route('/about')
def about() :

    return 'This is about page though'

if __name__ == '__main__' : 
    app.run()