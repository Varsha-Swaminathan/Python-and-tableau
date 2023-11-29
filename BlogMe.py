# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
data=pd.read_excel('../articles.xlsx')
data.describe()
data.info()
data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['engagement_reaction_count'].sum()
data=data.drop('engagement_comment_plugin_count', axis=1)

keyword='crash'

def keywordflag(keyword):
    length=len(data)
    keyword_flag=[]
    for x in range(0,length):
        heading=data['title'][x]
        try:
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

kf=keywordflag('murder')

data['keyword_flag']=pd.Series(kf)
# i=0
# for x in range(0,length):
#     heading=data['title'][x]
#     if 'murder' in heading:
#         i=i+1
#         print(i)
#     else:
#         i=i+1
#         print(i)

# len(data)

# data.loc[data['title'].isnull(),'value_is_NaN'] = 'Yes'
# data.loc[data['title'].notnull(), 'value_is_NaN'] = 'No'
# data.loc[data['value_is_NaN']=='Yes']['value_is_NaN'].count()
# data=data.drop('value_is_NaN', axis=1)

sent_int=SentimentIntensityAnalyzer()
text=data['title'][15]
sent=sent_int.polarity_scores(text)


title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]

length=len(data)


for x in range(0, length):
    try:
        text=data['title'][x]
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
title_neg_sentiment=pd.Series(title_neg_sentiment)
title_pos_sentiment=pd.Series(title_pos_sentiment)
title_neu_sentiment=pd.Series(title_neu_sentiment)

data['title_neg_sentiment']=title_neg_sentiment
data['title_pos_sentiment']=title_pos_sentiment
data['title_neu_sentiment']=title_neu_sentiment



data.to_excel('blog_clean.xlsx',sheet_name='blogmedata',index=False)














