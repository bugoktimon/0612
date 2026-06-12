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

print(mart.keys())
print(mart.values())
# items() : key와 value를 쌍(튜플)으로 모아서 가져오기 (★가장 많이 씀)
print(mart.items())

for fruit, price in mart.items():
    print(f"{fruit}의 가격은 {price}원입니다.") # f뜻은 내 안에 변수 있다.는 의미


