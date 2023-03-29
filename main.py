#WRITE YOUR CODE IN THIS FILE // numL >= 1:
def hasL(w):
    numL = 0
    for i in range(0,len(w)):
        w[i] == "l"
        numL = numL + 1
        if w[i] == "l":
            return True
    else:
        return False
print(hasL("dog"))
print(hasL("alabama"))


