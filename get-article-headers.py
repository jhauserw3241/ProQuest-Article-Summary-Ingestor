# Import libraries
import os
import sys
from datetime import datetime

# Assign global variables
INPUT_FILE = "../ProQuestDocuments-2020-07-27.txt"
OUTPUT_XLSX_FILE = "../test-output.xlsx"
ARTICLE_SEPARATOR = "____________________________________________________________\n"

def main():
    # Get the start time of the current process
    start = datetime.now()

    # Storage objects
    article = {}
    headers = ["Title", "Abstract", "ISSN", "Document type", "Author", "Publication info", "Links", "Full text", "Credit", "Subject", "Location", "Publication title", "Publication year", "Publication date", "Section", "Publisher", "Place of publication", "Country of publication", "Publication subject", "Source type", "Language of publication", "First page" "ProQuest document ID", "Document URL", "Copyright", "Last updated", "Database"]
    article_info_line_index = 0
    current_header = ""

    unique_headers = []

    # Open the input text file
    with open(INPUT_FILE, "r") as input_file:
        # Read through every line of the input file
        for line in input_file.readlines():
            # Discard empty lines
            if line == "\n":
                continue
            # Handle line separators 
            elif line == ARTICLE_SEPARATOR:
                #for key in article:
                #    print(key + ": " + article[key])

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
                    line_contents = line_parts[0]

                if line_header != "" and line_header not in unique_headers:
                    unique_headers.append(line_header)

                """
                # Handle where there is an unexpected header
                if line_header != "" and line_header in headers:
                    # Update the current header for the content
                    current_header = line_header
                else:
                    # Add the value that was assumed to be a header back to the content
                    line_contents = ": ".join(line_parts[0:len(line_parts)])
                
                # Add a key with the current header value to the article representation if it doesn't exist
                if line_header not in article:
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
                elif current_header == "Publication info" and article_info_line_index == 2:
                    article["Document URL"] = line_contents
                # Handle every other piece of information
                else:
                    article[current_header] = "{}\n\n{}".format(article[current_header], line_contents)

            article_info_line_index += 1
            """
    for header in unique_headers:
        print(header)

    # Print out the total time taken to run the script
    end = datetime.now()
    diff_time = end - start
    print("Total Time: {} seconds".format(diff_time.total_seconds()))

if __name__ == "__main__":
    main()