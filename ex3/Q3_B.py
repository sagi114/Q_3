def maxProfit(arr):
    count_max=0
    flag = 1
    for a in range(len(arr)):
        for b in range(len(arr)):
            if b <= a:
                continue
            else:
                num = arr[b]-arr[a]
                if flag == 1:
                    count_max = num
                    flag =0
                elif num>count_max:
                    count_max = num
    return count_max


if __name__ == '__main__':
    num=maxProfit([1,2,3])
    print(num)
    num = maxProfit([5,2,10])
    print(num)
    num = maxProfit([1, 2, 1,2])
    print(num)
    num = maxProfit([7,2,4,8,7])
    print(num)