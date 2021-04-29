# -*- coding: utf-8 -*-
import requests


def main():
    print('####################')
    print('### Consulta CEP ###')
    print('####################')
    print()

    cep_input = input('Digite o CEP para a consulta: ')

    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input)
    )

    adress_data = request.json()

    if 'erro' not in adress_data:  # Se não tiver a palavra erro exibe o resultado abaixo
        print('==> CEP ENCONTRADO <=== \n')

        print('CEP: {}'.format(adress_data['cep']))
        print('Logradouro: {}'.format(adress_data['logradouro']))
        print('Complemento: {}'.format(adress_data['complemento']))
        print('Bairro: {}'.format(adress_data['bairro']))
        print('Cidade: {}'.format(adress_data['localidade']))
        print('Estado: {}'.format(adress_data['uf']))
    else:
        print('CEP inválido')

    print('---------------------------')
    option = int(
        input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n\n=> '))
    if option == 1:
        main()
    else:
        print('\nSaindo...')


if __name__ == '__main__':
    main()
