def average(*args):
    total = 0	#total = sum(args)
    for n in args:
        total += n
        
    print(f"매개변수로 전달된 값: {args}")
        
    return total / len(args)
    

print("평균: ", average(1, 2, 3, 4, 5))
print("-" * 40)
print("평균: ", average(30, 10, 20))