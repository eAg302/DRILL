class Star:
    type = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)

print('x IS ', Star.x) #OK
Star.change() #OK
print('x Is ',Star.x) #OK

star = Star() #OK
print('x IS ', star.x) #OK
star.change() #Error


# 파이썬 클래스에서 생성자 없어도 되긴함
# 클래스를 통해 생성한 객체(인스턴스) 가 하나인 경우 = 싱글톤
# 싱글톤을 쓰는 이유 : 글로벌을 한 곳에 모아서 단일하게 사용하기위해


# 파이썬은 다음과 같이 처리함
# star.change() ==> Star.change(star)
# 파이썬의 변수는 그 자체가 포인터임


