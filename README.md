# GoogleDorks Toolkit

![GoogleDorks Toolkit](https://raw.githubusercontent.com/SalehLardhi/google-dorks-toolkit/main/image.png)

GoogleDorks Toolkit is a Python script designed to help security researchers and penetration testers automate Google dorking for finding potential vulnerabilities and information about a target domain. The tool utilizes Google search queries, also known as Google dorks, to identify possible security issues and gather valuable information.

## Features

- **Customizable Dorks**: Users can provide their own list of dorks to be used in the Google search queries.
- **Domain Search**: The tool allows users to specify a target domain for the Google dorking process.
- **Results Output**: Search results are saved to an output file, providing a convenient way to review and analyze the findings.
- **Vulnerability Detection**: Optional detection of vulnerabilities by searching for the identified domains in a specified file (`OpenForReport.txt` in this case).

## Usage

## Prerequisites

- Python 3.x
- Required Python packages: `googlesearch`, `enum`, `argparse`, `pyfiglet`

## Installation



```
pip install googlesearch-python
pip install pyfiglet
```



## Command-line Arguments

    - `-d`, `--domain`: Specify the target domain for Google dorking.
    - `-n`, `--number_of_pages`: Set the number of pages to search.
    - `-t`, `--time`: Specify the time between requests to avoid being blocked by Google.
    - `-o`, `--output`: (Optional) Specify the output file name for saving the results.
    - `--search`: (Optional) Search matched domains in OpenForReport.txt.
    - `-l`, `--list`: (Optional) Add your own dorks list.

## Example
```
python google_dorks_toolkit.py -d example.com -n 5 -t 2 -o results.txt --search yes
```

## Developers

- Saleh Lardhi
- Zaid Frarah
- Mohammed Mahros

## Note

This tool is intended for educational and ethical use only. Use it responsibly and ensure compliance with applicable laws and regulations.
## Disclaimer

The developers are not responsible for any misuse or damage caused by this script. Use it at your own risk.
