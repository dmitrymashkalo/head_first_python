from flask import Flask, render_template, request

app = Flask(__name__)


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """ Returns the set of letters from "letters" found in the specified "phrase"."""
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> 'None':
    with open('vsearch.log', 'a') as log:
        print(req, res, end='', file=log)



@app.route('/search', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search_for_letters(phrase, letters))

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search for letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
