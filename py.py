user = {
    "name" : "홍길동",
    "age" : 55,
    "skills" : ["Python", "Git"]
}
user["name"] = "스티브잡스"

print(user["name"],"은 나이가 ", user["age"], "먹었습니다.")

# print(user["name"]) # 아래 보다 이 방법이 더 빠름 

# print(user.get("age"))

#2
mart = {
    "apple": 1000, 
    "banana":2500, 
    "orange":1500
}
mart["apple"] = 5000

print(mart.keys()) # 결과 list
print(mart.values()) # 결과 list
# items() : key와 value를 쌍(튜플)으로 모아서 가져오기 (★가장 많이 씀) 
print(mart.items()) # 결과 튜플

for fruit, price in mart.items():
    print(f"{fruit}의 가격은 {price}원입니다.") # f뜻은 내 안에 변수 있다.는 의미


for key in mart.keys():  # 리스트
    print(f"mart 딕셔너리의 key값은 {key}가 있습니다.")



mart2 = {"apple": 1000, "banana": 2500} # key, value

print("apple" in mart2)  # True
print("grape" in mart2)  # False


# 튜플에 대해서 - 튜플은 수정이 불가함. 
my_tuple = (1, 2, 3)
another_tuple = 10, 20, 30 # 소괄호 생략 가능
# my_tuple[0] = 99 # 이렇게 수정하면 에러남. 수정할 수 없음.

my_list = [1, 2, 3]
my_list[0] = 99 # [99, 2, 3]으로 정상 변경됨

# 리스트와 튜플의 결정적 차이 (중요!)
# 리스트 [ ]: 데이터 변경 가능 (Mutable). 수정, 추가, 삭제가 마음대로 가능합니다.
# 튜플 ( ): 데이터 변경 불가능 (Immutable). 한 번 생성되면 절대 바꿀 수 없습니다.

numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1:4]) # (1, 2, 3) -> 인덱스 1부터 3까지


a = (1, 2)
b = (3, 4)

print(a + b)  # (1, 2, 3, 4) -> 새로운 튜플 생성
print(a * 3)  # (1, 2, 1, 2, 1, 2) -> 3번 반복


# 1. 패킹
info = ('Tom', 20, 'Seoul')

# 2. 언패킹 (튜플의 개수와 변수의 개수가 같아야 합니다)
name, age, city = info

print(name)  # Tom
print(age)   # 20
print(city)  # Seoul


x = 10
y = 20

# 두 값을 서로 바꾸기 (튜플 언패킹 원리)
x, y = y, x

print(x)  # 20
print(y)  # 10


sample = (1, 2, 3, 2, 4, 2)
print(sample.count(2)) # 2가 3개 들어있음
print(sample.index(3)) # index는 순번

# 깃 테스트를 위한 주석

