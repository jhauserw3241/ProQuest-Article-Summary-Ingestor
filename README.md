# ProQuest-Article-Summary-Ingestor

## Objective
The ProQuest website provides a database of articles that researchers can review about specific topics. This searching functionality allows you to download a lot of information about the articles into an Excel file. However, they do not provide the ability for a user to download the full text of the article through the GUI. The ProQuest database does provide the full text within a text file. The goal of this script is to turn the text file into an Excel file for ease of reading.

## Technology Stack
These scripts use Python 3. The Python xlsxwriter library is used for the creation and modification of Excel files in this script.

## Steps
Follow the below steps to utilize the scripts.
1. Run a search on the ProQuest database.
2. Download the results of the search into the text file format. The text file should match the included example-input.txt. Additionally, all of the results need to be consolidated into one text file before feeding the results into the Python script.
3. Create a Python virtual environment. Reference: https://docs.python.org/3/library/venv.html
4. Activate the virtual environment.

    `source <name of virtual environment>\bin\activate`
5. Import the list of required libraries into the virtual environment.

    `pip install -r requirements.txt`
6. Run the get-article-headers.py script to get the list of possible headers from the input text file. The headers are identified by being the first phrase in a line in the text file before the characters ": ".

    `python get-article-headers.py  <path-to-input-text-file>.txt`
7. Delete any lines of text from the possible headers file (headers.txt) that aren't expected headers. The list of possible headers will be newline delimited.
8. Run the ingestor script on the input file.

    `python ingest-articles-text-file.py <path-to-input-text-file>.txt <path-to-output-excel-file>.xlsx`

Note: The file that the results will be overwritten and any contents of that file will be deleted.
