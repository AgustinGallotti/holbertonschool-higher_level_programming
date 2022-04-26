#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
	print(number,'Is negative\n')
elif number > 0:
	print(number,'Is positive\n')
else:
	print(number,'Is zero\n')
