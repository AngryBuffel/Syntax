import os
import re
import sys
import random
import datetime
import pandas as pd
import PySimpleGUI as sg

#----------Functions-Definition--------------------------------------------------------------------------
def choose_files():
    sg.theme('Reds')
    layout = [[sg.Input(key='_FILES_'), sg.FilesBrowse()], [sg.OK(), sg.Cancel()]]
    window = sg.Window('Choose Files...', layout)
    event, values = window.Read()
    file_names = values['_FILES_'].split(';')
    window.close()
    return file_names

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def clean_flatten(ugly_nested_list):
    c= 0
    for item in ugly_nested_list:
        pattern = r'\W'
        ugly_nested_list[c] = re.sub(pattern, '', item)
        c += 1
    return ugly_nested_list

def file_conv(file_name):
    ext = re.search(".csv$", file_name)
    ext2 = re.search(".xls$", file_name)
    xlfname = re.sub("csv$", "xlsx", file_name)
    if (ext):
        conv2xl = pd.read_csv(file_name, header=4)
        conv2xl.to_excel(xlfname)
        df = pd.read_excel(xlfname)
    elif (ext2):
        df = pd.read_excel(file_name,header=5)
    else:
        df = pd.read_excel(file_name)
    return df

def make_pivot2(label,df):
    ftype = re.search("Summary$", label)
    if ftype:
        pt = df[['Rule Code','Active']]
    else:
        pt = pd.pivot_table(df,index = 'Rule Code', columns ='WAV Status', fill_value=0, aggfunc = 'size')
        pt['Sum'] = pt.sum(axis=1)
        pt.loc['Grand Total'] = pt.sum()
    return pt

def save_file(ofn,df):
    cwdir = os.path.dirname(fname[0])
    out_name = os.path.join(cwdir,ofn+'.xlsx')
    df.to_excel(out_name)
    return None

#----------Main-Body--------------------------------------------------------------------------
fname = choose_files()
sheetnames = []

for source in fname:
    m = re.findall("[ \w-]+?(?=_20)", source)
    sheetnames.append(m)

clean_sheetnames = clean_flatten(flatten(sheetnames))
sg.popup('Reports', clean_sheetnames)

d = {clean_sheetnames[fname.index(source)]: file_conv(source) for source in fname}

p = {key: make_pivot2(key,value) for key, value in d.items()}

dict_df = pd.concat(p, axis=1, sort=True)
dict_df = dict_df.drop('Grand Total')
dict_df = dict_df.fillna(0)
dict_df.loc['Grand Total'] = dict_df.sum()
dict_df

d['pivot'] = dict_df

date = datetime.datetime.now()
with pd.ExcelWriter(os.path.join(os.path.dirname(fname[0]),date.strftime("%Y%m%d") + '_traffic_reports.xlsx')) as writer:
    for key, value in d.items():
        value.to_excel(writer, sheet_name=key)

        
sg.theme('Reds')
sg.popup('Files Merged!')
