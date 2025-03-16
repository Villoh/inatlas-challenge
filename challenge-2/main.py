import os
from io_utils import download_file
from data_processor import extract_employees_from_gz_file, generate_reports, normalize_employee_data

def main():
    # URL for the compressed employees file.
    # Note: The file is available until Fri Mar 21 18:43:24 UTC 2025.
    url = "https://interview-challenges-resources.s3.eu-west-1.amazonaws.com/database/interview-challenges-database-option-b.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA24XR2QJMWWOU2CL4%2F20250314%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20250314T184258Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9a6e215cf2b8627b2ef58a32f82dea945d26aa0bea55b8311d8a20f35e9f12f0"
    compressed_file = "./challenge-2/resources/interview-challenges-database-option-b"
    csv_path = "./challenge-2/resources/csv"

    # Step 1: Download the compressed file
    download_file(url, compressed_file)

    # Step 2: Extract the contents of the tar.gz file
    employee_csv = extract_employees_from_gz_file(compressed_file, csv_path)

    # Step 3: Process the extracted CSV data (this step is not implemented in the provided code)
    normalize_employee_data(employee_csv, csv_path)

    # Step 4: Generate reports based on the processed data
    generate_reports(employee_csv, csv_path)

if __name__ == '__main__':
    main()