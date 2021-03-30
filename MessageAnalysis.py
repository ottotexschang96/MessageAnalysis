# There are 1 millons message replies in reviews.txt file

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

new = []
for d in data:
	if len(d) < 100: 
 		new.append(d)
print('There are', len(new),'messages that the length is less than 100') #the length calculates how many characters
print(new[0])
print(new[1])