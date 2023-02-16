from flask import Flask, render_template, request, escape, session, copy_current_request_context
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread
from time import sleep


app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecretKey'
app.config['dbconfig'] = {'host': '127.0.0.1',
                        'user': 'vsearch',
                        'password': 'vsearchpassword',
                        'database': 'vsearchlogDB'}


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Returns the set of letters from "letters" found in the specified "phrase"."""
    return set(letters).intersection(set(phrase))


@app.route('/search', methods=['POST'])
def do_search() -> 'html':

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> 'None':
        """ Save requests logs in database """
        sleep(15)
        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
                cursor.execute(_SQL, (req.form['phrase'],
                                    req.form['letters'],
                                    req.remote_addr,
                                    req.headers.get('User-Agent'),
                                    res))
        except Exception as err:
            print('Somthing went wrong:', str(err))

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))

    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as error:
        print('Logging failed with this error:', str(error))

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    title = 'Welcome to search for letters on the web!'
    return render_template('entry.html',
                           the_title=title)


@app.route('/viewlog')
@check_logged_in
def view_log() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote addr', 'User agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_title=titles,
                               the_data=contents)
    except ConnectionError as error:
        print('Is your database switched on? Error:', str(error))
    except CredentialsError as error:
        print('Credentials error:', str(error))
    except SQLError as error:
        print('SQL Error:', str(error))
    except Exception as error:
        print('Somthing went wrong:', str(error))
    return 'Error'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are logged out.'


if __name__ == '__main__':
    app.run(debug=True)
