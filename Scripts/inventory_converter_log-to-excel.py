#!python
import re
import csv 
import itertools
import webbrowser
import pandas as pd
from os import remove
from os import listdir
from os.path import isfile, join
from datetime import datetime


"""CLEAN NON-FP RAW INVENTORY TEXT"""

def non_fp_inventory(raw_line):
    line_list = line.split(",")
    inventory_list = []
    clean_inventory_list = []
    temporary_list = []
    for member in line_list:
        inventory_list.append(member.strip())
    for raw_member in inventory_list:
        temporary_list = raw_member.split(" ")
        clean_component = temporary_list[1]
        clean_inventory_list.append(clean_component)
    return clean_inventory_list

"""FOR PRINTING RESULT OF ALL FILES INSIDE DIRECTORIES"""

device_choice = input("FP or non-FP: ")
print(" ")
if device_choice == 'FP':
    onlyfiles = [f for f in listdir('fp-inventory') if isfile(join('fp-inventory', f))]
    for i in onlyfiles:
        print(i)
elif device_choice == 'non-FP':
    onlyfiles = [f for f in listdir('non-fp-inventory') if isfile(join('non-fp-inventory', f))]
    for i in onlyfiles:
        print(i)

"""PRE-PROCESSING"""

choosen_file = input("\nSelect a file: ")
today_date = datetime.today().strftime('%d-%m-%Y')
print("\nConverting...")
path = "result"

"""READ AND PROCESS THE FILE"""

if device_choice == 'non-FP':
    with open('non-fp-inventory/'+choosen_file ,'r') as showfile:
        lines = showfile.readlines()
        if ':' in lines[0]:
            hostname = re.findall('[:]([^#]*)', lines[0])
        else:
            hostname = re.findall('^(.*?)#', lines[0])
        upper_text = None
        lower_text = None
        all_inventory_list = []
        for line in lines:
            if 'NAME' in line:
                if 'Ethernet1' in line:
                    clean_text = non_fp_inventory(line)
                    upper_text = clean_text
                else:
                    line_list = re.findall('"([^"]*)"', line)
                    upper_text = line_list
            elif 'PID' in line:
                clean_text = non_fp_inventory(line)
                lower_text = clean_text
                result_line = upper_text + lower_text
                all_inventory_list.append(result_line)

    cols = ["LOCATION", "DESCRIPTION", "PID", "VID", "SN"]

    rows = all_inventory_list

    with open('inventory_result.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(cols)
        write.writerows(rows)

    read_file = pd.read_csv('inventory_result.csv')
    read_file.to_excel(f'result/{hostname[0]}_Inventory_{today_date}.xlsx', index = None, header=True, encoding='utf-8')

    print(f"\nComplete converting {hostname[0]} Log file into excel in Result folder\n")
    webbrowser.open(path)
    remove('inventory_result.csv')

