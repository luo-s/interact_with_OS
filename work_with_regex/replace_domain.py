#!/usr/bin/env python3
import csv
import re
import sys

# replace 'abc.edu' with 'xyz.edu'

csv_file = sys.argv[1] 
report_file = 'report.txt'

def contain_domain(email, domain):
    domain_pattern = r'[\w\.-]+@'+domain+'$'
    if re.match(domain_pattern, email):
        return True
    return False

def replace_domain(email, old_domain, new_domain):
    old_domain_pattern = r'' + old_domain + '$'
    email = re.sub(old_domain_pattern, new_domain, email)
    return email

user_data = []
def main():
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    with open(csv_file, 'r', encoding='UTF-8') as f:
        user_data_list = list(csv.reader(f))
        user_data.append(user_data_list[0])
        for i, user in enumerate(user_data_list[1:]):
            email = user[1].strip()
            if contain_domain(email, old_domain):
                row = [user[0], ' ' + replace_domain(email, old_domain, new_domain)]
                user_data.append(row)
            else:
                user_data.append(user)

    with open(report_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(user_data)

main()

# to execute: 
# chmod +x replace_domain.py
# ./replace_domain.py user_emails.csv