def decor_for_add(func):
    def inner(a,b):
        print("#"*30)
        print("TheSum:",end="")
        func(a,b)
        print("#"*30)
    return inner

@decor_for_add
def add(a,b):
    print(a+b)

add(20,0)


#Withou decarator


def decor(func):
    def inner(name):
        if name=="Tarun":
            print("#"*30)
            print("Hello Tarun, you are very important for us..!!")
            print("Very Very Good Morning..!!")
            print("#"*30)
        else:
            func(name)
    return inner
def wish(name):
    print("Good Morning:",name)
decorated_wish=decor(wish)
decorated_wish("Tarun")

#calling inner and outer.

def outer(a,b):
    def inner():
        val=a+b
        return val
    return inner()

def outer1(a,b):
    def inner(a,b):
        val=a+b
        return val
    return inner(a,b)

su1=outer(5,6)
su2=outer1(5,3)
print(su1,su2)