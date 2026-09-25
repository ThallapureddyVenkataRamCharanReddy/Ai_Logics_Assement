n=int(input())
a=list(map(int, input().split()))

m=int(input())
b=list(map(int, input().split()))

result=[]
carry=0

for i in range(max(n, m)):
    x=a[i] if i < n else 0
    y=b[i] if i < m else 0

    total=x + y + carry

    result.append(total % 10)
    carry=total // 10

if carry:
    result.append(carry)

print(*result)
# I tried solving this using th linked list, but I got some errors while creating and connecting the nodes.so,I used Python lists to solve the problem and understand the logic better.
