misha = 'Mishka'
cris = 'Chris'
friend_win = 'Friendship is magic!^^'

misha_count = 0
cris_count = 0

n = int(input())

for i in range(0, n):
    round_play = input()
    if int(round_play[0]) > int(round_play[2]):
        misha_count += 1
    elif int(round_play[0]) < int(round_play[2]):
        cris_count += 1

if misha_count > cris_count:
    print(misha)
elif misha_count < cris_count:
    print(cris)
else:
    print(friend_win)
