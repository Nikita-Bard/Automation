def bank (x, y):
    for a in range(1, y+1):
        count = x + (x/10)
        x = count
        
        print(round(count, 2))

bank (21000, 5)