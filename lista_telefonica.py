from os import system
from prettytable import PrettyTable
import csv

def csv_para_lista(caminho_arquivo):
	with open(caminho_arquivo, 'r') as arquivo:
		lista = list(csv.reader(arquivo))
	return lista

def persistir_csv(caminho_arquivo, lista):
	with open(caminho_arquivo, 'w') as arquivo:
		escritor = csv.writer(arquivo)
		escritor.writerows(lista)

def montar_tabela(matriz):
	tabela = PrettyTable()
	tabela.field_names = matriz[0]
	for i in matriz:
		if i[0] == 'Nome' and i[1] == 'Telefone':
			continue
		tabela.add_row(i)
	return tabela

while True:
	print('Digite 1: Listar')
	print('Digite 2: Buscar')
	print('Digite 3: Adicionar')
	print('Digite 4: Excluir')
	print('Digite 5: Sair')

	opcao = int(input('\nDigite a opção desejada '))

	dados = csv_para_lista('arquivos/dados.csv')

	match opcao:
		case 1:
			tabela = montar_tabela(dados)
			system('clear') or None
			print(tabela)
		case 2:
			nome = input('Digite o nome: ')
			encontrado = None
			for item in dados:
				if item[0] == nome:
					encontrado = item[1]
					break
			if not encontrado:
				system('clear') or None
				print('Não encontrado')
				continue
			system('clear') or None
			print(f'Telefone: {encontrado}')
		case 3:
			nome = input('Digite o nome: ')
			telefone = input('Digite o telefone: ')
			dados.append([nome, telefone])
			persistir_csv('arquivos/dados.csv', dados)
			system('clear') or None
			print('Telefone cadastrado com sucesso!')
		case 4:
			nome = input('Digite o nome: ')
			encontrado = None
			for item in dados:
				if item[0] == nome:
					encontrado = item
					break
			if not encontrado:
				system('clear') or None
				print('Não encontrado')
				continue
			dados.remove(encontrado)
			persistir_csv('arquivos/dados.csv', dados)
			system('clear') or None
			print('Excluido com sucesso')
		case 5:
			system('clear') or None
			break