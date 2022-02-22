word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=' ,'z=']

for A in croatia:
    word = word.replace(A, "*")

print(len(word))




word = input()

answer = len(word)  # 일단 총 길이를 재고 여기서 차감하는 형태로 문제 구성
for idx, letter in enumerate(word):
    # 일단 길이 자체가 3이 이상인 경우만 첫번째 케이스를 해야함
    if letter == '=' and word[idx-1] == 'z' and idx >= 2 and word[idx-2] == 'd':  # dz=
        answer -= 2  # 3개짜리는 1개로 세야 하니까 -2 로 조정!
    elif letter == '=' and word[idx-1] in {'c', 's', 'z'}:  # set in 을 활용하는 경우 빠른 풀이 가능 O(1)
        answer -= 1  # c=, s=, z= 를 커버하는 케이스
    elif letter == 'j' and word[idx-1] in {'l', 'n'}:
        answer -= 1  # lj, nj 를 커버하는 케이스
    elif letter == '-' and word[idx-1] in {'c', 'd'}:
        answer -= 1  # c-, d- 를 커버하는 케이스

print(answer)
