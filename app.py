from glpi import Glpi
import csv

glpi = Glpi()

with open('planilha.csv', 'r', encoding='latin-1') as planilha:
    tabela = csv.reader(planilha, delimiter=';')
    count = 1
    for linha in tabela:
        if count != 1:
            body = { 
                'input': {
                    'name': linha[3],
                    'projects_id': linha[1],
                    'content': linha[5],
                    'campozeroonefield': linha[0]
                }
            }
            glpi.addItem(body)

        count += 1
        










