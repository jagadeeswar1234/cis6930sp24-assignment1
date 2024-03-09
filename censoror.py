import argparse
import glob
from assignment1.censor_functions import censor_names, censor_dates, censor_phones, censor_addresses
from pathlib import Path



def process_file(file_path, censor_flags, output_dir):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Apply censoring functions based on the flags
    if censor_flags['names']:
        content = censor_names(content)
    if censor_flags['dates']:
        content = censor_dates(content)
    if censor_flags['phones']:
        content = censor_phones(content)
    if censor_flags['address']:
        content = censor_addresses(content)

    # Write the censored content to a new file in the output directory
    output_path = Path(output_dir) / (Path(file_path).stem + '.censored')
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description="The Censoror: Censor sensitive information from text files.")
    parser.add_argument('--input', type=str, nargs='+', help="Glob pattern(s) for files to process.")
    parser.add_argument('--output', type=str, help="Directory to store the censored files.")
    parser.add_argument('--names', action='store_true', help="Censor names.")
    parser.add_argument('--dates', action='store_true', help="Censor dates.")
    parser.add_argument('--phones', action='store_true', help="Censor phone numbers.")
    parser.add_argument('--address', action='store_true', help="Censor addresses.")
    parser.add_argument('--stats', required=True, help="File or stderr for statistics.")

    # Add more arguments as necessary

    args = parser.parse_args()

    # Dictionary to store which censoring functions to apply
    censor_flags = {
        'names': args.names,
        'dates': args.dates,
        'phones': args.phones,
        'address': args.address
    }

    # Ensure output directory exists
    Path(args.output).mkdir(parents=True, exist_ok=True)

    # Process each file matching the input glob pattern(s)
    for pattern in args.input:
        for file_path in glob.glob(pattern):
            process_file(file_path, censor_flags, args.output)

    # stats_info = f"Processed {len(processed_files)} files: {', '.join(str(file) for file in processed_files)}"
    # if args.stats == 'stderr':
    #     print(stats_info, file=sys.stderr)
    # else:
    #     with open(args.stats, 'w', encoding='utf-8') as stats_file:
    #         stats_file.write(stats_info)

if __name__ == "__main__":
    main()
