
import random


# Each word is mapped to a word and the frequency of that word
WORDS = {}

# Each group of letters is mapped to the most probable next letter
LETTERS = {}

INPUT_FILE = 'sci-fi-stories.txt'

class MarkovChain():
	def __init__(self, input_file, letter_depth, word_depth):
		self.input_file=input_file
		self.letter_depth=letter_depth
		self.word_depth=word_depth

	def traverse_stories(self):
		f = open(self.input_file, 'r')
		depth_letters = 'ra'
		#depth_words = f[0].split()[0:word_depth]
		for line in f:
			for character in line:
				if depth_letters in LETTERS:
					LETTERS[depth_letters].append(character)
				else: 
					LETTERS[depth_letters] = [character]

				depth_letters = depth_letters[1:] + character
		f.close()

	def traverse_stories_words(self):
		f = open(self.input_file, 'r')
		word = 'the'
		for line in f:
			for next_word in line.split():
				if word in WORDS:
					WORDS[word].append(next_word)
				else:
					WORDS[word] = [next_word]
			word = next_word

	def generate_story_letters(self):
		seed = 'ui'
		end_length = 1000
		count = 0
		out = ' '
		while count < end_length:
			if seed in LETTERS:
				index = int(random.random() * len(LETTERS[seed]))
				next_let = LETTERS[seed][index]
			else:
				next_let = chr(int(random.random() * 26) + 97)
				print 'random'
			seed = seed[1:] + next_let
			out += next_let
			count += 1
		print out

	def generate_story_words(self):
		seed = 'the'
		end_length = 100
		count = 0
		out = ' '
		while count < end_length:
			count += 1
			if seed in WORDS:
				index = int(random.random() * len(WORDS[seed]))
				next_word = WORDS[seed][index]
			else:
				next_word = 'the'

			seed = next_word
			out += next_word + ' '
		print out




if __name__ == '__main__':
	mc = MarkovChain(INPUT_FILE, 2, 1)
	mc.traverse_stories()
	#print LETTERS
	mc.generate_story_letters()
	print "+++++++++++"
	mc.traverse_stories_words()
	mc.generate_story_words()
					