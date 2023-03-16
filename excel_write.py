import xlsxwriter


def excel_write(table) -> None:
    columns_20 = ['A', 'C', 'P']
    columns_10 = ['B', 'D', 'F', 'H', 'I']
    lenght1 = len(table) - 1
    lenght2 = len(table[0])
    count = 0
    workbook = xlsxwriter.Workbook('ExcelFile.xlsx')   # otwiera i nazywa plik w excelu
    worksheet = workbook.add_worksheet()    # dodaje arkusz
    for x in columns_20:
        worksheet.set_column(f'{x}:{x}', 20)
    for y in columns_10:
        worksheet.set_column(f'{y}:{y}', 10)
    worksheet.set_column('E:E', 16)
    worksheet.set_column('O:O', 18)
    bold = workbook.add_format({'bold': True})
    for head in table[0]:
        worksheet.write(0, count, head, bold)
        count += 1
    for col in range(lenght2):
        for row in range(1, lenght1):
            worksheet.write(row, col, table[row][col])
    workbook.close()
