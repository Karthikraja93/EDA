#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import seaborn as sns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# In[5]:


df_metadata = pd.read_csv('./metadata_category_clothing_shoes_and_jewelry_only.csv')


# In[6]:


df_metadata.shape


# In[7]:


df = pd.read_csv('./reviews_Clothing_Shoes_and_Jewelry_5.csv')


# In[235]:


df.shape


# In[9]:


df_merged = pd.merge(df, df_metadata, on='asin')


# In[10]:


df_merged.shape


# In[18]:


df_merged.head(5)


# In[70]:


df_merged.info()


# In[76]:


df_merged.nunique()


# In[ ]:


df_merged['salesrank'] = df_merged['salesrank'].fillna('')


# In[66]:


df_merged['category_derived'] = df_merged['salesrank'].apply(lambda x: x.partition(':')[0]) 
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace('"', ''))
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace('{', ''))
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace("'", ''))
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace("}", ''))


# In[85]:


df_merged['category_derived'].value_counts()


# ##### Clothing 50% Shoes 25% Jewelry 10% Others 14%    
# (Chart - https://docs.google.com/spreadsheets/d/1nZReNM1AGumiB4DOTW5sKBuJ8zSA60EtEcO0-tzKdLY/edit#gid=775562)

# In[29]:


df_merged['overall'].value_counts()


# #### 60% of ratings consist of 5 stars, 20% of ratings consist of 4 stars, 10% of ratings consist of 3 stars, 5% of ratings consist of 2 stars, 5% of ratings consist of 1 star

# ## Helpfulness

# In[11]:


df_merged['positive_helpful'] = df_merged['helpful'].apply(lambda x: x[1:2]) 
df_merged['negative_helpful'] = df_merged['helpful'].apply(lambda x: x[4:5])
df_merged['positive_helpful'] = df_merged['positive_helpful'].astype(int)
df_merged['negative_helpful'] = df_merged['negative_helpful'].apply(lambda x: x.replace(' ', '0')) 
df_merged['negative_helpful'] = df_merged['negative_helpful'].apply(lambda x: x.replace(',', '0')) 
df_merged['negative_helpful'] = df_merged['negative_helpful'].astype(int)
df_merged['total_helpful'] = df_merged['negative_helpful'] + df_merged['positive_helpful']
df_merged['positive_helpful_ratio'] = (df_merged['positive_helpful']/df_merged['total_helpful']).fillna(0)
df_merged['len_reviewText'] = df_merged['reviewText'].str.len()


# In[621]:


len(df_merged[df_merged['total_helpful']==0])


# In[622]:


len(df_merged[df_merged['total_helpful']!=0])


# In[626]:


sum(df_merged[df_merged['total_helpful']!=0]['negative_helpful'])


# In[624]:


sum(df_merged[df_merged['total_helpful']!=0]['positive_helpful'])


# In[627]:


sum(df_merged[df_merged['total_helpful']!=0]['total_helpful'])


# #### ~70% didnt have helpfulness voting

# In[478]:


df_merged[df_merged['total_helpful']!=0].groupby('overall').agg({'positive_helpful_ratio':'mean'})


# ####  The higher the ratings . The higher are the upvotes for helpfulness

# In[ ]:


df_merged_c['len_summary'] = df_merged_c['summary'].str.len()
df_merged_c['len_summary_bins'] = pd.qcut(df_merged_c['len_summary'], 3, labels = list('LMH'))
df_merged_c['len_reviewText_bins'] = pd.qcut(df_merged_c['len_reviewText'], 3, labels = list('LMH'))


# #### Greater the length of review greater is the postive helpful ratio. No difference in postive helpful ratio even if the reviews are cleaned for punctuations etc
# chart - https://docs.google.com/spreadsheets/d/1nZReNM1AGumiB4DOTW5sKBuJ8zSA60EtEcO0-tzKdLY/edit#gid=775562

# In[479]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_reviewText_bins').agg({'positive_helpful_ratio':'mean'})


