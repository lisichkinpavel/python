def text_convertor(text):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ascii_uppercase[ascii_lowercase.index(text[0])] + text[1:]


input_string = 'i must not use title method'
converted_list = list(map(text_convertor, input_string.split(' ')))
print(' '.join(converted_list))
