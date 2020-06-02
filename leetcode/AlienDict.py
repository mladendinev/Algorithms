def isAlienSorted(words, order):
    pos = {letter: idx for idx, letter in enumerate(order)}

    maxwordlength = max([len(word) for word in words])

    for idx in range(maxwordlength):
            churki = [pos[word[idx]] for word in words]
            if sorted(churki) != churki:
                return False

    return True


words = ["hello", "leetcode"]

order = "hlabcdefgijkmnopqrstuvwxyz"
order[0].isalpha()
isAlienSorted(words, order)