# #### longer reviews are helpful by 20% compared to shorter reviews

# In[480]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_summary_bins').agg({'positive_helpful_ratio':'mean'})


# In[175]:


df_merged_c['reviewText_cleaned'] = df_merged_c['reviewText'].str.replace(r'[^\w\s]+', '')
df_merged_c['reviewText_cleaned'] = df_merged_c['reviewText_cleaned'].fillna('')
df_merged_c['reviewText_cleaned'] = df_merged_c['reviewText_cleaned'].apply(lambda x: x.replace(' ', ''))

df_merged_c['summary_cleaned'] = df_merged_c['summary'].str.replace(r'[^\w\s]+', '')
df_merged_c['summary_cleaned'] = df_merged_c['summary_cleaned'].fillna('')
df_merged_c['summary_cleaned'] = df_merged_c['summary_cleaned'].apply(lambda x: x.replace(' ', ''))

df_merged_c['len_reviewText_cleaned'] = df_merged_c['reviewText_cleaned'].str.len()
df_merged_c['len_summary_cleaned'] = df_merged_c['summary_cleaned'].str.len()
df_merged_c['len_summary_cleaned_bins'] = pd.qcut(df_merged_c['len_summary_cleaned'], 3, labels = list('LMH'))
df_merged_c['len_reviewText_claned_bins'] = pd.qcut(df_merged_c['len_reviewText_cleaned'], 3, labels = list('LMH'))


# In[198]:


df_merged_c[["len_reviewText_cleaned", "len_summary_cleaned"]].describe()


# In[481]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_reviewText_claned_bins').agg({'positive_helpful_ratio':'mean'})


# In[482]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_summary_cleaned_bins').agg({'positive_helpful_ratio':'mean'})


# ## Category Wise Analysis

# In[109]:


df_merged_c = df_merged.copy()


# In[110]:


df_merged_c['category_derived'].loc[~df_merged_c['category_derived'].isin(['Clothing', 'Shoes','Jewelry'])]='Others'


# In[506]:


df_merged_c.groupby('category_derived').agg({'overall':'mean'})


# In[237]:


df_merged_c.groupby('category_derived').reviewerID.nunique()


# In[226]:


df_merged_c.groupby('category_derived').asin.nunique()


# In[238]:


df_merged_c.groupby('category_derived').reviewText.nunique()


# ####  Reviews per Product across Category :Clothing 12.97 , Shoes 11.58 ,  Jewelry 11.07 , Others 11.07
# chart - https://docs.google.com/spreadsheets/d/1nZReNM1AGumiB4DOTW5sKBuJ8zSA60EtEcO0-tzKdLY/edit#gid=775562

# In[113]:


with sns.axes_style('white'):
    g = sns.factorplot(x = "overall", hue = "category_derived" ,data=df_merged_c, aspect=2.0,kind='count')
    g.set_ylabels("Total number of ratings")


# In[483]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby(['category_derived','len_reviewText_claned_bins']).agg({'positive_helpful_ratio':'mean'})


# #### Similar pattern is observed for positive helpful ratio across categories compared to overall cleaned reviews bins

# In[484]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby(['category_derived','len_summary_cleaned_bins']).agg({'positive_helpful_ratio':'mean'})


# ## Pricing

# In[192]:


with sns.axes_style('white'):
    g = sns.factorplot(x = "len_summary_cleaned_bins", y = "price" ,data=df_merged_c, aspect=2.0,kind='bar')
    g.set_ylabels("Price")


# In[193]:


with sns.axes_style('white'):
    g = sns.factorplot(x = "len_reviewText_claned_bins", y = "price" ,data=df_merged_c, aspect=2.0,kind='bar')
    g.set_ylabels("Price")


# In[207]:


df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','len_summary_cleaned_bins']).agg({'price':'mean'})


# In[208]:


df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','len_reviewText_claned_bins']).agg({'price':'mean'})


# In[210]:


