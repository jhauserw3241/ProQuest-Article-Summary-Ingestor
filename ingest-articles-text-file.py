# Import libraries
import xlsxwriter
import os
import sys
from datetime import datetime

# Assign global variables
HEADER_FILE = "headers.txt"
ARTICLE_SEPARATOR = "____________________________________________________________\n"

def main():
    # Read in arguments
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    # Get the start time of the current process
    start = datetime.now()

    # Open the Excel file
    workbook = xlsxwriter.Workbook(output_file_path)
    worksheet = workbook.add_worksheet()

    worksheet_row_index = 0

    # Pull in the article headers
    possible_headers = []
    with open(HEADER_FILE, "r") as header_file:
        header_index = 0
        for header_line in header_file.readlines():
            header = header_line.split("\n")[0]
            possible_headers.append(header)
            worksheet.write(worksheet_row_index, header_index, header)
            header_index += 1

    # Storage objects
    article = {}
    article_info_line_index = 0
    current_header = ""

    # Open the input text file
    with open(input_file_path, "r") as input_file:
        # Read through every line of the input file
        for line in input_file.readlines():
            # Discard empty lines
            if line == "\n":
                continue
            # Handle line separators 
            elif line == ARTICLE_SEPARATOR:
                # Go through all the headers
                for header_index in range(len(possible_headers)):
                    # Get the current header
                    header_val = possible_headers[header_index]

                    # Get the content for the current header within the article
                    content_val = ""
                    if header_val in article:
                        content_val = article[header_val]
                    
                    # Write out the contents for the header in the Excel worksheet
                    worksheet.write(worksheet_row_index, header_index, content_val)
                worksheet_row_index += 1

                # Empty out the article object
                article = {}
                current_header = ""
                article_info_line_index = 0
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
                    line_contents = line_text

                # Handle where there is an unexpected header
                if line_header != "" and line_header in possible_headers:
                    # Update the current header for the content
                    current_header = line_header
                else:
                    # Add the value that was assumed to be a header back to the content
                    line_contents = line_text
                
                # Add a key with the current header value to the article representation if it doesn't exist
                if current_header not in article:
                    article[current_header] = ""

                # Handle the short hand for the article title
                if article_info_line_index == 0:
                    continue
                # Handle the relevant links for the artcle
                elif current_header == "Links":
                    if article[current_header] == "":
                        article[current_header] = line_contents
                    else:
                        article[current_header] = "{}\n{}".format(article[current_header], line_contents)
                # Separate out the document URL from the publication information
                elif current_header == "Publication info" and "http" in line_contents:
                    article["Document URL"] = line_contents
                # Handle every other piece of information
                else:
                    if article[current_header] == "":
                        article[current_header] = line_contents
                    else:
                        article[current_header] = "{}\n{}".format(article[current_header], line_contents)

            article_info_line_index += 1

    # Close the Excel file
    workbook.close()

    # Print out the total time taken to run the script
    end = datetime.now()
    diff_time = end - start
    print("Total Time: {} seconds".format(diff_time.total_seconds()))

if __name__ == "__main__":
    main()