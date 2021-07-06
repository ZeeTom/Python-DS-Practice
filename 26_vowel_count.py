def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counter = {}; 

    for char in phrase:
        if char.lower() in vowels:
            if char.lower() not in vowel_counter:
                vowel_counter[char.lower()] = 0
            vowel_counter[char.lower()] += 1
    
    return vowel_counter