def mystery(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        result = mystery(s[1:])
        return result + s[0]

print(mystery('help'))
print(mystery('goodbye'))
