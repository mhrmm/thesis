# import wordnet
from nltk.corpus import wordnet as wn


class PuzzleGenerator():
      def __init__(self):
          self.puzzles = {}

      def get_words(self, n = 500):
          '''
             Method to get all the words from wordnet
             and return them as a list
          '''
          # used set to make sure the words are unique
          return list(set(list(wn.words())))[:n]
 
      def get_hyponyms(self, word):
          '''
             Method takes a given word and returns 
             the hyponyms of all the senses of that word.
          '''
          # create empty list to store hyponyms
          hyponyms = []
          # get the hyponym for each sense of the given word
          for sense in wn.synsets(word):
              # get the words instead of the senses
              words = [word.name() for word in sense.lemmas()]
              # add words to list of hyponyms
              hyponyms.extend(words)
          # return list of hyponyms
          return hyponyms

      def generate_hyponyms(self):
          '''
             Method gets a list of words from wordnet and
             returns a mapping of each word and its hyponyms
          '''
          # define dictionary to store mapping
          mapping = {}
          # get all teh words from wordnet
          words = self.get_words()
          # for each word get its hyponyms
          for word in words:
              mapping[word] = self.get_hyponyms(word)
          # return word : hyponyms pairs
          return mapping

      def filter_puzzles(self, mapping):
          '''
             Method takes a dictionary containing key value
             pairs of words and hyponyms and returns pairs
             that have 4 or more hyponyms.
          '''
          # define a dictionary to store pairs that satisfy our condition
          filtered_mapping = {}
          # iterate through our mapping to see if it satisfies the condition
          for key, value in mapping:
              if len(value) >= 4:
                 filtered_mapping[key] = value
          # return the filtered mapping
          return filtered_mapping

puzzle_generator = PuzzleGenerator()
puzzles = puzzle_generator.generate_hyponyms()
for puzzle in puzzles:
    print(puzzle)
    print(puzzles[puzzle])
    print()
