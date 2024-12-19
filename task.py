import pandas as pd
import requests
import xml.etree.ElementTree as ET

pd.options.display.max_columns = None

# fees = pd.read_parquet("https://storage.yandexcloud.net/norvpublic/fees.parquet")

# transactions = pd.read_parquet(
#     "https://storage.yandexcloud.net/norvpublic/transactions.parquet"
# )

# def get_rate(date):

#     url = "https://www.cbr.ru/DailyInfoWebServ/DailyInfo.asmx"

#     SOAPEnvelope = f"""
#     <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#     <soap:Body>
#         <KeyRate xmlns="http://web.cbr.ru/">
#         <fromDate>{date}</fromDate>
#         <ToDate>{date}</ToDate>
#         </KeyRate>
#     </soap:Body>
#     </soap:Envelope>"""

#     options = {"Content-Type": "text/xml; charset=utf-8"}

#     response = requests.post(url, data=SOAPEnvelope, headers=options)
#     root = ET.fromstring(response.text)

#     for i in root.iter("Rate"):
#         return float(i.text)

# transactions["date"] = transactions["date"].dt.date

# transactions = transactions.assign(Rate=transactions["date"].apply(get_rate))

# transactions = (
#     transactions.set_index("ATM_ID").join(fees.set_index("ATM_ID")).iloc[0:, :6]
# )

# transactions = transactions.assign(result=transactions['bal_end_of_day'] >= transactions['cash_out'])

# transactions = transactions.loc[((transactions['bal_end_of_day'] > 0))]

# print(transactions)

# transactions.to_excel('transactions.xlsx')

# transactions = pd.read_excel('transactions.xlsx')

# for i in range(4):
#     transactions.loc[((transactions['ATM_ID'] == f'ATM_{i+1}'))].to_excel(f'ATM_{i+1}.xlsx', index=False)

ATM_1 = pd.read_excel('ATM_1.xlsx')
print(round(ATM_1['result'].sum()/len(ATM_1),2))

ATM_2 = pd.read_excel('ATM_2.xlsx')
print(round(ATM_2['result'].sum()/len(ATM_2),2))

ATM_3 = pd.read_excel('ATM_3.xlsx')
print(round(ATM_3['result'].sum()/len(ATM_3),2))

ATM_4 = pd.read_excel('ATM_4.xlsx')
print(round(ATM_4['result'].sum()/len(ATM_4),2))

print(ATM_1)