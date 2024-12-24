# Link Extractor

This script processes a list of URLs, extracts links from `window.open` JavaScript calls on those pages, and saves the extracted links to a text file.

## Prerequisites

Make sure you have Python installed on your system. The script uses the following Python libraries:
- `requests`
- `beautifulsoup4`

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4
Usage
Prepare the Input File:
Create a text file named input_files.txt in the same directory as the script. This file should contain the list of URLs you want to process, with each URL on a new line.

Run the Script:
Execute the script with Python:

python link_extractor.py
Output:
The script will create (or append to) a file named extracted_links.txt in the same directory, containing the links extracted from the window.open JavaScript calls found in the provided URLs.

Script Details
Functions
extract_link_from_window_open(url):

Sends a GET request to the given URL.
Parses the page content with BeautifulSoup.
Uses a regular expression to find all instances of window.open JavaScript calls and extracts the URL from them.
Returns a list of extracted links or None if an error occurs.
save_links_to_file(links, filename):

Appends the extracted links to the specified file.
Creates the file if it does not exist.
process_urls_from_file(input_filename, output_filename):

Reads the input file line by line.
Processes each URL using extract_link_from_window_open.
Saves the extracted links using save_links_to_file.
Error Handling
The script includes error handling for:

HTTP request errors.
File read/write errors.
General exceptions during link extraction.
Example
Input File (input_files.txt):

Code
http://example.com/page1
http://example.com/page2
Output File (extracted_links.txt):

Code
http://link1.com
http://link2.com
Additional Notes
Ensure the URLs in the input file are valid and accessible.
The output file is appended with new links each time the script is run.
License
This project is licensed under the MIT License.

This README provides a comprehensive guide on how to use your script, including installation, usage, and details about the script's functionality.
