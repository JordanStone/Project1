#!/usr/bin/python
#stacktime.py
#

import sys
import time
import arraystack
import pointerstack

def pushtime(stack,ran):
	start = time.time()
	for n in range(0,ran):
		stack.PUSH("VAL")
	elapsed = round(time.time() - start,5)
	return elapsed

def poptime(stack,ran):
	start = time.time()
	for n in range(0,ran):
		stack.POP()
	elapsed = round(time.time() - start,5)
	return elapsed

def pypush(stack,ran):
	start = time.time()
	for n in range(0,ran):
		stack.append("VAL")
	elapsed = round(time.time() - start,5)
	return elapsed

def pypop(stack,ran):
	start = time.time()
	for n in range(0,ran):
		stack.pop()
	elapsed = round(time.time() - start,5)
	return elapsed

def main():

	t = []
	u = []
	v = []

	x = arraystack.arrayStack(-1)
	y = arraystack.arrayStack(-1)
	z = arraystack.arrayStack(-1)

	a = pointerstack.pointerStack()
	b = pointerstack.pointerStack()
	c = pointerstack.pointerStack()

	pyA = pypush(t,10000)
	pyB = pypush(u,15000)
	pyC = pypush(v,20000)

	arrA = pushtime(x,10000)
	arrB = pushtime(y,15000)
	arrC = pushtime(z,20000)

	pointA = pushtime(a,10000)
	pointB = pushtime(b,15000)
	pointC = pushtime(c,20000)

	print "================PUSH=================="
	print "|_SIZE_|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "| 10000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "| 15000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "| 20000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "======================================"


	pyA = pypop(t,10000)
	pyB = pypop(u,15000)
	pyC = pypop(v,20000)

	arrA = poptime(x,10000)
	arrB = poptime(y,15000)
	arrC = poptime(z,20000)

	pointA = poptime(a,10000)
	pointB = poptime(b,15000)
	pointC = poptime(c,20000)

	print "================POP==================="
	print "|_SIZE_|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "| 10000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "| 15000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "| 20000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "======================================"

if __name__ == "__main__":
	main()
