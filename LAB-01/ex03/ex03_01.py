def tinh_tong_so_chan(lst):
    tong=0
    for num in lst:
        if num % 2 ==0 :
            tong+= num 
    return tong
input_list = input("nhap danh sach cac so , cach nhau ban dau phay: ")
numbers= list(map(int,input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("tong cac so chan trong list la ",tong_chan)
