#!/usr/bin/env python3
import sys
import re

# lookfing for 'CRON ERROR failed to start'

def error_search(log_file):
    error = input('What is the error? ')
    error_list = error.split(' ')
    error_pattern = ['error']
    for i in range(len(error_list)):
        error_pattern.append(r'{}'.format(error_list[i].lower()))
    returned_error = []
    with open(log_file, 'r', encoding='UTF-8') as f:
        logs = f.readlines()
        for log in logs:
            if all(re.search(pattern, log.lower()) for pattern in error_pattern):
                returned_error.append(log)
    return returned_error

def generate_report(returned_error):
    with open('errors_found.txt', 'w') as f:
        for error in returned_error:
            f.write(error)

if __name__ == '__main__':
    log_file = log_file = sys.argv[1]
    returned_error = error_search(log_file)
    generate_report(returned_error)
    sys.exit(0)

# to execute:
# chmod +x find_error.py
# ./find_error.py