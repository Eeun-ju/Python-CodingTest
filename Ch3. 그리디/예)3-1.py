n = int(input("점원이 받은 금액"))

count_coin = 0

if n//500 !=0:
    count_coin +=n//500
    n = n%500
    print(count_coin)
    print()
    if n//100 !=0:
        count_coin +=n//100
        n = n%100
        print(count_coin)
        print()
        if n//10 !=0:
            count_coin +=n//10
            print(count_coin)
            print()
print(count_coin)
              
