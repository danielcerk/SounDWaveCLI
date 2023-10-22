from playlist import playlist
from musica import musica
from info import info

'''

Transformar caminho e nome em argumentos
criar a opção de pausar, reiniciar, retomar

'''


def run():

	# Argumentos do app

	arguments = info.info()
	args = arguments.add_arguments()


	# Ações envolvendo playlist e música

	pl = playlist.PlayList()
	play_musica = musica.musicPlayer()

	if args.newpl:

	    pl.novaPlaylist(args.newpl)


	elif args.delpl:

	    pl.deletePlaylist(args.delpl)


	elif args.editpl:

	    # args.editpl é o nome antigo, existente
	    # args.novo_nome é o novo nome

	    # juntos eles devem editar o nome da chave

	    pl.editPlayList(args.editpl, args.n)


	elif args.readpl:


	    pl.readPlaylist(args.readpl)


	elif args.runpl:

	    play_musica.runPlaylist(args.runpl)


	elif args.newmusica:


	    pl.addVideo(args.n, args.newmusica, args.c)


	elif args.delmusica:


	    pl.deleteVideo(args.n, args.delmusica)


	elif args.playmusica:


	    play_musica.play(args.playmusica)
	    

if __name__ == '__main__':

	run()