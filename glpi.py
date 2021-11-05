import requests
import json

class Glpi:

    def __init__(self):
        self.app_token = 'w8StUeTfmBBPtIkeolVl1XJZAVNDTRSLa45XNNTY'
        self.user_token = 'hhOaEWziKAdmrMQGCyRxIQ2c3uiwsqu2ElP2hXiv'
        self.session_token = ''
        self.host = 'https://netba.com.br/aquieduca/apirest.php/'
        self.initSession()

    def initSession(self):                
        header = {
            'App-Token': self.app_token,
            'Authorization': f'user_token {self.user_token}'
        }
        response = requests.get(f'{self.host}initSession',headers=header)
        content = response.json()
        self.session_token = content['session_token']        
    
    def getAnItem(self):
        header = {
            'App-Token': self.app_token,
            'Session-Token': self.session_token
        }
        response = requests.get(f'{self.host}projecttask/9',headers=header)
        content = response.json()

    def getSubItems(self):
        header = {
            'App-Token': self.app_token,
            'Session-Token': self.session_token
        }
        response = requests.get(f'{self.host}project/1/task',headers=header)
        content = response.json()
        print(content)


    def listSearchOptions(self):
        header = {
            'App-Token': self.app_token,
            'Session-Token': self.session_token
        }
        response = requests.get(f'{self.host}listSearchOptions/projecttask',headers=header)
        content = response.json()
        print(content)


    def addItem(self,body):
        header = {
            'App-Token': self.app_token,
            'Session-Token': self.session_token,
            'Content-Type': 'application/json'
        }        

        response = requests.post(f'{self.host}projecttask/',headers=header,data=json.dumps(body))
        content = response.json()
        print(content)