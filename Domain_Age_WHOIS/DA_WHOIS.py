"""
The script was developed by RTK in collaboration with ChatGPT.
"""

import subprocess
import re
from datetime import datetime

def get_domain_info(domain):
    try:
        # Run the whois command and capture the output
        process = subprocess.Popen(['whois', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Check if the command was successful
        if process.returncode == 0:
            # Decode the output and find the creation and modification date
            output_text = output.decode('utf-8')
            creation_date_match = re.search(r'Creation Date: (.+)', output_text)
            modification_date_match = re.search(r'Updated Date: (.+)', output_text)
            if creation_date_match:
                # Extract and parse the creation date
                creation_date_str = creation_date_match.group(1).strip()
                creation_date = datetime.strptime(creation_date_str, '%Y-%m-%dT%H:%M:%SZ')
                # Calculate the age of the domain
                domain_age = (datetime.now() - creation_date).days
                
                # Print the creation and modification date
                print("Domain Information:")
                print(f"\033[91mCreation Date: {creation_date_str}\033[0m (Domain Age: {domain_age} days)")
                
                # Print the modification date if available
                if modification_date_match:
                    print(f"Modification Date: {modification_date_match.group(1).strip()}")
                    
                return True
            else:
                print("Failed to find Creation Date in WHOIS information.")
                return False
        else:
            print(f"Failed to fetch WHOIS information for {domain}.")
            print(f"Error: {error.decode('utf-8')}")
            return False
    except Exception as e:
        print(f"Failed to fetch WHOIS information for {domain}.")
        print(f"Error: {e}")
        return False

# Prompt the user to enter a domain
while True:
    user_domain = input("Enter the domain to fetch WHOIS information (e.g., example.com): ")
    # Fetch WHOIS information for the provided domain
    if get_domain_info(user_domain):
        show_full_record = input("Do you want to show the entire WHOIS record? (yes/no): ")
        if show_full_record.lower() == "yes":
            print("Full WHOIS Record:")
            process = subprocess.Popen(['whois', user_domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            output_text = output.decode('utf-8')
            print(re.sub(r'Creation Date: (.+)', r'\033[91mCreation Date: \1\033[0m', output_text))
    else:
        show_full_record = input("Do you want to show the entire WHOIS record? (yes/no): ")
        if show_full_record.lower() == "yes":
            print("Full WHOIS Record:")
            process = subprocess.Popen(['whois', user_domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            output_text = output.decode('utf-8')
            print(re.sub(r'Creation Date: (.+)', r'\033[91mCreation Date: \1\033[0m', output_text))
        break
