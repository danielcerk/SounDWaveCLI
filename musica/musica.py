import pygame
import keyboard
import time

pygame.mixer.pre_init(44100, -16, 2, 2048)

class musicPlayer:

	def __init__(self, musica: str):

		self.musica = musica


	# ok

	def play(self, musica):

		pygame.init()

		try:

			pygame.mixer.music.load(musica)
			pygame.mixer.music.play()

			while pygame.mixer.music.get_busy():

				pass

		except pygame.error:
				
			print('Musica não encontrada . Por favor, verifique a ortografia .')

		pygame.quit()