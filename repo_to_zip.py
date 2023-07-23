import requests
import shutil
import os
import argparse

def download_repo_zip(url, filename):
    if not url.endswith('/'):
        url += '/'
    archive_url = url + 'archive/main.zip'
    response = requests.get(archive_url, stream=True)
    cwd = os.getcwd()
    save_path = os.path.join(cwd, filename)
    with open(save_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def main():
    parser = argparse.ArgumentParser(description='Download a GitHub repository as a ZIP file.')
    parser.add_argument('url', help='The URL of the GitHub repository.')
    parser.add_argument('filename', nargs='?', help='The filename for the downloaded ZIP file.')
    args = parser.parse_args()
    if args.filename is None:
        repo_name = args.url.split('/')[-1] if args.url[-1] != '/' else args.url.split('/')[-2]
        args.filename = repo_name + '.zip'
    download_repo_zip(args.url, args.filename)

if __name__ == '__main__':
    main()
