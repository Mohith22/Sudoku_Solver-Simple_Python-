#Sudoku Solver Using BackTracking
#Author : Mohith Damarapati-NIT Surat-BTech:3rd year-Computer Science
#Date : 19/12/2016


#This Program Shows All The Possible Solutions For A Given Sudoku

#Note : It Is Recommended To Input A Single Solution Soduko For Good Results

''' --------------------------------------------------------------------------- '''


#Import NumPy 

import numpy as np 

#Sudoku Grids - 9*9 - Initialize all grids to zeros

sudoku = np.zeros((9,9),dtype=int)

#Row Checking
def checkr(val,r,c):
	for i in range(9):
		if sudoku[r][i]==val and i!=c:
			return False
	return True

#Column Checking
def checkc(val,r,c):
	for i in range(9):
		if sudoku[i][c]==val and i!=r:
			return False
	return True

#Box Checking
def checkb(val,r,c):
	rs=r-r%3
	cs=c-c%3
	for i in range(3):
		for j in range(3):
			if sudoku[i+rs][j+cs]==val and (i+rs!=r or j+cs!=c):
				return False
	return True

def check(val,r,c):
 	'''print sudoku
	print val
	print r
	print c'''
	if (checkr(val,r,c)) and (checkc(val,r,c)) and (checkb(val,r,c)): 
		#print "Working"
		return True
	else:
		return False

#sudoku_solve Function - Solves Sudoku Using BackTracking
def sudoku_solve(i,j):
	if i==9:
		print "Solved Sudoku Is: \n"
		for k in range(9):
			print "|",
			for l in range(9):
				print sudoku[k][l],
				print "|",
			print "\n"
	if i!=9:
		if d[i][j]!=0:
			if j==8:
				s = sudoku_solve(i+1,0)  
			else:
				s = sudoku_solve(i,j+1)
		else:
			
			while True:
				sudoku[i][j]+=1
				if check(sudoku[i][j],i,j):
					if j==8:
						s = sudoku_solve(i+1,0)
					else:
						s = sudoku_solve(i,j+1)
				if sudoku[i][j]==9:
					sudoku[i][j]=0
					break

#Sudoku-Solver User Interface

print "*** Sudoku Solver ***"
print "\n "
print "Rules For Enterning Input :"
print "- Enter Valid Number Only - (1 to 9)"
print "- Enter 0 For Blank Entries"
print "- Enter From Left To Right (For Each Row)"
print "\n "

print "Enter Each Character And Press Enter"
print "\n"

#Input The Sudoku

for i in range(9):
	for j in range(9):
		sudoku[i][j] = input()
d = sudoku
x = 0

#Calling sudoku_solve Function
ans = sudoku_solve(0,0)















