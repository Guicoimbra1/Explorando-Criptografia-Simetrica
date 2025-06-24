import os 
import time
from pathlib import Path
from cryptography.fernet import Fernet

ROOT_PATH = Path(__file__).parent

# Este programa criptografa e descriptografa textos e arquivos usando a biblioteca cryptography.

lista_extensoes = [
    '.txt', '.jpg', '.png', '.jpeg', '.pdf', '.docx', '.xlsx', '.pptx',
    '.mp3', '.mp4', '.avi', '.mkv', '.zip', '.rar', '.tar', '.gz',
    '.7z', '.exe', '.bat', '.sh', '.html', '.css', '.js', '.json',
    '.xml', '.csv', '.md', '.yml', '.yaml', '.sql', '.log', '.conf', '.ogg'
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def detecta_arquivo(nome_arquivo):
    return any(nome_arquivo.endswith(ext) for ext in lista_extensoes)

def gerar_chave():
    limpar_tela()
    
    chave = Fernet.generate_key()
    with open(ROOT_PATH / 'chave.key', 'wb') as file:
        file.write(chave)
    print('Chave de criptografia gerada com sucesso!')
    print(f'\nChave: {chave.decode()}\n')
    print('A chave também foi salva no arquivo chave.key na mesma pasta do programa.\n')
    return chave


def criptografar():
    limpar_tela()

    print('\nSe for um arquivo, digite o nome do arquivo com a extensão(ex: arquivo.txt).\n')
    texto = input('Digite um texto ou nome do arquivo a ser criptografado: ')
    arquivo = detecta_arquivo(texto)
    fernet = Fernet(input('\nDigite uma chave de criptografia adequada para fernet (base64, 32 bytes): ').encode())

    if arquivo:
        with open(ROOT_PATH / texto, 'rb') as arquivo:
            texto_arquivo = arquivo.read()
        with open(ROOT_PATH / texto, 'wb') as arquivo:
            arquivo.write(fernet.encrypt(texto_arquivo))
        limpar_tela()    
        print(f'O arquivo {texto} foi criptografado com sucesso!')
        return None
    else:
        texto_criptografado = fernet.encrypt(texto.encode())
        limpar_tela()
        print('Texto criptografado com sucesso!\n')
        print(f'{texto_criptografado.decode()}\n')

def descriptografar():
    limpar_tela()

    print('\nSe for um arquivo, digite o nome do arquivo com a extensão(ex: arquivo.txt).\n')
    texto = input('Digite o texto ou arquivo a ser descriptografado: ')
    arquivo = detecta_arquivo(texto)
    fernet = Fernet(input('\nDigite a chave de descriptografia adequada: ').encode())

    if arquivo:
        with open(ROOT_PATH / texto, 'rb') as arquivo:
            texto_arquivo = arquivo.read()
        with open(ROOT_PATH / texto, 'wb') as arquivo:
            arquivo.write(fernet.decrypt(texto_arquivo))
        limpar_tela()
        print(f'O arquivo {texto} foi descriptografado com sucesso!')
    else:
        texto_descriptografado = fernet.decrypt(texto).decode()
        limpar_tela()
        print('Texto descriptografado com sucesso!\n')
        print(f'{texto_descriptografado}\n')

def menu():
    limpar_tela()

    print('Bem-vindo ao meu programa de criptografia!'.center(100))
    print('Você pode criptografar ou descriptografar textos e arquivos.'.center(100))
    print('Se for um arquivo, Certifique-se de que o arquivo esteja na mesma pasta do programa.\n'.center(100))
    resposta = input(""" 
                    [c] para criptografar
                    [d] para descriptografar
                    [k] para gerar uma chave de criptografia 
                    [q] para sair

                    Digite a opção desejada: """).lower()
    return resposta

def main():

    while True:
        instrucao = menu()

        if instrucao not in ['c', 'd', 'k', 'q']:
            print('Opção inválida! Por favor, digite "c" para criptografar, "d" para descriptografar, "k" para gerar uma chave ou "q" para sair.')
            
        elif instrucao == 'k':
            gerar_chave()

        elif instrucao == 'c':
            try:
                criptografar()
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

        elif instrucao == 'd':
            try:
                descriptografar()
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
        
        elif instrucao == 'q':
            limpar_tela()
            print('Saindo do programa...')
            time.sleep(1)
            exit()
        
        input('\nPressione Enter para voltar...')

main()
