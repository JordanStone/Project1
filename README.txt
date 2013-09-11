NAME: Jordan Stone

CONTENTS:
All program code is written in Python and are in the .py format.
	Folder Project1:
		README.txt - text document detailing the files submitted in this project and
		completeness of every section of the project.

		REPORT.txt - text document detailing results from the time tests used in
		this project and analysis of these results.

	Folder p1:
		arraylist.py - contains the code for the class arrayList.py, an array
		implementation of a list ADT.

		pointerlist.py - contains the code for the class pointerList.py, a pointer
		implementation of a list ADT, i.e. a linked list.

		test.py - test code that goes through all functions of both list
		implementations and compares them to expected or built-in object results.

	Folder p2:
		arraystack.py - contains the code for the class arrayStack.py, an array
		implementation of a stack ADT.

		pointerstack.py - contains the code for the class pointerStack.py, a pointer
		implementation of a stack ADT.

		test.py - test code that goes through all functions of both stack
		implementations and compares them to expected or built-in object results.

	Folder p3:
		test.py - test code that measures and displays time taken for both
		constructed list implementations to INSERT, RETRIEVE, and DELETE data, compared
		to time taken by a built-in list.

		arraylist.py - contains the code for the class arrayList.py, an array
		implementation of a list ADT.

		pointerlist.py - contains the code for the class pointerList.py, a pointer
		implementation of a list ADT, i.e. a linked list.

	Folder p4:
		test.py - test code that measures and displays time taken for both
		constructed stack  implementations to PUSH and POP data, compared to time taken
		by a built-in stack.

		arraystack.py - contains the code for the class arrayStack.py, an array
		implementation of a stack ADT.

		pointerstack.py - contains the code for the class pointerStack.py, a pointer
		implementation of a stack ADT.

COMPLETE:
	Problems p1, p2, and p3 are complete without issue as far as I can see.

UNFINISHED:
	On problem 4, the pointer implementation is observed to display a
	strangely low time for size 15000. This time is lower than the one for
	10000. Also, the 20000 time is only slightly larger than the 10000 time,
	which does not seem to be the expected result. 
	
	I am unsure what is causing this strange time, and do not know whether 
	it is linked to the ADT or to the test code.

COMPILATION & EXECUTION:
	Each relevant piece of code for each problem is the default of their
	included makefiles, and can be run by "make", as well as "make test".
	This will run the test.py in p1, p2, p3, and p4.

TEST CASES:
	Test cases for both the list implementations and stack implementations
	make use of functions that assume a generic list or stack and compare it
	to the behavior of the built-in list for Python, which can act as either
	a list or a stack. 
	
	The test cases assume common functionality of the ADTs and do not
	currently test for every possible case. Still, the test cases confirm that
	the constructed ADTs are adequate for the required time testing they are
	meant to undergo.

PROGRAM OUTPUT:
	The list and stack ADTs do not output anything to console unless there is
	an error with given input in a function.

	Test.py for p1 and p2 output results for various method tests - which ADT
	is being tested and how so is labeled, followed by the result of the test.
	
	Test.py for p3 and p4 will output the tables for each time test. 
	p3 includes time tables for INSERT (from the front and in back), RETRIEVE
	(transversal), and DELETE (from the front and in back).
	p4 includes time tables for PUSH and POP.
