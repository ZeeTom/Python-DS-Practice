def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_frequecies={}
    for ltr in phrase:
        if ltr not in letter_frequecies:
            letter_frequecies[ltr]=0
        letter_frequecies[ltr] += 1
        
     return letter_frequecies