df_merged_c[df_merged_c.price.isnull()].groupby('category_derived').agg({'len_summary_cleaned':'mean'})


# In[212]:


df_merged_c[df_merged_c.price.isnull()].groupby('category_derived').agg({'len_reviewText_cleaned':'mean'})


# In[213]:


df_merged_c[df_merged_c.price.notnull()].groupby('category_derived').agg({'len_summary_cleaned':'mean'})


# In[243]:


df_merged_c['price_bins'] = pd.qcut(df_merged_c['price'], 3, labels = list('LMH'))


# In[257]:


df_merged_c['price_bins'].value_counts()


# In[267]:


df_merged_c[df_merged_c.price.notnull()].groupby('price_bins').reviewerID.nunique()


# In[804]:


df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','price_bins','pos_neg']).reviewText.nunique()


# In[803]:


df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','price_bins','pos_neg']).asin.nunique()


# In[277]:


#Price Variation by time


# In[290]:


df_merged_c.head(5)


# In[338]:


df_merged_c['salesrank_derived'] = df_merged_c['salesrank'].apply(lambda x: x.partition(':')[2])
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace('"', ''))
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace('{', ''))
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace("'", ''))
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace("}", ''))


# In[339]:


df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace(' ', ''))


# In[361]:


df_merged_c_1 = df_merged_c[df_merged_c['salesrank_derived']!='']


# In[362]:


df_merged_c_1['salesrank_derived'] = df_merged_c_1['salesrank_derived'].astype(int)


# In[372]:


df_merged_c[df_merged_c.price.notnull()].groupby('asin').price.nunique()


# In[374]:


df_merged_c.columns


# #### Price & Salesrank do not vary over time

# ## Reviewer Behaviour

# In[401]:



df_merged_c['date'] = pd.to_datetime(df['unixReviewTime'],unit='s')


# In[402]:


from datetime import date
from datetime import datetime, timedelta


# In[403]:


df_merged_c['date'] = df_merged_c['date'].apply(lambda x: x.date().strftime("%Y-%m-%d"))


# In[413]:


df_merged_c.head(5)


# In[418]:


df_merged_c['month'] = df_merged_c['date'].apply(lambda x: x[5:7])


# In[579]:


df_merged_c['year'] = df_merged_c['date'].apply(lambda x: x[0:4])


# In[637]:


df_merged_c['year'] = df_merged_c['year'].astype(int)


# In[638]:


df_merged_c[(df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)].groupby(['category_derived','month']).agg({'reviewText':'count'})


# In[633]:


df_merged_c['asin_reviewer'] = df_merged_c['asin'] + df_merged_c['reviewerID']


# In[498]:


df_merged_c['asin_reviewer'].nunique()


# #### Reviewer did not write more than one reviews for a product

# In[436]:


df_merged_c.groupby('reviewerID').len_reviewText_claned_bins.nunique()


# In[493]:


df_merged_c_2 = df_merged_c[['reviewerID','len_reviewText_claned_bins']]


# In[494]:


df_merged_c_3 = df_merged_c_2.groupby(['reviewerID','len_reviewText_claned_bins']).size().unstack()


# In[490]:


df_merged_c_4 = df_merged_c[df_merged_c['total_helpful']!=0][['reviewerID','len_reviewText_claned_bins']]


# In[491]:


df_merged_c_5 = df_merged_c_4.groupby(['reviewerID','len_reviewText_claned_bins']).size().unstack()


# In[448]:


df_merged_c.groupby('reviewerID').reviewText.nunique().sort_values(ascending=False)


# In[496]:


df_merged_c[df_merged_c['total_helpful']!=0].groupby('reviewerID').agg({'positive_helpful_ratio':'mean'})


# #### High frequent reviewers wrote 70% of reviews either Long or Medium size (Avg Helpfulness score - 0.466 excluding 0 helpfulness)
# 
# 

# #### Less frequent reviewers wrote 55% of reviews either Low size(Avg Helpfulness score - 0.429 excluding 0 helpfulness)
# 

