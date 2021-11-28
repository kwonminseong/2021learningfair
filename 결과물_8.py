#8조 오징어게임 달고나 + 징검다리

import turtle
import random

# 프로그램 내 변수-----------------------------------------------------------------------------------------------------------------------

show = 0
start = 0
start_1 = 0
setting_value = 0
Easter_egg_1 = 0
Answer_2 = 0
bad_Answer = 0
dalgona_problem_answer = 0
death_point = 0

#-------------------------------------

count_life = 0
success = 0
success_step = 0
index = 0
shit_answer = 0
dalgona_point = 0

#프로그렘 시작------------------------- --------------------------------------------------------------------------------------------------

print("\n")
print("\n")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢛⣻⣽⣿⣾⣿⣶⣮⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣱⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣦⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣿⡿⠋⠀⠀⠀⠀⠀⠉⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣾⣿⠀⣀⣀⣤⠄⠀⠀⣀⣘⢿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣯⠐⣾⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⡟⠛⠛⠛⠉⢿⠀⠋⠛⠛⠿⢿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣷⣄⡐⠀⠀⠘⠀⠀⠀⠀⣄⣸⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢿⣿⣿⣿⣦⡄⣴⣤⡀⣠⣾⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢸⣿⣿⣿⣿⣃⣘⣿⣁⣹⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢹⣿⣿⣿⣿⣿⣛⣿⣛⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣟⠛⠛⠛⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⣤⣻⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣉⣀⣀⣀⣀⣀⣀⣸⣿⣿⣿⣿⣧⣽⣿⣼⣿⣿⣿⣿⣀⣀⣀⣀⣀⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("\n")

print("프론트맨 : 오징어 게임에 참여하신 여러분들 환영합니다.\n")
Name = input("오징어 게임에 참가할 이름을 입력해 주십시오. : ")

print("어떠한 오징어 게임에 참여하시겠습니까?")

