from flask import Flask, render_template, request, escape

app = Flask(__name__)


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Returns the set of letters from "letters" found in the specified "phrase"."""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> 'None':
    """ Write the usage log to the end of the 'vsearch.log' file."""
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)

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
def view_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for i in log:
            contents.append([])
            for item in i.split('|'):
                contents[-1].append(escape(item))

    titles = ('Form Data', 'Remote addr', 'User agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_title=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
