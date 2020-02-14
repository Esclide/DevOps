def letters_range(start, end, step=1):
    return [chr(x) for x in range(ord(start), ord(end), step)]


print(letters_range('p', 'g', -2))
