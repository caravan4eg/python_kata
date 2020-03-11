"""
test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
'void success at all costs!' should equal 'Avoid success at all costs!'
'ibvq fhpprff ng nyy pbfgf!' should equal 'Nibvq fhpprff ng nyy pbfgf!'
"""

# def rot13(message):
#     rot13=''
#     for s in message:
#         if s.isalpha() and 97 <= ord(s) <= 109 and s.islower():
#             rot13 += chr(ord(s)+13)

#         if s.isalpha() and 109 < ord(s) <= 122 and s.islower():
#             rot13 += chr(ord(s)-13)


#         if s.isalpha() and 66 <= ord(s) <= 77 and s.isupper():
#             rot13 += chr(ord(s)+13)

#         if s.isalpha() and 77 < ord(s) <= 90 and s.isupper():
#             rot13 += chr(ord(s)-13)
#         if not s.isalpha():
#             rot13 += s

#     return rot13

def rot13(phrase):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    transform = dict(zip(key, val))
    print(transform)
    return ''.join(transform.get(char, char) for char in phrase)

print(rot13('void success at all costs!'))
