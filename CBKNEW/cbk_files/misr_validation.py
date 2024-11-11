import pandas as pd
from io import StringIO, BytesIO


def misr_fixes(file):
    file.seek(0)
    dfBM = pd.read_csv(file, header=None, dtype=str)
    BM_codes = {    'AINB': '0003',
    'ARAI': '0010',
    'ARLB': '0001',
    'EBIL': '0001',
    'EGGB': '0098',
    'ETHN': '0595',
    'EXDE': '0014',
    'FIEG': '0001',
    'HDBK': '0001',
    'MSHQ': '0001',
    'NBEG': '0001',
    'QNBA': '0021',
    'SBNK': '0001',
    'SUCA': '0013',
    'UBOE': '0001',
    'ALEX': '2099',
    'AGRI': '0001',
    'CIBE': '0085',
    'CITI': '0000',
    'EAAB': '0001',
    'EBBK': '0001',
    'DIBB': '0002',
    'MIDB': '0001',
    'NBAD': '0221',
    'ABRK': '0102',
    'ECBA': '0010',
    'BDAC': '0101',
    'ADCB': '0099',
    'ABDI': '0750',
    'ARAB': '5000',
    'DEIB': '0099',
    'WABA': '0001',
    'BCBI': '0034',
    'BCAI': '0001'}
    total_rows = dfBM.shape[0]
    for idx in range(total_rows - 1):
        field_BM = dfBM.iloc[idx, 13]
        field_BM_mode = dfBM.iloc[idx,3]
        if isinstance(field_BM, str):
            branch_code = BM_codes[field_BM[:4]]
            dfBM.iloc[idx, 13] = field_BM[:8] + 'XXX                              ' + branch_code
            dfBM.iloc[idx,4] = 3

    output = StringIO()  
    dfBM.to_csv(output, index=False, header=False)

    output.seek(0)
    output_str = output.getvalue()

    return output_str
