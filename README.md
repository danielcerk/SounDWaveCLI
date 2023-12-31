<div align='center'>
  <h1>SounDWaveCLI</h1>
  <p>
     <samp>
       SounDWave-CLI é uma CLI para ouvir sua música
    	preferida diretamente do prompt de comando de 
    	forma simples e fácil .
     </samp>
   </p> 
</div>

# Primeiros passos

Clone este repositório.

```
git clone https://github.com/danielcerk/SounDWaveCLI.git
```

Para instalar dependências.

```
pip install -r requirements.txt
```

# Parâmetros

<div align="center">

  | Parâmetro | Descrição | Obrigatório |
  | --- | --- | --- |
  | `--newpl` | Cria nova playlist. | Sim |
  | `--editpl` | Edita determinada playlist | Sim |
  | `--readpl` | Ler determinada playlist | Sim |
  | `--runpl` | Ouvir sua playlist | Sim |
  | `--delpl` | Deleta determinada playlist | Sim |
  | `--newmusica` | Adiciona nova música | Sim |
  | `--delmusica` | Deleta determinada música | Sim |
  | `--playmusica` | Dar play em música | Sim |
  | `--c` | Especificar o local que está localizado a música | Não |
  | `--n` | Criar novo nome para playlist playlist | Não |

  
</div>

# Uso

Aqui está alguns exemplos de como usar a SounDWave-CLI:

Criar playlist:

```
python main.py --newpl nome_playlist
```

Editar nome da playlist:

```
python main.py --editpl nome_antigo -n nome_novo
```

Ver todos as músicas da playlist:

```
python main.py --readpl nome_playlist
```

Ouvir as músicas da playlist:

```
python main.py --runpl nome_playlist
```

Deletar playlist:

```
python main.py --delpl nome_playlist
```

Adicionar música:

```
python main.py --newmusica nome_musica -c caminho_localizado -n nome_playlist
```

Deletar música:

```
python main.py --delmusica nome_musica -n nome_playlist
```

Dar play em música:

```
python main.py --playmusica caminho_musica
```



# Dependências

- certifi
- charset-normalizer
- fudge
- idna
- pygame
- requests
- simplejson
- urllib3


# Licença
<p>Código licenciado sob <a href='https://github.com/danielcerk/SounDWaveCLI/blob/main/LICENSE'> licença MIT</a></p>
