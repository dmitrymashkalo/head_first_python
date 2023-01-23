def search_for_vowels(phrase: str) -> set:
    """ Outputs the vowels found in the input word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: set) -> set:
    """ Returns the set of letters from "letters" found in the specified "phrase"."""
    return set(letters).intersection(set(phrase))


print(search_for_letters('hello', 'aeiou'))
