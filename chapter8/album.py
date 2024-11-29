def make_album(artist, title, song_count=None):
    if song_count:
        album = {artist: [title, song_count]}
    else:
        album = {artist: [title]}
    return album

fir = make_album("jon", "I feel bad")
print(fir)
sec = make_album("bill", "I feel good")
print(sec)
thi = make_album("mel", "I feel dumb")
print(thi)
fou = make_album("ber", "I love it", 11)
print(fou)