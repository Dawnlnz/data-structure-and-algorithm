import time

# 如果a+b+c=1000，且a^2 + b^2 = c^2，求满足条件的1000以内的a b c的组合

start_time = time.time()

# 使用枚举法
'''
for a in range(0,1000):
    for b in range(0,1000):
        for c in range(0,1000):
            if a+b+c==1000 and a**2 + b**2 == c**2:
                print("a,b,c: %d, %d, %d"%(a,b,c))
'''
# 改进
for a in range(0,1000):
    for b in range(0,1000):
        c = 1000 - a - b
        if  a**2 + b**2 == c**2:
            print("a,b,c: %d, %d, %d"%(a,b,c))
end_time = time.time()

print("time: %d"%(end_time - start_time))
print("finished!")