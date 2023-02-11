
def getText(line, chars_per_line:int=None):
	if chars_per_line is None:
		return ''.join(getChars(line))

	chars = [line[i:i+chars_per_line] for i in range(0, len(line), chars_per_line)]
	text = [getChars(''.join(s)) for s in chars]

	return '\n'.join(text)

def getChars(chars):
	s = ""

	for i in range(3):
		for c in chars:
			char = getChar(c)
			if char is not None: s += char[i]
			
		s += "\n"

	return s

def getChar(char):
  c = {
    "A" : \
'''
  /\\   
 /--\\  
/    \\ 
''',
	
	"B" : \
'''
|‾\\ 
|-< 
|_/ 
''',

    "C" : \

'''
 /‾ 
|   
 \\_ 
''',

	"D" : \
'''
|‾\\ 
| | 
|_/ 
''',

	"E" : \
'''
|‾‾ 
|-- 
|__ 
''',

	"F" : \
'''
|‾‾ 
|-  
|   
''',

	"G" : \
'''
|‾‾| 
| __ 
|__| 
''',

	"H" : \
'''
|  | 
|--| 
|  | 
''',

	"I" : \
'''
‾|‾ 
 |  
_|_ 
''',

	"J" : \
'''
‾‾| 
  | 
|_| 
''',

	"K" : \
'''
| / 
|<  
| \\ 
''',

	"L" : \
'''
|   
|   
|__ 
''',

	"M" : \
'''
|\\_/| 
|   | 
|   | 
''',

	"N" : \
'''
|\\  | 
| \\ | 
|  \\| 
''',

	"O" : \
'''
 /‾\\  
|   | 
 \\_/  
''',

	"P" : \
'''
|‾\\ 
|-/ 
|   
''',

	"Q" : \
'''
 /‾\\  
|  \\| 
 \\_/\\ 
''',

	"R" : \
'''
|‾\\ 
|_/ 
| \\ 
''',

	"S" : \
'''
/‾ 
‾\\ 
_/ 
''',

	"T" : \
'''
‾|‾ 
 |  
 |  
''',

	"U" : \

'''
| | 
| | 
\\_/ 
''',

	"V" : \
'''
\\    / 
 \\  /  
  \\/   
''',

	"W" : \
'''
\\       / 
 \\  |  /  
  \\/‾\\/   
''',
	
	"X" : \
'''
\\ / 
 X  
/ \\ 
''',

	"Y" : \
'''
\\   / 
 \\_/  
  |   
''',

	"Z" : \
'''
‾‾/ 
 /  
/__ 
''',

	"1" : \
'''
 /| 
/ | 
  | 
''',

	"2" : \
'''
/‾| 
 /  
/__ 
''',

	"3" : \

'''
/‾\\ 
  < 
\\_/ 
''',

	"4" : \
'''
 /|  
/_|_ 
  |  
''',

	"5" : \
'''
|‾‾ 
 ‾\\ 
__/ 
''',

	"6" : \
'''
/‾  
|‾\\ 
\\_/ 
''',

	"7" : \
'''
‾‾/ 
 /  
/   
''',

	"8" : \
'''
/‾\\ 
>-< 
\\_/ 
''',

	"9" : \
'''
/‾\\ 
\\_| 
__/ 
''',

	"0" : \
'''
 /‾\\  
| \\ | 
 \\_/  
''',
	
	# space
	" " : \
'''
   
   
   
''',

	"." : \
'''
   
   
0  
''',

	"," : \
'''
   
   
)  
''',

	"!" : \
'''
 | 
 | 
 . 
'''

  }.get(char.upper(), None)

  if c is None:
  	return None

  c = c.split("\n")

  # remove blank spaces
  c.pop(0)
  c.pop()

  return c


print(getText("Hello World!", 15))
