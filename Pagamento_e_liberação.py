import webbrowser

url_site = 'https://github.com/luisgabriel1'
conta = 1000
plano_b = 200
plano_p = 400
plano_g = 600
email = ''
app = False
pag = False
print('Qual plano você deseja ')
planos = input(
    'Para Bronze envie: B\nPra Prata envie: P\nPara Gold envie: G\n').upper()
if planos == 'B':
    pagar = input('Envie P, para liberar o app:  ').upper()

    if pagar == 'P':
        pag = True
        app = True
        if pag == True:
            print()
        if pag == True and app == True:
            conta -= plano_b
            email = f'O seu Pagamento Foi concluido com sucesso.\nApp foi liberado.\nO valor que resta em sua conta é de {conta}'
            print(f'{email}')
            webbrowser.open(url_site)
    elif pagar != 'P':
        print('Faça o pagamento')
elif planos == 'P':
    pagar = input('Envie P, para liberar o app:  ').upper()

    if pagar == 'P':
        pag = True
        app = True
        if pag == True:
            print()
        if pag == True and app == True:
            conta -= plano_p
            email = f'O seu Pagamento Foi concluido com sucesso.\nApp foi liberado.\nO valor que resta em sua conta é de {conta}'
            print(f'{email}')
            webbrowser.open(url_site)
    elif pagar != 'P':
        print('Faça o pagamento')
elif planos == 'G':
    pagar = input('Envie P, para liberar o app:  ').upper()

    if pagar == 'P':
        pag = True
        app = True
        if pag == True:
            print()
        if pag == True and app == True:
            conta -= plano_g
            email = f'O seu Pagamento Foi concluido com sucesso.\nApp foi liberado.\nO valor que resta em sua conta é de {conta}'
            print(f'{email}')
            webbrowser.open(url_site)
    elif pagar != 'P':
        print('Faça o pagamento')

