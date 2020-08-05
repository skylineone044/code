import random
from _datetime import datetime
from datetime import date

def setup():
	#setting up necessary files for the program to run correctly
	with open("saved_data.txt", "a+"):
		pass
	with open("saved_data.txt", "r") as setupFile:
		data = setupFile.readlines(1)
		data = "".join(data)
	if "denominator" in data:
		#checkin wether there is already the "explaination" in the file
		pass
	else:
		with open("saved_data.txt", "a+") as saveFile:
			lenght = len(hrs) + 3
			saveFile.write(lenght * " " + "denominator" + 5 * " " + "average tries" + "\n")
			saveFile.write(datum + "\n")
	with open("date_data.txt", "a+"):
		pass



def calculator(num2, denominator):
	#this function calculates the average tries, is the backbone of this project
	global dn
	dn = denominator
	def checker(num2):
		#this function calculates the tries
		n1 = random.randint(0, num2)
		n2 = random.randint(0, num2)
		global tries
		tries = 0	
		while n1 != n2:
			n1 = random.randint(0, num2)
			n2 = random.randint(0, num2)
			tries += 1
		return tries
	n = 0
	sumtries = 0
	while n < denominator:
		checker(num2)
		n += 1
		sumtries += tries
	avgTries = sumtries / denominator
	global avgT
	avgT = avgTries



def writeToFile(denominator, avgTries, timeDate, timeHrs):
	#this function writes all of the results with timestamps
	#to the saved_data.txt file
	with open("date_data.txt", "r") as rData:
		try:
			global xdata
			xdata = rData.readlines()[-1]
			#reading only the last line to go easy on memory
			xdata = "".join(xdata)
		except IndexError:
			#if it is the firs time running, its gonna return an error
			#because there is no lines to read so we just write it in
			#and set xdata equal to the date given
			with open("date_data.txt", "a") as wData:
				wData.write(timeDate)
				xdata = datum
		if timeDate in xdata:
			#if the current date matches the last one in the date_data.txt
			#file we add only the hours so we get a cleaner result
			with open("saved_data.txt", "a") as sData:
				lenght = 16 - len(str(denominator))
				sData.write(timeHrs + " | " + str(denominator) + lenght * "-" + str(avgTries) + "\n")
		else:
			#if the two dates does not match, we write the date in date_data.txt
			#and in saved_data.txt and add the hours and data afterwards
			with open("date_data.txt", "a") as dData:
				dData.write("\n" + timeDate)
			with open("saved_data.txt", "a") as sData:
				sData.write(timeDate + "\n")
				lenght = 16 - len(str(denominator))
				sData.write(timeHrs + " | " + str(denominator) + lenght * "-" + str(avgTries) + "\n")



def main():
	#this function houses all the others and the time variables
	today = date.today()
	now = datetime.now()
	global datum
	datum = today.strftime("%B %d %Y")
	global hrs
	hrs = now.strftime("%H:%M:%S")
	setup()
	calculator(1000, 10)
	#first: the interval of numbers we want to compare(from 0-number given)
	#second: how may times we want to run it
	writeToFile(dn, avgT, datum, hrs)
	#first: how many times we ran the calculations
	#second: the averave of tries
	#third: date of executing
	#fourth: time of executing

main()
#calling the main function, basically executing the code