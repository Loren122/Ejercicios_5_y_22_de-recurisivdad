# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
def Rom_a_dec(r):
    r = r.upper()
    romanos = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if len(r) == 0:
        return 0
    
    elif len(r) == 1:
        return romanos[r]
    
    else:
        # IX=9 XI=11
        if romanos[r[0]] < romanos[r[1]]:
            return romanos[r[1]] - romanos[r[0]] + Rom_a_dec(r[2:])
        else:
            return romanos[r[0]] + Rom_a_dec(r[1:])
    
n_dec = Rom_a_dec('xxv')
print(n_dec)