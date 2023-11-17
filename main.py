import requests

def random_color():
    quantidade_de_cores = int(input('Digite a quantidade de cores que deseja gerar: '))
    url = 'https://x-colors.yurace.pro/api/random'
    if quantidade_de_cores:
        url += f'?number={quantidade_de_cores}'
    else:
        ''
    response = requests.get(url)

    try:
        if response.status_code == 200:
            color_json = response.json()
            print(color_json)
        else:
            print('Erro de conexão')
    except (KeyError, IndexError) as e:
        print(f'Erro nos dados: {e}')

def color_shades():
    color = input('Digite a cor: ')
    url = f'https://x-colors.yurace.pro/api/random/{color}'
    response = requests.get(url)

    try:
        if response.status_code == 200:
            color_json = response.json()
            print(color_json)
        else:
            print(f'Erro de conexão: {response.status_code}')
    except (KeyError, IndexError) as e:
        print(f'Erro de dados: {e}')


def convert_hex_to_rgb():
    try:
        color_hex = input('Digite a cor (só os numerais): ')
        url = f'https://x-colors.yurace.pro/api/hex2rgb?value={color_hex}'
        response = requests.get(url)

        response.raise_for_status()  # Isso lançará uma exceção se o código de status não for 2xx

        color_convert = response.json()
        print(color_convert)

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')
    except ValueError as e:
        print(f'Erro de valor: {e}')

def convert_hex_to_hsl():
    try:
        color_hex = input('Digite a cor (só os numerais): ')
        url = f'https://x-colors.yurace.pro/api/hex2hsl?value={color_hex}'
        response = requests.get(url)

        response.raise_for_status()

        color_convert = response.json()
        print(color_convert)

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')
    except ValueError as e:
        print(f'Erro de valor: {e}')

def convert_rgb_to_hex():
    try:
        color_rgb = int(input('Digite a cor (só os numerais): '))
        url = f'https://x-colors.yurace.pro/api/hex2hsl?value={color_rgb}'
        response = requests.get(url)

        response.raise_for_status()

        color_convert = response.json()
        print(color_convert)

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')
    except ValueError as e:
        print(f'Erro de valor: {e}')

def convert_rgb_to_hsl():
    try:
        color_rgb = int(input('Digite a cor (só os numerais): '))
        url = f'https://x-colors.yurace.pro/api/rgb2hsl?value={color_rgb}'
        response = requests.get(url)

        response.raise_for_status()

        color_convert = response.json()
        print(color_convert)

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')
    except ValueError as e:
        print(f'Erro de valor: {e}')

def convert_hsl_to_hex():
    try:
        color_hsl = int(input('Digite a cor (só os numerais): '))
        url = f'https://x-colors.yurace.pro/api/hsl2hex?value={color_hsl}'
        response = requests.get(url)

        response.raise_for_status()

        color_convert = response.json()
        print(color_convert)

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')
    except ValueError as e:
        print(f'Erro de valor: {e}')

def convert_hsl_to_rgb():
    try:
        color_hsl = int(input('Digite a cor (só os numerais): '))
        url = f'https://x-colors.yurace.pro/api/hsl2rgb?value={color_hsl}'
        response = requests.get(url)

        response.raise_for_status()

        color_convert = response.json()
        print(color_convert)

    except requests.exceptions.RequestException as e:
        print(f'Erro na solicitação: {e}')
    except ValueError as e:
        print(f'Erro de valor: {e}')




while True:
    print('\n'+ '-'*30 + ' Gerador de cores ' + '-'*30)

    print('\n' + 'Escolha uma opção: ')
    print('[1] - Gerar cores aleatórias')
    print('[2] - Gerar cores com base na cor fornecida')
    print('[3] - Converter HEX para RGB')
    print('[4] - Converter HEX para HSL')
    print('[5] - Converter RGB para HEX')
    print('[6] - Converter RGB para HSL')
    print('[7] - Converter HSL para HEX')
    print('[0] - SAIR')


    opcao = int(input('Digite a opcao: '))

    if opcao == 1:
        random_color()
    elif opcao == 2:
        color_shades()
    elif opcao == 3:
        convert_hex_to_rgb()
    elif opcao == 4:
        convert_hex_to_hsl()
    elif opcao == 5:
        convert_rgb_to_hex()
    elif opcao == 6:
        convert_rgb_to_hsl()
    elif opcao == 7:
        convert_hsl_to_hex()
    elif opcao == 0:
        break
    else:
        print('Opção inválida')