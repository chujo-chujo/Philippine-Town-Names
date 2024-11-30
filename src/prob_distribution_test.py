import matplotlib.pyplot as plt
import pprint

option_A = 5*[60] + 19*[25] + 330*[6] + 431*[3] + 556*[1]
option_B = 5*[100] + 19*[20] + 330*[5] + 431*[2] + 556*[1]
option_C = 5*[200] + 19*[25] + 330*[5] + 431*[2] + 556*[1]
option_D = 5*[250] + 19*[30] + 330*[5] + 431*[2] + 556*[1]
option_E = 5*[127] + 19*[15] + 330*[3] + 431*[2] + 556*[1]

options = [option_A, option_B, option_C, option_D, option_E]

data = []
for option in options:
	b = list()
	count = set()
	for item in option:
		if item not in count:
			b.append(round(item/sum(option) * 100, 4))    
			count.add(item)
	data.append(b)

pprint.pprint(data)

labels = ['A', 'B', 'C', 'D', 'E']
x_ticks_labels = ['>=1,500,000', '>500,000', '>70,000', '>35,000', '<=35,000']
for i, prob in enumerate(data):
    plt.plot(prob, marker='o', label=labels[i])

plt.xticks(ticks=range(len(x_ticks_labels)), labels=x_ticks_labels)
plt.xlabel('Population')
plt.ylabel('Probability [%]')
plt.title('Comparison of prob. distributions')
plt.legend()
plt.grid(True)

plt.show()