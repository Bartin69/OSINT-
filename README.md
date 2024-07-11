# OSINT Tool using BeautifulSoup

## Overview

This project is a Python-based OSINT (Open Source Intelligence) tool designed to search for user information across various social media platforms. The tool leverages the BeautifulSoup library for web scraping and the Requests library for sending HTTP requests. It is capable of retrieving user details from platforms like VK, Telegram, Odnoklassniki, Pinterest, and more.

## Features

- **Retry Mechanism**: Robust request function with retries and delays to handle network issues and server errors.
- **Multi-Platform Support**: Functions to search for user information across multiple social networks.
- **JSON Output**: Saves the search results in a JSON file for easy analysis and portability.
- **Console Output**: Prints search results to the console for immediate viewing.

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/osint-tool.git
2. Navigate to the project directory:
   ```sh
   cd osint-tool
3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt


Run the script and input the desired username or name when prompted:

      ```sh
     python main.py


Code Description:
request_with_retries
This function sends HTTP requests to a given URL with a specified number of retries and delay between retries.
      ```python
      def request_with_retries(url, retries=3, delay=5):
       for i in range(retries):
           try:
               response = requests.get(url)
               if response.status_code == 200:
                   return response
               else:
                   print(f"Failed with status code: {response.status_code}")
           except requests.exceptions.RequestException as e:
               print(f"Request failed: {e}")
           time.sleep(delay)
       return None

search_telegram
Fetches profile information from Telegram by parsing the shared data script.

Other Social Media Functions
Similar functions for VK, Odnoklassniki, Pinterest to fetch user information by parsing the HTML content.

search_person
Aggregates the results from various social media search functions into a single dictionary.

save_results_to_file
Saves the aggregated search results into a JSON file.

Example Output
Run the script and input the desired username or name when prompted. The results will be printed to the console and saved in a JSON file named osint_results.json.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
