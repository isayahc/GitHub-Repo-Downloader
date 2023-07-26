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
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files:
            zipf.write(file)

def main():
    parser = argparse.ArgumentParser(description="Download and zip a webpage.")
    parser.add_argument('url', help='The URL of the webpage to download.')
    args = parser.parse_args()
    file, title = download_webpage(args.url)
    if file is not None:
        zip_files([file], f'{title}.zip')

if __name__ == "__main__":
    main()
