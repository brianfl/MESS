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
    with pd.ExcelWriter('MESS' + str(int(time.time())) + '.xlsx') as writer:
        for key in frame_dict:
            frame_dict[key].to_excel(writer, sheet_name=key)
    print("Excel book created called MESS" + str(int(time.time())))
        

loan_list = [
    'ffrhx', 'oosyx', 'eiblx', 'rpifx', 'sambx', 'gsfrx', 'bfrix', 'lfrfx',
    'cshix', 'jfidx', 'bkln', 'ftsl', 'snln', 'flrt', 'evftc'
]
loan_data = retrieve_data(loan_list)
loan_frame = create_frame(loan_data, trailing = ['nav_return', 'category_rank'],
annual=['expense_ratio'])

em_list = [
    'dfcex','odvyx','newfx','lzemx','vemax','prmsx','abemx','femsx','hiemx','vwo'
]
em_data = retrieve_data(em_list)
em_frame = create_frame(em_data, trailing = ['nav_return', 'category_rank'],
annual=['expense_ratio'])

es_list = [
    'veusx','hfeix','presx','meurx','fieux','bafhx','aedyx','vesix','jfeix','idjik','vgk'
]
es_data = retrieve_data(es_list)
es_frame = create_frame(es_data, trailing = ['nav_return', 'category_rank'],
annual=['expense_ratio'])

form_book(
    {'Bank Loan': loan_frame,
    'Emerging Markets': em_frame,
    'Europe Stock': es_frame}
)

# Idea: A specific failure condition for 404 errors. Can skip retries entirely.
# How to stop double posting of completed status on failures?
# RPIFX giving incorrect data? Investigate.