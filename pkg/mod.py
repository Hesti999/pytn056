name = "Andhika"
age = 25


def salam(*vals):
    if len(vals) == 0:
        print("salam kenal, saya", name)
    else:
        print("salam kenal, saya", vals)

salam()        
    
class Salam:
    pass

if (__name__ == '__main__'):
    print("jalan sebagai skrip")
    import sys
    if len(sys.argv) > 1:
        salam(sys.argv[1:])
    else:
        salam()