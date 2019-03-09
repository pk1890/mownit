
def epsilon(curr:float):
    if(1.0 + curr/2 != 1.0):
        return epsilon(curr/2)
    else: 
        return curr

print("Epsilon floata: ", epsilon(1.0))