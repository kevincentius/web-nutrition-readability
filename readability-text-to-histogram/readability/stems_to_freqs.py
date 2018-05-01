import csv
import math

import nltk
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
import numpy as np
from readability.env import Environment


class StemsToFreqs(object):

    def __init__(self, remove_stopwords, debug = False):
        self.debug = debug
        self.remove_stopwords = remove_stopwords
        
        self.stem_frequencies = {}
        
        stemmer = nltk.stem.SnowballStemmer('english')
        stop_words = set(stopwords.words('english'))
        
        with open(Environment.gutenberg_path) as csv_file:
            reader = csv.reader(csv_file, delimiter='\t')
            for row in reader:
                word = row[1].lower()
                word_freq = float(row[2])
                stem = stemmer.stem(word)
                
                # remove stopwords
                if self.remove_stopwords and word in stop_words:
                    pass
                elif stem in self.stem_frequencies:
                    self.stem_frequencies[stem]['words'].append(word)
                    self.stem_frequencies[stem]['frequency'] += word_freq
                else:
                    self.stem_frequencies[stem] = {
                        'stem': stem,
                        'words': [word],
                        'frequency': float(word_freq)
                    }
        
        
        if self.debug:
            for key, value in self.stem_frequencies.items():
                if len(value['words']) > 1:
                    print(key, value['words'])
            
            for sw in stop_words:
                print(sw, sw in self.stem_frequencies)

                
    def stems_to_freqs(self, stems):
        freqs = []
        not_found = []
        for stem in stems:
            if stem in self.stem_frequencies:
                freqs.append(self.stem_frequencies[stem]['frequency'])
            else:
                # TODO: not found means difficult word! Do not ignore?
                not_found.append(stem)
        
        if self.debug:
            print('Unknown words', not_found)
        return freqs
    
    
    def freqs_to_histogram(self, freqs, num_bins):
        max_value = max(item[1]['frequency'] for item in self.stem_frequencies.items())
        
        # scale data using power 0.2 to better distribute the bin range in the histogram
        power = 0.15
        bins = np.arange(0, math.pow(max_value+1, power), math.pow(max_value, power)/num_bins)
        pow_freqs = np.power(freqs, power)
        
        # calculate the histogram
        return np.histogram(pow_freqs, bins)[0]
    
    
    def plot_linear_hist(self, frequencies, num_bins):
        max_value = max(item[1]['frequency'] for item in self.stem_frequencies.items()) + 1
        bins = np.arange(0, max_value+1, max_value/num_bins)
        plt.hist(frequencies, bins=bins)
        plt.show()
    
    def plot_log_hist(self, frequencies, num_bins):
        max_value = max(item[1]['frequency'] for item in self.stem_frequencies.items()) + 1
        bins = np.arange(0, math.log(max_value), math.log(max_value)/num_bins)
        log_freqs = np.log(frequencies)
        plt.hist(log_freqs, bins=bins)
        plt.show()
        
    def plot_pow_hist(self, frequencies, num_bins):
        max_value = max(item[1]['frequency'] for item in self.stem_frequencies.items()) + 1
        power = 0.2
        bins = np.arange(0, math.pow(max_value, power), math.pow(max_value, power)/num_bins)
        pow_freq = np.power(frequencies, power)
        plt.hist(pow_freq, bins=bins)
        plt.show()
                
    
if __name__ == '__main__':
    stf = StemsToFreqs()
    
    pass
