#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:32:03 2017

@author: quinlan.alexander@gmail.com
"""

import pandas as pd
import numpy as np
import urllib
import os.path

url = 'https://tcga.xenahubs.net/download/TCGA.BRCA.sampleMap/mutation_curated_wustl'
dataFile = "brcaData.tsv"

if not os.path.isfile(dataFile):
    print("downloading with urllib")
    urllib.urlretrieve(url, dataFile)
    
brca = pd.read_table(dataFile)

print 'brca data frame contains {} rows.'.format(brca['sample'].count())

