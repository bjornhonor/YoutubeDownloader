from pytube import YouTube

print('''.  . ,--,--'  ,.   ,.   .         .-,--.                .            .        
|  | `- |     `|  / . ,-| ,-. ,-. ' |   \ ,-. . , , ,-. |  ,-. ,-. ,-| ,-. ,-.
|  |  , |      | /  | | | |-' | | , |   / | | |/|/  | | |  | | ,-| | | |-' |  
`--|  `-'      `'   ' `-^ `-' `-' `-^--'  `-' ' '   ' ' `' `-' `-^ `-^ `-' '  
.- |                                                                          
`--'        ''')


print('''_   _   _   _   _   _   _     _   _   _   _   _     _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ 
( A | u | t | h | o | r | : ) ( B | r | u | n | o ) ( C | a | r | r | a | r | a )
 \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ ''')

url = input('\nDigite a url do video: ')
path = input('Indique o caminho de onde voce quer salvar: ')

video = YouTube(url)

print('\nFazendo o download de:', video.title)
print('Duracao:', video.length, 'segundos')

video.streams.get_highest_resolution().download()

print("\nDownload concluido!")

