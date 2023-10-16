import pygame
import soundcloud
import time

pygame.init()

class musicPlayer:

	def __init__(self, nome_musica: str, artista: str):

		self.nome_musica = nome_musica
		self.artista = artista


	def play(self, nome_musica, artista):


		client = soundcloud.Client(client_id='SEU_CLIENT_ID')

		musica_url = f'https://soundcloud.com/{artista}/{nome_musica}'

		track = client.get('/resolve', url=musica_url)

		stream_url = client.get(track.stream_url, allow_redirects=False)

		stream_url = str(client.get(track.stream_url, allow_redirects=False).location)

		pygame.mixer.music.load(stream_url)

		pygame.mixer.music.play()

		print(f"Reproduzindo: {track.title} de {track.user['username']}")


	# Para pausar, continuar e replay podemos usar atalhos na tecla


	def pause(self):

		# Pausa a reprodução

		pygame.mixer.music.pause()
		print("Pausado")

	def continuar_a_musica(self):

		# Retome a reprodução
		
		pygame.mixer.music.unpause()
		print("Retomado")


	def replay(self):

		# Reinicia a faixa para o início

		pygame.mixer.music.rewind()
		print("Reiniciado")




