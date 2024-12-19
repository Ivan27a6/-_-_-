import pandas as pd

transactions = pd.read_excel('transactions.xlsx')

print(transactions)

# for i in range(4):
#     transactions.loc[((transactions['ATM_ID'] == f'ATM_{i+1}'))].to_excel(f'ATM_{i+1}.xlsx', index=False)
# print('Done')