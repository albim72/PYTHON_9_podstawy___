#funckja wyższego rzędu
def message(msg):
    return f"pobrana informacja: {msg}"

def multiinfo(msg,wart,wsp):
    return f"{msg} -> {wart*wsp}"

def infoset(funkcja,*args):
    return funkcja(*args)

print(infoset(message,"tysiące liczb - 745847583745837458"))
print(infoset(multiinfo,"mnożenie dwóch wartości",56,7))

#funkcja dekorująca

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu....")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka!")

zawijanie("ciastek")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodzinowym torcie!")

dmuchanie("świeczek")
