import pygame
import keyboard
import threading
import json
import time


class musicPlayer:

	def __init__(self):

		self.musica = None
		self.nome_playlist = None
		self.volume = 1.0
		self.estado_volume_mudado = False

	def controlar_musica(self):

		while True:

			if keyboard.is_pressed('p'):

				pygame.mixer.music.pause()

			if keyboard.is_pressed('r'):

				pygame.mixer.music.unpause()

			if keyboard.is_pressed('space'):

				pygame.mixer.music.rewind()

			if keyboard.is_pressed('+') and not self.estado_volume_mudado:

				self.aumentar_volume()
				self.volume_changed = True

			if keyboard.is_pressed('-') and not self.estado_volume_mudado:

				self.diminuir_volume()
				self.estado_volume_mudado = True

			if not keyboard.is_pressed('+') and not keyboard.is_pressed('-'):

				self.estado_volume_mudado = False

			if keyboard.is_pressed('b'):

				break


	def aumentar_volume(self):

		if self.volume < 1.0:

			self.volume += 0.1
			pygame.mixer.music.set_volume(self.volume)

	def diminuir_volume(self):

		if self.volume > 0.0:

			self.volume -= 0.1
			pygame.mixer.music.set_volume(self.volume)

	def play(self, musica):

		pygame.init()

		try:

			pygame.mixer.music.load(musica)

			print('Pressione b para sair')

			pygame.mixer.music.set_volume(self.volume)
			# Ouvir a música

			music_thread = threading.Thread(target=pygame.mixer.music.play)
			music_thread.start()

			# Controlar a música

			control_thread = threading.Thread(target=self.controlar_musica())
			control_thread.start()
	
			music_thread.join()
			control_thread.join()

		except pygame.error:
				
			print('Musica não encontrada . Por favor, verifique a ortografia .')

		pygame.quit()


	def runPlaylist(self, nome_playlist):

		pygame.init()

		with open('playlist.json', 'r') as arquivo:

			dados = json.load(arquivo)


		if nome_playlist in dados:

			playlist = dados[nome_playlist]

			for i in playlist:

				nome = i['nome']
				caminho = i['caminho']

				try:

					pygame.mixer.music.load(caminho)

					print(f'Música: {nome}')

					duracao_musica = pygame.mixer.Sound(caminho).get_length()

					minutos = int(duracao_musica // 60)
					segundos = int(duracao_musica % 60)

					print(f'Duração da música: {minutos} minutos e {segundos} segundos')

					pygame.mixer.music.play()

					while pygame.mixer.music.get_busy():

						pass
					
					

					print('Pressione b para ir pra próxima música')

					# Ouvir a música

					music_thread = threading.Thread(target=pygame.mixer.music.play)
					music_thread.start()

					# Controlar a música

					control_thread = threading.Thread(target=self.controlar_musica())
					control_thread.start()
				

					music_thread.join()					
					control_thread.join()

				except pygame.error:

					print('Musica não encontrada . Por favor, verifique a ortografia .')

			print('Reprodução finalizada : )')

			pygame.quit()

				