# #### The above statements implies high frequent reviewers are more helpful by 10% compared to low frequent users

# ## Misc

# In[503]:


df_merged_c.groupby('overall').agg({'len_reviewText_cleaned':'mean'})


# ####  Higher ratings have less review length 

# In[515]:


df_merged_c.groupby('asin').agg({'reviewText_cleaned':'count'}).sort_values(by='reviewText_cleaned', ascending=False)


# In[516]:


df_merged_c.groupby('asin').agg({'reviewText_cleaned':'count'}).sort_values(by='reviewText_cleaned', ascending=False).head(20)


# In[522]:


df_asin_top = df_merged_c.loc[df_merged_c['asin'].isin(['B005LERHD8','B0aa05GYGD7O','B008WYDP1C','B0058XIMMM','B00CKGB85I','B007RD9DS8','B002RADHJC','B000T9VK56','B0000C321X','B0001ZNZJM','B007WNWEFC','B007WA3K4Y','B00012O12A','B007NLX16O','B0008EOEPK','B0007YR8WW','B0067GUM2W','B000O32MLI','B001IB70JY','B004Q7AB4I'])]


# In[554]:


df_merged_c['pos_neg'] = [1 if x > 3 else 0 for x in df_merged_c.overall]


# In[531]:


from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


# In[538]:


# !install_package_python3.sh wordcloud


# In[534]:


import nltk
nltk.download('stopwords')
stops = stopwords.words('english')


# In[535]:


def tokenize(text):
    tokenized = word_tokenize(text)
    no_punc = []
    for review in tokenized:
        line = "".join(char for char in review if char not in string.punctuation)
        no_punc.append(line)
    tokens = lemmatize(no_punc)
    return tokens


def lemmatize(tokens):
    lmtzr = WordNetLemmatizer()
    lemma = [lmtzr.lemmatize(t) for t in tokens]
    return lemma


# In[539]:


import wordcloud


# In[570]:


df_merged_c[df_merged_c['pos_neg']==1].review_nonum[1504]


# In[569]:


df_merged_c['review_nonum'] = df_merged_c['reviewText'].str.replace('\d+', '')
df_merged_c['review_nonum'] = df_merged_c['review_nonum'].str.replace(r'[^\w\s]+', '')
df_merged_c['review_nonum'] = df_merged_c['review_nonum'].fillna('')


# In[571]:


cloud_p = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[df_merged_c['pos_neg']==1].review_nonum))


# In[572]:


fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p);


# In[573]:


cloud_n = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[df_merged_c['pos_neg']==0].review_nonum))


# In[574]:


fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n);


# In[575]:


df_merged_c['pos_neg'].value_counts()


# In[576]:


df_merged_c.head(5)


# In[592]:


df_merged_c.groupby(['year']).agg({'reviewText':'count'})


# In[595]:


df_merged_c.groupby(['year']).reviewerID.nunique()


# #### Reviewers are wring more reviews across years

# #### Bigrams before removing stop words

# In[670]:


def get_top_n_bigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


# In[604]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


# In[762]:


df_merged_c['total_review'] = df_merged_c['reviewText'] + ' ' + df_merged_c['summary']


# In[765]:


df_merged_c['total_review_comwords'] = df_merged_c['total_review'].fillna('')


# In[ ]:


df_merged_c['total_review_nonum'] = df_merged_c['total_review_comwords'].str.replace('\d+', '')
df_merged_c['total_review_nonum'] = df_merged_c['total_review_nonum'].str.replace(r'[^\w\s]+', '')
df_merged_c['total_review_nonum'] = df_merged_c['total_review_nonum'].fillna('')


# In[ ]:


df_merged_c['reviewText_comwords'] = df_merged_c['reviewText'].fillna('')


# #### Across all the months

# In[766]:


common_words_good = get_top_n_bigram(df_merged_c[df_merged_c['pos_neg']==1]['total_review_comwords'], 30)


# In[767]:


