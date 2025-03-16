import csv
import os
import requests
import gzip

def download_file(url, local_filename):
    """
    Downloads a file from the given URL and saves it as local_filename.
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


def save_gzip_to_txt(gz_file_path, txt_file_path):
    """
    Extracts a .gz file and saves its contents into a .txt file.
    
    :param gz_file_path: Path to the input .gz file.
    :param txt_file_path: Path to the output .txt file.
    """
    if os.path.exists(txt_file_path):
        print(f"{txt_file_path} already exists. Skipping extraction.")
        return
    try:
        with gzip.open(gz_file_path, "rt", encoding="utf-8") as gz_file, open(txt_file_path, "w", encoding="utf-8") as txt_file:
            for line in gz_file:
                txt_file.write(line)  # Write each line to the text file
        print(f"Extraction complete! Saved as: {txt_file_path}")
    except Exception as e:
        print(f"Error: {e}")
