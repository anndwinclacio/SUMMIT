#---------- LSA MODULE ----------#

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# LIBRARIES NEEDED
import math 
import numpy    # for matrix creation and svd
import nltk     # for preprocessing

# PREPROCESSING 
from nltk.tokenize import word_tokenize, sent_tokenize     
from nltk.corpus import stopwords 
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters  

# LSA PROCESS
from numpy.linalg import eigh, norm
from lsapkg.utils import ItemsCount

from operator import attrgetter
from collections import namedtuple

# TUPLE OF THE SENTENCES
SentenceInfo = namedtuple("SentenceInfo", ("sentence", "order", "rating", ))

class LSA_Summarizer():
    
    MIN_DIMENSIONS = 3
    REDUCTION_RATIO = 1/1

    # ESTABLISHING THE LIST OF THE STOP WORDS
    _stop_words = list(stopwords.words('english')) # subject to change --- find better list of stop words


    ##### LSA ALGORITHM #####
    def __call__(self, paragraphs, sentences_count):

        ##### PREPROCESSING #####

        print("\n\n---DOCUMENT----\n")  
        document = self._text_document_converter(paragraphs)
        print(document)

        ##### TO SHOW THE PROCESS - SENTENCE SPLITTING #####
        sentences = self._sentence_splitter(paragraphs)
        print("\n\n---SENTENCE SPLITTING----\n")
        print(sentences)

        ##### TO SHOW THE PROCESS - TOKENIZATION #####
        words = self._words_tokenize(sentences)         # tokenization
        print("\n\n----TOKENIZATION----\n")
        print(words)

        dictionary = self._create_dictionary(words)

        ##### TO SHOW THE PROCESS - STOP WORDS REMOVAL #####
        print("\n\n----DICTIONARY OF UNIQUE WORDS----\n\n")
        print(dictionary)

        matrix = self._create_matrix(document, dictionary, sentences)      # creation of matrix

        ##### TO SHOW THE PROCESS - CREATION OF MATRIX #####
        print("\n\n----CREATION OF MATRIX----\n\n")
        print(matrix)

        matrix = self._compute_term_frequency(matrix)                      # computation of term frequency

        ##### TO SHOW THE PROCESS - TERM FREQUENCY #####
        print("\n\n----COMPUTATION OF TERM FREQUENCY----\n\n")
        print(matrix)

        u, sigma, v = self._singular_value_decomposition(matrix)

        ##### TO SHOW THE PROCESS - SVD #####
        print("\n----SVD----\n")
        print("\n\n----MATRIX: U----\n\n")
        print(u)
        print("\n\n----MATRIX: SIGMA----\n\n")
        print(sigma)
        print("\n\n----MATRIX: V----\n\n")
        print(v)

        ranks = iter(self._compute_ranks(sigma, v))
       
        return self._get_best_sentences(sentences, sentences_count, lambda s: next(ranks)) 

    # CREATION OF DICTIONARY
    def _create_dictionary(self, words):

        words = tuple(words)

        words = map(self.normalize_word, words) # converting words into its lowercase
        
        unique_words = frozenset(word for word in words if word not in self._stop_words)

        return dict((w,i) for i, w in enumerate(unique_words))      # the dictionary will look like this {'word': 'i'}
        

    # CREATION OF MATRIX
    # cells contains number of occurence of words (rows) in sentences (columns)
    def _create_matrix(self, document, dictionary, sentences):
       
        words_count = len(dictionary)
        sentences_count = len(sentences)

        matrix = numpy.zeros((words_count, sentences_count)) # make an array that is filled with zeros
        for col, sentence in enumerate(sentences):
            words = word_tokenize(sentence)
            for word in words:
                # All valid words not including the stop words
                if word in dictionary:
                    row = dictionary[word] 
                    matrix[row, col] += 1 

        return matrix
    
    # COMPUTING TERM-FREQUENCY MATRIX
    # compute the TF metrics for each column (sentence) of the given matrix
    def _compute_term_frequency(self, matrix, smooth=0.4):

        assert 0.0 <= smooth <1.0

        max_words_frequencies = numpy.max(matrix, axis=0)
        rows, cols = matrix.shape
        for row in range(rows):
            for col in range(cols):
                max_word_frequency = max_words_frequencies[col]
                if max_word_frequency != 0:
                    frequency = matrix[row, col]/max_word_frequency
                    matrix[row, col] = smooth + (1.0 - smooth) * frequency

        return matrix

    # SINGULAR VALUE DECOMPOSITION
    def _singular_value_decomposition(self, matrix):

        # COMPUTING FOR THE SIGMA AND V-MATRIX
        sigma, v = eigh(matrix.T@matrix)   
        
        # COMPUTING FOR U-MATRIX
        row, col = matrix.shape
        list = []
        # i = col
  
        for i in range(col):
            element = matrix@v[:,i]/norm(matrix@v[:,i])
            list.append(element)

        u = numpy.array(list).T
    
        return u, sigma, v
        
    # COMPUTING RANKS
    def _compute_ranks(self, sigma, v_matrix):
        assert len(sigma) == v_matrix.shape[0]

        dimensions = max(LSA_Summarizer.MIN_DIMENSIONS, int(len(sigma)*LSA_Summarizer.REDUCTION_RATIO))
        powered_sigma = tuple(pow(s,2) if i < dimensions else 0.0 
                        for i,s in enumerate(sigma))

        ranks = []

        for column_vector in v_matrix.T:
            rank = sum(s * pow(v,2) for s, v in zip(powered_sigma, column_vector))
            ranks.append(math.sqrt(rank))

        ##### TO SHOW THE PROCESS - SVD #####
        print("\n\n----SCORES OF THE SENTENCES----\n\n")
        print(ranks)

        return ranks

    
    ##### OTHER NECESSARY FUNCTIONS #####
    
    # Converting the word into its lowercase
    @staticmethod
    def normalize_word(word):
        return word.lower() 

    # Getting the best sentences
    @staticmethod
    def _get_best_sentences(sentences, count, rating, *args, **kwargs):
        rate = rating

        if isinstance(rating, dict):
            assert not args and not kwargs
            rate = lambda s: rating[s]   
        
        info = (SentenceInfo(s, o, rate(s, *args, **kwargs))
            for o, s in enumerate(sentences)) 
        
        # Sorting sentence by rating in Descending Order
        info = sorted(info, key=attrgetter("rating"), reverse=True)

        # Get 'count' first best rated sentences
        if not isinstance(count, ItemsCount):
            count = ItemsCount(count)
        info = count(info)

        # Sorting sentence by their order in document
        info = sorted(info, key=attrgetter("order"))

        ##### TO SHOW THE PROCESS - SVD #####
        print("\n\n----LIST OF BEST SENTENCES----\n\n")
        print(info)

        return tuple(i.sentence for i in info)

    # ARRAY TO STRING
    def _text_document_converter(self, sentences):
        str = " "
        return(str.join(sentences))

    # SENTENCE SPLITTER - MODIFIED
    def _sentence_splitter(self, paragraphs):
        
        list_abbrev_law = ['ca-g.r', 'ca-gr', 'g.r', 'cr-h.c', 'no', 'nos', 'r.a', 'col', 'u.s', 'a.m', 'p.m', 'st', 'brgy', 'inc', 'a.k.a', 'atty', 'dr', 'mr', 'ms', 'mrs.', 'insp', 'asst', 'pros', 'nos', 'sec', 'r.t']

        punkt_param = PunktParameters()
        punkt_param.abbrev_types = set(list_abbrev_law)
        sentence_splitter = PunktSentenceTokenizer(punkt_param)

        sentences = []

        for paragraph in paragraphs:
            temp_sentences = sentence_splitter.tokenize(paragraph)
            for sentence in temp_sentences:
                sentences.append(sentence)

        return sentences
    
    # WORDS TOKENIZE - MODIFIED
    def _words_tokenize(self, sentences):
        
        words = []

        for sentence in sentences:
            temp_words = word_tokenize(sentence)
            for word in temp_words:
                words.append(word)

        return words