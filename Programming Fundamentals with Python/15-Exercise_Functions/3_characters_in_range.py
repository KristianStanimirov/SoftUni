def string_func(char_1, char_2):
    start_char = ord(char_1)
    end_char = ord(char_2)
    list_chars = []
    for i in range(start_char + 1, end_char):
        list_chars.append(chr(i))
    return list_chars


first_char = input()
second_char = input()
print(' '.join(string_func(first_char, second_char)))
