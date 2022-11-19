import requests
import zipfile
import os

url = "https://github.com/CapitalOneRecruiting/DA-Airline-Data-Challenge/raw/main/data.zip"

def fetch_zip_file(url: "str"):
    """
    Download, unzip and extract files with url
    
    Parameters
    ----------
    url : str
        Any valid string path is acceptable. The string could be a URL. Valid
        URL schemes include http, ftp, s3, and file
    """
    # Try to acquire the zip file
    try:
        response = requests.get(url)
    except OSError:
        print("Connection Failed!")
        return None

    # Check if the request works
    if response.status_code == 200:
        # Save dataset to file
        print("File request successfully")
        open("data/data.zip", "wb").write(response.content)
    else:
        print("ZIP file request failed!")
        return None

def main():
    # Get the ZIP file
    fetch_zip_file(url)

    # Unzip
    with zipfile.ZipFile("data/data.zip", "r") as zip_ref:
        zip_ref.extractall("data")

    # Delete zip file
    if len(os.listdir("data")) > 0:
        os.remove("data/data.zip")
    else:
        pass