import argparse


class info:

	def __init__(self):

		pass

	def add_arguments(self):

		parser = argparse.ArgumentParser(description='''

    	SounDWave-CLI é uma CLI para ouvir sua música
    	preferida diretamente do prompt de comando de 
    	forma simples e fácil .

		''')

		for i in self.arguments():
			
			parser.add_argument(i[0], help=i[1])

		return parser.parse_args()

	def arguments(self):

		return [

		('--newpl', 'Comando para criar nova playlist.'),
		('--editpl', 'Comando para editar determinada playlist.'),
		('--readpl', 'Comando para ler determinada playlist.'),
		('--runpl', 'Use o comando para ouvir sua playlist.'),
		('--delpl', 'Comando para deletar determinada playlist.'),
		('--newmusica', 'Comando para adicionar nova música.'),
		('--delmusica', 'Comando para deletar determinada música.'),
		('--playmusica', 'Comando para iniciar sua música.'),
		('--c', 'Caminho que está localizado a música'),
		('--n', 'Usado para substituir o nome antigo da playlist por um novo.')
		]