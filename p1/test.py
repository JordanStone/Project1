#!/usr/bin/python
#test.py
#

import sys

import arraylist
import pointerlist

def genTest(lis):	
	passed = True
	expectLis = []

	print "INSERT 10 vals from 1 to 10:"
	for n in range(0,10): 
		lis.INSERT(n+1,0)
		expectLis.insert(0,n+1)
		if lis.RETRIEVE(n) != expectLis[n]:
			passed = False

	testPass("INSERT",passed)
	passed = True

	print "RETRIEVE"
	for n in range(0,10):
		if lis.RETRIEVE(n) != expectLis[n]:
				passed = False
	
	testPass("RETRIEVE",passed)
	passed = True

	print "LOCATE"
	for n in reversed(xrange(1,11)):
		if lis.LOCATE(n) != expectLis.index(n):
				passed = False

	testPass("LOCATE",passed)
	passed = True

	print "FIRST:"
	if lis.FIRST() != 0:
		passed = False

	testPass("FIRST",passed)
	passed = True

	print "END:"
	if lis.END() != 10:
		passed = False
	
	testPass("END",passed)
	passed = True

	print "NEXT:"
	if lis.NEXT(5) != 6:
		passed = False

	testPass("NEXT",passed)
	passed = True

	print "PREVIOUS:"
	if lis.PREVIOUS(7) != 6:
		passed = False
	
	testPass("PREVIOUS",passed)
	passed = True

	print "DELETE:"
	lis.DELETE(3)
	expectLis.pop(3)
	for n in range(0,9):
		if lis.RETRIEVE(n) != expectLis[n]:
			passed = False
	
	testPass("DELETE",passed)
	passed = True

	print "MAKENULL:"
	lis.MAKENULL()
	expectLis = [None]
	if lis.RETRIEVE(0) != expectLis[0]:
		passed = False
	
	testPass("MAKENULL",passed)

def testPass(name,passed):
	if (passed):
		print "The method", name, "has passed."
	else:
		print "The method", name, "has failed."

def main():
	x = arraylist.arrayList()
	y = pointerlist.pointerList()

	print "Testing arraylist:"
	genTest(x)

	print '\n',"Testing pointerlist:"
	genTest(y)	

if __name__ == "__main__":
	main()

