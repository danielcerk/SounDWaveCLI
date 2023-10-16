from playlist import playlist
from musica import musica
import argparse as arg
import keyboard

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
parser.add_argument('nome', nargs='?', help='Usado para substituir o nome antigo da playlist por um novo.')
parser.add_argument('url', nargs='?', help='Url do vídeo .')
parser.add_argument('--readpl', help='Comando para ler determinada playlist.')
parser.add_argument('--delpl', help='Comando para deletar determinada playlist.')


# Video

parser.add_argument('--newvideo', help='Comando para criar nova playlist.')
parser.add_argument('--delvideo', help='Comando para deletar determinada playlist.')

# Musica player

# Cada música precisa de um nome e o autor

parser.add_argument('--playmusic', help='Comando para iniciar sua música')


args = parser.parse_args()


pl = playlist.PlayList('', '', '', '','', {})
play_musica = musica.musicPlayer('', '')

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



elif args.newvideo:


    pl.addVideo(args.nome, args.newvideo, args.url)


elif args.delvideo:


    pl.deleteVideo(args.nome, args.delvideo)


elif args.playmusic:

    #play_musica.play(args.playmusic, args.nome)

    keyboard.on_press_key("p", print('Pausar'))
    keyboard.on_press_key("k", print('Continuar'))
    keyboard.on_press_key("r", print('Reiniciar'))

