a = int(input("請輸入一個五位數:"))
digits = [int(digit) for digit in str(a)]
print("結果:")
for digit in digits:
    print(digit)
