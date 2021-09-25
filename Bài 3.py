n = int(input("Nhập số cần tính giai thừa: "))
def giaiThua(n):
    if(n<=0):
        print("bạn đã nhập sai, xin hãy kiểm tra lại")
    else:
        if n == 0:
            return 1
        return n * giaiThua(n - 1)
print(giaiThua(n))