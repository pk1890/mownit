from matplotlib import pyplot as plt

f = open("error3", "r")

contents = f.readlines()

xs = []
ys = []
i = 0
dataEnd = False
for line in contents:
    if line[0] =="#":
        dataEnd = True
    if(not dataEnd):
        xs.append(i*25000)
        ys.append(float(line.split()[2]))
        i+=1
    else:
        print(line)    

print("Bezwzględny: ", ys[-1], "Względny: ", ys[-1]/(1e7*0.5))
plt.plot(xs, ys)
plt.show()