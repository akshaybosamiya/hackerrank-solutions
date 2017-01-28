#https://www.hackerrank.com/challenges/exceptions
T = input().strip()
for i in range(int(T)):
    a,b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)