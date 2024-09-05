def message(msg):
    return f"pobrana informacja: {msg}"

def multiinfo(msg,wart,wsp):
    return f"{msg} -> {wart*wsp}"

def infoset(funkcja,*args):
    return funkcja(*args)

print(infoset(message,"tysiące liczb - 745847583745837458"))
print(infoset(multiinfo,"mnożenie dwóch wartości",56,7))
