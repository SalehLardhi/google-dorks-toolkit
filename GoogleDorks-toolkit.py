from googlesearch import search
from enum import Enum
import argparse
import pyfiglet
import re
import subprocess
import os
import json

#print the name in cool way
result = pyfiglet.figlet_format("GoogleDorks Toolkit")
print(result)

x = '\033[0m'
u = '\033[4m'
R = '\033[1;91m'
r = '\033[0;91m'
g = '\033[0;92m'
y = '\033[0;33m'
w = '\033[0;37m'

def print_dotted_text_with_developers(text, developers):
    border = f'{R}+' + '.' * (len(text) + 2) + f'{R}+'
    content = f'{R}| {text} |'
    developer_info = f'{R}| Developers: {", ".join(developers)} |'
    
    print(border)
    print(content)
    print(border)
    print(developer_info)
    print(border)

text_to_display = "Seiyun University - seiyunu.edu.ye"
developers_list = ["Saleh Lardhi", "Zaid Frarah", "Mohammed Mahros"]
print_dotted_text_with_developers(text_to_display, developers_list)
print('\033[0;37m \033[0m')
# Create an argument parser
parser = argparse.ArgumentParser(description='Your script description here')

# Add command-line arguments
parser.add_argument('-d', '--domain', required=True, help='Domain to search')
parser.add_argument('-n', '--number_of_pages', type=int, required=True, help='Number of pages to search')
parser.add_argument('-t', '--time', type=int, required=True, help='Time between requests')

parser.add_argument('-o', '--output', help='Specify output file name')
#parser.add_argument('--tor', help='Use torify to bypass Google captcha')
parser.add_argument('--search', help='Search matched domains in OpenForReport.txt')
parser.add_argument('-l', '--list', help='Add your own dorks list')

# Parse the command-line arguments
args = parser.parse_args()

# Access the arguments using args.<argument_name>
domain = args.domain
num_of_pages = args.number_of_pages
time_between_req = args.time
output_file = args.output
counter = 0
dorks_list_file = args.list or "dorks.txt"
search_in_vdp = args.search


saved_results = []

try:
        with open(dorks_list_file, 'r') as dorks_file:
            dorks = dorks_file.readlines()

        for dork_line in dorks:
            Dork, author, references, severity = map(str.strip, dork_line.split('<>'))
            query = f'{Dork} site:{domain}'

            print(f'\nChecking Dork: {query} - {author} - {references} - {severity}')
            urls = []
            for url in search(query, tld='com', num=num_of_pages, stop=num_of_pages, pause=time_between_req):
                urls.append(url)
                print(f'{counter + 1}) {url}')

                # Extract the domain from the URL
                extracted_domain = re.search(r'https?://([^/]+)', url).group(1)

                # Check if --search option is specified
                if search_in_vdp == "yes" or search_in_vdp == "y":
                    # Use grep to search for the domain in OpenForReport.txt
                    grep_command = f"grep -q {extracted_domain} OpenForReport.txt"
                    grep_process = subprocess.run(grep_command, shell=True)

                    # Check the exit code of the grep process
                    if grep_process.returncode == 0: 
                        print('\033[1;31m'+ "Note:"+ '\033[0m \033[0;32m' + f"This Website ( {extracted_domain} ) is vulnerable and has VDP/bbp so, you can report them legally!" +'\033[0m')
                counter += 1
                if counter == num_of_pages:
                    break

            if urls:
                saved_results.append({
                    'dork_line': dork_line,
                    'urls': urls
                })
        # Save the results to the specified output file
        with open(output_file, 'a') as output_file:
            for result in saved_results:
                output_file.write(f"Dork Line: {result['dork_line']}\n")
                for url in result['urls']:
                    output_file.write(f"{url}\n")


except KeyboardInterrupt:
    print('\nExit! Thanks for using;)')

except Exception as e:
    print(f'An error occurred: {e}')
