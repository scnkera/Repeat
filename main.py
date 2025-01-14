def first_uncommon(matrix, n):
    # Your implementation here!
    hash_table = {}
    for row in matrix:
        for letter in row:
            if letter not in hash_table:
                hash_table[letter] = 1
            else:
                hash_table[letter] += 1

    # option 1
    # viable_list = []

    # for letter, freq in hash_table.items():
    #     if freq < n:
    #         viable_list.append(letter)

    # letter = viable_list[0]

    # return letter

    # option 2

    for row in matrix:
        for letter in row:
            if hash_table[letter] < n:
                return letter



matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert first_uncommon(matrix_1, 2) == 'd'
assert first_uncommon(matrix_1, 3) == 'r'
assert first_uncommon(matrix_1, 4) == 'u'

matrix_2 = (
    ('💜',),
)
assert first_uncommon(matrix_2, 2) == '💜'
assert first_uncommon(matrix_2, 525600) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")