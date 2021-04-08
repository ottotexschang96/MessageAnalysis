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
print(data[0])

# Reading order: data, words, wc
wc = {} # word_count
# Nested for loop 
for d in data: # d is a string; data is a list
	words = d.split(' ') # it splits d into several pieces of strings
	# print(words)
	# break
	for word in words:
		if word in wc: # if word not in wc: 
			wc[word] += 1 
		else:
			wc[word] = 1 #add new key & value
for word in wc:
	if wc[word] >1000000:
		print(word, wc[word])
print(len(wc))
print(wc['Allen'])

while True:
	word = input('Please type the keyword you want to search:')
	if word == 'q':
		break
	if word in wc:
		print('The repeating times of', word, ':', wc[word])
	else:
		print('There is no such word')
print('Thank you for your searching')
	

# sum_len = 0
# for d in data:
# 	sum_len += len(d)
# print('Average length in a message reply is:', sum_len / len(data))

# # print(data[0])
# # print('-----------------------------')
# # print(data[1])

# new = []
# for d in data:
# 	if len(d) < 100: 
#  		new.append(d)
# print('There are', len(new),'messages that the length is less than 100') # the length calculates how many characters
# print(new[0])
# print(new[1])

# good = [] #*
# for d in data: # use for loop to take out d from data *
# 	if 'good' in d: #*
# 		good.append(d) #*
# print('Therea are', len(good), 'messages which mention good')
# print(good[0])
# # 'a' in 'abc' -> True
# # '1' in 'abc' -> False

# # List comprehension (to compress the writings in the upper section into one line) *
# good = [d for d in data if 'good' in d] # 1 means good.append(d)
# print(good)

# bad = ['bad' in d for d in data] # 'bad' in d will result in true or false
# print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)