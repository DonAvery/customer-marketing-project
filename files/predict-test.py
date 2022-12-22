#!/usr/bin/env python
# coding: utf-8

import requests

host = "churn-serving-env.eba-m6viypea.us-east-1.elasticbeanstalk.com"
url = f'http://{host}/predict'

customer_id = 'xyz-123'
customer = {
  "id": 2131,
  "year_birth": 1959,
  "education": "PhD",
  "marital_status": "Divorced",
  "income": 62859.0,
  "kidhome": 0,
  "teenhome": 1,
  "dt_customer": "2012-12-30",
  "recency": 37,
  "mntwines": 1063,
  "mntfruits": 89,
  "mntmeatproducts": 102,
  "mntfishproducts": 16,
  "mntsweetproducts": 12,
  "mntgoldprods": 25,
  "numdealspurchases": 4,
  "numwebpurchases": 9,
  "numcatalogpurchases": 4,
  "numstorepurchases": 6,
  "numwebvisitsmonth": 6,
  "acceptedcmp3": 0,
  "acceptedcmp4": 0,
  "acceptedcmp5": 0,
  "acceptedcmp1": 0,
  "acceptedcmp2": 0,
  "complain": 0,
  "cust_age": 56
}

response = requests.post(url, json=customer).json()
print(response)


if response['response'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)
