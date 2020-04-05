dolg = input()

if dolg[0] == '-':
    srt_dolg_1 = dolg[:-1]
    srt_dolg_2 = dolg[:-2] + dolg[-1:]

    if srt_dolg_1 == '-':
        print(0)
    else:
        print(max(int(srt_dolg_1), int(srt_dolg_2)))
else:
    print(dolg)
