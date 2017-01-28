student=list()
n=int(input())
student = [[input(), float(input())] for _ in range(n)]
second_lowest=sorted(set([marks for name, marks in student]))[1]
print('\n'.join([a for a,b in sorted(student) if b == second_lowest]))
    
