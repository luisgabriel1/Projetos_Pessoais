votos, lula, bolsonaro = [], [], []
while True:
    pesquisa = input('Lula ou Bolsonaro  [ L / B ]. Para sair envie S\n').upper()
    votos += pesquisa

    if pesquisa == 'L':
        lula += pesquisa

    elif pesquisa == 'B':
        bolsonaro += pesquisa

    elif pesquisa == 'S':
        votos_1 = int(len(votos) - len(pesquisa))
        calc_b, calc_l = int((len(bolsonaro) / votos_1) * 100), int((len(lula) / votos_1) * 100)
        print(f'Lula está com {calc_l}% votos.\nBolsonaro está com {calc_b}% de votos.')
        break

