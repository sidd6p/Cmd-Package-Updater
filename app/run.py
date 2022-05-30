import readFile, showTable
import getopt, sys


args_list = sys.argv[1:]

options = "i:u"
long_option = ["input=", "update"]

try:
    arguments, values = getopt.getopt(args_list, options, long_option)
    data = ""

    for current_arguments, current_values in arguments:
        if (current_arguments.lower() in ("-i", "--input")):
            data = readFile.read(current_values)
        elif (current_arguments.lower() in ("-u", "--update")):
            print ("Updating the file....")

    if (len(data) != 0):
        showTable.show(data)

except getopt.error as error:
    print (str(error))
