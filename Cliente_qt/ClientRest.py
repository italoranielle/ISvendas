import requests


Server_url = 'http://127.0.0.1:8000/api/v1'


class Produtos:
    def __init__(self):
        self.products = ''
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
            self.products =  result.json()
            return result.json()
