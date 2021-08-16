# 01 장 파이썬이란 무엇인가?
# 파이썬 : 인터프리터 언어 (한 줄씩 소스 코드를 해석해서 그때 그때 실행해 결과를 바로 확인할 수 있는 언어)

# simple.py
languages = ['python', 'perl', 'c', 'Java']

for lang in languages:
    if lang in ['python', 'perl']:  # 파이썬은 단락을 구분하는 괄호 문자가 보이지 않음 
        print("%6s need interpreter" %lang)
    elif lang in ['c', 'Java']:
        print("%6s need compiler" %lang)
    else:
        print("should not reach here")

# 파이썬은 복소수도 지원한다. 파이썬에서는 j를 사용하여 복소수를 나타낸다.
a = 2+ 3j
b = 3
print(a*b)