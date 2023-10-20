from playlist import playlist
from musica import musica
from info import info


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

	    pl.editPlayList(args.editpl, args.caminho)


	elif args.readpl:


	    pl.readPlaylist(args.readpl)


	elif args.runpl:

	    print('Rodando playlist')


	elif args.newmusica:


	    pl.addVideo(args.nome, args.newmusica, args.caminho)


	elif args.delmusica:


	    pl.deleteVideo(args.caminho, args.delmusica)


	elif args.playmusica:


	    play_musica.play(args.playmusica)


	elif args.version:

	    arguments.version()


if __name__ == '__main__':

	run()