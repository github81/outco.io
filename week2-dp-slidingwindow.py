

"""


"ADOBECODEBANC", "ABC"

l	r	fullString[r]	d = {}			c = ['A','B','C']	
0	0	'A'				{'A':1}			['B','C']
0	1	'D'				{'A':1}			['B','C']
0	2	'O'				{'A':1}			['B','C']
0	3	'B'				{'A':1,			['C']
						'B': 1}
0	4	'E'				{'A':1,			['C']
						'B': 1}
0	5	'C'				{'A':1,			['C']
						'B': 1
						'C': 1}			[]

min_str = r-l
1	5	fullString[l]
		'A'				d = {'A':0,
							'B':1,
							'C':1}		

	
						


minimumWindowSubstring(fullString,chars):

	
	l = 0
	r = 0
	d = {}
	c = list(chars)
	
	#"ADOBECODEBANC", "ABC"
	
	while l < len(fullString):
	
		if fullString[r] in c:
			d[fullString[r]] += 1
			c.remove()		


"""

def minimumWindowSubstring2(fullString,chars):
	
	
	min_len = len(fullString)
	min_str = fullString
	
	d = {
		'A':1,
		'B':1,
		'C':1
		}
	c = 3
	
	for l in range(0,len(fullString)):
	
		t_d = d.copy()
		t_c = c
	
		for r in range(l,len(fullString)):

			if fullString[r] in t_d and t_d[fullString[r]] > 0:
				t_d[fullString[r]] -= 1
				t_c -= 1

			if t_c == 0:
				if r - l < min_len:
					min_len = r - l + 1
					min_str = fullString[l:r+1]
				break	
				
	print(min_len)								
	print(min_str)

def minimumWindowSubstring(fullString,chars):

	min_len = len(fullString)
	min_str = fullString
	
	d = {
		'A':1,
		'B':1,
		'C':1
		}
	c = 3
	t_c = c

	l = 0
	r = 0

	while l < len(fullString):
	
		#hunting phase

		
		#catch-up phase
		
		pass
		
			

if __name__ == "__main__":
	fullString = "ADOBECODEBANC"
	chars = "ABC"
	minimumWindowSubstring2(fullString,chars)