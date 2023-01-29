# arr = [['a', 2, 100], # Job Array
# 		['b', 1, 19],
# 		['c', 2, 27],
# 		['d', 1, 25],
# 		['e', 3, 15]]
arr=[['a',4,20],
     ['b',1,10],
     ['c',1,40],
     ['d',1,30]]
arr.sort(key=lambda x:x[2])
c=1
print(arr)
for i in range (len(arr)-1, -1, -1):
    if arr[i][1]>=c:        
        print(arr[i][0])
        c=c+1
        arr.remove(arr[i])


        
        
    

