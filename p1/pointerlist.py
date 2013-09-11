#!/usr/bin/python
#pointerlist.py
#

import sys

class _Node:
	def __init__(self, cargo=None, link=None):
		self.car = cargo
		self.link = link
	def __str__(self):
		return str(self.car)

class pointerList:

	def __init__(self):
		self.head = _Node()
		
	def FIRST(self):
		if self.head.car == None:
			return self.END()
		else: 
			return 0

	def END(self):
		count = 0
		q = self.head
		while q.link != None:
			count += 1
			q = q.link
		return count

	def RETRIEVE(self, p):
		count = 0
		q = self.head
		while count != p:
			count += 1
			q = q.link
		return q.car

	def LOCATE(self, x):
		count = 0
		q = self.head
		while q.car != x:
			count += 1
			q = q.link
		return count

	def NEXT(self,p):
		if p < 0:
			return -1
		return p + 1

	def PREVIOUS(self,p):
		if p < 0:
			return -1
		count = 0
		q = self.head
		while count != p-1:
			count += 1
			q = q.link
		return count

	def INSERT(self, x, p):
		if self.head is None:
			self.head = _Node(x)
		elif p == 0:
			self.head = _Node(x, self.head)
		else:
			count = 0
			q = self.head
			while count < p-1:
				count += 1
				q = q.link
			q.link = _Node(x, q.link)

	def DELETE(self,p):
		if self.head is None:
			print "Error, list is empty."
		elif p == 0:
			self.head = self.head.link
		else:
			count = 0
			q = self.head
			while count != p-1:
				count += 1
				q = q.link
			q.link = q.link.link
			self = q

	def MAKENULL(self):
		self.head.link = None
		self.head.car = None
		return self
