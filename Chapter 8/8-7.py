def make_album(artist, album, song_number=None):
    if song_number:
        full_album={'artist':artist.title(), 'album':album.title(),'song_number':song_number}
    else:
        full_album={'artist':artist.title(), 'album':album.title()}
    return full_album

print(make_album('lady gaga','romance',12))
print(make_album('王菲', '传奇'))
print(make_album('孙燕姿','完美的一天'))
