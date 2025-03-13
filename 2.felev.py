print("Adj meg egy hálózati címet és a hozzátartozó maszkot!")

ip = input("Add meg az IP címet: ")
mask = input("Add meg az alhálózati maszkot: ")

print("A hálózati cím:", '.'.join(str(int(a) & int(b)) for a, b in zip(ip.split('.'), mask.split('.'))))
