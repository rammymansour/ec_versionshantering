from subprocess import Popen as Popen

#this feels better yes ?
def print(variabel):
        Popen(["echo", variabel])

for x in range(15):
	print("This is sparta")
