#import sys

#sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    p, a, b = map(int, input().split())

    def count(page, alpha): # page: 전체 페이지 숫자.
        cnt = 0
        s = 1
        e = page

        while s <= e:
            cnt += 1
            middle = s + int((e-s)/2)
            # print(f'#{alpha}, {cnt}: {middle}')

            if middle == alpha: # alpha: 각 알파벳이 찾으려는 page 번호.
                return cnt
            elif middle > alpha:
                e = middle
            else:
                s = middle
    
    cnt_a = count(p, a)
    cnt_b = count(p, b)

    if cnt_a > cnt_b:
        print(f'#{test_case} B')
    elif cnt_a < cnt_b:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')


    # ///////////////////////////////////////////////////////////////////////////////////
