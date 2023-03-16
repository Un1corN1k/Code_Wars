with open("data.txt", "r") as f:
    a,b,c =  list(map(int,f.read().split()))
print(a)