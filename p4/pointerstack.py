#!/usr/bin/python
#pointerstack.py
#

import sys

class _Node:
	def __init__(self, cargo=None, link=None):
		self.car = cargo
		self.link = link
	def __str__(self):
		return str(self.car)

class pointerStack:	
	def __init__(self):
		self.head = _Node()

	def PUSH(self, x):
		newHead = _Node(x,self.head)
		self.head = newHead
	
	def POP(self):
		head = self.head
		self.head = head.link

	def TOP(self):
		if self.EMPTY():
			print "Error, stack is empty."
		else:
			return self.head.car

	def EMPTY(self):
		if self.head.car == None:
			return True
		else:
			return False

	def MAKENULL(self):
		self.head.car = None
		self.head.link = None
