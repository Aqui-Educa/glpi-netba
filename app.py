from glpi import Glpi


app_token = 'w8StUeTfmBBPtIkeolVl1XJZAVNDTRSLa45XNNTY'
glpi = Glpi()
session_token = glpi.initSession()
glpi.getAnItem(app_token,session_token)