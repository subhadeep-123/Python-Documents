def words_mapping(val):
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i, j in enumerate(val):
        if j < 'n':
            val[i] = words[25 - int(words.index(j))]
        else:
            val[i] = words[25 - int(words.index(j))]
    return ''.join(val)


if __name__ == '__main__':
    print(words_mapping(list(map(str, input()))))
