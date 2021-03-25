from data import retrieve_data
import pandas as pd
import time

def create_frame(ticker_dictionary, annual=None, trailing=None):

    potential_annual = [
        'price_return', 'nav_return', 'benchmark_return', 'category_return', 'expense_ratio', 'turnover_ratio', 'category_rank'
    ]
    potential_trailing = [
        'price_return', 'nav_return', 'benchmark_return', 'category_return', 'category_rank'
    ]

    index = [ticker for ticker in ticker_dictionary]
    annual_columns = []
    trailing_columns = []
    subdata = {}
    if annual is not None:
        if annual == 'all':
            annual = potential_annual
            for label in potential_annual:
                for tag in ticker_dictionary[index[0]]['annual'][label]:
                    annual_columns.append('a' + '_' + label + '_' + tag)
        else:
            assert(type(annual) == list), 'Enter annual labels as a list.'
            for label in annual:
                assert (label in potential_annual), 'Invalid annual label provided: ' + label 
                for tag in ticker_dictionary[index[0]]['annual'][label]:
                    annual_columns.append('a' + '_' + label + '_' + tag)
        for ticker in ticker_dictionary:
            temp_data = []
            for label in ticker_dictionary[ticker]['annual']:
                if label in annual:
                    if len(ticker_dictionary[ticker]['annual'][label]) == 0:
                        for i in range(1, 12):
                            temp_data.append("None")
                    else: 
                        for tag in ticker_dictionary[ticker]['annual'][label]:
                            temp_data.append(ticker_dictionary[ticker]['annual'][label][tag])
            try:
                subdata[ticker] = subdata[ticker] + temp_data
            except:
                subdata[ticker] = temp_data

    if trailing is not None:
        if trailing == 'all':
            trailing = potential_trailing
            for label in potential_trailing:
                for tag in ticker_dictionary[index[0]]['trailing'][label]:
                    trailing_columns.append('t' + '_' + label + '_' + tag)
        else:
            assert(type(trailing) == list), 'Enter trailing labels as a list.'
            for label in trailing:
                assert (label in potential_trailing), 'Invalid trailing label provided: ' + label 
                for tag in ticker_dictionary[index[0]]['trailing'][label]:
                    trailing_columns.append('t' + '_' + label + '_' + tag)
        for ticker in ticker_dictionary:
            temp_data = []
            for label in ticker_dictionary[ticker]['trailing']:
                if label in trailing:
                    if len(ticker_dictionary[ticker]['trailing'][label]) == 0:
                        for i in range(1, 11):
                            temp_data.append("None")
                    else:
                        for tag in ticker_dictionary[ticker]['trailing'][label]:
                            temp_data.append(ticker_dictionary[ticker]['trailing'][label][tag])
            try:
                subdata[ticker] = subdata[ticker] + temp_data
            except:
                subdata[ticker] = temp_data
    
    data = [subdata[key] for key in subdata]
    dataframe = pd.DataFrame(
        data=data, index=index, columns=annual_columns+trailing_columns
    )
    return dataframe
    
def form_book(frame_dict):
    pass
        

data = retrieve_data(['spy', 'bnd', 'vfiax', 'qqq', 'dodwx'])
frame = create_frame(data, trailing = ['nav_return'])

# Next step: Forming an Excel book with multiple sheets based on groups.

frame.to_csv('book1.csv')