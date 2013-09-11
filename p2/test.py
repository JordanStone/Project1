#!/usr/bin/python
#test.py
#

import sys
import arraystack
import pointerstack

def genTest(stack):	
	passed = True
	
	expectStack = []

	print "PUSH 10 values from 1 to 10:"
	for n in range(0,10): 
		stack.PUSH(n+1)
		expectStack.insert(0,n+1)
		if stack.TOP() != expectStack[0]:
			passed = False
	
	testPass("PUSH",passed)
	passed = True
	
	print "TOP:"
	if stack.TOP() != expectStack[0]:
		passed = False

	testPass("TOP",passed)
	passed = True
	
	print "POP:"
	stack.POP()
	expectStack.pop(0)

	if stack.TOP() != expectStack[0]:
		passed = False
	
	testPass("POP",passed)
	passed = True

	print "MAKENULL:"
	stack.MAKENULL()
	expectStack = [None]
	if stack.TOP() != expectStack[0]:
		passed = False

	testPass("MAKENULL",passed)
	passed = True

def testPass(name,passed):
	if (passed):
		print "The method", name, "has passed."
	else:
		print "The method", name, "has failed."

def main():

	x = arraystack.arrayStack()
	y = pointerstack.pointerStack()

	print "Testing arraystack:"
	genTest(x)

	print '\n',"Testing pointerstack:"
	genTest(y)	

if __name__ == "__main__":
	main()
