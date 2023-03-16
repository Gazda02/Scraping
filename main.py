import requests
from time import sleep
from bs4 import BeautifulSoup
from excel_write import excel_write


def main():
    """page = ''
    page_open = requests.get(page)
    page_txt = page_open.text
    page_parser = BeautifulSoup(page_txt, 'html.parser')
    table_raw = page_parser.find("tbody")
    cells = table_raw.find_all('td')"""

    # start
    filepath = r"C:\Users\Gazda Karol\Desktop\!doctype  .txt"
    file = open(filepath, "r")
    file = file.read()
    file = BeautifulSoup(file, "html.parser")
    table_raw = file.find("tbody")
    cells = table_raw.find_all('td')
    # end

    table = [['', 'IMEI', 'Make', 'Model', 'Model Code', 'Timestamp', 'Version', 'Liq.', 'CPO', 'Func',
              'Customer Grade', 'Cleared', 'Power Down', 'Customer', 'Mode', 'Cell ID', 'Failures', 'Exceptions', 'ID']]

    count = 0
    list_part = []
    for cell in cells:    # take text form the code
        count += 1
        part = cell.getText()
        list_part.append(part)
        if count == 19:    # sets rows in separate list
            table.append(list_part)
            count = 0
            list_part = []
    i = 0
    while i < len(table):   # remove first item (index) from the lists
        table[i].pop(0)
        i += 1
    excel_write(table)


while True:
    main()
    sleep(180)
