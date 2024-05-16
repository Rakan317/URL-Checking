# URL-Checking
this repository might contains script which help detecting bad URLs 


# SSL Certificate Checker

## Overview

This Python script, `SSLCC.py`, is designed to check the SSL certificate of a given URL and provide information about the certificate. It verifies whether the SSL certificate is valid and displays details such as issuer, subject, serial number, validity period, public key algorithm, and signature algorithm.



## Requirements

The script requires Python 3.x to run. There are no external dependencies beyond the built-in Python modules, which include `ssl`, `socket`, and `datetime`.

## Usage

To use the script, follow these steps:

1. Make sure you have Python 3.x installed on your system.
2. Download the `SSLCC.py` script.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the `SSLCC.py` script.
5. Run the script by executing the following command:

python SSLCC.py


6. Enter the URL when prompted to check the SSL certificate.

## Functionality

The script performs the following tasks:

- Accepts a URL input from the user.
- Checks if the URL starts with "http://" or "https://". If not, it prepends "https://" to the URL.
- Attempts to establish an SSL connection to the provided URL.
- Retrieves the SSL certificate from the server.
- Parses and prints detailed information about the SSL certificate, including issuer, subject, serial number, validity period, public key algorithm, and signature algorithm.
- Handles various SSL certificate issues, such as expiration, incorrect host, self-signed, untrusted root, revoked, and failed pinning test.
- Displays appropriate error messages if the SSL certificate retrieval fails.

## Example

Here is an example usage of the script:

$ python SSL_Certification_Cheker.py  
$ Enter the URL to check SSL certificate (e.g., example[.]com): `example[.]com`  
SSL Certificate information:  
Issuer: CN=Let's Encrypt Authority X3,O=Let's Encrypt,C=US  
Subject: CN=`www.example[.]com `  
Serial Number: 032B99D23989F6D58A1BAC6E3AC42D81F7AE   
Valid From: 2021-09-01 22:00:00   
Valid Until: 2021-11-30 22:00:00   
Public Key Algorithm: rsaEncryption  
Signature Algorithm: sha256WithRSAEncryption  
`hxxps://www.example[.]com` **has a valid SSL certificate.**

$ python SSL_Certification_Cheker.py   
Enter the URL to check SSL certificate (e.g., example[].com): `expired.badssl[.]com`     
Failed to retrieve SSL certificate for `hxxps://expired.badssl[.]com`.   
Reason: **The certificate has expired.**    
Please make sure the URL `hxxps://expired.badssl[.]com` is correct and accessible.   

To test the script you can use the examples shown in `hxxps://badssl[.]com`

# Author

All of these scripts was developed by RTK in collaboration with ChatGPT.

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
