import pandas as pd
from io import StringIO, BytesIO


def misr_fixes(file):
    file.seek(0)
    dfBM = pd.read_csv(file, header=None, dtype=str)

    total_rows = dfBM.shape[0]
    for idx in range(total_rows - 1):
        field_BM = dfBM.iloc[idx, 13]
        field_BM_mode = dfBM.iloc[idx,3]
        if isinstance(field_BM, str):
            dfBM.iloc[idx, 13] = field_BM[:8] + 'XXX                              0' + field_BM[8:]
            dfBM.iloc[idx,4] = 3

    output = StringIO()  
    dfBM.to_csv(output, index=False, header=False)

    output.seek(0)
    output_str = output.getvalue()

    return output_str