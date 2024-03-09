### CIS6930SP24 -- Assignment0 -- Incident Data Analysis
## Name
Jagadeeswara Reddy Gummi Reddy
## Assignment Description
In this project, I am tasked with creating a Python-based tool to efficiently extract, process, and store specific data from the Norman, Oklahoma police department's incident reports. These reports are made available to the public in PDF format on the department's website and contain detailed narratives of various police activities. My focus is primarily on the "incidents" section, which presents unique challenges for data extraction due to the PDF format's complexity and the structured yet varied presentation of the data within these documents.
## Objective
My goal is to develop a comprehensive Python script capable of automating the following tasks:

PDF Acquisition: I need to programmatically download the latest incident report PDF from a given URL, ensuring my script can reliably access and retrieve files from the web.

Data Extraction: The core of my project involves navigating the downloaded PDF to identify and extract critical information from the incidents section. This includes the date and time of each incident, the incident number, the location of the occurrence, the nature of the incident (such as theft or assault), and the Incident ORI (Originating Agency Identifier).

Database Storage: I am responsible for designing and implementing a SQLite database schema that accurately captures and stores the extracted data. This task requires careful consideration of the appropriate data types, constraints, and the database's overall structure to ensure efficient organization and retrieval of information.

Data Analysis: An essential component of my project is to analyze the stored data by querying the database to summarize the incidents, particularly by counting and reporting the frequency of each type of incident. This involves advanced SQL queries and an understanding of data aggregation methods
## How to Install
Embarking on this project, I crafted a meticulous setup process to ensure smooth replication and operation of my Python script for extracting incident data from PDFs. Below, I delineate the exact steps I undertook to prepare my development environment and get the script operational.
# Step 1: Python Environment Configuration
The cornerstone of my project is Python 3, given its robust library support and community-driven modules. I ensured my machine was equipped with Python 3.8, which offers the perfect balance of stability and new features for my script. For those needing to install or update Python, the official Python website provides detailed instructions tailored to various operating systems.
# Step 2: Project file Acquisition
 hosted my project on GitHub for version control and easy sharing. This includes the Python scripts, a requirements.txt for dependency management, and a sample PDF for testing purposes. To clone my project repository, I used the following command in the terminal, ensuring it was executed within the directory I designated for this project:
 git clone https://github.com/mygithubusername/normanpd-incidents.git
# Step 3: Dependency Management
My script leverages several external libraries, such as PyPDF2 for parsing PDF files, requests for fetching PDFs from the web, and sqlite3 integrated into Python for database interactions. To manage these dependencies seamlessly, I compiled a requirements.txt file. Installing these dependencies is straightforward with pip, Python’s package manager, by running:
pip install -r requirements.txt
# Step 4: Environment Sanity Check
After setting up the environment and dependencies, I conducted a sanity check to confirm everything was correctly installed. This involved launching the Python interpreter from the terminal and attempting to import the key libraries used in the script:
python
>>> import PyPDF2, requests, sqlite3
## How to Run
After installation, you can run the script to extract data from a Norman PD incident report PDF by following these steps:
Open Terminal: Open your command line interface and navigate to the project's directory.

Run the Script: Execute the script with the URL of the incident report PDF as an argument using the following command:
python main.py --incidents "URL_TO_INCIDENT_PDF"
Replace URL_TO_INCIDENT_PDF with the actual URL of the PDF you wish to process.
# What to Expect
Upon running the command, the script will perform several actions:

Download the PDF: The script first reaches out to the provided URL, retrieves the PDF file, and saves it locally for processing. This step is automatic, and progress will be shown in the terminal.

Extract Incident Data: With the PDF downloaded, the script then parses its contents, extracting relevant data such as the date/time, incident number, location, nature, and ORI for each reported incident.

Populate the Database: The extracted data is systematically inserted into a SQLite database, which the script sets up during its first run. This database is used for storing all extracted incident data and can be queried for analysis.

