#!/usr/bin/env python3

import sys
import re
import csv

sys_log = sys.argv[1]

user_info_dict = {}
user_error_dict = {}
error_dict = {}

with open(sys_log, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
                user_info = re.search(r'(\w{3} \d{2} \d{2}:\d{2}:\d{2}) (\w+.\w+) (\w+:) ([A-Z]{4,5}) (.+) \((.+)\)$', line)
                if user_info is None:
                        continue   
                user, category = user_info[6], user_info[4]  
                if category == 'ERROR':
                        user_error_dict[user] = user_error_dict.get(user, 0) + 1
                        error_dict[user_info[5]] = error_dict.get(user_info[5], 0) + 1 
                else:
                        user_info_dict[user] = user_info_dict.get(user, 0) + 1
                             
error_key = ['Error', 'Count']
error_body = list(error_dict.items())
error_body.sort(key=lambda x: x[1], reverse=True)

with open('error_message.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(error_key)
        writer.writerows(error_body)

user_key = ['Username', 'INFO', 'ERROR']
all_users = set(user_info_dict.keys()).union(user_error_dict.keys())
user_list = [[user, user_info_dict.get(user, 0), user_error_dict.get(user, 0)] for user in all_users]
user_list.sort(key=lambda x: x[0])

with open('user_statistics.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(user_key)
        writer.writerows(user_list)

# to execute:
# chmod +x ticky.py
# ./ticky.py syslog.log