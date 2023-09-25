# PDF File Copy Tool

The PDF File Copy Tool is a Python script that allows you to copy PDF files from your computer's Downloads directory within a specified time range and store them in a destination folder. This tool is helpful when you want to organize and archive PDF files based on their creation dates.

## Features

- Copies PDF files created within a specified time range.
- Renames copied files with the destination folder's name as a prefix.
- Platform-independent file paths for flexibility.

## Prerequisites

Before using this tool, make sure you have the following installed:

- Python 3.x
- The shutil library, which is typically included with Python.

## Usage

1. Clone this repository to your computer:

   ```bash
   git clone https://github.com/your-username/pdf-file-copy-tool.git

## Navigate to the project directory

## Run the script with the desired parameters:

python copy_pdf_files.py <destination_folder_name> <start_date> <end_date>

## destination_folder_name>: Specify the name of the destination folder where PDF files will be copied.

<start_date>: Specify the start date and time in the format 'YYYY-MM-DD HH:MM:SS'.
<end_date>: Specify the end date and time in the format 'YYYY-MM-DD HH:MM:SS'.
The tool will copy PDF files created within the specified time range to the destination folder, renaming them with the folder name as a prefix.

# Example

python copy_pdf_files.py "MyPDFs" "2023-09-24 10:00:00" "2023-09-24 12:00:00"

This command will copy PDF files created between 10:00 AM and 12:00 PM on September 24, 2023, to a folder named "MyPDFs."
