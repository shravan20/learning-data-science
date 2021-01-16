
f = 0
print("1.", f)

def someFunc():
    # global f
    f="Inside Function"
    print("2.",f)
    print("3.", f)

someFunc()
print("4.",f)
del f
# print("5.",f) throws an error