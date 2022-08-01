def maxProfit(arr):
    new_arr=[]
    count_plus=0
    count_minous=0
    index_last_plus=0
    #print(arr)
    for a in range(len(arr)-1):
        new_arr.append(arr[a+1]-arr[a])
    for a in range(len(new_arr)):
        if new_arr[a] > 0:
            index_last_plus = a
            #print(f"last plus index={index_last_plus}")
    for a in range(len(new_arr)):
        if a>index_last_plus:
            break
        if a==0 and new_arr[a]<0:
            continue
        else:
            if new_arr[a]<0:
                count_minous+=new_arr[a]
            else:
                count_plus+=new_arr[a]
    return count_plus#count_plus+count_minous
if __name__ == '__main__':
    num=maxProfit([1,2,3])
    print (num)
    num = maxProfit([5,2,10])
    print(num)
    num = maxProfit([1, 2, 1,2])
    print(num)
    num = maxProfit([7,2,4,8,7])
    print(num)