# GitHub Repo Downloader

This is a Python script for downloading a GitHub repository as a ZIP file. It uses the `requests` library to download the file, and the `argparse` library to provide a command line interface. If no filename is provided, the downloaded ZIP file is named `<repo-name>.zip`.

## **Installation**

1. Clone this repository or download the script.
2. Install the required libraries with pip: `pip install requests`.

## Usage

Run the script with the URL of the GitHub repository and the filename for the ZIP file:

```
python script.py <URL> <filename>
```

Replace `<URL>` with the URL of the GitHub repository, and `<filename>` with the filename you want for the ZIP file.

If no filename is provided, the ZIP file is named `<repo-name>.zip`:

```
python script.py <URL>
```

## Example

Here's an example where the script is used to download the 'brilliant-monocle-hackathon' repository:

```
python script.py https://github.com/isayahc/brilliant-monocle-hackathon
```

This will download the ZIP file as `brilliant-monocle-hackathon.zip` in your current working directory.

## License

This project is licensed under the terms of the MIT license.
