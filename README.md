# inventory_converter
Simple script to convert inventory log on Cisco Devices (Nexus / NCS) to excel file. Maybe some people need it, its best to make it. You can run direcly on "inventory_converter_log-to-excel.py" file. It needs netmiko, pandas, and openpyxl to run. You can install it using pip.

On folder "non-fp-inventory" there are some example of Inventory Log from Cisco NCS and Nexus devices. This script can parse inventory 
Location, Description, PID, VID, and SN from Log to excel file in no time. The result of excel file will be targeted on "result" folder.

Note : this is only version 0.1, and only non-FP device can run (non Firepower). Firepower log have different inventory structure and it is more complicated.
Will add in the future version.
Thanks. Hope this can help.
