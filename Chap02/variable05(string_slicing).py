# 02 - 2 문자열 자료형
# 슬라이싱으로 문자열 나누기 

a = "20210816Sunny"
#    0123456789101112
year= a[:4] # 처음부터 a[3] 까지
month = a[4:6]
day = a[6:8]
weather = a[8:]
print(year, month, day, weather)

# pithon 이라는 문자열은 python으로 바꾸려면?
a = "pithon"
print(a[:1]+'y'+a[2:])