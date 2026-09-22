name="sahil"
dol=23
print(f"My name is {name}and i have {dol:2f}")
print(f"MY name is {{name}}")
#doc string
def sq(n):
    '''Takes n no ,returns the sq of n'''
    print(n**2)
print(sq(9))
print(sq.__doc__)
import this