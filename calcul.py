import time #time모듈 불러오기

def add (x,y): #더하기
    return x+y
def remove (x,y): #빼기
    return x-y
def multiply (x,y): #곱하기
    return x*y
def divide (x,y): #나누기
    if y==0:
        return None
    else:
        return x/y
def square (x,y): #제곱
    return(x**y)
def rest (x,y): #나머지
    return x%y
    
while True:
    mode=input("\n무엇을할지 입력하세요!\n1.계산, 2.종료:") #방식 받기

    if mode == '1' : #계산을 한다면
        try:
            calcul=input("\n계산 방식을 입력하세요. 1.더하기, 2.빼기, 3.곱하기, 4.나누기, 5.제곱, 6.나머지:")#계산 방식 받기
            x=float(input("\n첫번째 수를 입력하세요!:")) #x값 받기
            y=float(input("\n두번째 수를 입력하세요!:")) #,y값 받기

            if calcul == '1':
                print("\n값:",add(x,y)) #더하기

            elif calcul == '2':
                print("\n값:",remove(x,y)) #빼기
            
            elif calcul == '3':
                print("\n값:",multiply(x,y)) #곱하기

            elif calcul == '4':
                division=divide(x,y)
                if division == None:
                    print("\n0으로 나눌 수 없습니다.")
                else:
                    print("\n값:",division) #나누기

            elif calcul == '5':
                print("\n값:",square(x,y)) #제곱

            elif calcul == '6':
                print("\n값:",rest(x,y)) #나머지
            
        except ValueError: #예외 처리
            print("숫자를 입력하세요!")

    elif mode == '2':
        print("계산기를 종료합니다!")
        time.sleep(0.4)
        break #종료

    else:
        print("올바른 수를 입력하세요!") #이상한 수 예외

