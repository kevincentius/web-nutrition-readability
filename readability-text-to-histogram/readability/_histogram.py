
from readability.stems_to_freqs import StemsToFreqs
from readability.text_to_stems import TextToStems
from readability.env import Environment
import os
import numpy as np

class HistogramGen:
    
    def generate_histogram(self,
            min_word_count = 25, # ignore texts that are shorter than this
            num_bins = 10,
            cat_ignore_list = ['poetry', 'read aloud poetry', 'drama']
    ):
        stemmer = TextToStems()
        counter = StemsToFreqs()
        
        np.set_printoptions(threshold=999999)
        data = np.reshape(np.array([]), [0, 2+num_bins])
        
        for grade in Environment.grades:
            grade_dir = Environment.data_set_path + grade[1]
            for category in os.listdir(grade_dir):
                if category not in cat_ignore_list:
                    cat_dir = grade_dir + '/' + category
                    for filename in os.listdir(cat_dir):
                        filepath = cat_dir + '/' + filename
                        # exiting with clause will close the file
                        # without 'with' clause, the file will only be closed upon garbage collection
                        with open(filepath, 'r', encoding="utf-8") as file:
                            text = file.read()
                            stems = stemmer.text_to_stems(text)
                            if (len(stems) >= min_word_count):
                                freqs = counter.stems_to_freqs(stems)
                                hist = counter.freqs_to_histogram(freqs, num_bins)
                                total = np.sum(hist)
                                data = np.vstack((data, np.append([grade[0], total], hist/total)))
                    
                    #counter.plot_pow_hist(freqs, num_bins)
        
        np.savetxt('word_freq_histogram_10', data)
        print(len(data), 'data processed')
        print(data)

if __name__ == '__main__':
    HistogramGen().generate_histogram()
    
    
