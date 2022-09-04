import pandas as pd
import matplotlib.pyplot as plt


def exercise_0(transactions.csv):
    df = panda.read_csv('transactions.csv')
    pass

def exercise_1(df):
    list(df.columns.values)
    pass

def exercise_2(df, k):
    df1 = df.head(1)
    print(df1)
    pass

def exercise_3(df, k):
    df.sample(k)
    pass

def exercise_4(df):
    print(pd.unique(df['type']))
    pass

def exercise_5(df):
    df1 = df['nameDest'].value_counts().iloc[:10].rename_axis('Top 10 Dest').reset_index(name='count')
    print(df1)
    pass

def exercise_6(df):
    df.loc[df['isFraud'] == 1]
    pass

def exercise_7(df):
    pass

def visual_1(df):
    fig, ax = plt.subplots()
    df['type'].value_counts().plot(ax=ax, kind='bar')
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass
