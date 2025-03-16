import os
import tarfile
import pandas as pd
import requests

EMPLOYEES_HEADER = ["EMPLOYEE_NAME", "EMPLOYEE_EMAIL", "JOB_NAME", "JOB_TYPE", "COMPANY_NAME", "TAX_ID",
                  "ACTIVITY", "ACTIVITY_PARENT", "ACTIVITY_GRAND_PARENT", "LAT", "LNG", "CONTINENT", "COUNTRY_NAME", "ISO2_CODE"]

def download_file(url, local_filename):
    """
    Downloads a file from the given URL and saves it as local_filename.
    Args:
        url (str): URL of the file to download.
        local_filename (str): Local filename where the downloaded file will be saved.
    """

    # Check if file already exists
    if os.path.exists(local_filename):
        print(f"{local_filename} already exists. Skipping download.")
        return
    
    # Create the directory if it doesn't exist
    directory = os.path.dirname(local_filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")

    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an error for bad status
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Downloaded file saved as {local_filename}")

def extract_employees_from_gz_file(gz_file, output_path):
    """
    Normalize the data from a gzip file and save it to structured CSV files.
    Args:
        gz_file (str): Path to the compressed file (gzip format).
        output_path (str): Directory path where structured CSV files will be saved.
    Returns:
        str: Path to the processed CSV file or None if extraction fails.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    with tarfile.open(gz_file, "r:*") as tar:
        # Iterate through the files in the tar archive
        for tar_file in tar.getnames():
            if tar_file.endswith('employee.csv'):
                # Check if the file already exists before processing
                output_file = os.path.join(output_path, f"raw_{tar_file}")
                if os.path.exists(output_file):
                    print(f"File {output_file} already exists. Skipping.")
                    return output_file
                print(f"Processing file: {tar_file}")
                # Read the CSV data using pandas
                with tar.extractfile(tar_file) as file:
                    # We assume the CSV file is semicolon-separated and has the proper header
                    df = pd.read_csv(file, header=None, sep=";")
                    df.columns = EMPLOYEES_HEADER  # Assign the appropriate header based on the CSV type
                    
                    df.to_csv(output_file, index=False)  # Save the normalized data as CSV
                    print(f"Saved normalized data to: {output_file}")
                    return output_file
    return None
