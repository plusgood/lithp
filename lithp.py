from __future__ import print_function
from converter import Converter
import sys
import os

def main(argv):
	try:
		fp = argv[1]
	except IndexError:
		print("Usage: %s <filepath>" % argv[0], file=sys.stderr)
	try:
		with open(fp) as f:
			program = f.read()
	except IOError:
		print("File not found", file=sys.stderr)
		return 1

	converter = Converter(program)

	dot_index = fp.rfind('.')
	if dot_index == -1:
		name = fp
	else:
		name = fp[:dot_index]

	with open(name+'.cpp', 'w') as f:
		f.write(converter.get_cpp())
	
	#-O2 is especially necessary for tail recursion optimization
	return os.system('g++ -O2 -o %s.exe %s.cpp' % (name, name))


if __name__ == '__main__':
	exit(main(sys.argv))
