from playlist import playlist
from musica import musica
import argparse as arg

# link do youtube deve ser substituido por soundcloud

parser = arg.ArgumentParser(description='''

    CliForWeb é uma Cli para monitorar a ativadade
    web de uma forma organizada como fazer agendamentos,
    playlists, ordem de entrada em sites, salvar urls e
    contas .

''')

# Uso para playlist

parser.add_argument('--newpl', help='Comando para criar nova playlist.')
parser.add_argument('--editpl', help='Comando para editar determinada playlist.')
parser.add_argument('caminho', nargs='?', help='Caminho que está localizado a música') # Substituir mais tarde por caminho
parser.add_argument('nome', nargs='?', help='Usado para substituir o nome antigo da playlist por um novo.')
parser.add_argument('--readpl', help='Comando para ler determinada playlist.')
parser.add_argument('--runpl', help='Use o comando para ouvir sua playlist')
parser.add_argument('--delpl', help='Comando para deletar determinada playlist.')


# Video

parser.add_argument('--newvideo', help='Comando para criar novo vídeo.')
parser.add_argument('--delvideo', help='Comando para deletar determinado vídeo.')

# Musica player

# Cada música precisa de um nome e o autor

parser.add_argument('--playmusic', help='Comando para iniciar sua música')


args = parser.parse_args()


pl = playlist.PlayList('', '', '', '','', {})
play_musica = musica.musicPlayer('')

if args.newpl:

    pl.novaPlaylist(args.newpl)


elif args.delpl:

    pl.deletePlaylist(args.delpl)


elif args.editpl:

    # args.editpl é o nome antigo, existente
    # args.novo_nome é o novo nome

    # juntos eles devem editar o nome da chave

    pl.editPlayList(args.editpl, args.nome)


elif args.readpl:


    pl.readPlaylist(args.readpl)


elif args.runpl:

    print('Rodando playlist')


elif args.newvideo:


    pl.addVideo(args.nome, args.newvideo, args.caminho)


elif args.delvideo:


    pl.deleteVideo(args.nome, args.delvideo)


elif args.playmusic:


    play_musica.play(args.playmusic)