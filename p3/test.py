#!/usr/bin/python
#listtime.py
#

import sys
import time
import arraylist
import pointerlist

def instime(lis,ran,pos):
	if pos == "front":
		start = time.time()
		for n in range(0,ran):
			lis.INSERT("VAL",0)
		elapsed = round(time.time() - start,5)
		return elapsed
	elif pos == "back":
		start = time.time()
		for n in range(0,ran):
			lis.INSERT("VAL",n)
		elapsed = round(time.time() - start,5)
		return elapsed

def rettime(lis,ran):
	start = time.time()
	for n in range(0,ran):
		lis.RETRIEVE(n)
	elapsed = round(time.time() - start,5)
	return elapsed

def deltime(lis,ran,pos):
	if pos == "front":
		start = time.time()
		for n in range(0,ran):
			lis.DELETE(0)
		elapsed = round(time.time() - start, 5)
		return elapsed
	elif pos == "back":
		start = time.time()
		for n in reversed(range(ran,0)):
			lis.DELETE(n)
		elapsed = round(time.time() - start,5)
		return elapsed

def pyins(lis,ran,pos):
	if pos == "front":
		start = time.time()
		for n in range(0,ran):
			lis.insert(0,"VAL")
		elapsed = round(time.time() - start,5)
		return elapsed
	elif pos == "back":
		start = time.time()
		for n in range(0,ran):
			lis.insert(n,"VAL")
		elapsed = round(time.time() - start,5)
		return elapsed

def pyret(lis,ran):
	start = time.time()
	for n in range(0,ran):
		lis[n]
	elapsed = round(time.time() - start,5)
	return elapsed

def pydel(lis,ran,pos):
	if pos == "front":
		start = time.time()
		for n in range(0,ran):
			lis.pop(0)
		elapsed = round(time.time() - start,5)
		return elapsed
	elif pos == "back":
		start = time.time()
		for n in reversed(range(ran,0)):
			lis.pop(n)
		elapsed = round(time.time() - start,5)
		return elapsed



def main():

	t = []
	u = []
	v = []
	ta = []
	ua = []
	va = []

	x = arraylist.arrayList()
	y = arraylist.arrayList()
	z = arraylist.arrayList()
	xa = arraylist.arrayList()
	ya = arraylist.arrayList()
	za = arraylist.arrayList()
	
	a = pointerlist.pointerList()
	b = pointerlist.pointerList()
	c = pointerlist.pointerList()
	aa = pointerlist.pointerList()
	ba = pointerlist.pointerList()
	ca = pointerlist.pointerList()

	pyA = pyins(t,2000,"front")
	pyB = pyins(u,4000,"front")
	pyC = pyins(v,8000,"front")

	arrA = instime(x,2000,"front")
	arrB = instime(y,4000,"front")
	arrC = instime(z,8000,"front")

	pointA = instime(a,2000,"front")
	pointB = instime(b,4000,"front")
	pointC = instime(c,8000,"front")

	print "=============INSERT(Front)=========="
	print "|SIZE|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "|2000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "|4000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "|8000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "===================================="

	pyA = pyins(ta,2000,"back")
	pyB = pyins(ua,4000,"back")
	pyC = pyins(va,8000,"back")

	arrA = instime(xa,2000,"back")
	arrB = instime(ya,4000,"back")
	arrC = instime(za,8000,"back")

	pointA = instime(aa,2000,"back")
	pointB = instime(ba,4000,"back")
	pointC = instime(ca,8000,"back")

	print "=============INSERT(Back)==========="
	print "|SIZE|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "|2000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "|4000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "|8000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "===================================="


	pyA = pyret(t,2000)
	pyB = pyret(u,4000)
	pyC = pyret(v,8000)
	
	arrA = rettime(x,2000)
	arrB = rettime(y,4000)
	arrC = rettime(z,8000)

	pointA = rettime(a,2000)
	pointB = rettime(b,4000)
	pointC = rettime(c,8000)

	print "============RETRIEVE================"
	print "|SIZE|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "|2000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "|4000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "|8000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "===================================="


	pyA = pydel(t,2000,"front")
	pyB = pydel(u,4000,"front")
	pyC = pydel(v,8000,"front")

	arrA = deltime(x,2000,"front")
	arrB = deltime(y,4000,"front")
	arrC = deltime(z,8000,"front")

	pointA = deltime(a,2000,"front")
	pointB = deltime(b,4000,"front")
	pointC = deltime(c,8000,"front")

	print "=============DELETE(Front)=========="
	print "|SIZE|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "|2000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "|4000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "|8000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "===================================="


	pyA = pydel(ta,2000,"front")
	pyB = pydel(ua,4000,"front")
	pyC = pydel(va,8000,"front")

	arrA = deltime(xa,2000,"front")
	arrB = deltime(ya,4000,"front")
	arrC = deltime(za,8000,"front")

	pointA = deltime(aa,2000,"front")
	pointB = deltime(ba,4000,"front")
	pointC = deltime(ca,8000,"front")

	print "=============DELETE(Back)==========="
	print "|SIZE|DATSTRUCT|__ARRAY__|_POINTER_|"
	print "|2000|",format(pyA,'.5f'),"|",format(arrA,'.5f'),"|",format(pointA,'.5f'),"|"
	print "|4000|",format(pyB,'.5f'),"|",format(arrB,'.5f'),"|",format(pointB,'.5f'),"|"
	print "|8000|",format(pyC,'.5f'),"|",format(arrC,'.5f'),"|",format(pointC,'.5f'),"|"
	print "===================================="


if __name__ == "__main__":
	main()
