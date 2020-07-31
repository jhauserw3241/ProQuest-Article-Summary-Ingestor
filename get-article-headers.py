# Import libraries
import os
import sys
from datetime import datetime

# Assign global variables
ARTICLE_SEPARATOR = "____________________________________________________________\n"

def main():
    # Get arguments
    input_file_path = sys.argv[1]

    # Get the start time of the current process
    start = datetime.now()

    # Storage objects
    unique_headers = []

    # Open the input text file
    with open(input_file_path, "r") as input_file:
        # Read through every line of the input file
        for line in input_file.readlines():
            # Discard empty lines
            if line == "\n":
                continue
            # Handle line separators 
            elif line == ARTICLE_SEPARATOR:
                continue
            # Handle rows with content
            else:
                # Remove the newline from the end of the line
                line_text = line.split("\n")[0]

                # Attempt to pull the header out of the line
                line_parts = line_text.split(": ")
                line_header = ""
                line_contents = ""
                # Handle lines where there is a value that looks like a header
                if len(line_parts) > 1:
                    line_header = line_parts[0]
                    line_contents = ": ".join(line_parts[1:len(line_parts)])
                # Handle lines where there does not appear to be a header
                elif len(line_parts) == 1:
                    line_contents = line_parts[0]

                # Add any new non-empty headers to the list of unique headers
                if line_header != "" and line_header not in unique_headers:
                    unique_headers.append(line_header)

    # Output the unique headers to a text file
    with open("headers.txt", "w") as output_file:
        for header in unique_headers:
            output_file.write(header + "\n")

    # Print out the total time taken to run the script
    end = datetime.now()
    diff_time = end - start
    print("Total Time: {} seconds".format(diff_time.total_seconds()))

if __name__ == "__main__":
    main()
