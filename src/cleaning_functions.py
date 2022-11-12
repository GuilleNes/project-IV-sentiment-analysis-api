import re


def drop_column(df_,columns):
    return df_.drop(columns, axis = 1, inplace= True)

def regex_column(df_, column):
    df_[column] = df_[column].str.replace('[^\w\s#@/:%.,_-]', '', regex=True, flags=re.UNICODE)
    return

def words_filter(df_,new_column, old_column, stopwords):
    df_[new_column] = df_[old_column].apply(lambda x: ' '.join([word for word in x.split() if word not in (stopwords)]))
    return

def sa (x, sia_):
    try:
        return sia_.polarity_scores(x)
    except:
        return x