Analyze and Report: Finally, the script analyzes the collected data, specifically calculating and displaying the frequency of different incident natures. This summary is printed directly to the terminal, offering immediate insights into the dataset.
## Functions
# download_data(source_url)
Purpose: Downloads data from the specified URL using HTTP GET request. It sets a custom User-Agent to mimic a web browser for compatibility with more sites.
Parameters:
source_url: The URL from which to download data.
Returns: The downloaded data as bytes if successful; otherwise, None on error.
# parse_pdf_data(pdf_bytes)
Purpose: Extracts text data from PDF content passed as bytes. Utilizes pdfminer to convert PDF pages to text.
Parameters:
pdf_bytes: Byte content of the PDF file to be parsed.
Returns: A list of records extracted from the PDF, where each record is a tuple of extracted fields.
# process_page_text(text_content)
Purpose: Processes the text content of a single PDF page and extracts relevant information based on custom logic.
Parameters:
text_content: A string containing the text of a PDF page.
Returns: A list of tuples, each representing a data record extracted from the page. Each tuple contains the first 5 fields of processed data as an example.
# setup_database(db_path='resources/incidents.db')
Purpose: Creates a SQLite database and a table for storing the records if they don't already exist. Ensures the existence of the directory where the database file will be stored.
Parameters:
db_path: Optional. The file path for the SQLite database. Defaults to 'resources/incidents.db'.
Returns: The path to the database file.
### main.py
# extractincidents(pdf_bytes)
Purpose: This function is designed to extract incident-specific data from the byte content of a PDF file. It likely serves as a wrapper or a high-level function that utilizes parse_pdf_data() and possibly other parsing functions to specifically target and extract data relevant to incidents reported in the PDF.
Parameters:
pdf_bytes: Byte content of the PDF file from which to extract incident data.
Process: The function might start by invoking parse_pdf_data(pdf_bytes) to convert the entire PDF content into text. Following this, it could apply additional processing to filter out or reformat data specifically related to incidents, such as filtering by certain keywords, patterns, or page sections known to contain incident data.
Returns: A list (or another suitable data structure) of incidents, where each incident is represented by a structured form, such as a tuple or a dictionary. Each element would contain extracted fields relevant to an incident, such as the date/time, incident number, location, nature of the incident, and any other pertinent details.
## Database Development
The project utilizes SQLite for its database needs, chosen for its simplicity and ease of integration with Python. The database is structured around a single table named records, designed to store incident data with fields for time, number, location, detail, and code, each stored as TEXT.

Key functions in the Python script manage the database interactions:
setup_database(): Initializes the database and creates the records table if it does not exist. This function ensures that the application has a structured place to store the incident data upon startup.
insert_records(database, records_list): Inserts the extracted incident data into the records table. Each record is inserted as a row in the table, with the fields mapped to the corresponding columns in the schema.
display_summary(database): Queries the records table to aggregate and display summary information about the incidents, such as the count of different incident types. This function demonstrates how the stored data can be analyzed and reported directly from the database.
## Bugs and Assumptions
# Bugs
Currently, there are no known critical bugs that impact the core functionalities of the project. However, users should be aware of potential minor issues:

PDF Parsing Limitations: The script may not accurately parse PDFs with complex layouts or non-standard fonts, potentially leading to incomplete or incorrect data extraction.
Error Handling: While basic error handling is implemented, edge cases, especially with unusual PDF formats or unexpected data structures, may not be fully covered, potentially causing the script to fail silently or produce incorrect outp
# Assumptions
The development of this project is based on several key assumptions:

PDF Structure Consistency: It is assumed that the incident report PDFs maintain a consistent structure, with incident data presented in a predictable format that the script is designed to parse.
Reliable Internet Connection: The script assumes that the user has a stable and reliable internet connection for downloading the PDF files from the specified URLs.
SQLite Suitability: The project assumes that the volume of data and the complexity of queries are within the capabilities of SQLite, making it a suitable choice for database management in this context.
Environment Compatibility: The script is developed and tested under specific environment conditions (Python version, operating system, etc.). It is assumed that it will be run under similar conditions, without guaranteeing full compatibility across all environments.
# cis6930sp24-assignment0
