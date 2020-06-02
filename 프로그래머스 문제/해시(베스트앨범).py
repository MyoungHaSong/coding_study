from collections import defaultdict
def solution(genres,  plays):
    play_count_g = defaultdict(int)
    songs_in_g = defaultdict(list)
    plays = [(idx, val) for idx, val in enumerate(plays)]
    for i in range(len(plays)):
        play_count_g[genres[i]] += plays[i][1]
        songs_in_g[genres[i]].append((-plays[i][1],plays[i][0]))
    order = sorted(play_count_g.keys(), key = lambda x : play_count_g[x], reverse = True)
    answer = list()
    for i in order:
        answer.extend([song_id for minus_play, song_id in sorted(songs_in_g[i])[:2]])
    return answer
        
        