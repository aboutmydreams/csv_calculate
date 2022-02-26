import pandas as pd


def csv_to_xlsx_pd():
    csv = pd.read_csv('./data_fix.csv', encoding='utf-8')
    csv.to_excel('./data.xlsx', sheet_name='data')
