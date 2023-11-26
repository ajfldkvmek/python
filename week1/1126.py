#strip() : 문자열 자르기 >> 기본: 공백제거, 매개변수지정> 일치하는 것들 제거
#
# '       abc'.strip())>> 'abc'
#
# 'abc'.strip('a')      >> 'bc'
# 'abca'.strip('a')     >> 'bc'
# 'abca'.strip('ac')    >> 'b'
# 
# '~~~'.count('~') >> 문자열에 count의 매개변수랑 일치하는 것의 수
#
# upper / lower >> 문자열 전체에 대해 대문자 / 소문자로 변경
#
# input(): 값 키보드로 입력
#

# python의 반복문>> for type in var: print(type) << for each문과 유사
line = 'olive'
for char in line:
    print("  "+ char)
print('-' * 30)

#문자열 길이>> len(str)
print(len('length of string'))
print('-' * 30)

# isupper: 문자열에서 대문자 char가 있는 지 보기 위해
line = 'Qwert Asdfg Zxcvb'
for char in line:
    if char.isupper():
        print(char)
print('-' * 30)

# format string>> f'~~ {}, {} .... ~~~'
num1 = 10
num2 = 20
num3 = 30

line = f'We have {num1}, {num2} and {num3}'
print(line)
print('-' * 30)

# substring
# 문자열 순서 바꾸기
songs = 'ABCDE'
print(songs)
songs = songs[1]+songs[2]+songs[3]+songs[4]+songs[0]
print(songs)
print('-' * 30)

# 특정 범위 잘라내기 (0부터 시작)
str1 = 'abcdefghijkl'
str2 = str1[3:7] #index3부터 index7까지 자르기
print(str2)
str3 = str1[3:] #3부터 뒤에 다 자르기
print(str3)
str4 = str1[:3] #3까지 자르기
print(str4)

str5 = str1[-4:] #뒤에서 부터 n만큼 자르기
print(str5)
## str1[8:20]이나 str1[-50:2]처럼 이상한 범위 지정해도 알아서 잘 잘라옴(각 'ijkl', 'ab')
print('-' * 30)

#for loop의 반복행위/범위 지정
s = 'abcdef'
for i in range(0, len(s), 3):
    print(s[i]) #>>문자열 s에 대해 0부터 s의 길이만큼 3칸씩 띄어서 출력

print('-' * 30)
for i in range(len(s)-1,-1,-1):
    print(s[i]) #역순 출력


#while loop
# i = 0
# while i < len(s): i선언후 범위지정
#   실행할행위
#   i = i+1
