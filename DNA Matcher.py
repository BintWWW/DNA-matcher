import os
import datetime
import time
from random import *
def main():
	# ------ CONSTANTS ----------
	READDATA   =  1
	PRINTDATA  =  2
	SIM_X      =  3
	EXIT       =  5
	TOUCH      =  4
	ERROR      = -1	
	
	# ------- Parallel Arrays -------
	firstNames = []
	lastNames  = []
	genders    = []
	ages       = []
	DNAs       = []
	theDNA     = []
	date       = []
	gotDATA = False  # flag to tell if we've already loaded a datafile
	
	choice = -1  # bogus setting to get us started
	
	while (choice != EXIT):
		print ("\n\n----------------------------------------------")
		print ("  1  -  Read DATA file")
		print ("  2  -  Print DATA file");
		print ("  3  -  Simulation");
		print ("  4  -  Touch")
		print ("  5  -  EXIT");
		
		print ("---------------------------")
		choice = input("ENTER: ")
		
		# trap bad user input
		if ( (str(READDATA) <= choice) and (choice <= str(EXIT)) ):
			# force to an integer, for example "1" to 1
			choice = eval(choice)			
		else:
			badInput = choice
			# force to an integer to test below
			choice = ERROR;		
			
		# ============ 1: READ DATA FILE =============================
		if ( choice == READDATA):
			getDATA( firstNames, lastNames, genders, ages, DNAs )
		
		# ============ 2: PRINT DATA FILE  =============================
		elif (choice == PRINTDATA):
			printDATA( firstNames, lastNames, genders, ages, DNAs )
			

		# ============ 3: SIMULATION =============================	
		elif (choice == SIM_X):
			sim_DNA( firstNames, lastNames, genders, ages, DNAs ,theDNA,date)	
		
		
		# ============ 5: EXIT =====================================	
		elif (choice == EXIT):
			
			print ("Goodbye ...")	
		# =============4: Touch========================================
		elif (choice == TOUCH):
			randomTouch(theDNA, DNAs, date,firstNames,lastNames, genders, ages)
		
		# ============ ? HUH ? =====================================
		else:  
			print ("ERROR: ", badInput, "is an invalid input. Try again.")	
	
	# end WHILE input is not EXIT
	
	print ("\n\nDone.\n")
# end main	


#-----------\
# getDATA()  \
#-----------------------------------------------------------
def getDATA( firstNames, lastNames, genders, ages, DNAs ):
	
	n = 0
	dB = input("Enter filename: ")

	if not os.path.exists(dB):
		print("\nSORRY, the file", dB, "does not exist.")
		print("Try another filename ...")
		
	else:	
		print("Open file", dB, "here, read lines, and store in arrays")
		File = open(dB,'r')
		for nextLine in File:
			fName, lName, gender, age, DNA = nextLine.split(':')
			firstNames.append(fName)
			lastNames.append(lName)
			genders.append(gender)
			ages.append(age)
			DNA = DNA.strip()
			DNAs.append(DNA)
			n+=1
		print("\n", n, "Records were read from the file", dB, "\n") 
		
		
	# else filename OK
	
# end getDATA()

#-------------\
# printDATA()  \
#-----------------------------------------------------------
def printDATA( firstNames, lastNames, genders, ages, DNAs ):
	x = len(firstNames)
	i =0
	print("First Name |Last Name  |Gender|Age| DNA(first 10 bp)")
	while (i<x):
		print("%-10s |%-10s |  %1s   | %s| %10s"% (firstNames[i],lastNames[i],genders[i],ages[i],DNAs[i][:10]),"...",sep="")
		i+=1
		

# end printDATA()
	

#----------\
# sim_DNA() \
#-----------------------------------------------------------
def sim_DNA( firstNames, lastNames, genders, ages, DNAs,theDNA ,date):
	
	
	FS = input("Enter filename: ")

	if not os.path.exists(FS):
		print("\nSORRY, the file", FS, "does not exist.")
		print("Try another filename ...")
	else:
		print("Open file", FS)
		FileSim = open(FS,'r')
		for nextLinefs in FileSim:
			nextLinefs = nextLinefs.strip()
			
			x,y = nextLinefs.split(',')
			date.append(x)
			theDNA.append(y)
	
	linearSearch( theDNA, DNAs, date , firstNames, lastNames, genders, ages)
	
# end sim_DNA()

#-------------\
# linearSearch \
#-----------------------------------------------------------
def linearSearch( theDNA, DNAs, date,firstNames,lastNames, genders, ages ):
	thex = len(theDNA)
	DNAx = len(DNAs)
	D=0
	Ds=0
	i=0
		
	go = True
	while (go ==True):
		
		while (DNAs[Ds].find(theDNA[D])!=-1 and len(theDNA[D])>9 and go ==True):
			check = DNAs[Ds].find(theDNA[D])
			print("^"*45)
			print("MATCH FOUND! Entry made at: ", date[Ds])
			print("%-10s |%-10s |  %1s   | %s |"% (firstNames[Ds],lastNames[Ds],genders[Ds],ages[Ds]))
			lower = theDNA[D].lower()
			print(DNAs[Ds])
			print(DNAs[Ds][:check],lower,DNAs[Ds][check+len(theDNA[D]):],sep='')
			print("="*45)
			
			if(D+1==thex):
				go =False
				D = D-1
			D+=1
			Ds=0
			
		Ds+=1
		if(len(theDNA[D])<MIN_DNA_LENGTH):
			print("DNA sequence obtained NOT long enough. ")
			print(theDNA[D], "is only ",len(theDNA[D]), " bp")
			print("Must be at least 10 bp")
			D+=1
			
		if(Ds+1>DNAx):
			print("WHOA! No DNA Match found for: ",theDNA[D],"\nWHO IS THIS???  WARNING: individual NOT in database! ")
			print("="*45)
			Ds=0
			D+=1
			
		
	
# end linearSearch()
def randomTouch(theDNA, DNAs, date,firstNames,lastNames, genders, ages):
	ntime = time.strftime("%H:%M:%S")
	ndate = time.strftime("%d/%m/%Y")

#-----------\
# START HERE \
#-----------------------------------------------------------	
if (__name__ == '__main__'):
	
	# CONSTANTS
	NOTFOUND = -1
	MIN_DNA_LENGTH = 10
	
	main()

#-----------------------------------------------------
