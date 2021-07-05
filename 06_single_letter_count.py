def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    appearances=0
    for ltr in word:
        if ltr.lower() == letter.lower():
            appearances += 1

    return appearances


# also 
# return word.count(letter)