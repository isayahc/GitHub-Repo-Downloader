import os
import argparse
import requests
from bs4 import BeautifulSoup
import zipfile
import string

def download_webpage(url, path='webpage'):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(path, exist_ok=True)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'webpage'
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        title = ''.join(c for c in title if c in valid_chars)
        with open(os.path.join(path, f'{title}.html'), 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        return os.path.join(path, f'{title}.html'), title
    else:
        print('Unable to download webpage.')
        return None, None

def zip_files(files, zip_name):
    os.makedirs(os.path.dirname(zip_name), exist_ok=True)  # Create the output directory if it doesn't exist
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)

def main():
    parser = argparse.ArgumentParser(description="Download and zip a webpage.")
    parser.add_argument('url', help='The URL of the webpage to download.')
    parser.add_argument('output_dir', nargs='?', default=os.getcwd(), help='The directory to save the downloaded ZIP file.')
    args = parser.parse_args()
    file, title = download_webpage(args.url)
    if file is not None:
        zip_name = os.path.join(args.output_dir, f'{title}.zip')  # Save the file in the output directory
        zip_files([file], zip_name)

if __name__ == "__main__":
    main()
