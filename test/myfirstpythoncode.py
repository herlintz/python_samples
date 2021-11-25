#%%
#define a generator to calculate the two consecutive numbers in the series
def fib(count = 4):
    #series starts with 0 and 1
    a, b = 0 , 1
    #each following item is the the total of the previous two
    for i in range (count):
        a , b = b, (a+b)
        yield b

#%%
while True:
    try:
        count = int(input('How many items in the series?(Must be a positive integer less than 1000) : '))
        if 0 < count < 1000:
            break
        else:
            continue
    except:
        continue

fib_series = [0]

for i in fib(count):

    print(i)


# %%
