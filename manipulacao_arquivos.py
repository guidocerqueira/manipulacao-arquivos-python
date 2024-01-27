# arquivo = open('arquivos/dados.txt', 'r')
# conteudo = arquivo.read()
# print(conteudo)
# arquivo.close()

# with open('arquivos/dados.txt', 'r') as arquivo:
# 	conteudo = arquivo.read()
# 	print(type(conteudo))

# with open('arquivos/dados.txt', 'r') as arquivo:
# 	linha = arquivo.readline()
# 	while linha:
# 		print(linha)
# 		linha = arquivo.readline()

# with open('arquivos/dados.txt', 'r') as arquivo:
# 	for x in range(3):
# 		linha = arquivo.readline()
# 		print(linha)

# with open('arquivos/dados.txt', 'r') as arquivo:
# 	conteudo = arquivo.readlines()
# 	for x in conteudo:
# 		print(x)

# with open('arquivos/dados.txt', 'w') as arquivo:
# 	arquivo.write('teste')

# with open('arquivos/dados.txt', 'a') as arquivo:
# 	arquivo.write('\nteste')

# nomes = ['\nantonio', '\njosé', '\nGustavo']

# with open('arquivos/dados.txt', 'a') as arquivo:
# 	arquivo.writelines(nomes)

# with open('arquivos/dados.txt', 'x') as arquivo:
# 	arquivo.write('\nteste')

# import os

# os.rename('arquivos/teste.txt', 'arquivos/dados.txt')
# os.remove('arquivos/dados.txt')

# import shutil

# shutil.move('arquivos/dados.txt', 'dados.txt')
# shutil.move('dados.txt', 'arquivos/dados.txt')