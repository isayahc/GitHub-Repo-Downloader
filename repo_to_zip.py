import requests
import shutil
import os
import argparse

def download_repo_zip(url, filepath):
    if not url.endswith('/'):
        url += '/'
    archive_url = url + 'archive/main.zip'
    response = requests.get(archive_url, stream=True)

    # Check if filepath is a directory
    if os.path.isdir(filepath):
        # Get the repository name from the URL
        repo_name = url.split('/')[-1] if url[-1] != '/' else url.split('/')[-2]
        # Append the repository name to the directory path
        filepath = os.path.join(filepath, repo_name + '.zip')
    
    output_dir, filename = os.path.split(filepath)  # Split the filepath into a directory path and filename
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
    save_path = filepath  # Save the file at the specified filepath
    with open(save_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

def main():
    parser = argparse.ArgumentParser(description='Download a GitHub repository as a ZIP file.')
    parser.add_argument('url', help='The URL of the GitHub repository.')
    parser.add_argument('filepath', help='The file path (including filename) where the downloaded ZIP file should be saved.')
    args = parser.parse_args()
    download_repo_zip(args.url, args.filepath)

if __name__ == '__main__':
    main()
