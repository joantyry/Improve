'''Check to see if a string has the same amount of 
'x's and 'o's. The method must return a boolean and 
be case insensitive. The string can contains any char.
'''
def xo(s):
    count = 0
    s = s.lower()
    if s.count("x") == s.count("o"):
        return True
    else: return False     