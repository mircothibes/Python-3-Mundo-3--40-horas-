def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\33[0:31mERRO -\"{entrada}\" é um preço inválido\33[m')
        else:
            valido = True
            return float(entrada)

