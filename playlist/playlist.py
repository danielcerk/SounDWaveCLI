
'''

    Playlist é uma classe relacionado a playlist do Youtube,
    atualmente ,eu posso criar, editar e remover qualquer vídeo
    ou playlist . Mas, no futuro pretendo add mais funcionalidades
    como , talvez, ouvir músicas pelo CLI .



'''


import json


class PlayList:

    def __init__(self, nome_playlist: str ,
                 nome_antigo_playlist: str, nome_novo_playlist: str,
                 nome_video: str, artista: str, playlist_json: dict):
    
        self.nome_playlist = nome_playlist
        self.nome_antigo_playlist = nome_antigo_playlist
        self.nome_novo_playlist = nome_novo_playlist
        self.nome_video = nome_video
        self.artista = artista
        self.playlist_json = playlist_json

    def novaPlaylist(self, nome_playlist):

        with open('playlist.json', 'r') as arquivo:
            
            dados = json.load(arquivo)


        playlist = [{

        }]

        dados[nome_playlist] = playlist

        with open('playlist.json', 'w') as arquivo:

            json.dump(dados, arquivo, indent=4)



    def readPlaylist(self, nome_playlist):


        with open('playlist.json', 'r') as arquivo:

            dados = json.load(arquivo)


        if nome_playlist in dados:


            print(dados[nome_playlist])


        else:


            print('Playlist inexistente . Por favor, verifique a sua ortografia .')  


    def editPlayList(self, nome_antigo_playlist, nome_novo_playlist):

        nome_antigo = nome_antigo_playlist
        nome_novo = nome_novo_playlist

        with open('playlist.json', 'r') as arquivo:

            dados = json.load(arquivo)

        if nome_antigo in dados:

            dados[nome_novo] = dados[nome_antigo]

            del dados[nome_antigo]

            with open('playlist.json', 'w') as arquivo:

                json.dump(dados, arquivo, indent=4)

        else:


            print('Playlist inexistente . Por favor, verifique a sua ortografia .')            
            


    def deletePlaylist(self, nome_playlist):

        nome_a_remover = nome_playlist


        with open('playlist.json', 'r') as arquivo:
            
            dados = json.load(arquivo)

        if nome_a_remover in dados:
    
            del dados[nome_a_remover]

            with open('playlist.json', 'w') as arquivo:

                json.dump(dados, arquivo, indent=4)

        else:


            print('Playlist inexistente . Por favor, verifique a sua ortografia .')
            

    def addVideo(self, nome_playlist, nome_video,
        artista):

        with open('playlist.json', 'r') as arquivo:

            dados = json.load(arquivo)


        link_video = f"https://soundcloud.com/{artista}/{nome_video}"


        video = {

            "nome": nome_video,
            "link": link_video


        }


        if nome_playlist in dados:

            dados[nome_playlist].append(video)

            with open('playlist.json', 'w') as arquivo:

                json.dump(dados, arquivo, indent=4)


        else:

            print('Playlist inexistente . Por favor, verifique a sua ortografia .')


    def deleteVideo(self, nome_playlist, nome_video):

        nome_a_remover = nome_video

        with open('playlist.json', 'r') as arquivo:

            dados = json.load(arquivo)
    
        if nome_a_remover in [playlist["nome"] for playlist in dados[nome_playlist]]:

            indice_a_remover = next((index for (index, playlist) in enumerate(dados[nome_playlist]) if playlist["nome"] == nome_a_remover), None)
    
            if indice_a_remover is not None:

                del dados[nome_playlist][indice_a_remover]
        
                with open('playlist.json', 'w') as arquivo:

                    json.dump(dados, arquivo, indent=4)

        else:


            print('Playlist inexistente . Por favor, verifique a sua ortografia .')

