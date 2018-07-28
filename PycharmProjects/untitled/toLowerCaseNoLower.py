def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    x = ""
    for s in str:
        s = ord(s)
        if ( 60 <= s <= 90):
            s = chr(s+32)
        else:
            s = chr(s)
        x = x + s
    return x

str = "Wisam Abunimeh"
x = toLowerCase(str)
print(x)