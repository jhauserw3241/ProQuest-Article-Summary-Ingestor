# Import libraries
import xlsxwriter
import os
import sys
from datetime import datetime

# Assign global variables
INPUT_FILE = "../ProQuestDocuments-2020-07-27.txt"
OUTPUT_XLSX_FILE = "../test-output.xlsx"
ARTICLE_SEPARATOR = "____________________________________________________________\n"

def main():
    # Get the start time of the current process
    print("Start")
    start = datetime.now()

    # Open the Excel file
    workbook = xlsxwriter.Workbook(OUTPUT_XLSX_FILE)
    worksheet = workbook.add_worksheet()

    # Open the input text file
    with open(INPUT_FILE, "r") as input_file:
        # Read through every line of the input file
        for line in input_file.readlines():
            # Discard empty lines
            if line == "\n":
                continue
            # Handle line separators 
            elif line == ARTICLE_SEPARATOR:
                continue
            else:
                print(line)

    # Close the Excel file
    workbook.close()

    # Print out the total time taken to run the script
    print("End")
    end = datetime.now()
    diff_time = start - end
    print("Total Time: {} seconds".format(diff_time.seconds / 3600))

if __name__ == "__main__":
    main()