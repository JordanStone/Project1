#!/usr/bin/python
#arraystack.py
#

import sys

MAXLENGTH = 1000000

class arrayStack:

	def __init__(self, roof=MAXLENGTH):
		self.arr = [None] * MAXLENGTH
		self.top = roof
	
	def PUSH(self, x):
		if self.top == 0:
			print "Error, Stack is full."
		else:
			self.top = self.top - 1
			self.arr[self.top] = x
	
	def POP(self):
		if self.EMPTY():
			print "Error, Stack is empty."
		else:
			self.top = self.top + 1

	def TOP(self):
		if self.EMPTY():
			return None
		else:
			return self.arr[self.top]

	def EMPTY(self):
		if self.top >= MAXLENGTH:
			return True
		else:
			return False

	def MAKENULL(self):
		self.top = MAXLENGTH
