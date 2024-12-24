import requests
from bs4 import BeautifulSoup
import re

# Function to extract link from window.open
def extract_link_from_window_open(url):
    try:
        # Send a GET request to the page
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
            return None

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all JavaScript function calls containing window.open
        pattern = r"window\.open\(['\"]([^'\"]+)['\"]"  # Modified regex to handle both single and double quotes
        links = re.findall(pattern, str(soup))

        return links
    except requests.exceptions.RequestException as e:
        print(f"Error while making request to {url}: {e}")
        return None
    except Exception as e:
        print(f"Error while extracting link from {url}: {e}")
        return None

# Function to save links to a txt file
def save_links_to_file(links, filename):
    try:
        with open(filename, 'a') as file:  # Append mode 'a' to add to the file
            for link in links:
                file.write(link + '\n')
        print(f"Links saved to {filename}")
    except Exception as e:
        print(f"Error while saving links: {e}")

# Function to process URLs from an input file
def process_urls_from_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            for line in infile:
                url = line.strip()
                if url:  # Process non-empty lines
                    print(f"Processing URL: {url}")
                    extracted_links = extract_link_from_window_open(url)
                    if extracted_links:
                        save_links_to_file(extracted_links, output_filename)
                    else:
                        print(f"No links were extracted from {url}.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred while processing the input file: {e}")

if __name__ == "__main__":
    input_filename = 'input_files.txt'  # Name of the input file with URLs
    output_filename = 'extracted_links.txt' # Name of the output file to save extracted links

    process_urls_from_file(input_filename, output_filename)
    print("Link extraction process complete.")
