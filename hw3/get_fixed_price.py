per = 0

def get_fixed_price(percent) : 
    global per
    per = percent


def A_price(A) : 
    return A / (100 - per) * 100

def B_price(B) :
    return B / (100 - per) * 100
