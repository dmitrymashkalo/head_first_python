def search_for_vowels(phrase: str) -> set:
    """ Outputs the vowels found in the input word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


print(search_for_vowels('Hello, world!'))
