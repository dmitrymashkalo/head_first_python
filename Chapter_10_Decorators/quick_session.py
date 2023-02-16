from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess'


@app.route('/setuser/<user>')
def set_user(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def get_user() -> str:
    return 'User value is currently set to: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