while True:
    S = int(input("\n1. 달고나 게임\n2. 징검다리 게임\n"))

    if death_point == 5:
        print("당신은 오징어 게임에 참여할 자격을 잃었다.\n\n\n탕!")

    if S == 1:
        #달고나 게임
        print("프론트맨 : 지금부터 달고나를 나눠드리겠습니다. 선택하십시오.")
        while True: # 사용자로부터 임의의 도형을 선택받는 알고리즘
            if Easter_egg_1 == 5:
                print("\n프론트맨 : 흠... 재미없군,\n\n탕!")
                start = start + 1 # 문제 풀기 알고리즘를 위한 점검용 변수
                print("\n(당신은 죽었습니다. 유감입니다.)")
                break
            setting_value = int(input("\n'숫자'를 입력하십시오. (단, 숫자는 정수이며, 1~4까지이다.)"))

            if setting_value == 1: #사각형
                print("\n")
                print(" ***")
                print(" ***")
                print(" ***")
                print("\n")
                break

            elif setting_value == 2: #삼각형
                print("\n")
                print("   *")
                print("  ***")
                print(" *****")
                print("\n")
                break

            elif setting_value == 3: #원
                print("\n")
                print("   **")
                print("  ****")
                print("   **")
                print("\n")
                break

            elif setting_value == 4: #사다리꼴
                print("\n")
                print("   ***")
                print("  *****")
                print(" *******")
                print("\n")
                break
                    
            else: #사용자가 1~4에서의 숫자가 아닌 다른 숫자를 입력할 경우.
                print("다시 입력하십시오.\n")
                Easter_egg_1 += 1

        if setting_value == 1: # 사용자가 선택한 도형에 따라 문제 예시 출력
            print("1 ○ 4 = 4") # 사각형 문제
            print("2 ○ 5 = 10")
            print("3 ○ 6 = 18")
            
        elif setting_value == 2:
            print("3 ○ 2 = 3") # 삼각형 문제
            print("2 ○ 4 = 4")
            print("1 ○ 6 = 3")
            
        elif setting_value == 3:
            print("2 ○ = 4, π(X)") # 원 문제
            print("3 ○ = 9, π(X)")
            print("4 ○ = 16, π(X)")
            
        else:
            print("2 ○ 5 ○ 2 = 7") # 사다리꼴 문제
            print("4 ○ 3 ○ 2 = 7")
            print("6 ○ 1 ○ 2 = 6")

        while start == 0: # 문제 풀기 알고리즘
            print("\n문제를 이해하셨습니까?")
            Answer_1 = int(input("(1. 네 / 2. 아니오)\n"))
            if Answer_1 == 1:
                
                for i in range(50):
                    print("\n")
                    
                print("프론트맨 : 문제를 푸십시오.")

                if setting_value == 1:
                    print("3 ○ 3 = ?") # 사각형 문제
                    dalgona_problem_answer = 9

                elif setting_value == 2:
                    print("4 ○ 7 = ?") # 삼각형 문제
                    dalgona_problem_answer = 12

                elif setting_value == 3:
                    print("2 ○ = ?") # 원 문제
                    dalgona_problem_answer = 4

                else:
                    print("3 ○ 7 ○ 3 = ?") # 사다리꼴 문제
                    dalgona_problem_answer = 15
                
                while start == 0:
                    Answer_3 = int(input("\n답안 입력하기 : "))
                    if Answer_3 == dalgona_problem_answer:
                        start += 1
                        start_1 += 1
                        break
                    if bad_Answer == 5:
                        print("\n(○에는 어떠한 연산이 적용된 것 같다.. 한 번 더 살펴보자.).")
                        if setting_value == 1: #사각형
                            print("\n")
                            print(" ***")
                            print(" ***")
                            print(" ***")
                            print("\n")

                        elif setting_value == 2: #삼각형
                            print("\n")
                            print("   *")
                            print("  ***")
                            print(" *****")
                            print("\n")

                        elif setting_value == 3: #원
                            print("\n")
                            print("   **")
                            print("  ****")
                            print("   **")
                            print("\n")

                        else: #사다리꼴
                            print("\n")
                            print("   ***")
                            print("  *****")
                            print(" *******")
                            print("\n")
                    elif bad_Answer == 8:
                        print("\n(...달고나 모양의 넓이와 관련된 것 같다. 한 번 더 살펴보자.)")
                        if setting_value == 1: #사각형
                            print("\n")
                            print(" ***")
                            print(" ***")
                            print(" ***")
                            print("\n")

                        elif setting_value == 2: #삼각형
                            print("\n")
                            print("   *")
                            print("  ***")
                            print(" *****")
                            print("\n")

                        elif setting_value == 3: #원
                            print("\n")
                            print("   **")
                            print("  ****")
                            print("   **")
                            print("\n")

                        else: #사다리꼴
                            print("\n")
                            print("   ***")
                            print("  *****")
                            print(" *******")
                            print("\n")
                    elif bad_Answer == 10:
                        print("\n\n프론트맨 : 유감입니다. \n탕!")
                        start += 1
                        break
                    else:
                        bad_Answer = bad_Answer
                    bad_Answer += 1
            elif Answer_1 == 2:
                print("\n다시 한 번 보십시오.\n")

            else:
                print("\n제시된 숫자만 입력하십시오.\n")

        if start_1 == 1: # 바꾸기
            print("\n")
            print(Name, "씨 축하합니다. \nturtle 창을 확인해주세요.")

            turtle.clear()
            turtle.speed(10) 
            turtle.hideturtle()
            turtle.up()
            turtle.goto(0, -200)
            turtle.down()

            turtle.color("#FCD28C")
            turtle.begin_fill()
            turtle.circle(200, 360)
            turtle.end_fill()
            # 기본 달고나 원형
            
            turtle.color("#AF9261")
            turtle.pensize(10)

            turtle.up()
            turtle.goto(0, 100)
            turtle.down()
            turtle.right(120)
            turtle.forward(50)
            turtle.up()
            turtle.goto(0,100)
            turtle.down()
            turtle.left(60)
            turtle.forward(50)
            # ㅅ

            turtle.up()
            turtle.right(30)
            turtle.forward(30)
            turtle.down()
            for i in range(4):
                turtle.forward(50)
                turtle.right(90)
            # ㅁ

            turtle.up()
            turtle.forward(80)
            turtle.down()
            turtle.right(90)
            for i in range(3):
                turtle.forward(50)
                turtle.left(90)
            # ㄷ

            turtle.pensize(5)
            turtle.up()
            turtle.right(180)
            turtle.forward(45)
            turtle.left(90)
            turtle.forward(30)
            turtle.down()
            for i in range(2):
                turtle.left(90)
                turtle.forward(280)
                turtle.left(90)
                turtle.forward(110)
            # 사각 테두리

            turtle.up()
            turtle.goto(0, -180)
            turtle.down()
            turtle.circle(180, 360)
            # 진한 원 둘레

            show = int(input("\n다시 한 번 보시겠습니까?\n\n(1. 네 / 2. 아니오)\n"))

        if show == 1:

            turtle.clear()
            turtle.speed(10) 
            turtle.hideturtle()
            turtle.up()
            turtle.goto(0, -200)
            turtle.down()

            turtle.color("#FCD28C")
            turtle.begin_fill()
            turtle.circle(200, 360)
            turtle.end_fill()
            # 기본 달고나 원형
            
            turtle.color("#AF9261")
            turtle.pensize(10)

            turtle.up()
            turtle.goto(0, 100)
            turtle.down()
            turtle.right(120)
            turtle.forward(50)
            turtle.up()
            turtle.goto(0,100)
            turtle.down()
            turtle.left(60)
            turtle.forward(50)
            # ㅅ

            turtle.up()
            turtle.right(30)
            turtle.forward(30)
            turtle.down()
            for i in range(4):
                turtle.forward(50)
                turtle.right(90)
            # ㅁ

            turtle.up()
            turtle.forward(80)
            turtle.down()
            turtle.right(90)
            for i in range(3):
                turtle.forward(50)
                turtle.left(90)
            # ㄷ

            turtle.pensize(5)
            turtle.up()
            turtle.right(180)
            turtle.forward(45)
            turtle.left(90)
            turtle.forward(30)
            turtle.down()
            for i in range(2):
                turtle.left(90)
                turtle.forward(280)
                turtle.left(90)
                turtle.forward(110)
            # 사각 테두리

            turtle.up()
            turtle.goto(0, -180)
            turtle.down()
            turtle.circle(180, 360)
            # 진한 원 둘레
        
        break
    
    elif S == 2:
        #징검다리 게임------------------------------------------------------------------------------------------
        stepping_stone_count = int(input("\n몇 개의 징검다리를 건널 지 입력하시오.  : "))

        count_life = stepping_stone_count - 1
        
        stepping_stone_setting = []
    
        for i in range(0, stepping_stone_count):
            stepping_stone_setting.append(random.randrange(1,3))

        while True:
            
            if success == 1:

                for i in range(50):
                    print("\n")
                               
                for i in range(0, stepping_stone_count):
                    if stepping_stone_setting[i] == 1:
                        print("│───│")
                        print("■      □")
                    else:
                        print("│───│")
                        print("□      ■")
                print("│───│")
                
                dalgona_point += 1
                print("당신은 성공했습니다.")
                break
            
            if count_life == 0:
                for i in range(50):
                    print("\n")
                print("현재 남은 목숨 :", count_life)
                print("당신은 죽었습니다.")
                break
          
            for i in range(50):
                print("\n")
                
            for i in range(0, success_step, 1):
                if stepping_stone_setting[i] == 1:
                    print("│───│")
                    print("■      □")
                else:
                    print("│───│")
                    print("□      ■")

            if success_step == stepping_stone_count-1:
                success = 1

            else:
                success = 0

            for i in range(0, (stepping_stone_count-success_step), 1):
                print("│───│")
                print("□      □")
            print("│───│")
    
            print("현재 남은 목숨 :", count_life)       
            answer = int(input("\n(어느 징검다리로 건널까...)\n1. 왼쪽 / 2, 오른쪽\n(숫자를 입력하십시오."))

            if shit_answer == 1:
                print("1 혹은 2를 입력하십시오.")
                shit_answer = 0

            if stepping_stone_setting[index] == answer:
                success_step += 1
                index += 1

            elif stepping_stone_setting[index] != answer:
                count_life -= 1
                
            else:
                shit_answer += 1

        if dalgona_point == 1:
            print("\n")
            print(Name, "씨 축하합니다. \nturtle 창을 확인해주세요.")

            turtle.clear()
            turtle.speed(10) 
            turtle.hideturtle()
            turtle.up()
            turtle.goto(0, -200)
            turtle.down()

            turtle.color("#FCD28C")
            turtle.begin_fill()
            turtle.circle(200, 360)
            turtle.end_fill()
            # 기본 달고나 원형
            
            turtle.color("#AF9261")
            turtle.pensize(10)

            turtle.up()
            turtle.goto(0, 100)
            turtle.down()
            turtle.right(120)
            turtle.forward(50)
            turtle.up()
            turtle.goto(0,100)
            turtle.down()
            turtle.left(60)
            turtle.forward(50)
            # ㅅ

            turtle.up()
            turtle.right(30)
            turtle.forward(30)
            turtle.down()
            for i in range(4):
                turtle.forward(50)
                turtle.right(90)
            # ㅁ

            turtle.up()
            turtle.forward(80)
            turtle.down()
            turtle.right(90)
            for i in range(3):
                turtle.forward(50)
                turtle.left(90)
            # ㄷ

            turtle.pensize(5)
            turtle.up()
            turtle.right(180)
            turtle.forward(45)
            turtle.left(90)
            turtle.forward(30)
            turtle.down()
            for i in range(2):
                turtle.left(90)
                turtle.forward(280)
                turtle.left(90)
                turtle.forward(110)
            # 사각 테두리

            turtle.up()
            turtle.goto(0, -180)
            turtle.down()
            turtle.circle(180, 360)
            # 진한 원 둘레

            show = int(input("\n다시 한 번 보시겠습니까?\n\n(n1. 네 / 2. 아니오)\n"))

        if show == 1:
            turtle.clear()
            turtle.speed(10) 
            turtle.hideturtle()
            turtle.up()
            turtle.goto(0, -200)
            turtle.down()

            turtle.color("#FCD28C")
            turtle.begin_fill()
            turtle.circle(200, 360)
            turtle.end_fill()
            # 기본 달고나 원형
            
            turtle.color("#AF9261")
            turtle.pensize(10)

            turtle.up()
            turtle.goto(0, 100)
            turtle.down()
            turtle.right(120)
            turtle.forward(50)
            turtle.up()
            turtle.goto(0,100)
            turtle.down()
            turtle.left(60)
            turtle.forward(50)
            # ㅅ

            turtle.up()
            turtle.right(30)
            turtle.forward(30)
            turtle.down()
            for i in range(4):
                turtle.forward(50)
                turtle.right(90)
            # ㅁ

            turtle.up()
            turtle.forward(80)
            turtle.down()
            turtle.right(90)
            for i in range(3):
                turtle.forward(50)
                turtle.left(90)
            # ㄷ

            turtle.pensize(5)
            turtle.up()
            turtle.right(180)
            turtle.forward(45)
            turtle.left(90)
            turtle.forward(30)
            turtle.down()
            for i in range(2):
                turtle.left(90)
                turtle.forward(280)
                turtle.left(90)
                turtle.forward(110)
            # 사각 테두리

            turtle.up()
            turtle.goto(0, -180)
            turtle.down()
            turtle.circle(180, 360)
            # 진한 원 둘레

        break
    
    else:
        print("다시 입력하십시오.")
        death_point += 1
