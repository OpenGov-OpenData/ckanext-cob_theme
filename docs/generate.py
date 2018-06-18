import os
import re
import sys
import shutil
import csv
import errno

def main():
   # take directory as argument
   directory = sys.argv[1];

   # creates new folder docs, the copy of ckan will be added to
   destination = "./doc"

   # if directory already exists, delete and recreate with new edits
   if os.path.exists(destination):
	shutil.rmtree(destination)
    
   # enter CSV file
   inputs = "./replace.csv"
   
   # call method createNewScript
   createNewScript(directory, destination, inputs)

def createNewScript(directory, destination, inputs):
	# create dictionary to store all inputs and outputs from the given CSV file
        dictionary = {}
	try:
	    # read csv file and get/set parameters
	    with open(inputs, 'rU') as csvfile:
		csvreader = csv.reader(csvfile)
                it = iter(csvreader)
                it.next()
		for row in csvreader:
		    dictionary[row[0]] = row[1]

	    shutil.copytree(directory, destination)
	    
	except IOError as e:
	    print e
	     
	try:
	    # modify all the files
	    for root, dirs, files in os.walk(destination):
		for file in files:
		    if file.endswith(".rst"):
		        absoluteFile = os.path.join(root, file)
                        # loop through the dictionary
		        for i in dictionary:
				curFile = []
				with open(absoluteFile) as targetFile: 
				     content = targetFile.readlines()
                                     # modify content
				     for line in content:
				         line = re.sub(r"(?<!\w)" + re.escape(i) + r"(?!\w)", dictionary[i], line)
				         curFile.append(line)
				with open(absoluteFile, 'w') as targetFile: 
				     for line in curFile:
				         targetFile.write(line)

	# will create all the parent directories
	except IOError as e:
	    if e.errno != errno.ENOENT:
		raise
	    os.makedirs(os.path.dirname(destination))
# call main method
if __name__ == '__main__':
	main()
