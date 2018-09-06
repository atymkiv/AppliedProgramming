#Варіант 12. Написати програму мовою Python для визначення розміру
#текстового файлу

import sys
import os

args = sys.argv[1:]
if args:
	name = args[0]
	if os.path.exists(name):
		info = os.stat(name)
		size = info.st_size
		print("The size of " + name + " is %s bites" %size)
	else:
		print ("%s does not exist" %name)
else:
	print("Please pass a file as the first argument to calculate its size")
