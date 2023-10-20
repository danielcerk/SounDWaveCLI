import pygame
import keyboard
import time

class musicPlayer:

	def __init__(self):

		self.musica = None

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