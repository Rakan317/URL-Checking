"""
The script was developed by RTK in collaboration with ChatGPT.
"""

import ssl
import socket
from datetime import datetime

def check_ssl_certificate(url):
    try:
        # Extract host and port from the URL
        host = url.split('://')[-1].split('/')[0]
        port = 443  # Default HTTPS port

        # Create SSL context
        context = ssl.create_default_context()

        # Establish SSL connection
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Retrieve SSL certificate
                cert = ssock.getpeercert()

                # Print SSL certificate information
                print("SSL Certificate information:")
                print(f"Issuer: {cert['issuer'][0][0]}")
                print(f"Subject: {cert['subject'][0][0]}")
                print(f"Serial Number: {cert.get('serialNumber', 'N/A')}")
                print(f"Valid From: {datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z')}")
                print(f"Valid Until: {datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')}")
                print(f"Public Key Algorithm: {cert.get('subjectPublicKeyAlgorithm', 'N/A')}")
                print(f"Signature Algorithm: {cert.get('signatureAlgorithm', 'N/A')}")
                return True
    except ssl.CertificateError as e:
        if 'expired' in url:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: The certificate has expired.")
        elif 'wrong.host' in url:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: The host name does not match the certificate.")
        elif 'self-signed' in url:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: The certificate is self-signed.")
        elif 'untrusted-root' in url:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: The certificate's root is not trusted.")
        elif 'revoked' in url:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: The certificate has been revoked.")
        elif 'pinning-test' in url:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: The certificate did not pass the pinning test.")
        else:
            print(f"Failed to retrieve SSL certificate for {url}.")
            print("Reason: Certificate verification failed.")
        return False
    except Exception as e:
        print(f"Failed to retrieve SSL certificate for {url}.")
        print(f"Error: {e}")
        return False

# Prompt the user to enter a URL
while True:
    user_url = input("Enter the URL to check SSL certificate (e.g., example.com): ")
    # Check if the URL starts with "http://" or "https://", if not, prepend "https://"
    if not user_url.startswith(('http://', 'https://')):
        user_url = 'https://' + user_url
    # Check SSL certificate for the provided URL
    if check_ssl_certificate(user_url):
        print(f"{user_url} has a valid SSL certificate.")
        break
    else:
        print(f"Please make sure the URL {user_url} is correct and accessible.")
