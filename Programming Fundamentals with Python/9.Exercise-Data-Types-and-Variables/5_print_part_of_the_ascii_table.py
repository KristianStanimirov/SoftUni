start_index = int(input())
last_index = int(input())
string_ascii = ''

for char in range(start_index, last_index + 1):
    if char == last_index:
        string_ascii += chr(char)
    else:
        string_ascii += chr(char) + ' '
print(string_ascii)
