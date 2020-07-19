'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    if word == "th":
        return 1

    elif len(word) == 2 and word != "th":
        return 0

    elif len(word) <= 1:
        return 0

    # Binary Recursive Magic

    else:
        half = len(word)//2
        first = word[:half]
        second = word[half:]
        answer = count_th(first) + count_th(second)
        return answer + count_th(word[half-1] + word[half])


print(count_th("thmenth"))
