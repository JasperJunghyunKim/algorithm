genres = ["classic", "pop", "classic", "classic", "pop", "pop", "pop", "rap"]
plays = [500, 600, 150, 800, 2500, 2500, 2500, 8000]

########################################
# T2 : sorted key 썼는데, 이것도 더러움
########################################
def solution(genres, plays):
    answer = []
    genres_in_order = dict()
    songs_in_order = dict()

    for index, (genre, play) in enumerate(zip(genres, plays)):
        genres_in_order[genre] = genres_in_order.get(genre, 0) + play
        if (genre, play) not in songs_in_order: songs_in_order[(genre, play)] = [index]
        else: songs_in_order[(genre, play)].append(index)

    genres_in_order = sorted(genres_in_order.items(), key = lambda x : -x[1])
    songs_in_order = sorted(songs_in_order.items(), key = lambda x : (x[0][0], -x[0][1]))
    for genre, _ in genres_in_order:
        print(genre)
        tmp = []
        for (g, p), t in songs_in_order:
            if genre == g:
                t.sort()
                tmp.extend(t)
        answer.extend(tmp[:2])

    return answer
########################################
# T1 : 노가다
########################################
# def solution(genres, plays):
#     answer = []
#     sorted_genres = dict()
#     sorted_songs = dict()

#     for index, (genre, play) in enumerate(zip(genres, plays)):
#         if genre not in sorted_genres: sorted_genres.update({genre : 0})
#         sorted_genres[genre] += play
#         if genre not in sorted_songs: sorted_songs.update({genre: dict()})
#         if play not in sorted_songs[genre]: sorted_songs[genre].update({play: []})
#         sorted_songs[genre][play].append(index)

#     # sort genre desc
#     genre_in_order = []
#     for genre, total_played in sorted_genres.items():
#         genre_in_order.append((total_played, genre))
#     genre_in_order.sort(reverse=True)

#     # print(genre_in_order)
#     # print(sorted_songs)

#     # derive result
#     for total_played, genre in genre_in_order:
#         song_in_order = []
#         for plays, tracks in sorted_songs[genre].items():
#             song_in_order.append((plays, sorted(tracks))) # (100, [1,2])
#         song_in_order.sort(reverse=True)
#         print(song_in_order)
#         if len(song_in_order[0][1]) >= 2: answer.extend(song_in_order[0][1][:2])
#         else: 
#             if len(song_in_order) == 1: answer.append(song_in_order[0][1][0])
#             else: 
#                 answer.append(song_in_order[0][1][0])
#                 answer.append(song_in_order[1][1][0])

#     return answer

print(solution(genres, plays))