import pickle
import pandas as pd

df_cc = pd.read_pickle('models/cc_df.pkl')
df_ccs = pd.read_pickle('models/ccs_df.pkl')
df_chianti = pd.read_pickle('models/chi_df.pkl')
df_pv = pd.read_pickle('models/pv_df.pkl')


def recommendations(input_string):
    if "Pai" in input_string:
        return df_pv.head(10)
    elif "hurch" in input_string:
        return  df_ccs.head(10)
    elif "hianti" in input_string:
        return df_chianti.head()
    elif "ontainer" in input_string:
        return df_cc.head(10)
