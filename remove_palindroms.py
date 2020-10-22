def remove_palindroms(spells):
    bad_words = []
    for spell in spells:
        word = spell.replace(' ', '')
        word = word.lower()
        if word == word[::-1]:
            bad_words.append(spell)
    for word in bad_words:
        spells.remove(word)
