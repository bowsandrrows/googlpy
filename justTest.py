def fix_start(s):
    svar = s.replace(s[0], '*')
    return s[0] + svar[1:]


print(fix_start('babbles'))


def mix_up(a, b):
    return f'{a.replace(a[0:2], b[0:2])} {b.replace(b[0:2], a[0:2])}'


print(mix_up('mix', 'pod'))


def verbing(s):
    if len(s) >= 3 and not s.endswith('ing'):
        return s + 'ing'
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s


print(verbing('swimming'))

"""A unicode string is a different type of object from a byte string but various libraries such as regular 
expressions work correctly if passed either type of string.

To convert a regular Python string to bytes, call the encode() method on the string. Going the other direction, 
the byte string decode() method converts encoded plain bytes to a unicode string:"""

ustring = 'A unicode \u018e string \xf1'
z = ustring.encode('utf-8')
print(z)
# b'A unicode \xc6\x8e string \xc3\xb1'

# bytes of utf-8 encoding. Note the b-prefix.
t = z.decode('utf-8')  # Convert bytes back to a unicode string
var = t == ustring  # It's the same as the original, yay!
print(var)  # True


def not_bad(s):
    char_list = ['!', '.', '?']
    if s[-1] in char_list:
        new_str = s.split('not')
        return new_str[0] + 'good' + s[-1]
    else:
        new_str = s.split('not')
        return new_str[0] + 'good'


not_bad('This dinner is not that bad')
