def order_string(string, start, end):
    if start < end:
        p = part_string(string, start, end)
        order_string(string, start, p - 1)
        order_string(string, p + 1, end)


def part_string(string, start, end):
    last_letter = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= last_letter:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    string1 = list(first_string.lower())
    string2 = list(second_string.lower())
    print(string1, string2)

    order_string(string1, 0, len(first_string) - 1)
    order_string(string2, 0, len(second_string) - 1)

    string1 = ''.join(string1)
    string2 = ''.join(string2)

    if string1 == '' or string2 == '':
        return (string1, string2, False)
    elif string1 == string2:
        return (string1, string2, True)
    else:
        return (string1, string2, False)
