# cis6930sp24-assignment1

**Name**: Jagadeeswara Reddy Gummi Reddy

# Text Censorship Tool

## Overview
This tool is designed to help censor sensitive information from text documents. It can automatically redact names, dates, phone numbers, and addresses from text files, making it ideal for privacy-conscious document processing. The tool leverages spaCy's Natural Language Processing (NLP) capabilities for accurate entity recognition and censorship.

## Features
- **Sensitive Data Censorship**: Redacts names, dates, phone numbers, and addresses.
- **Batch Processing**: Supports processing multiple files at once using glob patterns.
- **Customizable Censorship**: Users can specify what types of information to censor.
- **Statistics Generation**: Outputs a summary of the censorship process.

## Installation
Ensure you have Python and pipenv installed. Then, set up the project environment:

1. Clone the repository and navigate to the project directory.
**Clone the Repository**
git clone <https://github.com/jagadeeswar1234/cis6930sp24-assignment1>
2. Install dependencies: `pipenv install`
3. Activate the virtual environment: `pipenv shell`
4. Download the spaCy NLP model: `python -m spacy download en_core_web_md`

## Usage
Run the tool with the following command:
pipenv run python censoror.py --input '<input-glob-pattern>' --output '<output-directory>' [flags]

## Flags
--input: Glob pattern to match input files (e.g., '*.txt' for all text files).
--output: Directory to store censored files. Censored files retain the original name with .censored extension.
--names: Censor personal names.
--dates: Censor dates.
--phones: Censor phone numbers.
--address: Censor physical addresses.
--censor-char: Character used for censoring. Default is the Unicode full block (█).
--stats: Specify output for statistics (stderr, stdout, or a filename).

**Example Command**
pipenv run python censoror.py --input 'data/*.txt' --names --dates --phones --address --output 'censored/' --stats stderr

## Functions Description
censor_names(text, censor_char): Censors names in the provided text using the specified censor character.
censor_dates(text, censor_char): Censors dates, handling both numeric and written formats, including ordinal indicators.
censor_phones(text, censor_char): Censors various phone number formats.
censor_address(text, censor_char): Censors ZIP codes and postal addresses.
censor_file(input_file, output_file, censor_char, censor_functions): Applies specified censor functions to the text from input_file and writes the censored text to output_file.
write_statistics(stats, stats_output): Writes censorship statistics to the specified output (file, stderr, or stdout).

## Testing
Run tests to validate functionality:
'''bash
pipenv run python -m unittest discover -s tests

This will execute tests for each censoring function, ensuring they perform as expected.

## License
This project is open-sourced under the MIT License.

