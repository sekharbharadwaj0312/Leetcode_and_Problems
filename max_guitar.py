def max_guitar_earnings(N, songs):
    songs.sort(reverse=True)  

    earnings = 0
    for i in range(N):
        earnings += (N - i) * songs[i]

    return earnings

N = int(input())
songs = []
for _ in range(N):
    x_i = int(input())
    songs.append(x_i)

result = max_guitar_earnings(N, songs)
print(result)
