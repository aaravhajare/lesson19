def match_word(words) :

    p = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            lst.append(word)
            p += 1
    
    print(lst)

count = ["abc" , "aba" , "xyz" , "121"]

print(match_word(count))