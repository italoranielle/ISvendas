import requests
import pandas as pd
import json
from urllib.parse import quote


Server_url = 'http://127.0.0.1:8000/api/v1'



class Produto:
    def __init__(self):
        self.pk = None
        self.name = None
        self.description = None
        self.color =  None
        self.suplayer =  None
        self.wifi = False
        self.zegbee = False
        self.rf =  False
        self.attrs = {}
        self.unit_type = 'unit'
        self.barcode = None
        self.price_sell = None

        self.url = '{}/produto'.format(Server_url)

    def getPoduct(self,name):
        data = {
            'name': name
        }
        S = requests.Session()
        result = S.get(self.url, params=data).json()
        for key,item in result.items():
            setattr(self,key,item)


    def addattrs(self,key_,value):
        self.attrs[key_] = value

    def save(self):
        data = {
            'name':self.name, 
            'description':self.description, 
            'color':self.color, 
            'suplayer':self.suplayer, 
            'wifi':str(self.wifi), 
            'zegbee':str(self.zegbee), 
            'rf':str(self.rf), 
            'attrs':json.dumps(self.attrs),
            'unit_type':self.unit_type,
            'barcode':self.barcode,
            'price_sell':self.price_sell
        }
        S = requests.Session()
        result = S.post(self.url,data=data)
        if result.status_code == 201:
            return True
        else:
            return False


class Produtos:
    def __init__(self):
        self.products = pd.DataFrame([])
        self.url = '{}/produtos/'.format(Server_url)
        self.colouns_pt =  {'pk':'ID',
                            'name':'Nome', 
                            'description':'Descrição', 
                            'color':'cor', 
                            'suplayer' : 'Fornecedor', 
                            'unit_type':'unidade',
                            'price_sell':'preço'
                            }  
            
    def GetProducts(self,description):
        data = {
            'description': description
        }
        S = requests.Session()
        result = S.get(self.url, params=data)
        if result.status_code == 200:
            self.products =  pd.DataFrame(result.json()).rename(columns= self.colouns_pt)
            return result.json()

class PurchaseList:
    def __init__(self):
        self.PurchaTable = []
        self.list2server = []
        self.url = '{}/purchase/'.format(Server_url) 
        self.colouns_pt =  {
                            'name':'Nome', 
                            'description':'Descrição', 
                            'quantity':'Quantidade',
                            'unit':'Unidade',
                            'unit_price':'Preço',
                            'total_price':'Preço total',
                            }  

    def addItem(self,product,qtd,un,price):
        self.PurchaTable.append({'pk':product.pk,'name':product.name,'description':product.description,'quantity':qtd,'unit':un,'unit_price':price,'total_price':qtd*price})
        self.list2server.append({'product':product.pk,'quantity':qtd,'unit':un,'price':price})

    def save(self):
        S = requests.Session()
        result = S.post(self.url,json=self.list2server)
        if result.status_code == 201:
            return True
        else:
            return False

