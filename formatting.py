from data import retrieve_data
import pandas as pd
import time

def create_frame(ticker_dictionary, annual=None, trailing=None):
    if annual == 'all':

    elif annual == None:
    
    else:

    index = [ticker for ticker in ticker_dictionary]
    columns = []
    for index1, ticker in enumerate(ticker_dictionary):
        if index1 == 0: # need to set up the columns
            for form in ticker_dictionary[ticker]:
                for label in ticker_dictionary[ticker][form]:
                    for tag in ticker_dictionary[ticker][form][label]:
                        columns.append(label + '_' + tag)
    print(columns)
        

data = retrieve_data(['spy', 'bnd', 'vfiax'])
create_frame(data)