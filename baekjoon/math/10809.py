from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)


S = list(input())
# list(input()) -> 한 글자씩 잘라서 리스트에 넣어줌
l = [-1]*26

S_dict = {alphabet:S.index(alphabet) for alphabet in S}
# 리스트의 인덱스 함수는 중복이 있을 경우 작은 값을 반환한다
# 알파벳 - 처음 등장하는 위치
alphabet_dict = {alphabet:alphabet_list.index(alphabet) for alphabet in alphabet_list}

# {'b':0} -> {1:0}으로
# b -> 1 a -> 0 ... 알파벳 - 알파벳의 순서로 바꾸고, 
# 1 : 0 -> l list의 첫번째 인덱스를 0으로 ...

# S의 key -> alphabet_dict[S_key]

n_dict = {alphabet_dict[key] :S_dict[key] for key in S_dict.keys()}
# n_dict -> l list의 1번째 인덱스 -> 0, ...
for key, values in n_dict.items():
    l[key] = values

print(*l)