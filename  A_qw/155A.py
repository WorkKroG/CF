num = int(input())
st = input()
balls = st.split()

balls_min = balls[0]
balls_max = balls[0]
k = 0

for i in balls:
    if int(i) > int(balls_max):
        k += 1
        balls_max = i
    elif int(i) < int(balls_min):
        k += 1
        balls_min = i

print(k)
