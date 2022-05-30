from ast import arg
import getopt, sys

args_list = sys.argv[1:]

options = "i:u"
long_option = ["input=", "update"]

try:
    arguments, values = getopt.getopt(args_list, options, long_option)

    for current_arguments, current_values in arguments:
        if (current_arguments.lower() in ("-i", "--input")):
            print ("Input File is {}".format(sys.argv[-1]))
        elif (current_arguments.lower() in ("-u", "--update")):
            print ("Updating the file....")

except getopt.error as error:
    print (str(error))