common_words_bad = get_top_n_bigram(df_merged_c[df_merged_c['pos_neg']==0]['total_review_comwords'], 30)


# In[768]:


plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good]
y_good=[x[1] for x in common_words_good]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad]
y_bad=[x[1] for x in common_words_bad]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[663]:


def get_top_n_trigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(3, 3), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]


# In[769]:


common_words_good1 = get_top_n_trigram(df_merged_c[df_merged_c['pos_neg']==1]['total_review_comwords'], 30)
common_words_bad1= get_top_n_trigram(df_merged_c[df_merged_c['pos_neg']==0]['total_review_comwords'], 30)


# In[770]:


plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good1]
y_good1=[x[1] for x in common_words_good1]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad1]
y_bad1=[x[1] for x in common_words_bad1]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# In[640]:


df_merged_c['month'] = df_merged_c['month'].astype(int)


# In[772]:


set(df_merged_c['price_bins'])


# In[773]:


common_words_good_c = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Clothing')]['total_review_comwords'], 30)
common_words_bad_c = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Clothing')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good_c]
y_good=[x[1] for x in common_words_good_c]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad_c]
y_bad=[x[1] for x in common_words_bad_c]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[785]:


common_words_good_t_c = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Clothing')]['total_review_comwords'], 30)
common_words_bad_t_c= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Clothing')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good_t_c]
y_good1=[x[1] for x in common_words_good_t_c]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad_t_c]
y_bad1=[x[1] for x in common_words_bad_t_c]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# In[786]:


common_words_good_j = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Jewelry')]['total_review_comwords'], 30)
common_words_bad_j = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Jewelry')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good_j]
y_good=[x[1] for x in common_words_good_j]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad_j]
y_bad=[x[1] for x in common_words_bad_j]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[788]:


common_words_good_t_j = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Jewelry')]['total_review_comwords'], 30)
common_words_bad_t_j= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Jewelry')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good_t_j]
y_good1=[x[1] for x in common_words_good_t_j]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad_t_j]
y_bad1=[x[1] for x in common_words_bad_t_j]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# In[787]:


common_words_good_s = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Shoes')]['total_review_comwords'], 30)
common_words_bad_s = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Shoes')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good_s]
y_good=[x[1] for x in common_words_good_s]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad_s]
y_bad=[x[1] for x in common_words_bad_s]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[789]:


common_words_good_t_s = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Shoes')]['total_review_comwords'], 30)
common_words_bad_t_s= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Shoes')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good_t_s]
y_good1=[x[1] for x in common_words_good_t_s]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad_t_s]
y_bad1=[x[1] for x in common_words_bad_t_s]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# In[790]:


common_words_good_o = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Others')]['total_review_comwords'], 30)
common_words_bad_o = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Others')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good_o]
y_good=[x[1] for x in common_words_good_o]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad_o]
y_bad=[x[1] for x in common_words_bad_o]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[791]:


common_words_good_t_o = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['category_derived']=='Others')]['total_review_comwords'], 30)
common_words_bad_t_o= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['category_derived']=='Others')]['total_review_comwords'], 30)
plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good_t_o]
y_good1=[x[1] for x in common_words_good_t_o]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad_t_o]
y_bad1=[x[1] for x in common_words_bad_t_o]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# #### Peak Times

# In[654]:


common_words_good_em = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['month']>=9) & (df_merged_c['month']<=12) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)


# In[655]:


common_words_bad_em = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['month']>=9) & (df_merged_c['month']<=12)& (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)


# In[656]:


plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good_em]
y_good=[x[1] for x in common_words_good_em]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad_em]
y_bad=[x[1] for x in common_words_bad_em]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[674]:


common_words_good1_em = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1)  & (df_merged_c['month']>=9) & (df_merged_c['month']<=12) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)
common_words_bad1_em= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0)  & (df_merged_c['month']>=9) & (df_merged_c['month']<=12) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)


# In[675]:


plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good1_em]
y_good1=[x[1] for x in common_words_good1_em]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad1_em]
y_bad1=[x[1] for x in common_words_bad1_em]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# #### Non peak

# In[659]:


common_words_good_sm = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['month']>=1) & (df_merged_c['month']<=4) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)
common_words_bad_sm = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['month']>=1) & (df_merged_c['month']<=4)& (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)


# In[661]:


plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good=[x[0] for x in common_words_good_sm]
y_good=[x[1] for x in common_words_good_sm]
sns.barplot(x_good,y_good,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good)):
    plt.text(i-0.2,y_good[i]+100,'{}'.format(y_good[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad=[x[0] for x in common_words_bad_sm]
y_bad=[x[1] for x in common_words_bad_sm]
sns.barplot(x_bad,y_bad,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Bigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad)):
    plt.text(i-0.2,y_bad[i],'{}'.format(y_bad[i]),size=15,rotation=45)


# In[676]:


common_words_good1_sm = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1)  & (df_merged_c['month']>=1) & (df_merged_c['month']<=4) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)
common_words_bad1_sm= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0)  & (df_merged_c['month']>=1) & (df_merged_c['month']<=4) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)


# In[677]:


plt.figure(figsize=(25,8))
# good reviews bigrams
plt.subplot(1,2,1)
x_good1=[x[0] for x in common_words_good1_sm]
y_good1=[x[1] for x in common_words_good1_sm]
plt.bar(x_good1,y_good1,color='orange')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Positive Reviews",fontsize=20)
for i in range(len(x_good1)):
    plt.text(i-0.2,y_good1[i]+100,'{}'.format(y_good1[i]),size=15,rotation=45)
    
plt.subplot(1,2,2)
x_bad1=[x[0] for x in common_words_bad1_sm]
y_bad1=[x[1] for x in common_words_bad1_sm]
plt.bar(x_bad1,y_bad1,color='black')
plt.xticks(rotation=90,fontsize=20)
plt.title("Top 20 Trigrams in Negative Reviews",fontsize=20)
for i in range(len(x_bad1)):
    plt.text(i-0.2,y_bad1[i],'{}'.format(y_bad1[i]),size=15,rotation=45)


# ####  Word Cloud across categories

# In[793]:


cloud_p_c = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Clothing') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p_c);


# In[794]:


cloud_n_c = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Clothing') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n_c);


# In[795]:


cloud_p_j = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Jewelry') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p_j);


# In[796]:


cloud_n_j = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Jewelry') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n_j);


# In[797]:


cloud_p_s = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Shoes') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p_s);


# In[798]:


cloud_n_s = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Shoes') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n_s);


# #### sales rank check 

# In[723]:


df_check = df_merged_c[df_merged_c['salesrank_derived']!='']


# In[724]:


df_check['salesrank_derived'] = df_check['salesrank_derived'].astype(int)


# In[748]:


df_check.groupby(['salesrank_derived','category_derived']).agg({'reviewText':'count'}).sort_values(by = 'reviewText',ascending=False)


# In[735]:


df_check.groupby(['asin','salesrank_derived']).agg({'reviewText':'count'}).sort_values(by = 'reviewText',ascending=False).head(100)


# In[739]:


set(df_check[df_check['salesrank_derived']==5]['asin'])


# In[742]:


set(df_check[df_check['asin']=='B0007QCQGI']['date'])


# In[743]:


set(df_check[df_check['asin']=='B0000C321X']['date'])


# In[744]:


set(df_check[df_check['asin']=='B000O32MLI']['date'])


# In[749]:


set(df_check[df_check['category_derived']=='Jewelry']['salesrank_derived'])


# In[750]:


set(df_check[df_check['category_derived']=='Clothing']['salesrank_derived'])


# In[753]:


set(df_check[df_check['category_derived']=='Shoes']['salesrank_derived'])


# In[759]:


df_check[(df_check['category_derived']=='Shoes') & (df_check['salesrank_derived']==7)]


# In[ ]:




