def make_album(artist, album, song_number=None):
    if song_number:
        full_album={'artist':artist.title(), 'album':album.title(),'song_number':song_number}
    else:
        full_album={'artist':artist.title(), 'album':album.title()}
    return full_album

full_album={}
while True:
    artist=input("please type the artist name you like: (or type q to quit)")
    if artist=='q':
        break
    album=input("please type the album name you like: (or type q to quit)")
    if album=='q':
        break
    full_album=make_album(artist,album)
    print(full_album)

