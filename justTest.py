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

#=================================================================================

def not_bad(s):
    char_list = ['!', '.', '?']
    if s[-1] in char_list:
        new_str = s.split('not')
        return new_str[0] + 'good' + s[-1]
    else:
        new_str = s.split('not')
        return new_str[0] + 'good'


not_bad('This dinner is not that bad')
