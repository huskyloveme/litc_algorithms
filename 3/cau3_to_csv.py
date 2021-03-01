import requests
import pandas as pd
import json
import csv

print(pd.__version__)

username = 'd4433b61b377d84b316b245b1f33582b'
password = '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'
shopname = 'minhtd'

url = 'https://'+username+':'+password+'@'+shopname+'.myshopify.com/admin/api/2021-01/'

csv_path = 'csv/customers.csv'

authen_uri = 'shop.json'
get_customers = 'customers.json'

def sent_rq():
    
    resp = requests.Session().get(url+get_customers)
    
    dict_content = json.loads(resp.text)['customers']

    for c in dict_content:
        # d = json.loads(c)
        c.pop('default_address', None)
        c.pop('address1', None)
        c.pop('address2', None)
        c.pop('addresses', None)
    
    def getList(dict): 
        return dict.keys()

    fieldnames = getList(dict_content[0])

    try:
        with open(csv_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in dict_content:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    

if __name__ == '__main__':
    sent_rq()