def word_count(n,words):
    count = {}
    for word in words[:n]:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    print(len(count))

    for c in count.values():
        print(c, end = " ")
    print()

word_count(4,["bcdef", "abcdefg", "bcde", "bcdef"])
