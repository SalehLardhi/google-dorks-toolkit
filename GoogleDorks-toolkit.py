import argparse
import os
import time
import subprocess
import re
from googlesearch import search  # You may need to install this library
from enum import Enum

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

# Usage
text_to_display = "Google Toolkit"
developers_list = ["Saleh Lardhi", "Zaid Frarah", "Mohammed Mahros"]
print_dotted_text_with_developers(text_to_display, developers_list)





def search_dorks(domain, page, time, dorks_file, output_file, torify, custom_dorks_dir, only, search_domains_file):
    nyx = 0
    saved_results = []

    try:
        with open(dorks_file, 'r') as dorks_file:
            dorks = dorks_file.readlines()

        for dork_line in dorks:
            dork, author, references, severity = map(str.strip, dork_line.split('-'))
            query = f'{dork} site:{domain}'

            if torify:
                query = f'--tor {query}'

            print(f'\nChecking Dork: {query} - {author} - {references} - {severity}')

            urls = []
            for url in search(query, tld="com", lang="en", num=only, start=0, stop=None, pause=int(time)):
                urls.append(url)
                print(f'{nyx + 1}) {url}')
                nyx += 1
                if only and nyx >= only:
                    break
                if time:
                    time.sleep(int(time))

            if urls:
                saved_results.append({
                    'dork_line': dork_line,
                    'urls': urls
                })

    except KeyboardInterrupt:
        print('\nExit! Thanks for using;)')
        return saved_results

    except Exception as e:
        print(f'An error occurred: {e}')

    finally:
        if saved_results and output_file:
            with open(output_file, 'w') as output:
                for result in saved_results:
                    output.write(f"Dork: {result['dork_line']}\n")
                    for url in result['urls']:
                        output.write(f"{url}\n")
                    output.write("\n")

if __name__ == "__main__":
    # ... (rest of the code remains the same)

    parser = argparse.ArgumentParser(description="Dork Search Tool")

    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("-p", "--page", type=int, required=True, help="Number of pages to search")
    parser.add_argument("-t", "--time", type=int, required=True, help="Pause time between requests (in seconds)")
    parser.add_argument("-df", "--dorks-file", default="dorks.txt", help="Path to the dorks file")
    parser.add_argument("-o", "--output-file", help="Path to save the results file")
    parser.add_argument("--tor", action="store_true", help="Use torify to bypass Google captcha")
    parser.add_argument("-l", "--custom-dorks-dir", help="Use custom dorks directory")
    parser.add_argument("--only", type=int, help="Specify the number of URLs for every dork")
    parser.add_argument("--search", action="store_true", help="Search and compare with domains in OpenForReport.txt")

    args = parser.parse_args()

    if args.search and not os.path.exists("OpenForReport.txt"):
        print("Error: OpenForReport.txt not found. Please provide the correct path or create the file.")
        exit(1)

    if args.tor:
        try:
            subprocess.check_output(['torify', '--version'])
        except subprocess.CalledProcessError:
            print("Error: torify command not found. Make sure torify is installed.")
            exit(1)

    if args.custom_dorks_dir:
        args.dorks_file = os.path.join(args.custom_dorks_dir, args.dorks_file)

    if args.output_file is None:
        args.output_file = f"{args.domain}.txt"

    if args.search:
        with open("OpenForReport.txt", "r") as domain_file:
            search_domains = domain_file.read().splitlines()

        saved_results = search_dorks(args.domain, args.page, args.time, args.dorks_file, args.output_file, args.tor, args.custom_dorks_dir, args.only, search_domains)

    else:
        saved_results = search_dorks(args.domain, args.page, args.time, args.dorks_file, args.output_file, args.tor, args.custom_dorks_dir, args.only, None)

    if saved_results:
        print("\nResults saved successfully.")
    else:
        print("\nNo results found.")


