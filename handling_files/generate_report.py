#!/usr/bin/env python3
import csv
import sys

csv_file = sys.argv[1]

def read_employees(csv_file):
    employees = []
    # register a dialect to remove leading spaces
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    with open(csv_file, 'r', encoding='UTF-8') as f:
        reader = csv.DictReader(f, dialect='empDialect')
        for row in reader:
            employees.append(row)
    return employees

def process_data(employees):
    departments = {}
    for employee in employees:
        departments[employee['Department']] = departments.get(employee['Department'], 0) + 1
    return departments

def write_report(departments, report_file):
    with open(report_file, 'w+') as f:
        for key in sorted(departments):
            f.write(key + ':' + str(departments[key]) + '\n')

write_report(process_data(read_employees(csv_file)), 'report.txt')

