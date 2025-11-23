import csv
import os

FILE_PATH = 'alunos.csv'

def limpar_terminal():
    os.system('clear')

def voltar_para_o_menu():
    input('Digite uma tecla para voltar para o menu principal: ')
    main()

def imprime_boas_vindas():
    print('Bem vindo a escola PythonVille!\n')

def listar_todos_alunos():
    try:
        with open('alunos.csv', newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f, skipinitialspace=True)

            print(f"Colunas detectadas: {reader.fieldnames}")

            for line in reader:
                print(f"Nome: {line['nome']}")
    except FileNotFoundError as e:
        print(f'Arquivo não existe: {e.strerror}')


def listar_nota():
    print('Listando alunos...\n')
    listar_todos_alunos()

    name = input('Digite o nome do aluno que deseja listar nota: ').strip()

    aluno_encontrado = None
    with open('alunos.csv', newline='') as f:

        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for line in reader:
            if line['nome'] == name:
                print(f"\n--- Notas atuais de {name} ---")
                print(f"Nota 01: {line['nota01']}")
                print(f"Nota 02: {line['nota02']}")
                print(f"Nota 03: {line['nota03']}")
                print("-" * 30)

                aluno_encontrado = line
                break

    if not aluno_encontrado:
        print(f'Não foi possível encontrar o aluno {name}')

    voltar_para_o_menu()

def cadastrar_aluno():
    name = input('Digite o nome do aluno: ').strip()
    idade = int(input('Digite a idade do aluno: '))

    column = ['nome', 'idade', 'nota01', 'nota02', 'nota03', 'media']

    novo_aluno = {
        'nome': f'{name}',
        'idade': f'{idade}',
        'nota01': '0',
        'nota02': '0',
        'nota03': '0',
    }

    aluno_encontrado = None

    with open('alunos.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        for line in reader:
            if line['nome'] == name:
                aluno_encontrado = line
                break

    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        with open(FILE_PATH, 'r+', encoding='utf-8') as f:
            content = f.read()
            if not content.endswith('\n'):
                f.write('\n')

    
    if not aluno_encontrado:
        with open(FILE_PATH, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=column)

            writer.writerow(novo_aluno)
    else:
        print(f'ERRO: Aluno {name} já existe')

    voltar_para_o_menu()

def cadastrar_notas():
    listar_todos_alunos()
    linhas_atualizadas = []

    name = input('Digite o nome do aluno que deseja cadastrar nota: ')

    with open('alunos.csv', newline='', encoding='utf-8-sig') as f:
        find = False

        reader = csv.DictReader(f, skipinitialspace=True)
        headers = reader.fieldnames
        for line in reader:
            if line['nome'] == name:
                
                for i in range(3):
                    nota = input(f'Digite a nota {i+1}: ')
                    line[f'nota0{i+1}'] = nota

                find = True

            linhas_atualizadas.append(line)

    if find:
        with open(FILE_PATH, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)

            writer.writeheader()
            writer.writerows(linhas_atualizadas)
        print(f'Aluno {name} atualizado!')
    else:
        print(f'Não foi possível encontrar o aluno {name}')

    voltar_para_o_menu()
            
def menu():
    imprime_boas_vindas()
    print('1. Cadastrar aluno')
    print('2. Cadastrar nota')
    print('3. Listar notas de um aluno')
    print('4. Sair')

    opt = int(input('Digita a opção: '))

    match opt:
        case 1:
            cadastrar_aluno()
        case 2:
            cadastrar_notas()
        case 3: 
            listar_nota()
        case 4:
            print('Encerrando...')
    

def calcular_media():
    linhas_atualizadas = []

    with open('alunos.csv', newline='') as f:

        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for line in reader:
            nota01 = float(line['nota01'])
            nota02 = float(line['nota02'])
            nota03 = float(line['nota03'])

            media = round(float(nota01 + nota02 + nota03) / 3.0, 2)

            line['media'] = media

            linhas_atualizadas.append(line)

    with open(FILE_PATH, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)

        writer.writeheader()
        writer.writerows(linhas_atualizadas)

def app():
    menu()

def main():
    limpar_terminal()
    calcular_media()
    app()

if __name__ == '__main__':
    main()