# set up word count
def get_themes(text, num_themes):
#filename = 'gen-women/i-will-bring-the-light-of-the-gospel-into-my-home.txt'
#text = ''
#with open(filename, 'r') as r:
#	reading_text = False
#	for line in r:
#		if reading_text:
#			text += line
#		if 'TEXT' in line:
#			reading_text = True

	import re

	words = re.compile('[A-Za-z]+').findall(text)

	word_count_ = {}
	for word in words:
		word = word.lower()
		if word in word_count_:
			word_count_[word] += 1
		else:
			word_count_[word] = 1


	# remove common words

	common_words = {'the','and','of','to','we','in','a','with','our','his','that','is','i','as','for','have','or','can','on','us','all','her','s','this','when','who','was','will','are','she','others','life','one','young','bring','into','be','own','he','wind','my','through','may','but'}

	for key in word_count_:
		if key in common_words:
			word_count_[key] = -1

	word_count = [(k, word_count_[k]) for k in sorted(word_count_, key=word_count_.get, reverse=True)]

	words = list(word_count)
	themes = []
	for i in range(num_themes):
		themes.append(words[i])

	return themes
	# save top x gospel words
#	with open(filename, 'a') as a:
#		a.write('\n\nTHEMES\n')
#		for i in range(5):
#			a.write(words[i][0] + '\n')
