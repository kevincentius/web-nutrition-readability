'''
Created on Apr 30, 2018

@author: Eldemin
'''

class Environment(object):
    # set this `data_path` to where you put will put the data files in
    data_path = 'D:/master project/data/'
    
    # set this `core_standards_path` to where you extracted the core-standards-readability.zip
    # This zip file is available on our google drive:
    #    https://drive.google.com/open?id=1rR7egog3eNK5Tb3CwRBGJhMdUMkDkSD7
    data_set_path = data_path + 'core-standards-readability/'
    
    # data set label and folder names
    # this is dependent on the data set directory structure (folder names)
    grades = [
        [1, 'grade 1'],
        [2.5, 'grade 2-3'],
        [4.5, 'grade 4-5'],
        [7, 'grade 6-8'],
        [9.5, 'grade 9-10'],
        [12, 'grade 11-CCR']
    ]
    
    # set this `gutenberg_path` to where you have the wiktionary-2006-04-16-word-frequency.txt file
    # This file is available on our google drive:
    #   https://drive.google.com/open?id=1eaCkGNjdYQvwgrnTviJCdPvYVLoeOVL0
    gutenberg_path = data_path + 'wiktionary-2006-04-16-word-frequency.txt'
    
    # where the histogram should be saved
    histogram_path = 'D:/master project/eval/core-standards-histogram/histograms.csv';
    
        