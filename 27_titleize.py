def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    words = phrase.lower().split(" ")
    words = [word.capitalize() for word in words]
    return " ".join(words)
    # return phrase.title()
