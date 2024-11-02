from dataclasses import field
import math
import pandas as pd
import os
def compare_1A_C2(file1A, fileC2):
    df1A = pd.read_csv(file1A)
    dfC2 = pd.read_csv(fileC2)
    field_1A = df1A.iloc[17,4]
    field_C2 = dfC2.iloc[17,4]
    if field_1A != field_C2:
        str_to_return = 'Sorry. your 1A 01010505 ' + str(field_1A) + ' is not equal to C2 0301 ' + str(field_C2)
    else:
        str_to_return = 'Congrats. your 1A 01010505 ' + str(field_1A)  +' is equal to C2 0301 ' + str(field_C2)
    return str_to_return

def compare_1A_1B(file1A,file1B):
    df1A = pd.read_csv(file1A)
    df1B = pd.read_csv(file1B)

    field_1A0100 = df1A.iloc[27, 4]
    field_1B0100 =  df1B.iloc[39, 4] - df1B.iloc[39, 5]
    field_1B0100 = field_1B0100.round(3)
    if field_1A0100 != field_1B0100:
        str_to_return = 'Sorry, your 1A 0100 ' +  str(field_1A0100) + ' is not equal to 1B 0100 ' +  str(field_1B0100)
    else:
        str_to_return = 'Congrats, your 1A 0100 ' + str(field_1A0100) + ' is equal to  1B 0100' + str(field_1B0100 )
    return str_to_return


def compare_1B_1B1(file1B,  file1B1):
    df1B = pd.read_csv(file1B)
    df1B1 = pd.read_csv(file1B1, header=None)

    field_1B010601 = df1B.iloc[21, 4] - df1B.iloc[21, 5]
    field_1B1 = df1B1.iloc[0,6]

    if field_1B010601 != field_1B1:
        str_to_return = 'Sorry your 1B ' + str(field_1B010601) + ' is not equal to field 1B1' + str(field_1B1)
    else:
        str_to_return = 'Congrats, your 1B 010601 ' + str(field_1B010601) +  '  is equal to field 1B ' + str(field_1B1)
    return str_to_return
# remember to do header = none
def compare_4B_5B(file4B,  file5B):
    df4B = pd.read_csv(file4B, header=None)
    df5B = pd.read_csv(file5B, header=None)
    field_4B = df4B.iloc[0,12]
    total_rows = df5B.shape[0]
    field_5B = 0
    for idx in range(total_rows):
        field_5B += sum(df5B.iloc[idx,6:])
    if field_4B !=  field_5B:
        str_to_return = 'Sorry your 4B ' + str(field_4B) + ' is not equal to field 5B ' + str(field_5B)
    else:
        str_to_return = 'Congrats, your field 4B ' + str(field_4B) +  ' is equal to field 5B ' + str(field_5B)
    return str_to_return

def compare_4A_5A(file4A, file5A):
    df4A = pd.read_csv(file4A, header=None)
    df5A = pd.read_csv(file5A, header=None)
    field_4A = df4A.iloc[0,10]
    total_rows = df5A.shape[0]
    field_5A = 0
    for idx in range(total_rows):
        field_5A += sum(df5A.iloc[idx,6:])
    if field_4A !=  field_5A:
        str_to_return = 'Sorry your 4A ' + str(field_4A) +  ' is not equal to field 5A ' + str(field_5A)
    else:
        str_to_return = 'Congrats, your field 4A ' + str(field_4A) + ' is equal to field 5A ' +  str(field_5A)
    return str_to_return

def compare_4B_7(file4B, file7):
    df4B = pd.read_csv(file4B,header=None)
    df7 = pd.read_csv(file7, header=None)
    print(df4B.iloc[:,8])
    total_remittances_4B = sum(df4B.iloc[:,5])
    total_remittances_7 = df7.iloc[0,6]
    #print(total_remittances_7)
    if total_remittances_4B != total_remittances_7:
        str_to_return = 'Sorry. Total remittances based on 4B ' +  str(total_remittances_4B) + ' is not equal to total in 7 ' +  str(total_remittances_7)
    else:
        str_to_return = 'Congrats. Total remittances based on 4B' +  str(total_remittances_4B) + ' is equal to  total in 7' + str(total_remittances_7)
    return str_to_return

def compare_6_7(file6, file7):
    df6 = pd.read_csv(file6, header=None)
    df7 = pd.read_csv(file7, header=None)
    remittances_nonkuwaiti = df6.iloc[:,4]
    sum_remittances_nonkuwaiti = sum(remittances_nonkuwaiti)
    remittances_kw_ind = df6.iloc[:,6]
    sum_remittances_kw_ind = sum(remittances_kw_ind)
    remittances_kw_corp = df6.iloc[:,8]
    sum_remittances_kw_corp = sum(remittances_kw_corp)
    total_remittances_6 = sum_remittances_nonkuwaiti + sum_remittances_kw_ind + sum_remittances_kw_corp
    total_remittances_7 = df7.iloc[0,4]
    amount_nonkuwaiti = df6.iloc[:,5]
    amount_kw_ind = df6.iloc[:,7]
    amount_kw_corp = df6.iloc[:,9]
    total_amount_6 = sum(amount_nonkuwaiti) + sum(amount_kw_ind) + sum(amount_kw_corp)
    #total_amount_7 =
    if total_remittances_6 != total_remittances_7:
        str_to_return = 'Sorry total remittances in 6 ' + str(total_remittances_6) + ' is not equal to total remittances in 7 ' + str(total_remittances_7)
    else:
        str_to_return = 'Congrats total remittances in 6 ' + str(total_remittances_6) + ' is equal to total remittances in 7 '+ str(total_remittances_7)
    return str_to_return

def compare_5A_5B_5C():
    df5A = pd.read_csv('CIECEXC5A.exc', header=None)
    df5B = pd.read_csv('CIECEXC5B.exc', header=None)
    df5C = pd.read_csv('CIECEXC5C.exc', header=None)
    field_5C = df5C.iloc[0,4]
    total_rows_5A = df5A.shape[0]
    total_rows_5B = df5B.shape[0]
    field_5A = 0
    field_5B = 0
    for idx1 in range(total_rows_5A):
        field_5A += sum(df5A.iloc[idx1, 6:])
    for idx2 in range(total_rows_5B):
        field_5B += sum(df5B.iloc[idx2,6:])
    if field_5A - field_5B != field_5C:
        str_to_return = 'Sorry. 5A ', field_5A, ' - 5B ', field_5B, ' is not equal to 5C ', field_5C
    else:
        str_to_return= 'Congrats. 5A ', field_5A, ' - 5B ', field_5B, ' is not equal to 5C ', field_5C
    return str_to_return

"""
    compare_1A_C2())
compare_1A_1B()
compare_1B_1B1()
compare_4B_7()
compare_4A_5A()
compare_4B_5B()
compare_6_7()
compare_5A_5B_5C()
###
"""