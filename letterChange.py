def letterChange(str):
    str1 = ''
    str2 = ''

    for i in str:
        if i.isalpha():
            if i != 'z':
                str1 += chr(ord(i) + 1)
            else:
                str1 += 'a'
        else:
            str1 += i  # not an alphabet

    for char in str1:  
        if (char == "a") or (char == "e") or (char == "i") or (char == "o") or (char == "u"):
            char = char.upper()
        str2 = str2 + char

    return str2


print(letterChange('hello*3'))
