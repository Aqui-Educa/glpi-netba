import requests

class Glpi:
    def initSession(self):

        app_token = 'w8StUeTfmBBPtIkeolVl1XJZAVNDTRSLa45XNNTY'
        user_token = 'hhOaEWziKAdmrMQGCyRxIQ2c3uiwsqu2ElP2hXiv'

        ####################### INIT SESSION ############################
        header = {
            'App-Token': app_token,
            'Authorization': f'user_token {user_token}'
        }
        response = requests.get(f'https://netba.com.br/aquieduca/apirest.php/initSession',headers=header)
        content = response.json()
        return content['session_token']

        
    
    def getAnItem(self,app_token, session_token):
        ####################### GET AN ITEM ############################
        header = {
            'App-Token': app_token,
            'Session-Token': session_token
        }
        response = requests.get(f'https://netba.com.br/aquieduca/apirest.php/projecttask/7',headers=header)
        content = response.json()
        print(content['name'])