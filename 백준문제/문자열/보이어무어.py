def booyer_moore(s, p):
    r_p = ''.join((list(p)[::-1]))
    skip_dict = {char:idx for idx, char in enumerate(r_p)} # {'a': 0}
    i = 0
    while i < len(s) - len(p): # 시작점을 0으로, i는 인덱스므로 텍스트 길이에서 패턴 길이를 뺀것보다 작게.
        for j in range(len(p)-1, -1, -1): # 패턴 개수만큼 비교
            if p[j] != s[i+j]: # i는 시작점이므로 j를 더해준다.
                tmp = skip_dict.get(s[i+j]) # 같지 않은 경우, 해당 텍스트의 char를 skip_dict에서 찾음.
                if tmp == None:
                    i += len(p)
                else:
                    i += tmp
                break
        else:
            return 1
    return 0

print(booyer_moore('asdjfsdjlksjwaterasdfklkjlasdf', 'watder'))