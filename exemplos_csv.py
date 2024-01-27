import csv

# with open('arquivos/pessoas.csv', 'r') as arquivo:
# 	leitor = csv.reader(arquivo)
# 	next(leitor)
# 	for linha in leitor:
# 		print(f'Nome: {linha[0]} Email: {linha[2]}')

# with open('arquivos/pessoas.csv', 'a') as arquivo:
# 	escritor = csv.writer(arquivo)
# 	escritor.writerow(['Guido', '(71) 9 9999-9999', 'guido@email.com'])

with open('arquivos/pessoas.csv', 'r') as arquivo:
	lista = list(csv.reader(arquivo))

with open('arquivos/pessoas.csv', 'w') as arquivo:
	escritor = csv.writer(arquivo)
	#escritor.writerows(lista)
	for linha in lista:
		if linha[2] == 'guido@email.com':
			continue
		escritor.writerow(linha)