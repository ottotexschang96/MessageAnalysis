data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f: 
		data.append(line)
		count += 1
		if count % 1000 == 0: #print out the the length whenever it reached a thousand
			print(len(data))
print('Reading complete, there are', len(data), 'data points')

sum_len = 0
for d in data:
	sum_len += len(d)
print('Average length in a message reply is:', sum_len / len(data))

# print(data[0])
# print('-----------------------------')
# print(data[1])