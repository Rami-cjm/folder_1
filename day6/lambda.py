# a와 b를 받아서 더하는 함수 만들기

# def add_num(a, b):
#     print(a + b)


# add_num (3, 5)

# add_num = lambda a, b: a + b
# print(add_num(3, 5))


def word_len(a):
    print(len(a))

word_len("Hello World")
 
word_len = lambda a: len(a)
print(word_len("Hello World"))



# def squ(x):
#     print(x*x)

# squ(x)

squ = lambda x: x*x
print(squ(3))


my_list = [x*x for x in range(4)]
print(my_list)

#map을 사용하면 위의 x*x for x in range(4) 이말과 같아짐, map을 사용하면 뒤에 어디에서 가져올건지를 맨 뒤에 표시 해줘야함 my_list 적은 것 처럼
my_list_x = list(map(lambda x: x*x, my_list))


my_list_10 = my_list = [x for x in range(11)]
my_list_10 = list(map(lambda x:x, my_list_10))
print(my_list_10)

#my_even_numner =list(map(lambda x:range(11), if x % 2 == 0))

max_num = lambda x, y :print(x) if x > y else print(x)
max_num(3, 2)


my_list1 = list(filter(lambda x: x %2 ==0, range(11)))
print(my_list1)

list2 = [x for x in range (11) if x % 2 == 0]
print(list2)

list3 = list(filter(lambda x : x%2 ==0, range(11)))
print(list3)

list4 = list(map(lambda x, y : x + y, list2, list3))
print(list4)

#lambda 문제

#연습문제 1: 리스트의 각 요소에 2를 더한 새로운 리스트 생성
original_list = [1, 3, 5, 7, 9]
ex_1_list = list(map(lambda x :x + 2, original_list))
print(ex_1_list)

#연습문제 2: 홀수인 경우에만 제곱한 리스트 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex_2_list = list(map(lambda y:y if y % 2 == 0 else y*y, numbers))
print(ex_2_list)

#연습문제 3: 문자열의 길이가 5보다 큰 경우만 필터링
words = ["apple", "banana", "kiwi", "orange", "grape"]
ex_3_list = list(filter(lambda x: len(x) > 5, words))
print(ex_3_list)

#연습문제 4: 두 리스트의 각 요소를 곱한 리스트 생성
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
ex_4_list = list(map(lambda x, y: x+y, list1, list2))
print(ex_4_list)


#연습문제 5: 주어진 숫자의 제곱 또는 세제곱 계산
number = 7


#연습문제 6: 문제: 1~10까지의 숫자 중 lamda를 이용해서 숫자를 짝수, 홀수 그리고 0으로 구분하기
ex_6_list = list(map(lambda x: '0' if x ==0 else ("odd number" if x % 2 == 1 else 'even number'), range(11)))
print(ex_6_list)


