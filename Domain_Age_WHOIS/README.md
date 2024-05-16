# WHOIS Information Fetcher

This Python script allows you to fetch WHOIS information for a given domain name and display relevant details such as creation date, modification date, and the entire WHOIS record.

## Prerequisites

- Python 3.x
- `whois` command-line tool (usually pre-installed on Unix-like systems)

## Usage

1. Clone this repository to your local machine or download the `whois_fetcher.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script by executing the following command:

    ```bash
    python whois_fetcher.py
    ```

5. Enter the domain name you want to fetch WHOIS information for when prompted.
6. The script will display the creation date, modification date, and ask if you want to see the entire WHOIS record.
7. Optionally, you can choose to view the full WHOIS record by entering "yes" when prompted.

## Example

Enter the domain to fetch WHOIS information (e.g., example.com): google.com  
Domain Information:  
Creation Date: 1997-09-15T04:00:00Z (Domain Age: 9740 days)  
Modification Date: 2019-09-09T15:39:04Z   

Do you want to show the entire WHOIS record? (yes/no): yes

Full WHOIS Record:  
% IANA WHOIS server  
% for more information on IANA, visit http://www.iana.org  
% This query returned 1 object  
...  

# MIT License

Copyright (c) 2024 RTK

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

