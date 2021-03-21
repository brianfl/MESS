from data import retrieve_data
import pandas as pd
import time

def create_frame(ticker_dictionary, annual=None, trailing=None):

    potential_annual = [
        'price_return', 'nav_return', 'benchmark_return', 'category_return', 'expense_ratio', 'turnover ratio', 'category_rank'
    ]
    potential_trailing = [
        'price_return', 'nav_return', 'benchmark_return', 'category_return', 'category_rank'
    ]

    index = [ticker for ticker in ticker_dictionary]
    annual_columns = []
    trailing_columns = []
    if type(annual) != None:
        if annual == 'all':
            for label in potential_annual:
                annual_columns.append('a_' + label)
        else:
            assert (type(annual) == list), 'Enter annual labels as a list.'
            for label in annual:
                assert (label in potential_annual), 'Invalid annual label provided: ' + label 
                annual_columns.append(label)
    
    if type(trailing) != None:
        if trailing == 'all':
            for label in potential_trailing:
                trailing_columns.append('t_' + label)
        else:
            assert(type(trailing) == list), 'Enter trailing labels as a list.'
            for label in trailing:
                assert (label in potential_trailing), 'Invalid trailing label provided: ' + label 
                trailing_columns.append(label)

    data = []
    for ticker in ticker_dictionary:
        subdata = []
        for label in ticker_dictionary['annual']:
            if label in annual:
                for tag in ticker_dictionary['annual'][label]:
                    subdata.append()
    
    print(annual_columns)

    for i in j in i in j for i in 
        

data = retrieve_data(['spy', 'bnd', 'vfiax'])
create_frame(data, ['price_return', 'nav_return'])