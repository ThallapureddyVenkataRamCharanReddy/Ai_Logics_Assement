n=int(input())
slots=[list(map(int, input().split())) for _ in range(n)]
# print(slots)
slots.sort()
#i will sort based on start position
start,end=slots[0]
#forloop is starting from 1st index ,because we will iterate from 1st position
for s,e in slots[1:]:
    if s<=end:  #If the ranges overlap, merge them
        end=max(end, e)
    else:# If they don't overlap, print the previous range
        print(start, end)
      #update the start and end
        start,end=s,e
print(start,end)
#this is because , the  last range doesn't get printed inside the for loop
