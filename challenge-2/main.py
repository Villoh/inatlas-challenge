from io_utils import download_file, extract_employees_from_gz_file
from data_processor import normalize_employee_data, generate_reports

# URL for the compressed employees file.
# Note: The file is available until Fri Mar 21 18:43:24 UTC 2025.
URL = "https://interview-challenges-resources.s3.eu-west-1.amazonaws.com/database/interview-challenges-database-option-b.tar.gz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA24XR2QJMWWOU2CL4%2F20250314%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20250314T184258Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9a6e215cf2b8627b2ef58a32f82dea945d26aa0bea55b8311d8a20f35e9f12f0"
# Path for the compressed dataset
COMPRESSED_FILE = "./challenge-2/resources/interview-challenges-database-option-b"
# Path for the directory to save CSV files
CSV_PATH = "./challenge-2/resources/csv"

def process_employee_data():
    # Step 1: Download the compressed file
    download_file(URL, COMPRESSED_FILE)

    # Step 2: Extract the contents of the tar.gz file
    employee_csv = extract_employees_from_gz_file(COMPRESSED_FILE, CSV_PATH)

    if employee_csv is None:
        print("Failed to extract employees CSV file.")
        return

    # Step 3: Process the extracted CSV data (this step is not implemented in the provided code)
    normalize_employee_data(employee_csv, CSV_PATH)

    # Step 4: Generate reports based on the processed data
    generate_reports(employee_csv, CSV_PATH)


def main():
   process_employee_data()


if __name__ == '__main__':
    main()