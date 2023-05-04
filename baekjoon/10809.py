from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)


# S = list(input())
# list(input()) -> 한 글자씩 잘라서 리스트에 넣어줌
l = [-1]*26
S = ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
S_dict = {alphabet:S.index(alphabet) for alphabet in S}
# 리스트의 인덱스 함수는 중복이 있을 경우 작은 값을 반환한다
alphabet_dict = {alphabet:alphabet_list.index(alphabet) for alphabet in alphabet_list}
# S_dict의 key가 숫자로 바뀌어야 함
# {'b':0} -> {1:0}으로
# 'b' : 1
# for key in S_dict.keys():
    # S_dict[alphabet_dict[key]] = S_dict.pop(key)

