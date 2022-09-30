from pytube import Playlist

print('''.  . ,--,--' .-,--. .          .        .  .-,--.                .            .        
|  | `- |     '|__/ |  ,-. . . |  . ,-. |- ' |   \ ,-. . , , ,-. |  ,-. ,-. ,-| ,-. ,-.
|  |  , |     ,|    |  ,-| | | |  | `-. |  , |   / | | |/|/  | | |  | | ,-| | | |-' |  
`--|  `-'     `'    `' `-^ `-| `' ' `-' `' `-^--'  `-' ' '   ' ' `' `-' `-^ `-^ `-' '  
.- |                        /|                                                         
`--'                       `-'                                                         ''')

print('''_   _   _   _   _   _   _     _   _   _   _   _     _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
( A | u | t | h | o | r | : ) ( B | r | u | n | o ) ( C | a | r | r | a | r | a )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ ''')

url = input('Digite a url da Playlist: ')
path = input('Indique o caminho de onde voce quer salvar: ')

playlist = Playlist(url)
print('\nTamanho da Playlist:', len(playlist), 'tracks\n')
cont = 0

for v in playlist.videos:
    cont += 1
    print('Fazendo o download de:', v.title, '\t',cont,'/',len(playlist))
    v.streams.get_audio_only().download(path)
print("Download concluido!")

