veeru=int(input())
for i in range(veeru):
    N,X,P=list(map(int,input().split()))
    score=X*3
if score>=P:
    print("PASS")
else:
    print("FAIL")
    
