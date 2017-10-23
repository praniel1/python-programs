if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    for passnum in range(0,arr.length()-1):
        for i in range(passnum):
            if(arr[i]>arr[i+1]):
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp

    print arr[arr.length()-2]
