def hello():
    print("Hello, there!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_lst)):
            if i == 0:
                print(f"First I eat {my_lst[0]}")
            else:
                print(f"Next I eat {my_lst[i]}")

hello()
pack(2,5,7)
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])