import matplotlib.pyplot as plt

x = [100, 1000, 10000, 50000, 100000]


def ssplit(l):
    length = len(l)
    return [l[p:p + 5] for p in range(0, length, 5)]


def generate_results():
	algs = ["insertion", "selection", "shell", "bubble"]
	res = []

	with open('data.txt') as file:
		for line in file:
			if line.strip() not in algs:
				res.append(line.split()[1])

	return res


data = ssplit([float(x) for x in generate_results()])
print(data)
plt.figure(1)

plt.subplot(221)
plt.plot(x, data[0], 'ro')
plt.title('Insertion Sort')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade Numeros')
plt.grid(True)

plt.subplot(222)
plt.plot(x, data[1], 'ro')
plt.title('Selection Sort')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade Numeros')
plt.grid(True)

plt.subplot(223)
plt.plot(x, data[2], 'ro')
plt.title('Shell Sort')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade Numeros')
plt.grid(True)

plt.subplot(224)
plt.plot(x, data[3], 'ro')
plt.title('Bubble Sort')
plt.ylabel('Tempo(s)')
plt.xlabel('Quantidade Numeros')
plt.grid(True)

plt.subplots_adjust(hspace=0.5)

plt.show()
