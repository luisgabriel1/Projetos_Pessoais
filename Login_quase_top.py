# AVISOS: 
# Arrumar onde o programa deverá parar assim que executar algo 

import os
import webbrowser

y = 0

x = 0 

decisao_opc = ['SIM', 'S', 'YES', 'Y', 'OK', 'CLARO', 'QUERO']

decisao_opc1 = ['NAO', 'NÃO', 'N', 'NO', 'NUNCA', 'NEVER', 'NOT']

usr = ['duda']

keys = ['123']

link = 'https://www.netflix.com/browse'

while True:
    while x <= 1:
        user = input('Usuario: ')
        key = input('Senha: ')
        
        if user in usr and key in keys:
            print('Logado Com Sucesso')
            webbrowser.open(link)
            break
        
        elif user not in usr or key not in keys:
            print('Usuario ou senha Invalidos')
            x += 1
    
    else:
        pass
        os.system('clear')
        decisao = input('Quer cadastrar ? ').upper()
        if decisao in decisao_opc:
            user_cadastro = input('Como vai ser seu usuario: ')
            key_cadastro = input('Como será sua senha: ')
            usr.append(user_cadastro)
            keys.append(key_cadastro)
            os.system('clear')
            
        
            def login ():
                user_1 = input('Usuario: ')
                key_1 = input('Senha: ')
                return user_1, key_1
            login()
              

            if login() in usr and keys:
                print('Logado Com Sucesso')
                webbrowser.open(link)
                os.system('clear')
           
        
        elif decisao in decisao_opc1:
            
            print('Obrigado volte sempre !')
            break
        
        else:
            print('NÃO ENTENDI OQUE QUIS DIZER !')
        