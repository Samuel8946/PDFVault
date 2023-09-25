import os
import datetime
import argparse
import shutil

def file_date_range(pdfList, start, end, dest_folder):
    print("Copying files within the specified time range to folder:", dest_folder)
    startTime = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    endTime = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    endTime += datetime.timedelta(seconds=1)
    
    # Create the destination folder
    os.makedirs(dest_folder, exist_ok=True)
    user_home_directory = os.path.expanduser("~")
    src_directory_path = os.path.join(user_home_directory, "Downloads")

    for pdf_file, file_date in pdfList:
        if startTime <= file_date <= endTime:
            source_path = os.path.join(src_directory_path, pdf_file)
            dest_path = os.path.join(dest_folder, pdf_file)

            # Add the folder name to the copied file's name
            dest_filename = os.path.join(dest_folder, dest_folder + "_" + pdf_file)
            
            shutil.copy2(source_path, dest_filename)
            print(f"Copied {pdf_file} - {file_date.strftime('%Y-%m-%d %H:%M:%S')} to {dest_filename}")


def getPdfList(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"The directory '{directory_path}' does not exist.")
        return []

    # List all files in the directory
    files = os.listdir(directory_path)

    # Use filter and a lambda function to find PDF files
    pdf_files = list(filter(lambda file: file.lower().endswith(".pdf"), files))
    pdf_files2 = []

    if pdf_files:
        print("PDF files in the directory:")
        for pdf_file in pdf_files:
            file_path = os.path.join(directory_path, pdf_file)
            fileDate = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            pdf_files2.append((pdf_file, fileDate))
        pdf_files2.sort(key=lambda x: x[1])
        for pdf_file, file_date in pdf_files2:
            print(f"{pdf_file} - {file_date.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No PDF files found in the directory.")

    return pdf_files2

def main():
    parser = argparse.ArgumentParser(description="Copy PDF files created within a specified time range to a folder.")
    parser.add_argument("folder_name", help="Specify the name of the destination folder")
    parser.add_argument("start_date", help="Start date and time in the format 'YYYY-MM-DD HH:MM:SS'")
    parser.add_argument("end_date", help="End date and time in the format 'YYYY-MM-DD HH:MM:SS'")
    args = parser.parse_args()

    user_home_directory = os.path.expanduser("~")
    src_directory_path = os.path.join(user_home_directory, "Downloads")
    dest_folder = args.folder_name
    pdfList = getPdfList(src_directory_path)
    file_date_range(pdfList, args.start_date, args.end_date, dest_folder)

if __name__ == "__main__":
    main()
