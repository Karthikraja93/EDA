

```python
import pandas as pd
import seaborn as sns
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
```


```python
df_metadata = pd.read_csv('./metadata_category_clothing_shoes_and_jewelry_only.csv')
```


```python
df_metadata.shape
```




    (23033, 10)




```python
df = pd.read_csv('./reviews_Clothing_Shoes_and_Jewelry_5.csv')
```


```python
df.shape
```




    (278677, 10)




```python
df_merged = pd.merge(df, df_metadata, on='asin')
```


```python
df_merged.shape
```




    (278677, 19)




```python
df_merged.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reviewerID</th>
      <th>asin</th>
      <th>reviewerName</th>
      <th>helpful</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>unixReviewTime</th>
      <th>reviewTime</th>
      <th>metadataid</th>
      <th>salesrank</th>
      <th>imurl</th>
      <th>categories</th>
      <th>title</th>
      <th>description</th>
      <th>price</th>
      <th>related</th>
      <th>brand</th>
      <th>positive_helpful</th>
      <th>negative_helpful</th>
      <th>total_helpful</th>
      <th>positive_helpful_ratio</th>
      <th>len_reviewText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>A1KLRMWW2FWPL4</td>
      <td>0000031887</td>
      <td>Amazon Customer "cameramom"</td>
      <td>[0, 0]</td>
      <td>This is a great tutu and at a really great pri...</td>
      <td>5.0</td>
      <td>Great tutu-  not cheaply made</td>
      <td>1297468800</td>
      <td>02 12, 2011</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>172.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>A2G5TCU2WDFZ65</td>
      <td>0000031887</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I bought this for my 4 yr old daughter for dan...</td>
      <td>5.0</td>
      <td>Very Cute!!</td>
      <td>1358553600</td>
      <td>01 19, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>306.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>A1RLQXYNCMWRWN</td>
      <td>0000031887</td>
      <td>Carola</td>
      <td>[0, 0]</td>
      <td>What can I say... my daughters have it in oran...</td>
      <td>5.0</td>
      <td>I have buy more than one</td>
      <td>1357257600</td>
      <td>01 4, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>312.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>A8U3FAMSJVHS5</td>
      <td>0000031887</td>
      <td>Caromcg</td>
      <td>[0, 0]</td>
      <td>We bought several tutus at once, and they are ...</td>
      <td>5.0</td>
      <td>Adorable, Sturdy</td>
      <td>1398556800</td>
      <td>04 27, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>405.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>A3GEOILWLK86XM</td>
      <td>0000031887</td>
      <td>CJ</td>
      <td>[0, 0]</td>
      <td>Thank you Halo Heaven great product for Little...</td>
      <td>5.0</td>
      <td>Grammy's Angels Love it</td>
      <td>1394841600</td>
      <td>03 15, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>453.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 278677 entries, 0 to 278676
    Data columns (total 25 columns):
    Unnamed: 0                278677 non-null int64
    reviewerID                278677 non-null object
    asin                      278677 non-null object
    reviewerName              278208 non-null object
    helpful                   278677 non-null object
    reviewText                278653 non-null object
    overall                   278677 non-null float64
    summary                   278676 non-null object
    unixReviewTime            278677 non-null int64
    reviewTime                278677 non-null object
    metadataid                278677 non-null int64
    salesrank                 278677 non-null object
    imurl                     278677 non-null object
    categories                278677 non-null object
    title                     278409 non-null object
    description               15462 non-null object
    price                     113912 non-null float64
    related                   277882 non-null object
    brand                     48573 non-null object
    positive_helpful          278677 non-null int64
    negative_helpful          278677 non-null int64
    total_helpful             278677 non-null int64
    positive_helpful_ratio    278677 non-null float64
    len_reviewText            278653 non-null float64
    category_derived          278677 non-null object
    dtypes: float64(4), int64(6), object(15)
    memory usage: 65.3+ MB



```python
df_merged.nunique()
```




    Unnamed: 0                278677
    reviewerID                 39387
    asin                       23033
    reviewerName               34444
    helpful                      974
    reviewText                278525
    overall                        5
    summary                   179836
    unixReviewTime              2691
    reviewTime                  2691
    metadataid                 23033
    salesrank                  20017
    imurl                      22825
    categories                  6307
    title                      22787
    description                 1359
    price                       2640
    related                    22858
    brand                       1181
    positive_helpful              10
    negative_helpful              10
    total_helpful                 19
    positive_helpful_ratio        45
    len_reviewText              2966
    category_derived              23
    dtype: int64




```python
df_merged['salesrank'] = df_merged['salesrank'].fillna('')

```


```python
df_merged['category_derived'] = df_merged['salesrank'].apply(lambda x: x.partition(':')[0]) 
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace('"', ''))
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace('{', ''))
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace("'", ''))
df_merged['category_derived'] = df_merged['category_derived'].apply(lambda x: x.replace("}", ''))
```


```python
df_merged['category_derived'].value_counts()
```




    Clothing                     139752
    Shoes                         69238
    Jewelry                       29179
                                  14233
    Watches                       10166
    Sports &amp; Outdoors          8311
    Toys & Games                   2211
    Home &amp; Kitchen             2110
    Health & Personal Care         1009
    Beauty                          750
    Patio, Lawn & Garden            555
    Arts, Crafts & Sewing           377
    Kitchen & Dining                211
    Automotive                      144
    Industrial & Scientific          85
    Cell Phones & Accessories        77
    Electronics                      74
    Software                         58
    Baby                             57
    Home Improvement                 36
    Camera &amp; Photo               19
    Computers & Accessories          13
    Music                            12
    Name: category_derived, dtype: int64



##### Clothing 50% Shoes 25% Jewelry 10% Others 14%    
(Chart - https://docs.google.com/spreadsheets/d/1nZReNM1AGumiB4DOTW5sKBuJ8zSA60EtEcO0-tzKdLY/edit#gid=775562)


```python
df_merged['overall'].value_counts()
```




    5.0    163240
    4.0     58357
    3.0     30425
    2.0     15463
    1.0     11192
    Name: overall, dtype: int64



#### 60% of ratings consist of 5 stars, 20% of ratings consist of 4 stars, 10% of ratings consist of 3 stars, 5% of ratings consist of 2 stars, 5% of ratings consist of 1 star

## Helpfulness


```python
df_merged['positive_helpful'] = df_merged['helpful'].apply(lambda x: x[1:2]) 
df_merged['negative_helpful'] = df_merged['helpful'].apply(lambda x: x[4:5])
df_merged['positive_helpful'] = df_merged['positive_helpful'].astype(int)
df_merged['negative_helpful'] = df_merged['negative_helpful'].apply(lambda x: x.replace(' ', '0')) 
df_merged['negative_helpful'] = df_merged['negative_helpful'].apply(lambda x: x.replace(',', '0')) 
df_merged['negative_helpful'] = df_merged['negative_helpful'].astype(int)
df_merged['total_helpful'] = df_merged['negative_helpful'] + df_merged['positive_helpful']
df_merged['positive_helpful_ratio'] = (df_merged['positive_helpful']/df_merged['total_helpful']).fillna(0)
df_merged['len_reviewText'] = df_merged['reviewText'].str.len()
```


```python
len(df_merged[df_merged['total_helpful']==0])
```




    191656




```python
len(df_merged[df_merged['total_helpful']!=0])
```




    87021




```python
sum(df_merged[df_merged['total_helpful']!=0]['negative_helpful'])
```




    183576




```python
sum(df_merged[df_merged['total_helpful']!=0]['positive_helpful'])
```




    164151




```python
sum(df_merged[df_merged['total_helpful']!=0]['total_helpful'])
```




    347727



#### ~70% didnt have helpfulness voting


```python
df_merged[df_merged['total_helpful']!=0].groupby('overall').agg({'positive_helpful_ratio':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>overall</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1.0</th>
      <td>0.395152</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>0.400243</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>0.413713</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>0.453546</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>0.471050</td>
    </tr>
  </tbody>
</table>
</div>



####  The higher the ratings . The higher are the upvotes for helpfulness


```python
df_merged_c['len_summary'] = df_merged_c['summary'].str.len()
df_merged_c['len_summary_bins'] = pd.qcut(df_merged_c['len_summary'], 3, labels = list('LMH'))
df_merged_c['len_reviewText_bins'] = pd.qcut(df_merged_c['len_reviewText'], 3, labels = list('LMH'))
```

#### Greater the length of review greater is the postive helpful ratio. No difference in postive helpful ratio even if the reviews are cleaned for punctuations etc
chart - https://docs.google.com/spreadsheets/d/1nZReNM1AGumiB4DOTW5sKBuJ8zSA60EtEcO0-tzKdLY/edit#gid=775562


```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_reviewText_bins').agg({'positive_helpful_ratio':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>len_reviewText_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>L</th>
      <td>0.401140</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.430659</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.486350</td>
    </tr>
  </tbody>
</table>
</div>



#### longer reviews are helpful by 20% compared to shorter reviews


```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_summary_bins').agg({'positive_helpful_ratio':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>len_summary_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>L</th>
      <td>0.428552</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.449823</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.467374</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
df_merged_c[["len_reviewText_cleaned", "len_summary_cleaned"]].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>len_reviewText_cleaned</th>
      <th>len_summary_cleaned</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>278677.000000</td>
      <td>278677.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>244.963678</td>
      <td>16.913043</td>
    </tr>
    <tr>
      <th>std</th>
      <td>257.718106</td>
      <td>11.053658</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>109.000000</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>165.000000</td>
      <td>14.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>284.000000</td>
      <td>21.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>17752.000000</td>
      <td>112.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_reviewText_claned_bins').agg({'positive_helpful_ratio':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>len_reviewText_claned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>L</th>
      <td>0.401627</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.430917</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.486172</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby('len_summary_cleaned_bins').agg({'positive_helpful_ratio':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>len_summary_cleaned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>L</th>
      <td>0.429640</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.450753</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.467269</td>
    </tr>
  </tbody>
</table>
</div>



## Category Wise Analysis


```python
df_merged_c = df_merged.copy()
```


```python
df_merged_c['category_derived'].loc[~df_merged_c['category_derived'].isin(['Clothing', 'Shoes','Jewelry'])]='Others'

```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/pandas/core/indexing.py:205: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      self._setitem_with_indexer(indexer, value)



```python
df_merged_c.groupby('category_derived').agg({'overall':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>overall</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clothing</th>
      <td>4.197557</td>
    </tr>
    <tr>
      <th>Jewelry</th>
      <td>4.316975</td>
    </tr>
    <tr>
      <th>Others</th>
      <td>4.303150</td>
    </tr>
    <tr>
      <th>Shoes</th>
      <td>4.276943</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c.groupby('category_derived').reviewerID.nunique()
```




    category_derived
    Clothing    35076
    Jewelry     11911
    Others      21783
    Shoes       27326
    Name: reviewerID, dtype: int64




```python
df_merged_c.groupby('category_derived').asin.nunique()
```




    category_derived
    Clothing    10768
    Jewelry      2635
    Others       3655
    Shoes        5975
    Name: asin, dtype: int64




```python
df_merged_c.groupby('category_derived').reviewText.nunique()
```




    category_derived
    Clothing    139678
    Jewelry      29170
    Others       40493
    Shoes        69226
    Name: reviewText, dtype: int64



####  Reviews per Product across Category :Clothing 12.97 , Shoes 11.58 ,  Jewelry 11.07 , Others 11.07
chart - https://docs.google.com/spreadsheets/d/1nZReNM1AGumiB4DOTW5sKBuJ8zSA60EtEcO0-tzKdLY/edit#gid=775562


```python
with sns.axes_style('white'):
    g = sns.factorplot(x = "overall", hue = "category_derived" ,data=df_merged_c, aspect=2.0,kind='count')
    g.set_ylabels("Total number of ratings")
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/categorical.py:3704: UserWarning: The `factorplot` function has been renamed to `catplot`. The original name will be removed in a future release. Please update your code. Note that the default `kind` in `factorplot` (`'point'`) has changed `'strip'` in `catplot`.
      warnings.warn(msg)



![png](output_43_1.png)



```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby(['category_derived','len_reviewText_claned_bins']).agg({'positive_helpful_ratio':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th>len_reviewText_claned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Clothing</th>
      <th>L</th>
      <td>0.401641</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.436231</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.494686</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Jewelry</th>
      <th>L</th>
      <td>0.426701</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.441393</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.475164</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Others</th>
      <th>L</th>
      <td>0.391406</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.420695</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.496828</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Shoes</th>
      <th>L</th>
      <td>0.388633</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.418634</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.466047</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c['negative_helpful_ratio'] = (df_merged_c['negative_helpful']/df_merged_c['total_helpful']).fillna(0)
```


```python
df_merged['negative_helpful_ratio'].head(5)
```




    0    0.0
    1    0.0
    2    0.0
    3    0.0
    4    0.0
    Name: negative_helpful_ratio, dtype: float64




```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby(['category_derived','len_reviewText_claned_bins']).agg({'negative_helpful_ratio':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>negative_helpful_ratio</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th>len_reviewText_claned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Clothing</th>
      <th>L</th>
      <td>0.598359</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.563769</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.505314</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Jewelry</th>
      <th>L</th>
      <td>0.573299</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.558607</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.524836</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Others</th>
      <th>L</th>
      <td>0.608594</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.579305</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.503172</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Shoes</th>
      <th>L</th>
      <td>0.611367</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.581366</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.533953</td>
    </tr>
  </tbody>
</table>
</div>



#### Similar pattern is observed for positive helpful ratio across categories compared to overall cleaned reviews bins


```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby(['category_derived','len_summary_cleaned_bins']).agg({'positive_helpful_ratio':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th>len_summary_cleaned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Clothing</th>
      <th>L</th>
      <td>0.432933</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.455957</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.472101</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Jewelry</th>
      <th>L</th>
      <td>0.439195</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.454235</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.453656</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Others</th>
      <th>L</th>
      <td>0.426518</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.452374</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.477589</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Shoes</th>
      <th>L</th>
      <td>0.416469</td>
    </tr>
    <tr>
      <th>M</th>
      <td>0.436999</td>
    </tr>
    <tr>
      <th>H</th>
      <td>0.455036</td>
    </tr>
  </tbody>
</table>
</div>



## Pricing


```python
with sns.axes_style('white'):
    g = sns.factorplot(x = "len_summary_cleaned_bins", y = "price" ,data=df_merged_c, aspect=2.0,kind='bar')
    g.set_ylabels("Price")
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/categorical.py:3704: UserWarning: The `factorplot` function has been renamed to `catplot`. The original name will be removed in a future release. Please update your code. Note that the default `kind` in `factorplot` (`'point'`) has changed `'strip'` in `catplot`.
      warnings.warn(msg)



![png](output_51_1.png)



```python
with sns.axes_style('white'):
    g = sns.factorplot(x = "len_reviewText_claned_bins", y = "price" ,data=df_merged_c, aspect=2.0,kind='bar')
    g.set_ylabels("Price")
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/categorical.py:3704: UserWarning: The `factorplot` function has been renamed to `catplot`. The original name will be removed in a future release. Please update your code. Note that the default `kind` in `factorplot` (`'point'`) has changed `'strip'` in `catplot`.
      warnings.warn(msg)



![png](output_52_1.png)



```python
df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','len_summary_cleaned_bins']).agg({'price':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>price</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th>len_summary_cleaned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Clothing</th>
      <th>L</th>
      <td>20.444742</td>
    </tr>
    <tr>
      <th>M</th>
      <td>22.248228</td>
    </tr>
    <tr>
      <th>H</th>
      <td>23.353140</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Jewelry</th>
      <th>L</th>
      <td>13.280462</td>
    </tr>
    <tr>
      <th>M</th>
      <td>15.405192</td>
    </tr>
    <tr>
      <th>H</th>
      <td>17.459431</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Others</th>
      <th>L</th>
      <td>27.823274</td>
    </tr>
    <tr>
      <th>M</th>
      <td>33.304959</td>
    </tr>
    <tr>
      <th>H</th>
      <td>35.581282</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Shoes</th>
      <th>L</th>
      <td>47.653835</td>
    </tr>
    <tr>
      <th>M</th>
      <td>50.832328</td>
    </tr>
    <tr>
      <th>H</th>
      <td>57.230962</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','len_reviewText_claned_bins']).agg({'price':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>price</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th>len_reviewText_claned_bins</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">Clothing</th>
      <th>L</th>
      <td>18.899995</td>
    </tr>
    <tr>
      <th>M</th>
      <td>21.544905</td>
    </tr>
    <tr>
      <th>H</th>
      <td>25.590147</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Jewelry</th>
      <th>L</th>
      <td>12.728785</td>
    </tr>
    <tr>
      <th>M</th>
      <td>14.919959</td>
    </tr>
    <tr>
      <th>H</th>
      <td>19.798472</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Others</th>
      <th>L</th>
      <td>24.558089</td>
    </tr>
    <tr>
      <th>M</th>
      <td>27.891895</td>
    </tr>
    <tr>
      <th>H</th>
      <td>42.172475</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">Shoes</th>
      <th>L</th>
      <td>42.273417</td>
    </tr>
    <tr>
      <th>M</th>
      <td>49.700051</td>
    </tr>
    <tr>
      <th>H</th>
      <td>61.386725</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c[df_merged_c.price.isnull()].groupby('category_derived').agg({'len_summary_cleaned':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>len_summary_cleaned</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clothing</th>
      <td>16.716972</td>
    </tr>
    <tr>
      <th>Jewelry</th>
      <td>15.607183</td>
    </tr>
    <tr>
      <th>Others</th>
      <td>17.935465</td>
    </tr>
    <tr>
      <th>Shoes</th>
      <td>17.692066</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c[df_merged_c.price.isnull()].groupby('category_derived').agg({'len_reviewText_cleaned':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>len_reviewText_cleaned</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clothing</th>
      <td>229.821011</td>
    </tr>
    <tr>
      <th>Jewelry</th>
      <td>216.376101</td>
    </tr>
    <tr>
      <th>Others</th>
      <td>301.452141</td>
    </tr>
    <tr>
      <th>Shoes</th>
      <td>267.974505</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c[df_merged_c.price.notnull()].groupby('category_derived').agg({'len_summary_cleaned':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>len_summary_cleaned</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Clothing</th>
      <td>16.603232</td>
    </tr>
    <tr>
      <th>Jewelry</th>
      <td>15.371647</td>
    </tr>
    <tr>
      <th>Others</th>
      <td>17.498881</td>
    </tr>
    <tr>
      <th>Shoes</th>
      <td>16.957463</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c['price_bins'] = pd.qcut(df_merged_c['price'], 3, labels = list('LMH'))
```


```python
df_merged_c['price_bins'].value_counts()
```




    L    39491
    H    37957
    M    36464
    Name: price_bins, dtype: int64




```python
df_merged_c[df_merged_c.price.notnull()].groupby('price_bins').reviewerID.nunique()

```




    price_bins
    L    18893
    M    21865
    H    21704
    Name: reviewerID, dtype: int64




```python
df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','price_bins','pos_neg']).reviewText.nunique()

```




    category_derived  price_bins  pos_neg
    Clothing          L           0           3347
                                  1          11677
                      M           0           4036
                                  1          16335
                      H           0           2953
                                  1          13869
    Jewelry           L           0           2797
                                  1          11034
                      M           0            967
                                  1           5075
                      H           0            708
                                  1           4167
    Others            L           0           2262
                                  1           7484
                      M           0           1600
                                  1           7124
                      H           0           1786
                                  1          10110
    Shoes             L           0            211
                                  1            672
                      M           0            311
                                  1           1007
                      H           0            884
                                  1           3473
    Name: reviewText, dtype: int64




```python
df_merged_c[df_merged_c.price.notnull()].groupby(['category_derived','price_bins','pos_neg']).asin.nunique()
```




    category_derived  price_bins  pos_neg
    Clothing          L           0          1023
                                  1          1273
                      M           0          1404
                                  1          1755
                      H           0          1185
                                  1          1537
    Jewelry           L           0           727
                                  1           951
                      M           0           440
                                  1           630
                      H           0           376
                                  1           559
    Others            L           0           616
                                  1           760
                      M           0           591
                                  1           794
                      H           0           753
                                  1          1134
    Shoes             L           0            70
                                  1            78
                      M           0           118
                                  1           138
                      H           0           395
                                  1           505
    Name: asin, dtype: int64




```python
#Price Variation by time
```


```python
df_merged_c.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reviewerID</th>
      <th>asin</th>
      <th>reviewerName</th>
      <th>helpful</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>unixReviewTime</th>
      <th>reviewTime</th>
      <th>metadataid</th>
      <th>salesrank</th>
      <th>imurl</th>
      <th>categories</th>
      <th>title</th>
      <th>description</th>
      <th>price</th>
      <th>related</th>
      <th>brand</th>
      <th>positive_helpful</th>
      <th>negative_helpful</th>
      <th>total_helpful</th>
      <th>positive_helpful_ratio</th>
      <th>len_reviewText</th>
      <th>category_derived</th>
      <th>len_summary</th>
      <th>check</th>
      <th>len_summary_bins</th>
      <th>len_reviewText_bins</th>
      <th>reviewText_cleaned</th>
      <th>summary_cleaned</th>
      <th>len_reviewText_cleaned</th>
      <th>len_summary_cleaned</th>
      <th>len_summary_cleaned_bins</th>
      <th>len_reviewText_claned_bins</th>
      <th>price_bins</th>
      <th>salesrank_derived</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>A1KLRMWW2FWPL4</td>
      <td>0000031887</td>
      <td>Amazon Customer "cameramom"</td>
      <td>[0, 0]</td>
      <td>This is a great tutu and at a really great pri...</td>
      <td>5.0</td>
      <td>Great tutu-  not cheaply made</td>
      <td>1297468800</td>
      <td>02 12, 2011</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>172.0</td>
      <td>Others</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisisagreattutuandatareallygreatpriceItdoesnt...</td>
      <td>Greattutunotcheaplymade</td>
      <td>130</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>8547</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>A2G5TCU2WDFZ65</td>
      <td>0000031887</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I bought this for my 4 yr old daughter for dan...</td>
      <td>5.0</td>
      <td>Very Cute!!</td>
      <td>1358553600</td>
      <td>01 19, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>306.0</td>
      <td>Others</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtthisformy4yrolddaughterfordanceclassshe...</td>
      <td>VeryCute</td>
      <td>240</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>A1RLQXYNCMWRWN</td>
      <td>0000031887</td>
      <td>Carola</td>
      <td>[0, 0]</td>
      <td>What can I say... my daughters have it in oran...</td>
      <td>5.0</td>
      <td>I have buy more than one</td>
      <td>1357257600</td>
      <td>01 4, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>312.0</td>
      <td>Others</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>WhatcanIsaymydaughtershaveitinorangeblackwhite...</td>
      <td>Ihavebuymorethanone</td>
      <td>238</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>A8U3FAMSJVHS5</td>
      <td>0000031887</td>
      <td>Caromcg</td>
      <td>[0, 0]</td>
      <td>We bought several tutus at once, and they are ...</td>
      <td>5.0</td>
      <td>Adorable, Sturdy</td>
      <td>1398556800</td>
      <td>04 27, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>405.0</td>
      <td>Others</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Weboughtseveraltutusatonceandtheyaregothighrev...</td>
      <td>AdorableSturdy</td>
      <td>313</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>A3GEOILWLK86XM</td>
      <td>0000031887</td>
      <td>CJ</td>
      <td>[0, 0]</td>
      <td>Thank you Halo Heaven great product for Little...</td>
      <td>5.0</td>
      <td>Grammy's Angels Love it</td>
      <td>1394841600</td>
      <td>03 15, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>453.0</td>
      <td>Others</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>ThankyouHaloHeavengreatproductforLittleGirlsMy...</td>
      <td>GrammysAngelsLoveit</td>
      <td>333</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c['salesrank_derived'] = df_merged_c['salesrank'].apply(lambda x: x.partition(':')[2])
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace('"', ''))
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace('{', ''))
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace("'", ''))
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace("}", ''))
```


```python
df_merged_c['salesrank_derived'] = df_merged_c['salesrank_derived'].apply(lambda x: x.replace(' ', ''))
```


```python
df_merged_c_1 = df_merged_c[df_merged_c['salesrank_derived']!='']
```


```python
df_merged_c_1['salesrank_derived'] = df_merged_c_1['salesrank_derived'].astype(int)
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      """Entry point for launching an IPython kernel.



```python
df_merged_c[df_merged_c.price.notnull()].groupby('asin').price.nunique()
```


```python
df_merged_c.columns
```




    Index(['Unnamed: 0', 'reviewerID', 'asin', 'reviewerName', 'helpful', 'reviewText', 'overall', 'summary', 'unixReviewTime', 'reviewTime', 'metadataid', 'salesrank', 'imurl', 'categories', 'title', 'description', 'price', 'related', 'brand', 'positive_helpful', 'negative_helpful', 'total_helpful', 'positive_helpful_ratio', 'len_reviewText', 'category_derived', 'len_summary', 'check', 'len_summary_bins', 'len_reviewText_bins', 'reviewText_cleaned', 'summary_cleaned', 'len_reviewText_cleaned', 'len_summary_cleaned', 'len_summary_cleaned_bins', 'len_reviewText_claned_bins', 'price_bins', 'salesrank_derived'], dtype='object')



#### Price & Salesrank do not vary over time

## Reviewer Behaviour


```python

df_merged_c['date'] = pd.to_datetime(df['unixReviewTime'],unit='s')
```


```python
from datetime import date
from datetime import datetime, timedelta
```


```python
df_merged_c['date'] = df_merged_c['date'].apply(lambda x: x.date().strftime("%Y-%m-%d"))
```


```python
df_merged_c.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reviewerID</th>
      <th>asin</th>
      <th>reviewerName</th>
      <th>helpful</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>unixReviewTime</th>
      <th>reviewTime</th>
      <th>metadataid</th>
      <th>salesrank</th>
      <th>imurl</th>
      <th>categories</th>
      <th>title</th>
      <th>description</th>
      <th>price</th>
      <th>related</th>
      <th>brand</th>
      <th>positive_helpful</th>
      <th>negative_helpful</th>
      <th>total_helpful</th>
      <th>positive_helpful_ratio</th>
      <th>len_reviewText</th>
      <th>category_derived</th>
      <th>len_summary</th>
      <th>check</th>
      <th>len_summary_bins</th>
      <th>len_reviewText_bins</th>
      <th>reviewText_cleaned</th>
      <th>summary_cleaned</th>
      <th>len_reviewText_cleaned</th>
      <th>len_summary_cleaned</th>
      <th>len_summary_cleaned_bins</th>
      <th>len_reviewText_claned_bins</th>
      <th>price_bins</th>
      <th>salesrank_derived</th>
      <th>date</th>
      <th>month</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>A1KLRMWW2FWPL4</td>
      <td>0000031887</td>
      <td>Amazon Customer "cameramom"</td>
      <td>[0, 0]</td>
      <td>This is a great tutu and at a really great pri...</td>
      <td>5.0</td>
      <td>Great tutu-  not cheaply made</td>
      <td>1297468800</td>
      <td>02 12, 2011</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>172.0</td>
      <td>Others</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisisagreattutuandatareallygreatpriceItdoesnt...</td>
      <td>Greattutunotcheaplymade</td>
      <td>130</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>8547</td>
      <td>2011-02-12</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>A2G5TCU2WDFZ65</td>
      <td>0000031887</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I bought this for my 4 yr old daughter for dan...</td>
      <td>5.0</td>
      <td>Very Cute!!</td>
      <td>1358553600</td>
      <td>01 19, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>306.0</td>
      <td>Others</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtthisformy4yrolddaughterfordanceclassshe...</td>
      <td>VeryCute</td>
      <td>240</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2013-01-19</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>A1RLQXYNCMWRWN</td>
      <td>0000031887</td>
      <td>Carola</td>
      <td>[0, 0]</td>
      <td>What can I say... my daughters have it in oran...</td>
      <td>5.0</td>
      <td>I have buy more than one</td>
      <td>1357257600</td>
      <td>01 4, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>312.0</td>
      <td>Others</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>WhatcanIsaymydaughtershaveitinorangeblackwhite...</td>
      <td>Ihavebuymorethanone</td>
      <td>238</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2013-01-04</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>A8U3FAMSJVHS5</td>
      <td>0000031887</td>
      <td>Caromcg</td>
      <td>[0, 0]</td>
      <td>We bought several tutus at once, and they are ...</td>
      <td>5.0</td>
      <td>Adorable, Sturdy</td>
      <td>1398556800</td>
      <td>04 27, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>405.0</td>
      <td>Others</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Weboughtseveraltutusatonceandtheyaregothighrev...</td>
      <td>AdorableSturdy</td>
      <td>313</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2014-04-27</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>A3GEOILWLK86XM</td>
      <td>0000031887</td>
      <td>CJ</td>
      <td>[0, 0]</td>
      <td>Thank you Halo Heaven great product for Little...</td>
      <td>5.0</td>
      <td>Grammy's Angels Love it</td>
      <td>1394841600</td>
      <td>03 15, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>453.0</td>
      <td>Others</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>ThankyouHaloHeavengreatproductforLittleGirlsMy...</td>
      <td>GrammysAngelsLoveit</td>
      <td>333</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2014-03-15</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c['month'] = df_merged_c['date'].apply(lambda x: x[5:7])
```


```python
df_merged_c['year'] = df_merged_c['date'].apply(lambda x: x[0:4])
```


```python
df_merged_c['year'] = df_merged_c['year'].astype(int)
```


```python
df_merged_c[(df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)].groupby(['category_derived','month']).agg({'reviewText':'count'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reviewText</th>
    </tr>
    <tr>
      <th>category_derived</th>
      <th>month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="12" valign="top">Clothing</th>
      <th>01</th>
      <td>6016</td>
    </tr>
    <tr>
      <th>02</th>
      <td>5199</td>
    </tr>
    <tr>
      <th>03</th>
      <td>5105</td>
    </tr>
    <tr>
      <th>04</th>
      <td>5219</td>
    </tr>
    <tr>
      <th>05</th>
      <td>5394</td>
    </tr>
    <tr>
      <th>06</th>
      <td>5534</td>
    </tr>
    <tr>
      <th>07</th>
      <td>5934</td>
    </tr>
    <tr>
      <th>08</th>
      <td>6390</td>
    </tr>
    <tr>
      <th>09</th>
      <td>6489</td>
    </tr>
    <tr>
      <th>10</th>
      <td>8525</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10593</td>
    </tr>
    <tr>
      <th>12</th>
      <td>15168</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">Jewelry</th>
      <th>01</th>
      <td>1507</td>
    </tr>
    <tr>
      <th>02</th>
      <td>1397</td>
    </tr>
    <tr>
      <th>03</th>
      <td>1337</td>
    </tr>
    <tr>
      <th>04</th>
      <td>1177</td>
    </tr>
    <tr>
      <th>05</th>
      <td>1254</td>
    </tr>
    <tr>
      <th>06</th>
      <td>1021</td>
    </tr>
    <tr>
      <th>07</th>
      <td>1271</td>
    </tr>
    <tr>
      <th>08</th>
      <td>1415</td>
    </tr>
    <tr>
      <th>09</th>
      <td>1409</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1789</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2076</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3749</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">Others</th>
      <th>01</th>
      <td>2302</td>
    </tr>
    <tr>
      <th>02</th>
      <td>1728</td>
    </tr>
    <tr>
      <th>03</th>
      <td>1720</td>
    </tr>
    <tr>
      <th>04</th>
      <td>1845</td>
    </tr>
    <tr>
      <th>05</th>
      <td>1822</td>
    </tr>
    <tr>
      <th>06</th>
      <td>1738</td>
    </tr>
    <tr>
      <th>07</th>
      <td>1989</td>
    </tr>
    <tr>
      <th>08</th>
      <td>2186</td>
    </tr>
    <tr>
      <th>09</th>
      <td>1996</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2561</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2989</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4769</td>
    </tr>
    <tr>
      <th rowspan="12" valign="top">Shoes</th>
      <th>01</th>
      <td>2913</td>
    </tr>
    <tr>
      <th>02</th>
      <td>2459</td>
    </tr>
    <tr>
      <th>03</th>
      <td>2776</td>
    </tr>
    <tr>
      <th>04</th>
      <td>3311</td>
    </tr>
    <tr>
      <th>05</th>
      <td>3371</td>
    </tr>
    <tr>
      <th>06</th>
      <td>3290</td>
    </tr>
    <tr>
      <th>07</th>
      <td>3447</td>
    </tr>
    <tr>
      <th>08</th>
      <td>3491</td>
    </tr>
    <tr>
      <th>09</th>
      <td>3447</td>
    </tr>
    <tr>
      <th>10</th>
      <td>4496</td>
    </tr>
    <tr>
      <th>11</th>
      <td>5222</td>
    </tr>
    <tr>
      <th>12</th>
      <td>6718</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c['asin_reviewer'] = df_merged_c['asin'] + df_merged_c['reviewerID']
```


```python
df_merged_c['asin_reviewer'].nunique()
```




    278677



#### Reviewer did not write more than one reviews for a product


```python
df_merged_c.groupby('reviewerID').len_reviewText_claned_bins.nunique()
```




    reviewerID
    A001114613O3F18Q5NVR6    2
    A00146182PNM90WNNAZ5Q    2
    A00165422B2GAUE3EL6Z0    2
    A00338282E99B8OR2JYTZ    3
    A00354001GE099Q1FL0TU    2
                            ..
    AZZMQ85DPFEG3            3
    AZZNK89PXD006            1
    AZZT1ERHBSNQ8            1
    AZZTOUKVTUMVM            2
    AZZYW4YOE1B6E            3
    Name: len_reviewText_claned_bins, Length: 39387, dtype: int64




```python
df_merged_c_2 = df_merged_c[['reviewerID','len_reviewText_claned_bins']]
```


```python
df_merged_c_3 = df_merged_c_2.groupby(['reviewerID','len_reviewText_claned_bins']).size().unstack()
```


```python
df_merged_c_4 = df_merged_c[df_merged_c['total_helpful']!=0][['reviewerID','len_reviewText_claned_bins']]
```


```python
df_merged_c_5 = df_merged_c_4.groupby(['reviewerID','len_reviewText_claned_bins']).size().unstack()
```


```python
df_merged_c.groupby('reviewerID').reviewText.nunique().sort_values(ascending=False)
```




    reviewerID
    A2J4XMWKR8PPD0    136
    A2GA55P7WGHJCP     76
    A2KBV88FL48CFS     69
    AENH50GW3OKDA      68
    A2V5R832QCSOMX     62
                     ... 
    A2FWY7OWLFDRT3      5
    A2FWYHP0T4FGKD      5
    A3T6H846YFFH4G      4
    A13LURP1U7PZZO      4
    A1NF3H3XLK9OOO      4
    Name: reviewText, Length: 39387, dtype: int64




```python
df_merged_c[df_merged_c['total_helpful']!=0].groupby('reviewerID').agg({'positive_helpful_ratio':'mean'})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>positive_helpful_ratio</th>
    </tr>
    <tr>
      <th>reviewerID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A001114613O3F18Q5NVR6</th>
      <td>0.458333</td>
    </tr>
    <tr>
      <th>A00146182PNM90WNNAZ5Q</th>
      <td>0.413194</td>
    </tr>
    <tr>
      <th>A00165422B2GAUE3EL6Z0</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>A00404823GU1Q517KP4Z8</th>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>A0055084JB2YQW2IDOSQ</th>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>AZZHZZMH3U1VB</th>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>AZZKXNSXR6KBE</th>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>AZZMQ85DPFEG3</th>
      <td>0.391667</td>
    </tr>
    <tr>
      <th>AZZNK89PXD006</th>
      <td>0.500000</td>
    </tr>
    <tr>
      <th>AZZTOUKVTUMVM</th>
      <td>0.416667</td>
    </tr>
  </tbody>
</table>
<p>32959 rows × 1 columns</p>
</div>



#### High frequent reviewers wrote 70% of reviews either Long or Medium size (Avg Helpfulness score - 0.466 excluding 0 helpfulness)



#### Less frequent reviewers wrote 55% of reviews either Low size(Avg Helpfulness score - 0.429 excluding 0 helpfulness)


#### The above statements implies high frequent reviewers are more helpful by 10% compared to low frequent users

## Misc


```python
df_merged_c.groupby('overall').agg({'len_reviewText_cleaned':'mean'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>len_reviewText_cleaned</th>
    </tr>
    <tr>
      <th>overall</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1.0</th>
      <td>261.271801</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>266.970963</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>260.274675</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>264.165858</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>232.042594</td>
    </tr>
  </tbody>
</table>
</div>



####  Higher ratings have less review length 


```python
df_merged_c.groupby('asin').agg({'reviewText_cleaned':'count'}).sort_values(by='reviewText_cleaned', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reviewText_cleaned</th>
    </tr>
    <tr>
      <th>asin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>B005LERHD8</th>
      <td>441</td>
    </tr>
    <tr>
      <th>B005GYGD7O</th>
      <td>286</td>
    </tr>
    <tr>
      <th>B008WYDP1C</th>
      <td>249</td>
    </tr>
    <tr>
      <th>B0058XIMMM</th>
      <td>241</td>
    </tr>
    <tr>
      <th>B00CKGB85I</th>
      <td>225</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>B000VC3NUG</th>
      <td>5</td>
    </tr>
    <tr>
      <th>B005T4FKRA</th>
      <td>5</td>
    </tr>
    <tr>
      <th>B0028K3D86</th>
      <td>5</td>
    </tr>
    <tr>
      <th>B00ADZ1H8G</th>
      <td>5</td>
    </tr>
    <tr>
      <th>B0050XEPWQ</th>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>23033 rows × 1 columns</p>
</div>




```python
df_merged_c.groupby('asin').agg({'reviewText_cleaned':'count'}).sort_values(by='reviewText_cleaned', ascending=False).head(20)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reviewText_cleaned</th>
    </tr>
    <tr>
      <th>asin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>B005LERHD8</th>
      <td>441</td>
    </tr>
    <tr>
      <th>B005GYGD7O</th>
      <td>286</td>
    </tr>
    <tr>
      <th>B008WYDP1C</th>
      <td>249</td>
    </tr>
    <tr>
      <th>B0058XIMMM</th>
      <td>241</td>
    </tr>
    <tr>
      <th>B00CKGB85I</th>
      <td>225</td>
    </tr>
    <tr>
      <th>B007RD9DS8</th>
      <td>217</td>
    </tr>
    <tr>
      <th>B002RADHJC</th>
      <td>211</td>
    </tr>
    <tr>
      <th>B000T9VK56</th>
      <td>207</td>
    </tr>
    <tr>
      <th>B0000C321X</th>
      <td>205</td>
    </tr>
    <tr>
      <th>B0001ZNZJM</th>
      <td>197</td>
    </tr>
    <tr>
      <th>B007WNWEFC</th>
      <td>197</td>
    </tr>
    <tr>
      <th>B007WA3K4Y</th>
      <td>191</td>
    </tr>
    <tr>
      <th>B00012O12A</th>
      <td>189</td>
    </tr>
    <tr>
      <th>B007NLX16O</th>
      <td>189</td>
    </tr>
    <tr>
      <th>B0008EOEPK</th>
      <td>186</td>
    </tr>
    <tr>
      <th>B0007YR8WW</th>
      <td>185</td>
    </tr>
    <tr>
      <th>B0067GUM2W</th>
      <td>183</td>
    </tr>
    <tr>
      <th>B000O32MLI</th>
      <td>181</td>
    </tr>
    <tr>
      <th>B001IB70JY</th>
      <td>180</td>
    </tr>
    <tr>
      <th>B004Q7AB4I</th>
      <td>175</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_asin_top = df_merged_c.loc[df_merged_c['asin'].isin(['B005LERHD8','B0aa05GYGD7O','B008WYDP1C','B0058XIMMM','B00CKGB85I','B007RD9DS8','B002RADHJC','B000T9VK56','B0000C321X','B0001ZNZJM','B007WNWEFC','B007WA3K4Y','B00012O12A','B007NLX16O','B0008EOEPK','B0007YR8WW','B0067GUM2W','B000O32MLI','B001IB70JY','B004Q7AB4I'])]

```


```python
df_merged_c['pos_neg'] = [1 if x > 3 else 0 for x in df_merged_c.overall]
```


```python
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

```


```python
# !install_package_python3.sh wordcloud
```


```python
import nltk
nltk.download('stopwords')
stops = stopwords.words('english')

```

    [nltk_data] Downloading package stopwords to
    [nltk_data]     /home/yelaganamonikarthik/nltk_data...
    [nltk_data]   Unzipping corpora/stopwords.zip.



```python
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
```


```python
import wordcloud
```


```python
df_merged_c[df_merged_c['pos_neg']==1].review_nonum[1504]
```




    'No BS long sleeve  Fits like it should Soft and great color    and I love the way it hangs'




```python
df_merged_c['review_nonum'] = df_merged_c['reviewText'].str.replace('\d+', '')
df_merged_c['review_nonum'] = df_merged_c['review_nonum'].str.replace(r'[^\w\s]+', '')
df_merged_c['review_nonum'] = df_merged_c['review_nonum'].fillna('')
```


```python
cloud_p = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[df_merged_c['pos_neg']==1].review_nonum))
```


```python
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p);
```


![png](output_109_0.png)



```python
cloud_n = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[df_merged_c['pos_neg']==0].review_nonum))
```


```python
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n);
```


![png](output_111_0.png)



```python
df_merged_c['pos_neg'].value_counts()
```




    1    221597
    0     57080
    Name: pos_neg, dtype: int64




```python
df_merged_c.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reviewerID</th>
      <th>asin</th>
      <th>reviewerName</th>
      <th>helpful</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>unixReviewTime</th>
      <th>reviewTime</th>
      <th>metadataid</th>
      <th>salesrank</th>
      <th>imurl</th>
      <th>categories</th>
      <th>title</th>
      <th>description</th>
      <th>price</th>
      <th>related</th>
      <th>brand</th>
      <th>positive_helpful</th>
      <th>negative_helpful</th>
      <th>total_helpful</th>
      <th>positive_helpful_ratio</th>
      <th>len_reviewText</th>
      <th>category_derived</th>
      <th>len_summary</th>
      <th>check</th>
      <th>len_summary_bins</th>
      <th>len_reviewText_bins</th>
      <th>reviewText_cleaned</th>
      <th>summary_cleaned</th>
      <th>len_reviewText_cleaned</th>
      <th>len_summary_cleaned</th>
      <th>len_summary_cleaned_bins</th>
      <th>len_reviewText_claned_bins</th>
      <th>price_bins</th>
      <th>salesrank_derived</th>
      <th>date</th>
      <th>month</th>
      <th>asin_reviewer</th>
      <th>pos_neg</th>
      <th>review_nonum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>A1KLRMWW2FWPL4</td>
      <td>0000031887</td>
      <td>Amazon Customer "cameramom"</td>
      <td>[0, 0]</td>
      <td>This is a great tutu and at a really great pri...</td>
      <td>5.0</td>
      <td>Great tutu-  not cheaply made</td>
      <td>1297468800</td>
      <td>02 12, 2011</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>172.0</td>
      <td>Others</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisisagreattutuandatareallygreatpriceItdoesnt...</td>
      <td>Greattutunotcheaplymade</td>
      <td>130</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>8547</td>
      <td>2011-02-12</td>
      <td>02</td>
      <td>0000031887A1KLRMWW2FWPL4</td>
      <td>1</td>
      <td>This is a great tutu and at a really great pri...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>A2G5TCU2WDFZ65</td>
      <td>0000031887</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I bought this for my 4 yr old daughter for dan...</td>
      <td>5.0</td>
      <td>Very Cute!!</td>
      <td>1358553600</td>
      <td>01 19, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>306.0</td>
      <td>Others</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtthisformy4yrolddaughterfordanceclassshe...</td>
      <td>VeryCute</td>
      <td>240</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2013-01-19</td>
      <td>01</td>
      <td>0000031887A2G5TCU2WDFZ65</td>
      <td>1</td>
      <td>I bought this for my  yr old daughter for danc...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>A1RLQXYNCMWRWN</td>
      <td>0000031887</td>
      <td>Carola</td>
      <td>[0, 0]</td>
      <td>What can I say... my daughters have it in oran...</td>
      <td>5.0</td>
      <td>I have buy more than one</td>
      <td>1357257600</td>
      <td>01 4, 2013</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>312.0</td>
      <td>Others</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>WhatcanIsaymydaughtershaveitinorangeblackwhite...</td>
      <td>Ihavebuymorethanone</td>
      <td>238</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2013-01-04</td>
      <td>01</td>
      <td>0000031887A1RLQXYNCMWRWN</td>
      <td>1</td>
      <td>What can I say my daughters have it in orange ...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>A8U3FAMSJVHS5</td>
      <td>0000031887</td>
      <td>Caromcg</td>
      <td>[0, 0]</td>
      <td>We bought several tutus at once, and they are ...</td>
      <td>5.0</td>
      <td>Adorable, Sturdy</td>
      <td>1398556800</td>
      <td>04 27, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>405.0</td>
      <td>Others</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Weboughtseveraltutusatonceandtheyaregothighrev...</td>
      <td>AdorableSturdy</td>
      <td>313</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2014-04-27</td>
      <td>04</td>
      <td>0000031887A8U3FAMSJVHS5</td>
      <td>1</td>
      <td>We bought several tutus at once and they are g...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>A3GEOILWLK86XM</td>
      <td>0000031887</td>
      <td>CJ</td>
      <td>[0, 0]</td>
      <td>Thank you Halo Heaven great product for Little...</td>
      <td>5.0</td>
      <td>Grammy's Angels Love it</td>
      <td>1394841600</td>
      <td>03 15, 2014</td>
      <td>44</td>
      <td>{'Sports &amp;amp; Outdoors': 8547}</td>
      <td>http://ecx.images-amazon.com/images/I/314qZjYe...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Girls', 'Cloth...</td>
      <td>Ballet Dress-Up Fairy Tutu</td>
      <td>This adorable basic ballerina tutu is perfect ...</td>
      <td>6.79</td>
      <td>{'also_bought': ['0000031852', '0000031895', '...</td>
      <td>Boutique Cutie</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>453.0</td>
      <td>Others</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>ThankyouHaloHeavengreatproductforLittleGirlsMy...</td>
      <td>GrammysAngelsLoveit</td>
      <td>333</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>8547</td>
      <td>2014-03-15</td>
      <td>03</td>
      <td>0000031887A3GEOILWLK86XM</td>
      <td>1</td>
      <td>Thank you Halo Heaven great product for Little...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c.groupby(['year']).agg({'reviewText':'count'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reviewText</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2003</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2004</th>
      <td>6</td>
    </tr>
    <tr>
      <th>2005</th>
      <td>27</td>
    </tr>
    <tr>
      <th>2006</th>
      <td>115</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>451</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>868</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>1661</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>3456</td>
    </tr>
    <tr>
      <th>2011</th>
      <td>9845</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>32648</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>128510</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>101064</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c.groupby(['year']).reviewerID.nunique()
```




    year
    2003        2
    2004        5
    2005       19
    2006       85
    2007      323
    2008      638
    2009     1203
    2010     2349
    2011     5501
    2012    13921
    2013    31689
    2014    27734
    Name: reviewerID, dtype: int64



#### Reviewers are wring more reviews across years

#### Bigrams before removing stop words


```python
def get_top_n_bigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(2, 2), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]
```


```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
```


```python
df_merged_c['total_review'] = df_merged_c['reviewText'] + ' ' + df_merged_c['summary']
```


```python
df_merged_c['total_review_comwords'] = df_merged_c['total_review'].fillna('')
```


```python
df_merged_c['total_review_nonum'] = df_merged_c['total_review_comwords'].str.replace('\d+', '')
df_merged_c['total_review_nonum'] = df_merged_c['total_review_nonum'].str.replace(r'[^\w\s]+', '')
df_merged_c['total_review_nonum'] = df_merged_c['total_review_nonum'].fillna('')
```


```python
df_merged_c['reviewText_comwords'] = df_merged_c['reviewText'].fillna('')
```

#### Across all the months


```python
common_words_good = get_top_n_bigram(df_merged_c[df_merged_c['pos_neg']==1]['total_review_comwords'], 30)
```


```python
common_words_bad = get_top_n_bigram(df_merged_c[df_merged_c['pos_neg']==0]['total_review_comwords'], 30)
```


```python
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
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_127_1.png)



```python
def get_top_n_trigram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(3, 3), stop_words='english').fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
    return words_freq[:n]
```


```python
common_words_good1 = get_top_n_trigram(df_merged_c[df_merged_c['pos_neg']==1]['total_review_comwords'], 30)
common_words_bad1= get_top_n_trigram(df_merged_c[df_merged_c['pos_neg']==0]['total_review_comwords'], 30)
```


```python
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
```


![png](output_130_0.png)



```python
df_merged_c['month'] = df_merged_c['month'].astype(int)
```


```python
set(df_merged_c['price_bins'])
```




    {'H', 'L', 'M', nan}




```python
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

```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_133_1.png)



```python
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

```


![png](output_134_0.png)



```python
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

```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_135_1.png)



```python
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

```


![png](output_136_0.png)



```python
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

```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_137_1.png)



```python
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

```


![png](output_138_0.png)



```python
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

```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_139_1.png)



```python
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

```


![png](output_140_0.png)


#### Peak Times


```python
common_words_good_em = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['month']>=9) & (df_merged_c['month']<=12) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)

```


```python
common_words_bad_em = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['month']>=9) & (df_merged_c['month']<=12)& (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)

```


```python
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
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_144_1.png)



```python
common_words_good1_em = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1)  & (df_merged_c['month']>=9) & (df_merged_c['month']<=12) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)
common_words_bad1_em= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0)  & (df_merged_c['month']>=9) & (df_merged_c['month']<=12) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)

```


```python
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
```


![png](output_146_0.png)


#### Non peak


```python
common_words_good_sm = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==1) & (df_merged_c['month']>=1) & (df_merged_c['month']<=4) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)
common_words_bad_sm = get_top_n_bigram(df_merged_c[(df_merged_c['pos_neg']==0) & (df_merged_c['month']>=1) & (df_merged_c['month']<=4)& (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)

```


```python
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
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning
    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variables as keyword args: x, y. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.
      FutureWarning



![png](output_149_1.png)



```python
common_words_good1_sm = get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==1)  & (df_merged_c['month']>=1) & (df_merged_c['month']<=4) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)
common_words_bad1_sm= get_top_n_trigram(df_merged_c[(df_merged_c['pos_neg']==0)  & (df_merged_c['month']>=1) & (df_merged_c['month']<=4) & (df_merged_c['year']>= 2006)& (df_merged_c['year']<= 2013)]['reviewText_comwords'], 30)

```


```python
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
```


![png](output_151_0.png)


####  Word Cloud across categories


```python
cloud_p_c = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Clothing') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p_c);

```


![png](output_153_0.png)



```python
cloud_n_c = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Clothing') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n_c);

```


![png](output_154_0.png)



```python
cloud_p_j = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Jewelry') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p_j);

```


![png](output_155_0.png)



```python
cloud_n_j = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Jewelry') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n_j);

```


![png](output_156_0.png)



```python
cloud_p_s = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Shoes') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_p_s);

```


![png](output_157_0.png)



```python
cloud_n_s = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['category_derived']=='Shoes') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_n_s);

```


![png](output_158_0.png)


#### sales rank check 


```python
df_check = df_merged_c[df_merged_c['salesrank_derived']!='']
```


```python
df_check['salesrank_derived'] = df_check['salesrank_derived'].astype(int)
```

    /dsw/snapshots/snapshot_dsw_default_jupyter/python3/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      """Entry point for launching an IPython kernel.



```python
df_check.groupby(['salesrank_derived','category_derived']).agg({'reviewText':'count'}).sort_values(by = 'reviewText',ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reviewText</th>
    </tr>
    <tr>
      <th>salesrank_derived</th>
      <th>category_derived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>214</th>
      <th>Jewelry</th>
      <td>441</td>
    </tr>
    <tr>
      <th>140</th>
      <th>Clothing</th>
      <td>351</td>
    </tr>
    <tr>
      <th>918</th>
      <th>Clothing</th>
      <td>350</td>
    </tr>
    <tr>
      <th>42</th>
      <th>Clothing</th>
      <td>342</td>
    </tr>
    <tr>
      <th>4</th>
      <th>Clothing</th>
      <td>328</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>14466</th>
      <th>Shoes</th>
      <td>5</td>
    </tr>
    <tr>
      <th>95155</th>
      <th>Jewelry</th>
      <td>5</td>
    </tr>
    <tr>
      <th>1413</th>
      <th>Jewelry</th>
      <td>5</td>
    </tr>
    <tr>
      <th>44655</th>
      <th>Clothing</th>
      <td>5</td>
    </tr>
    <tr>
      <th>9455</th>
      <th>Clothing</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>19922 rows × 1 columns</p>
</div>




```python
df_check.groupby(['asin','salesrank_derived']).agg({'reviewText':'count'}).sort_values(by = 'reviewText',ascending=False).head(100)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>reviewText</th>
    </tr>
    <tr>
      <th>asin</th>
      <th>salesrank_derived</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>B005LERHD8</th>
      <th>214</th>
      <td>441</td>
    </tr>
    <tr>
      <th>B005GYGD7O</th>
      <th>42</th>
      <td>286</td>
    </tr>
    <tr>
      <th>B008WYDP1C</th>
      <th>589</th>
      <td>249</td>
    </tr>
    <tr>
      <th>B0058XIMMM</th>
      <th>13</th>
      <td>241</td>
    </tr>
    <tr>
      <th>B00CKGB85I</th>
      <th>43</th>
      <td>225</td>
    </tr>
    <tr>
      <th>B007RD9DS8</th>
      <th>346</th>
      <td>217</td>
    </tr>
    <tr>
      <th>B002RADHJC</th>
      <th>19</th>
      <td>211</td>
    </tr>
    <tr>
      <th>B0000C321X</th>
      <th>5</th>
      <td>205</td>
    </tr>
    <tr>
      <th>B007WNWEFC</th>
      <th>314</th>
      <td>197</td>
    </tr>
    <tr>
      <th>B0001ZNZJM</th>
      <th>9</th>
      <td>197</td>
    </tr>
    <tr>
      <th>B007WA3K4Y</th>
      <th>1630</th>
      <td>191</td>
    </tr>
    <tr>
      <th>B00012O12A</th>
      <th>4</th>
      <td>189</td>
    </tr>
    <tr>
      <th>B007NLX16O</th>
      <th>848</th>
      <td>189</td>
    </tr>
    <tr>
      <th>B0008EOEPK</th>
      <th>8462</th>
      <td>186</td>
    </tr>
    <tr>
      <th>B0007YR8WW</th>
      <th>25</th>
      <td>185</td>
    </tr>
    <tr>
      <th>B0067GUM2W</th>
      <th>698</th>
      <td>183</td>
    </tr>
    <tr>
      <th>B000O32MLI</th>
      <th>5</th>
      <td>181</td>
    </tr>
    <tr>
      <th>B001IB70JY</th>
      <th>28453</th>
      <td>180</td>
    </tr>
    <tr>
      <th>B004Q7AB4I</th>
      <th>8</th>
      <td>175</td>
    </tr>
    <tr>
      <th>B003NX87U6</th>
      <th>228</th>
      <td>168</td>
    </tr>
    <tr>
      <th>B006PGGJOE</th>
      <th>80</th>
      <td>168</td>
    </tr>
    <tr>
      <th>B002PHLVJA</th>
      <th>11563</th>
      <td>162</td>
    </tr>
    <tr>
      <th>B008KK0ZJ8</th>
      <th>18</th>
      <td>161</td>
    </tr>
    <tr>
      <th>B0083S18LQ</th>
      <th>2490</th>
      <td>161</td>
    </tr>
    <tr>
      <th>B005UVM368</th>
      <th>3116</th>
      <td>158</td>
    </tr>
    <tr>
      <th>B0007YVP1W</th>
      <th>37</th>
      <td>158</td>
    </tr>
    <tr>
      <th>B000KEG4V0</th>
      <th>140</th>
      <td>153</td>
    </tr>
    <tr>
      <th>B00DNQIIE8</th>
      <th>607</th>
      <td>153</td>
    </tr>
    <tr>
      <th>B004YM2FV2</th>
      <th>4</th>
      <td>151</td>
    </tr>
    <tr>
      <th>B008NCYALM</th>
      <th>918</th>
      <td>148</td>
    </tr>
    <tr>
      <th>B003XDVUEQ</th>
      <th>46</th>
      <td>148</td>
    </tr>
    <tr>
      <th>B0007CKMA4</th>
      <th>67</th>
      <td>148</td>
    </tr>
    <tr>
      <th>B008X0EW44</th>
      <th>1871</th>
      <td>143</td>
    </tr>
    <tr>
      <th>B00DMWQOYY</th>
      <th>2020</th>
      <td>142</td>
    </tr>
    <tr>
      <th>B0078FXHNM</th>
      <th>586</th>
      <td>142</td>
    </tr>
    <tr>
      <th>B000XDDERK</th>
      <th>3</th>
      <td>141</td>
    </tr>
    <tr>
      <th>B002KMI7OC</th>
      <th>15</th>
      <td>140</td>
    </tr>
    <tr>
      <th>B000J6ZYL0</th>
      <th>12</th>
      <td>139</td>
    </tr>
    <tr>
      <th>B001Q5QLP6</th>
      <th>7</th>
      <td>138</td>
    </tr>
    <tr>
      <th>B003DNR2HK</th>
      <th>1550</th>
      <td>137</td>
    </tr>
    <tr>
      <th>B0074T7TY0</th>
      <th>773</th>
      <td>137</td>
    </tr>
    <tr>
      <th>B00550PLV8</th>
      <th>162</th>
      <td>137</td>
    </tr>
    <tr>
      <th>B007WAU1VY</th>
      <th>2366</th>
      <td>136</td>
    </tr>
    <tr>
      <th>B0008172S4</th>
      <th>781</th>
      <td>135</td>
    </tr>
    <tr>
      <th>B00CIBCJ62</th>
      <th>735</th>
      <td>134</td>
    </tr>
    <tr>
      <th>B0068VM5T4</th>
      <th>22939</th>
      <td>134</td>
    </tr>
    <tr>
      <th>B000FBO0DM</th>
      <th>4</th>
      <td>133</td>
    </tr>
    <tr>
      <th>B000QW6LE6</th>
      <th>23</th>
      <td>131</td>
    </tr>
    <tr>
      <th>B0002TOZ1E</th>
      <th>162</th>
      <td>127</td>
    </tr>
    <tr>
      <th>B005CSNTJY</th>
      <th>284</th>
      <td>127</td>
    </tr>
    <tr>
      <th>B000DZUGOM</th>
      <th>2</th>
      <td>126</td>
    </tr>
    <tr>
      <th>B004R1II48</th>
      <th>26</th>
      <td>126</td>
    </tr>
    <tr>
      <th>B00CN47GXA</th>
      <th>918</th>
      <td>123</td>
    </tr>
    <tr>
      <th>B00D1MR8YU</th>
      <th>83</th>
      <td>123</td>
    </tr>
    <tr>
      <th>B001HEF6W0</th>
      <th>114</th>
      <td>121</td>
    </tr>
    <tr>
      <th>B0013KDS96</th>
      <th>68</th>
      <td>119</td>
    </tr>
    <tr>
      <th>B0000ANHST</th>
      <th>11</th>
      <td>117</td>
    </tr>
    <tr>
      <th>B007WAEBPQ</th>
      <th>2337</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B0053XF2U2</th>
      <th>140</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B0051U15E4</th>
      <th>191</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B008RUOCJU</th>
      <th>246768</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B00DQYNS3I</th>
      <th>1</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B0009F0Z38</th>
      <th>307</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B001AOZVSQ</th>
      <th>166</th>
      <td>114</td>
    </tr>
    <tr>
      <th>B0026P45QW</th>
      <th>110</th>
      <td>113</td>
    </tr>
    <tr>
      <th>B0007YXTOS</th>
      <th>81</th>
      <td>112</td>
    </tr>
    <tr>
      <th>B0006LMBJ6</th>
      <th>8</th>
      <td>112</td>
    </tr>
    <tr>
      <th>B00BNB3A0W</th>
      <th>4180</th>
      <td>111</td>
    </tr>
    <tr>
      <th>B000EIJG0I</th>
      <th>100</th>
      <td>111</td>
    </tr>
    <tr>
      <th>B000072UMJ</th>
      <th>10</th>
      <td>111</td>
    </tr>
    <tr>
      <th>B000FH4JJQ</th>
      <th>41</th>
      <td>110</td>
    </tr>
    <tr>
      <th>B0012QM8IS</th>
      <th>24518</th>
      <td>109</td>
    </tr>
    <tr>
      <th>B0076R6KY0</th>
      <th>244</th>
      <td>109</td>
    </tr>
    <tr>
      <th>B0081IZ3UA</th>
      <th>33</th>
      <td>106</td>
    </tr>
    <tr>
      <th>B0031U0PO2</th>
      <th>116</th>
      <td>105</td>
    </tr>
    <tr>
      <th>B001188FZC</th>
      <th>616</th>
      <td>105</td>
    </tr>
    <tr>
      <th>B00DMWQK0W</th>
      <th>552</th>
      <td>104</td>
    </tr>
    <tr>
      <th>B004M6XUI2</th>
      <th>97</th>
      <td>103</td>
    </tr>
    <tr>
      <th>B009DNWFD0</th>
      <th>11837</th>
      <td>103</td>
    </tr>
    <tr>
      <th>B002APTA9K</th>
      <th>83</th>
      <td>102</td>
    </tr>
    <tr>
      <th>B0007QCOTM</th>
      <th>28</th>
      <td>102</td>
    </tr>
    <tr>
      <th>B0051D7GF8</th>
      <th>330</th>
      <td>102</td>
    </tr>
    <tr>
      <th>B003DNR4XC</th>
      <th>1278</th>
      <td>102</td>
    </tr>
    <tr>
      <th>B009ZDEXQK</th>
      <th>44</th>
      <td>102</td>
    </tr>
    <tr>
      <th>B006SCSOOS</th>
      <th>1022</th>
      <td>102</td>
    </tr>
    <tr>
      <th>B0009B3IN6</th>
      <th>23</th>
      <td>101</td>
    </tr>
    <tr>
      <th>B003YBHF82</th>
      <th>20</th>
      <td>100</td>
    </tr>
    <tr>
      <th>B0012M0XSE</th>
      <th>119</th>
      <td>99</td>
    </tr>
    <tr>
      <th>B000MXIMHI</th>
      <th>18</th>
      <td>99</td>
    </tr>
    <tr>
      <th>B000KD44G8</th>
      <th>211</th>
      <td>98</td>
    </tr>
    <tr>
      <th>B007DLVLAW</th>
      <th>5</th>
      <td>97</td>
    </tr>
    <tr>
      <th>B000KGOHLM</th>
      <th>752</th>
      <td>96</td>
    </tr>
    <tr>
      <th>B0011D2FL2</th>
      <th>68</th>
      <td>96</td>
    </tr>
    <tr>
      <th>B000EX15NY</th>
      <th>143</th>
      <td>95</td>
    </tr>
    <tr>
      <th>B0018OM1TU</th>
      <th>38</th>
      <td>94</td>
    </tr>
    <tr>
      <th>B0019MPRJW</th>
      <th>51</th>
      <td>94</td>
    </tr>
    <tr>
      <th>B00AAJPBH8</th>
      <th>16</th>
      <td>93</td>
    </tr>
    <tr>
      <th>B000MQWYM4</th>
      <th>19</th>
      <td>93</td>
    </tr>
    <tr>
      <th>B002K6F79G</th>
      <th>30</th>
      <td>93</td>
    </tr>
    <tr>
      <th>B00DM05D5C</th>
      <th>1000</th>
      <td>92</td>
    </tr>
  </tbody>
</table>
</div>




```python
set(df_check[df_check['salesrank_derived']==5]['asin'])
```




    {'B0000C321X',
     'B0007QCQGI',
     'B000O32MLI',
     'B007DLVLAW',
     'B007DLVLC0',
     'B007DLVLDY',
     'B007DM6S72'}




```python
set(df_check[df_check['asin']=='B0007QCQGI']['date'])
```




    {'2006-03-09',
     '2008-12-06',
     '2009-01-08',
     '2009-08-19',
     '2010-01-21',
     '2010-10-09',
     '2010-11-18',
     '2011-07-09',
     '2011-12-06',
     '2012-07-07',
     '2012-07-19',
     '2012-07-28',
     '2012-07-30',
     '2012-08-12',
     '2012-08-19',
     '2012-09-28',
     '2012-11-09',
     '2012-11-20',
     '2012-12-12',
     '2012-12-17',
     '2012-12-28',
     '2013-01-21',
     '2013-01-22',
     '2013-03-30',
     '2013-04-05',
     '2013-04-10',
     '2013-04-22',
     '2013-05-09',
     '2013-05-26',
     '2013-06-20',
     '2013-07-10',
     '2013-07-17',
     '2013-07-28',
     '2013-08-20',
     '2013-08-21',
     '2013-08-25',
     '2013-08-30',
     '2013-09-06',
     '2013-09-10',
     '2013-09-17',
     '2013-10-05',
     '2013-10-14',
     '2013-10-18',
     '2013-10-22',
     '2013-10-28',
     '2013-10-30',
     '2013-11-06',
     '2013-11-08',
     '2013-11-16',
     '2013-11-18',
     '2013-12-16',
     '2013-12-30',
     '2014-01-04',
     '2014-01-07',
     '2014-01-10',
     '2014-01-25',
     '2014-01-27',
     '2014-02-09',
     '2014-02-18',
     '2014-02-21',
     '2014-02-26',
     '2014-02-27',
     '2014-03-04',
     '2014-03-07',
     '2014-03-12',
     '2014-03-20',
     '2014-03-24',
     '2014-04-03',
     '2014-04-05',
     '2014-04-30',
     '2014-05-09',
     '2014-05-26',
     '2014-06-18',
     '2014-07-01',
     '2014-07-02'}




```python
set(df_check[df_check['asin']=='B0000C321X']['date'])
```




    {'2007-03-11',
     '2007-05-13',
     '2009-01-08',
     '2009-01-12',
     '2009-09-02',
     '2009-12-03',
     '2009-12-21',
     '2010-01-26',
     '2010-01-31',
     '2010-02-08',
     '2010-03-16',
     '2010-10-30',
     '2010-11-26',
     '2011-01-06',
     '2011-01-18',
     '2011-02-16',
     '2011-02-22',
     '2011-02-26',
     '2011-04-08',
     '2011-05-01',
     '2011-05-22',
     '2011-05-30',
     '2011-07-24',
     '2011-08-19',
     '2011-08-28',
     '2011-10-08',
     '2011-11-15',
     '2011-12-03',
     '2011-12-11',
     '2011-12-29',
     '2012-01-16',
     '2012-01-17',
     '2012-02-20',
     '2012-04-12',
     '2012-05-05',
     '2012-05-07',
     '2012-06-02',
     '2012-07-20',
     '2012-07-23',
     '2012-08-11',
     '2012-09-18',
     '2012-09-29',
     '2012-10-05',
     '2012-10-16',
     '2012-10-22',
     '2012-10-30',
     '2012-11-12',
     '2012-11-19',
     '2012-11-26',
     '2012-11-30',
     '2012-12-02',
     '2012-12-03',
     '2012-12-04',
     '2012-12-08',
     '2012-12-13',
     '2012-12-19',
     '2012-12-26',
     '2012-12-28',
     '2013-01-02',
     '2013-01-03',
     '2013-01-06',
     '2013-01-07',
     '2013-01-08',
     '2013-01-18',
     '2013-01-19',
     '2013-01-22',
     '2013-01-24',
     '2013-01-25',
     '2013-01-26',
     '2013-02-01',
     '2013-02-14',
     '2013-02-18',
     '2013-02-19',
     '2013-02-22',
     '2013-03-02',
     '2013-03-15',
     '2013-03-17',
     '2013-03-19',
     '2013-04-02',
     '2013-04-09',
     '2013-04-21',
     '2013-04-26',
     '2013-05-04',
     '2013-06-03',
     '2013-06-10',
     '2013-06-12',
     '2013-06-17',
     '2013-07-03',
     '2013-07-06',
     '2013-07-09',
     '2013-07-18',
     '2013-07-28',
     '2013-08-05',
     '2013-08-13',
     '2013-08-21',
     '2013-08-29',
     '2013-08-31',
     '2013-09-04',
     '2013-09-08',
     '2013-09-14',
     '2013-09-15',
     '2013-09-20',
     '2013-09-24',
     '2013-10-01',
     '2013-10-05',
     '2013-10-16',
     '2013-10-24',
     '2013-11-02',
     '2013-11-03',
     '2013-11-05',
     '2013-11-06',
     '2013-11-07',
     '2013-11-10',
     '2013-11-13',
     '2013-11-25',
     '2013-12-03',
     '2013-12-04',
     '2013-12-07',
     '2013-12-11',
     '2013-12-14',
     '2013-12-15',
     '2013-12-19',
     '2013-12-23',
     '2013-12-24',
     '2013-12-26',
     '2014-01-01',
     '2014-01-02',
     '2014-01-07',
     '2014-01-09',
     '2014-01-13',
     '2014-01-14',
     '2014-01-15',
     '2014-01-16',
     '2014-01-20',
     '2014-01-27',
     '2014-01-30',
     '2014-02-01',
     '2014-02-10',
     '2014-02-18',
     '2014-02-20',
     '2014-02-21',
     '2014-02-23',
     '2014-02-25',
     '2014-03-02',
     '2014-03-03',
     '2014-03-06',
     '2014-03-08',
     '2014-03-13',
     '2014-03-17',
     '2014-03-21',
     '2014-03-22',
     '2014-03-25',
     '2014-03-27',
     '2014-03-28',
     '2014-04-01',
     '2014-04-02',
     '2014-04-05',
     '2014-04-07',
     '2014-04-13',
     '2014-04-14',
     '2014-04-19',
     '2014-04-28',
     '2014-05-02',
     '2014-05-04',
     '2014-05-06',
     '2014-05-09',
     '2014-05-12',
     '2014-05-13',
     '2014-05-16',
     '2014-05-17',
     '2014-05-31',
     '2014-06-01',
     '2014-06-02',
     '2014-06-17',
     '2014-06-20',
     '2014-06-23',
     '2014-06-30',
     '2014-07-01',
     '2014-07-04',
     '2014-07-09',
     '2014-07-11',
     '2014-07-12'}




```python
set(df_check[df_check['asin']=='B000O32MLI']['date'])
```




    {'2008-04-12',
     '2008-05-19',
     '2008-07-12',
     '2008-08-17',
     '2008-11-02',
     '2008-11-16',
     '2009-01-18',
     '2009-04-08',
     '2009-04-25',
     '2009-09-17',
     '2009-09-29',
     '2010-06-29',
     '2010-07-10',
     '2010-08-25',
     '2010-11-10',
     '2010-12-21',
     '2011-01-20',
     '2011-02-12',
     '2011-02-13',
     '2011-03-07',
     '2011-04-18',
     '2011-05-13',
     '2011-06-19',
     '2011-06-25',
     '2011-07-01',
     '2011-08-11',
     '2011-08-25',
     '2011-10-06',
     '2011-10-13',
     '2011-10-19',
     '2011-12-13',
     '2011-12-31',
     '2012-01-15',
     '2012-01-18',
     '2012-03-17',
     '2012-03-22',
     '2012-03-26',
     '2012-04-17',
     '2012-04-27',
     '2012-05-07',
     '2012-05-16',
     '2012-05-17',
     '2012-05-24',
     '2012-06-03',
     '2012-06-16',
     '2012-06-18',
     '2012-06-22',
     '2012-07-09',
     '2012-07-10',
     '2012-07-25',
     '2012-08-15',
     '2012-08-29',
     '2012-10-06',
     '2012-10-07',
     '2012-10-14',
     '2012-10-16',
     '2012-11-03',
     '2012-11-28',
     '2012-11-30',
     '2012-12-04',
     '2013-01-03',
     '2013-01-04',
     '2013-01-05',
     '2013-01-10',
     '2013-01-16',
     '2013-01-23',
     '2013-02-06',
     '2013-02-11',
     '2013-02-18',
     '2013-02-21',
     '2013-02-22',
     '2013-02-27',
     '2013-03-13',
     '2013-03-15',
     '2013-03-17',
     '2013-03-19',
     '2013-03-26',
     '2013-04-01',
     '2013-04-10',
     '2013-04-16',
     '2013-04-18',
     '2013-04-21',
     '2013-04-25',
     '2013-05-03',
     '2013-05-10',
     '2013-05-17',
     '2013-06-02',
     '2013-06-13',
     '2013-06-17',
     '2013-06-20',
     '2013-06-21',
     '2013-06-22',
     '2013-06-25',
     '2013-07-04',
     '2013-07-05',
     '2013-07-14',
     '2013-07-18',
     '2013-07-19',
     '2013-07-22',
     '2013-07-23',
     '2013-07-25',
     '2013-08-02',
     '2013-08-10',
     '2013-08-30',
     '2013-09-04',
     '2013-09-08',
     '2013-09-12',
     '2013-09-16',
     '2013-09-17',
     '2013-09-24',
     '2013-09-26',
     '2013-10-02',
     '2013-10-03',
     '2013-10-17',
     '2013-10-26',
     '2013-11-10',
     '2013-11-11',
     '2013-11-12',
     '2013-11-15',
     '2013-11-20',
     '2013-11-21',
     '2013-11-25',
     '2013-11-28',
     '2013-12-01',
     '2013-12-03',
     '2013-12-21',
     '2014-01-01',
     '2014-01-06',
     '2014-01-08',
     '2014-01-29',
     '2014-02-03',
     '2014-02-07',
     '2014-02-13',
     '2014-02-16',
     '2014-02-17',
     '2014-02-18',
     '2014-02-22',
     '2014-02-25',
     '2014-02-26',
     '2014-03-06',
     '2014-03-10',
     '2014-03-14',
     '2014-03-19',
     '2014-03-27',
     '2014-03-31',
     '2014-04-05',
     '2014-04-08',
     '2014-04-11',
     '2014-04-13',
     '2014-04-16',
     '2014-05-09',
     '2014-05-11',
     '2014-05-28',
     '2014-05-29',
     '2014-06-03',
     '2014-06-05',
     '2014-06-08',
     '2014-06-11',
     '2014-06-13',
     '2014-06-14',
     '2014-06-18',
     '2014-06-19',
     '2014-06-25',
     '2014-07-03',
     '2014-07-04'}




```python
set(df_check[df_check['category_derived']=='Jewelry']['salesrank_derived'])
```




    {1,
     2,
     3,
     65542,
     7,
     8,
     49161,
     65546,
     11,
     9,
     65549,
     13,
     15,
     57359,
     16,
     24594,
     17,
     32785,
     21,
     14,
     23,
     40977,
     18,
     24602,
     26,
     28,
     20,
     30,
     65567,
     33,
     34,
     35,
     36,
     65575,
     39,
     41,
     24618,
     41004,
     45,
     46,
     47,
     49,
     51,
     52,
     32821,
     53,
     10,
     58,
     60,
     61,
     62,
     49216,
     8256,
     319554,
     49219,
     66,
     68,
     71,
     72,
     73,
     75,
     76,
     77,
     57422,
     80,
     81,
     82,
     24657,
     84,
     65621,
     24662,
     85,
     88,
     49240,
     90,
     24668,
     24672,
     99,
     100,
     104,
     105,
     49258,
     16488,
     110,
     65649,
     114,
     116,
     117,
     118,
     57462,
     119,
     32889,
     121,
     24697,
     124,
     127,
     128,
     130,
     24708,
     133,
     135,
     136,
     137,
     138,
     139,
     140,
     141,
     142,
     144,
     8338,
     146,
     24725,
     149,
     8342,
     150,
     152,
     155,
     156,
     49309,
     157,
     159,
     160,
     73889,
     162,
     165,
     166,
     167,
     168,
     171,
     175,
     24752,
     177,
     123059,
     114868,
     32952,
     24760,
     186,
     184,
     65724,
     8381,
     189,
     191,
     193,
     194,
     195,
     197,
     8390,
     201,
     57546,
     203,
     65741,
     207,
     8400,
     211,
     213,
     214,
     215,
     218,
     49374,
     222,
     224,
     24802,
     227,
     24804,
     229,
     230,
     231,
     16616,
     233,
     234,
     238,
     16624,
     240,
     242,
     57586,
     244,
     49392,
     16632,
     249,
     57594,
     250,
     253,
     106753,
     33028,
     264,
     265,
     268,
     269,
     271,
     272,
     8464,
     8467,
     282,
     284,
     286,
     287,
     41248,
     24865,
     291,
     8484,
     41253,
     292,
     295,
     57641,
     65834,
     49451,
     299,
     297,
     352558,
     8497,
     309,
     310,
     311,
     33080,
     312,
     314,
     313,
     316,
     317,
     8204,
     320,
     49472,
     322,
     323,
     324,
     82245,
     327,
     24903,
     16713,
     330,
     332,
     74060,
     336,
     338,
     339,
     41300,
     341,
     342,
     343,
     344,
     346,
     348,
     349,
     350,
     351,
     353,
     33124,
     357,
     361,
     364,
     365,
     16750,
     367,
     370,
     754034,
     371,
     372,
     374,
     375,
     377,
     378,
     41340,
     381,
     382,
     386,
     387,
     41347,
     16774,
     391,
     394,
     8586,
     400,
     402,
     403,
     406,
     408,
     409,
     16794,
     8605,
     123294,
     415,
     24991,
     74144,
     418,
     422,
     49575,
     423,
     49577,
     428,
     429,
     25006,
     430,
     432,
     433,
     434,
     435,
     437,
     438,
     439,
     440,
     16830,
     8641,
     450,
     41413,
     454,
     25030,
     456,
     458,
     473,
     475,
     16860,
     476,
     16859,
     480,
     481,
     33250,
     483,
     8677,
     485,
     488,
     489,
     491,
     8683,
     492,
     494,
     16878,
     500,
     8692,
     501,
     33271,
     8696,
     504,
     507,
     508,
     509,
     511,
     513,
     33285,
     41483,
     524,
     525,
     526,
     33295,
     16912,
     523,
     41491,
     16915,
     90645,
     534,
     535,
     536,
     538,
     25117,
     541,
     8740,
     98853,
     550,
     551,
     16936,
     552,
     555,
     90667,
     558,
     561,
     33330,
     16947,
     557620,
     567,
     574,
     575,
     8767,
     579,
     582,
     585,
     586,
     8779,
     591,
     8783,
     594,
     596,
     8793,
     16989,
     607,
     611,
     8804,
     615,
     616,
     617,
     618,
     621,
     622,
     623,
     41584,
     8816,
     626,
     628,
     631,
     633,
     637,
     638,
     639,
     641,
     644,
     33416,
     648,
     25229,
     653,
     25232,
     658,
     33428,
     8864,
     41632,
     17060,
     677,
     676,
     680,
     688,
     690,
     691,
     692,
     693,
     697,
     698,
     49851,
     702,
     704,
     706,
     8899,
     713,
     41677,
     720,
     58068,
     724,
     8918,
     734,
     17121,
     17122,
     739,
     741,
     743,
     33513,
     74475,
     748,
     749,
     750,
     751,
     752,
     747,
     761,
     764,
     41727,
     58111,
     17152,
     768,
     770,
     772,
     58117,
     774,
     771,
     33547,
     779,
     781,
     49935,
     785,
     786,
     791,
     792,
     795,
     17181,
     798,
     8992,
     801,
     802,
     66342,
     808,
     9008,
     41777,
     58165,
     25399,
     33592,
     825,
     827,
     829,
     831,
     832,
     9026,
     9029,
     838,
     839,
     841,
     41803,
     846,
     848,
     25425,
     849,
     25429,
     854,
     855,
     33632,
     50024,
     873,
     876,
     877,
     878,
     9077,
     885,
     33656,
     890,
     17274,
     893,
     894,
     897,
     82818,
     903,
     906,
     907,
     58252,
     909,
     66446,
     911,
     915,
     916,
     917,
     918,
     33685,
     25496,
     921,
     920,
     926,
     928,
     9120,
     74659,
     935,
     939,
     941,
     946,
     9139,
     947,
     99253,
     949,
     951,
     952,
     25522,
     9146,
     955,
     58301,
     41917,
     959,
     964,
     74695,
     967,
     969,
     970,
     9167,
     50130,
     66515,
     979,
     41942,
     982,
     983,
     9174,
     9180,
     988,
     990,
     995,
     996,
     997,
     66534,
     1000,
     1001,
     1002,
     1007,
     1013,
     1018,
     1019,
     66555,
     1021,
     1024,
     41984,
     1030,
     66568,
     9225,
     50184,
     1038,
     1042,
     9235,
     1043,
     42005,
     1046,
     1045,
     1057,
     1064,
     1066,
     1067,
     1068,
     9258,
     33838,
     1071,
     1072,
     9269,
     1078,
     1080,
     17466,
     50240,
     1089,
     1092,
     99398,
     1095,
     17482,
     9292,
     42061,
     25678,
     1103,
     50257,
     25684,
     1109,
     1108,
     25688,
     17499,
     1117,
     1119,
     17504,
     1121,
     17506,
     1123,
     25705,
     1131,
     1134,
     1135,
     1136,
     25713,
     1137,
     1144,
     42104,
     17530,
     1146,
     58488,
     66687,
     1152,
     58496,
     1153,
     1156,
     50311,
     25741,
     1166,
     25748,
     1177,
     9371,
     1180,
     1181,
     1185,
     17570,
     1187,
     1188,
     9382,
     1192,
     17579,
     1195,
     1197,
     1198,
     1202,
     1206,
     1207,
     1209,
     1210,
     1211,
     25785,
     1213,
     197822,
     25797,
     1223,
     1227,
     1229,
     42194,
     1234,
     1237,
     124117,
     1240,
     42201,
     42203,
     1244,
     1247,
     1251,
     1255,
     1256,
     42215,
     74986,
     1264,
     34035,
     1269,
     9461,
     1271,
     25849,
     1277,
     1278,
     50432,
     1281,
     1283,
     34051,
     1285,
     9479,
     1288,
     25869,
     66830,
     1293,
     1296,
     1294,
     42258,
     50451,
     1300,
     1298,
     17687,
     1307,
     34077,
     17695,
     1312,
     17697,
     66850,
     1317,
     1320,
     1322,
     75051,
     9517,
     1327,
     9521,
     1331,
     1335,
     1336,
     17722,
     1339,
     83261,
     1341,
     1346,
     1349,
     9543,
     9545,
     1356,
     17747,
     1364,
     1367,
     50528,
     1378,
     1381,
     1382,
     42345,
     1387,
     9583,
     34160,
     83313,
     1394,
     1395,
     25971,
     9589,
     1392,
     1399,
     1400,
     9592,
     42359,
     1403,
     1406,
     1409,
     1412,
     17797,
     1413,
     25988,
     25998,
     1423,
     1428,
     42391,
     58780,
     1436,
     1438,
     1439,
     1441,
     50593,
     26021,
     1448,
     1450,
     34219,
     1451,
     1453,
     1455,
     1458,
     9653,
     1463,
     17852,
     1471,
     1478,
     1485,
     1486,
     26064,
     1489,
     26068,
     1492,
     67039,
     1506,
     1508,
     1510,
     26088,
     1515,
     42481,
     1522,
     1524,
     1533,
     1536,
     9731,
     1542,
     58890,
     42507,
     1547,
     1548,
     1550,
     1551,
     1553,
     1557,
     1560,
     1562,
     9757,
     58909,
     58910,
     1569,
     1574,
     1576,
     1580,
     1582,
     1583,
     1584,
     1586,
     1589,
     1591,
     1596,
     1597,
     50750,
     1603,
     1608,
     1617,
     18001,
     1620,
     9815,
     1628,
     26205,
     1631,
     26208,
     9825,
     1634,
     9828,
     1637,
     1640,
     1641,
     9833,
     1643,
     67177,
     75378,
     1653,
     42618,
     67198,
     9855,
     1668,
     1669,
     9862,
     345732,
     1673,
     1674,
     34453,
     9880,
     1693,
     1694,
     1695,
     18086,
     1703,
     18088,
     1707,
     1709,
     1710,
     1722,
     9915,
     1724,
     1723,
     59070,
     26305,
     26309,
     18118,
     1744,
     83669,
     67287,
     83675,
     1756,
     1759,
     1760,
     91876,
     9965,
     1779,
     1780,
     1783,
     1784,
     1786,
     1790,
     1795,
     9990,
     1800,
     1801,
     1803,
     1805,
     34575,
     1808,
     26385,
     1811,
     10007,
     10008,
     34587,
     1820,
     1821,
     34590,
     1825,
     67366,
     1831,
     18214,
     67377,
     1844,
     1850,
     1851,
     10045,
     1859,
     1864,
     1867,
     42829,
     51022,
     42832,
     1872,
     34650,
     1883,
     10076,
     26463,
     10084,
     1895,
     1898,
     1901,
     1907,
     59253,
     1910,
     75641,
     1915,
     1916,
     1917,
     75645,
     1919,
     10108,
     1921,
     92033,
     18299,
     10107,
     1926,
     51080,
     10121,
     26505,
     1932,
     51085,
     1934,
     1933,
     1939,
     59290,
     1949,
     92063,
     34725,
     10150,
     1961,
     18346,
     1966,
     1968,
     10161,
     18354,
     1972,
     1973,
     1974,
     42938,
     18363,
     1979,
     1980,
     1983,
     42943,
     1985,
     26565,
     1991,
     1992,
     42951,
     1994,
     1996,
     10189,
     18382,
     59345,
     26578,
     2002,
     2004,
     2006,
     42966,
     2008,
     2009,
     10199,
     2012,
     51166,
     ...}




```python
set(df_check[df_check['category_derived']=='Clothing']['salesrank_derived'])
```




    {32769,
     4,
     5,
     6,
     7,
     8,
     10,
     11,
     12,
     13,
     14,
     16,
     17,
     18,
     19,
     21,
     22,
     98327,
     24,
     25,
     23,
     27,
     26,
     32795,
     30,
     31,
     32800,
     32,
     34,
     37,
     38,
     39,
     40,
     42,
     43,
     44,
     131116,
     32815,
     48,
     50,
     32819,
     32820,
     53,
     55,
     32824,
     163897,
     57,
     58,
     60,
     61,
     62,
     196673,
     65,
     67,
     32836,
     68,
     229443,
     66,
     72,
     294980,
     70,
     75,
     32845,
     393295,
     80,
     81,
     82,
     83,
     84,
     32855,
     196696,
     87,
     32857,
     90,
     96,
     97,
     98,
     99,
     103,
     65640,
     262250,
     107,
     32875,
     109,
     110,
     113,
     32881,
     115,
     116,
     32883,
     32886,
     119,
     120,
     124,
     125,
     126,
     130,
     131,
     132,
     65670,
     134,
     196744,
     32905,
     138,
     139,
     140,
     137,
     142,
     143,
     144,
     65676,
     146,
     147,
     98449,
     149,
     141,
     151,
     152,
     153,
     154,
     155,
     196759,
     32921,
     161,
     162,
     163,
     166,
     196776,
     170,
     172,
     173,
     32942,
     175,
     196784,
     229554,
     178,
     180,
     181,
     32950,
     183,
     184,
     185,
     229558,
     182,
     191,
     192,
     196801,
     194,
     195,
     197,
     200,
     202,
     203,
     98510,
     208,
     209,
     211,
     212,
     213,
     215,
     218,
     219,
     32989,
     223,
     224,
     225,
     32995,
     228,
     227,
     231,
     3178727,
     32999,
     236,
     238,
     239,
     164079,
     241,
     242,
     131313,
     244,
     245,
     250,
     251,
     252,
     253,
     256,
     257,
     33027,
     259,
     295171,
     262,
     263,
     721158,
     266,
     267,
     164108,
     269,
     272,
     273,
     275,
     282,
     98587,
     284,
     33053,
     285,
     287,
     289,
     290,
     291,
     293,
     294,
     296,
     297,
     300,
     301,
     303,
     304,
     305,
     33074,
     307,
     33076,
     309,
     310,
     229684,
     312,
     306,
     33079,
     315,
     316,
     318,
     319,
     262465,
     321,
     323,
     33092,
     324,
     229702,
     327,
     328,
     329,
     330,
     331,
     332,
     229709,
     334,
     326,
     335,
     338,
     339,
     340,
     341,
     342,
     343,
     65881,
     347,
     348,
     349,
     351,
     352,
     353,
     354,
     164196,
     357,
     360,
     362,
     363,
     65901,
     368,
     369,
     65906,
     371,
     374,
     375,
     376,
     377,
     378,
     295292,
     852349,
     381,
     382,
     384,
     385,
     386,
     391,
     392,
     393,
     394,
     396,
     397,
     131470,
     131471,
     400,
     164237,
     65938,
     403,
     98708,
     402,
     406,
     407,
     164240,
     409,
     410,
     411,
     33179,
     405,
     414,
     415,
     416,
     197026,
     419,
     418,
     421,
     422,
     423,
     424,
     33193,
     229802,
     420,
     98732,
     431,
     432,
     433,
     459188,
     438,
     439,
     440,
     33206,
     197054,
     448,
     229825,
     450,
     197058,
     452,
     453,
     456,
     131529,
     458,
     457,
     460,
     461,
     462,
     463,
     33232,
     465,
     464,
     470,
     475,
     476,
     477,
     33246,
     479,
     481,
     484,
     487,
     488,
     490,
     493,
     494,
     495,
     496,
     497,
     498,
     164337,
     500,
     66033,
     33270,
     503,
     504,
     505,
     506,
     507,
     508,
     33275,
     510,
     33277,
     509,
     66048,
     514,
     33284,
     518,
     519,
     521,
     523,
     526,
     527,
     530,
     531,
     534,
     535,
     536,
     538,
     33307,
     540,
     33311,
     546,
     547,
     33315,
     66082,
     550,
     551,
     66087,
     553,
     554,
     548,
     524844,
     558,
     66095,
     560,
     561,
     559,
     562,
     564,
     565,
     566,
     131636,
     567,
     570,
     571,
     574,
     576,
     578,
     579,
     581,
     33351,
     588,
     589,
     590,
     592,
     593,
     594,
     595,
     596,
     597,
     599,
     601,
     33371,
     606,
     229982,
     607,
     608,
     612,
     613,
     615,
     616,
     619,
     33387,
     620,
     621,
     623,
     393842,
     627,
     628,
     630,
     631,
     632,
     635,
     636,
     638,
     164480,
     640,
     98946,
     641,
     98950,
     647,
     648,
     650,
     131723,
     651,
     653,
     33422,
     654,
     659,
     660,
     661,
     663,
     664,
     665,
     671,
     672,
     677,
     679,
     681,
     682,
     33450,
     33452,
     685,
     686,
     687,
     230062,
     689,
     693,
     695,
     696,
     697,
     328379,
     700,
     702,
     703,
     704,
     706,
     708,
     709,
     711,
     716,
     717,
     718,
     164556,
     720,
     721,
     99023,
     726,
     33494,
     731,
     33499,
     733,
     734,
     230109,
     735,
     33506,
     739,
     740,
     131813,
     741,
     743,
     745,
     230122,
     747,
     66287,
     752,
     754,
     755,
     33523,
     757,
     761,
     197370,
     763,
     764,
     765,
     164605,
     768,
     771,
     773,
     774,
     33541,
     776,
     777,
     775,
     66315,
     778,
     781,
     780,
     783,
     784,
     785,
     786,
     787,
     99086,
     792,
     794,
     796,
     797,
     799,
     801,
     802,
     805,
     806,
     808,
     230186,
     810,
     812,
     815,
     816,
     818,
     820,
     66356,
     822,
     823,
     825,
     826,
     829,
     830,
     831,
     838,
     839,
     841,
     843,
     844,
     846,
     848,
     262993,
     850,
     33617,
     853,
     854,
     855,
     857,
     33626,
     862,
     866,
     164707,
     868,
     869,
     870,
     871,
     872,
     874,
     33645,
     66413,
     879,
     880,
     99185,
     877,
     33651,
     883,
     878,
     887,
     33655,
     889,
     888,
     890,
     892,
     164732,
     893,
     894,
     896,
     897,
     898,
     899,
     900,
     902,
     904,
     905,
     907,
     908,
     909,
     911,
     912,
     914,
     915,
     916,
     917,
     918,
     921,
     922,
     927,
     928,
     930,
     918435,
     932,
     935,
     938,
     939,
     941,
     943,
     948,
     33720,
     953,
     954,
     955,
     956,
     961,
     962,
     963,
     966,
     967,
     969,
     970,
     971,
     972,
     978,
     979,
     980,
     982,
     985,
     263131,
     988,
     33756,
     990,
     991,
     66529,
     33764,
     997,
     998,
     361447,
     1000,
     1004,
     1005,
     1006,
     33775,
     1009,
     1012,
     99317,
     1014,
     1015,
     1017,
     1018,
     1022,
     1024,
     1025,
     33794,
     295938,
     1028,
     1034,
     1035,
     263178,
     1038,
     1039,
     1040,
     1041,
     1042,
     66583,
     1047,
     1049,
     197657,
     1051,
     230427,
     1053,
     66589,
     33823,
     1056,
     1055,
     1057,
     1058,
     1060,
     197670,
     1063,
     230441,
     1069,
     66606,
     1070,
     1073,
     1075,
     1078,
     1081,
     1082,
     1085,
     164926,
     1087,
     1086,
     1094,
     1095,
     132167,
     263245,
     1103,
     197712,
     1105,
     66639,
     1108,
     1109,
     1110,
     132183,
     1111,
     1112,
     1114,
     1118,
     1119,
     1120,
     33886,
     1122,
     1123,
     296036,
     1124,
     1126,
     99430,
     1128,
     1129,
     230508,
     1138,
     1140,
     1141,
     263289,
     1146,
     1147,
     1148,
     1150,
     33919,
     1153,
     33921,
     33923,
     1156,
     1159,
     1160,
     1162,
     1167,
     132240,
     1170,
     1173,
     1174,
     1183,
     99488,
     1185,
     33954,
     1187,
     197796,
     1190,
     1191,
     197800,
     1194,
     1195,
     132268,
     1196,
     1198,
     1199,
     1200,
     1201,
     33970,
     1203,
     99505,
     1205,
     66739,
     1209,
     1210,
     1212,
     1214,
     1220,
     1222,
     1224,
     1226,
     1228,
     33996,
     1237,
     1238,
     1240,
     1246,
     1247,
     1248,
     1250,
     1253,
     1255,
     1257,
     1258,
     1259,
     132329,
     1261,
     1262,
     1263,
     1264,
     197871,
     34033,
     1267,
     34036,
     1269,
     1271,
     1274,
     1275,
     1277,
     1278,
     1279,
     132354,
     1282,
     296196,
     1285,
     1283,
     1284,
     1288,
     1289,
     1292,
     1294,
     1298,
     1299,
     1301,
     1302,
     99607,
     1308,
     66847,
     34080,
     1313,
     1312,
     1311,
     1316,
     1317,
     1319,
     34090,
     1325,
     197934,
     165167,
     1328,
     1327,
     66866,
     34098,
     1332,
     1335,
     197943,
     1339,
     1340,
     34108,
     1342,
     1341,
     1344,
     1346,
     1348,
     1349,
     1350,
     1352,
     1354,
     1355,
     1359,
     1361,
     1362,
     197975,
     1368,
     1370,
     1371,
     1372,
     132445,
     1374,
     1375,
     1376,
     1377,
     1378,
     34147,
     1373,
     1381,
     1382,
     1383,
     1384,
     1386,
     1387,
     1390,
     1391,
     1392,
     1393,
     1394,
     1397,
     1399,
     1403,
     165244,
     1404,
     1407,
     1409,
     165249,
     1411,
     132481,
     1413,
     1412,
     1417,
     34186,
     99723,
     1420,
     1423,
     1425,
     99730,
     1426,
     1428,
     165269,
     1429,
     1431,
     1435,
     1437,
     1438,
     1440,
     1441,
     1442,
     99747,
     34208,
     1445,
     1444,
     34215,
     66984,
     1450,
     34220,
     1453,
     1454,
     1455,
     1459,
     1460,
     1462,
     1464,
     99772,
     1468,
     1470,
     1471,
     165313,
     1475,
     263619,
     1477,
     1479,
     1480,
     1481,
     1483,
     1484,
     1486,
     1487,
     1490,
     34263,
     1496,
     1498,
     99803,
     1503,
     1504,
     263649,
     1506,
     34276,
     1509,
     1510,
     1511,
     1512,
     1513,
     1516,
     1517,
     ...}




```python
set(df_check[df_check['category_derived']=='Shoes']['salesrank_derived'])
```




    {1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     10,
     32778,
     12,
     13,
     11,
     15,
     17,
     18,
     19,
     20,
     98323,
     21,
     23,
     24,
     65554,
     65562,
     27,
     30,
     31,
     32,
     33,
     35,
     36,
     37,
     38,
     39,
     40,
     41,
     42,
     65576,
     32806,
     44,
     46,
     50,
     51,
     52,
     131124,
     54,
     56,
     57,
     32824,
     59,
     60,
     61,
     62,
     64,
     66,
     67,
     68,
     71,
     65608,
     72,
     74,
     75,
     76,
     32844,
     78,
     83,
     84,
     32853,
     87,
     88,
     89,
     91,
     93,
     94,
     96,
     98,
     99,
     100,
     102,
     104,
     105,
     107,
     110,
     111,
     112,
     113,
     114,
     115,
     116,
     65650,
     65654,
     65646,
     122,
     123,
     126,
     32894,
     128,
     129,
     132,
     133,
     65668,
     135,
     136,
     138,
     65676,
     141,
     32910,
     143,
     144,
     142,
     140,
     65684,
     148,
     152,
     153,
     131226,
     155,
     156,
     157,
     161,
     162,
     165,
     169,
     170,
     171,
     173,
     174,
     175,
     98479,
     177,
     178,
     179,
     181,
     184,
     32953,
     185,
     186,
     188,
     189,
     193,
     194,
     196,
     197,
     203,
     205,
     206,
     207,
     210,
     211,
     32979,
     214,
     32982,
     216,
     217,
     218,
     219,
     221,
     222,
     223,
     224,
     226,
     227,
     228,
     229,
     233,
     65769,
     235,
     236,
     237,
     238,
     33008,
     65777,
     242,
     243,
     244,
     246,
     249,
     250,
     251,
     252,
     254,
     255,
     259,
     260,
     261,
     263,
     264,
     265,
     65803,
     65805,
     270,
     271,
     272,
     278,
     65814,
     280,
     281,
     98582,
     164123,
     279,
     285,
     286,
     282,
     284,
     289,
     292,
     65829,
     294,
     295,
     296,
     33060,
     298,
     299,
     302,
     65840,
     305,
     307,
     310,
     313,
     315,
     317,
     319,
     321,
     323,
     325,
     326,
     327,
     33095,
     65865,
     329,
     331,
     332,
     335,
     338,
     339,
     345,
     347,
     348,
     98652,
     350,
     351,
     352,
     353,
     354,
     357,
     358,
     359,
     360,
     363,
     364,
     365,
     369,
     370,
     372,
     373,
     376,
     377,
     378,
     379,
     33149,
     382,
     383,
     381,
     388,
     391,
     393,
     395,
     65933,
     398,
     397,
     402,
     404,
     406,
     408,
     33177,
     409,
     411,
     412,
     413,
     415,
     417,
     419,
     421,
     422,
     425,
     65962,
     33196,
     431,
     432,
     433,
     434,
     437,
     440,
     441,
     443,
     445,
     448,
     449,
     451,
     454,
     33222,
     457,
     459,
     460,
     461,
     462,
     463,
     465,
     466,
     468,
     470,
     471,
     472,
     66009,
     474,
     475,
     33246,
     480,
     482,
     484,
     487,
     491,
     492,
     493,
     494,
     495,
     499,
     502,
     503,
     33272,
     507,
     508,
     509,
     510,
     512,
     514,
     517,
     518,
     519,
     520,
     66056,
     523,
     525,
     526,
     527,
     528,
     530,
     531,
     532,
     66069,
     533,
     534,
     536,
     535,
     539,
     33308,
     540,
     542,
     543,
     545,
     547,
     549,
     550,
     33317,
     551,
     553,
     554,
     556,
     557,
     66094,
     559,
     562,
     563,
     564,
     567,
     568,
     569,
     570,
     571,
     572,
     573,
     574,
     578,
     579,
     580,
     581,
     582,
     586,
     587,
     590,
     592,
     594,
     597,
     598,
     601,
     33369,
     603,
     606,
     609,
     610,
     617,
     618,
     620,
     623,
     624,
     33392,
     33393,
     626,
     631,
     632,
     633,
     635,
     636,
     638,
     639,
     640,
     642,
     98948,
     645,
     646,
     647,
     33415,
     649,
     650,
     651,
     652,
     655,
     658,
     33426,
     660,
     661,
     33428,
     666,
     667,
     98972,
     669,
     670,
     673,
     66212,
     678,
     679,
     680,
     681,
     682,
     683,
     686,
     131759,
     688,
     690,
     691,
     693,
     695,
     700,
     701,
     702,
     704,
     705,
     33474,
     707,
     709,
     710,
     711,
     712,
     716,
     719,
     723,
     33494,
     727,
     728,
     729,
     726,
     737,
     738,
     741,
     744,
     745,
     746,
     66282,
     747,
     748,
     751,
     758,
     761,
     762,
     768,
     770,
     773,
     777,
     780,
     782,
     783,
     785,
     786,
     788,
     790,
     791,
     796,
     798,
     66335,
     800,
     801,
     802,
     803,
     33568,
     805,
     66345,
     815,
     66351,
     33585,
     66354,
     819,
     820,
     824,
     825,
     826,
     827,
     66364,
     66365,
     828,
     836,
     839,
     840,
     842,
     843,
     845,
     66382,
     849,
     850,
     66388,
     852,
     855,
     856,
     859,
     862,
     863,
     868,
     870,
     872,
     874,
     876,
     880,
     881,
     885,
     886,
     887,
     889,
     890,
     893,
     897,
     898,
     902,
     33671,
     33672,
     907,
     908,
     909,
     910,
     912,
     917,
     918,
     921,
     922,
     926,
     33694,
     928,
     930,
     33698,
     932,
     934,
     938,
     939,
     942,
     33714,
     164788,
     132021,
     950,
     948,
     952,
     953,
     66490,
     955,
     949,
     959,
     99263,
     960,
     964,
     966,
     968,
     969,
     970,
     973,
     974,
     689103,
     977,
     33746,
     978,
     981,
     982,
     983,
     987,
     989,
     33759,
     995,
     996,
     997,
     998,
     99303,
     1001,
     1002,
     1004,
     1008,
     66547,
     1012,
     1016,
     1017,
     1019,
     1020,
     33789,
     1022,
     1021,
     33787,
     1026,
     1027,
     1029,
     1036,
     66572,
     1037,
     1039,
     1038,
     1041,
     1043,
     1044,
     1046,
     1047,
     1050,
     1051,
     1053,
     1055,
     1058,
     1062,
     1064,
     1066,
     1067,
     66605,
     1070,
     1073,
     1077,
     1083,
     33852,
     1086,
     1091,
     1097,
     1100,
     1101,
     1102,
     1106,
     1107,
     1114,
     1119,
     1121,
     1122,
     1123,
     1125,
     1128,
     33901,
     1135,
     1140,
     1141,
     1148,
     1149,
     1150,
     1152,
     1153,
     1155,
     1156,
     1158,
     1160,
     1161,
     1162,
     1164,
     1165,
     1166,
     1170,
     1171,
     1175,
     1177,
     1182,
     1183,
     1184,
     66722,
     1187,
     1189,
     1192,
     1193,
     1196,
     1201,
     1202,
     1204,
     1205,
     1207,
     1211,
     1212,
     1216,
     1217,
     1218,
     1219,
     1221,
     1224,
     1225,
     1227,
     1228,
     1230,
     1233,
     1234,
     1235,
     1238,
     1239,
     1241,
     1242,
     66781,
     1245,
     66782,
     1247,
     1249,
     1246,
     1251,
     34019,
     1253,
     296166,
     1256,
     1257,
     66796,
     1264,
     1266,
     1268,
     1269,
     1270,
     1275,
     1276,
     1278,
     1281,
     1284,
     1285,
     1289,
     1292,
     1293,
     1294,
     66834,
     1299,
     1300,
     1298,
     1302,
     1305,
     1307,
     1312,
     1318,
     66857,
     1323,
     1328,
     1329,
     1330,
     1331,
     1334,
     1336,
     1338,
     1339,
     1341,
     1342,
     1344,
     1347,
     1348,
     1354,
     1357,
     34127,
     1361,
     1362,
     1363,
     1364,
     1366,
     1369,
     1371,
     1373,
     1375,
     34145,
     1378,
     1379,
     1382,
     1383,
     1384,
     1385,
     1387,
     1392,
     34161,
     1393,
     1396,
     1397,
     1398,
     1399,
     1404,
     34173,
     1409,
     1410,
     1413,
     1424,
     1425,
     1429,
     34199,
     1433,
     1442,
     1443,
     1444,
     1445,
     1446,
     1448,
     1453,
     66990,
     1454,
     1458,
     1461,
     66999,
     1464,
     67000,
     1465,
     1471,
     99776,
     34240,
     1473,
     1475,
     67010,
     1476,
     1480,
     1482,
     1486,
     1487,
     1488,
     1490,
     67027,
     1491,
     1497,
     1498,
     1507,
     1510,
     1513,
     1516,
     1521,
     1522,
     1528,
     1529,
     1533,
     1534,
     34301,
     1536,
     1535,
     1543,
     1546,
     1547,
     1550,
     1552,
     1555,
     1557,
     1558,
     1563,
     1565,
     1566,
     1568,
     67108,
     67109,
     1574,
     1573,
     1576,
     1577,
     1579,
     1580,
     1582,
     34351,
     1584,
     67120,
     1589,
     1590,
     1591,
     1593,
     1594,
     1596,
     1597,
     1598,
     1600,
     1605,
     67145,
     1610,
     1611,
     1609,
     1615,
     1617,
     1620,
     1629,
     1630,
     67168,
     1633,
     1637,
     1638,
     1641,
     1644,
     1647,
     1651,
     1653,
     1656,
     1659,
     1660,
     1661,
     1666,
     1667,
     34435,
     1669,
     1670,
     1671,
     67206,
     1673,
     1674,
     34446,
     1678,
     1681,
     67229,
     1693,
     1695,
     1694,
     1698,
     1702,
     100009,
     1716,
     1718,
     1719,
     34488,
     1720,
     1724,
     1728,
     1731,
     1734,
     1737,
     1742,
     1743,
     1744,
     1745,
     1747,
     1748,
     1749,
     1750,
     1753,
     34525,
     1758,
     1760,
     1762,
     1763,
     1764,
     34532,
     67305,
     1771,
     1773,
     1774,
     1779,
     1783,
     1785,
     34556,
     1789,
     1788,
     1791,
     1792,
     34562,
     34568,
     1801,
     1802,
     1804,
     1805,
     1812,
     1816,
     1817,
     1820,
     1821,
     100125,
     1824,
     1825,
     1829,
     1830,
     34601,
     34603,
     1836,
     1837,
     34609,
     1844,
     100148,
     1846,
     67382,
     34612,
     1848,
     1852,
     34621,
     67396,
     1861,
     1862,
     1863,
     1869,
     ...}




```python
df_check[(df_check['category_derived']=='Shoes') & (df_check['salesrank_derived']==7)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reviewerID</th>
      <th>asin</th>
      <th>reviewerName</th>
      <th>helpful</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>unixReviewTime</th>
      <th>reviewTime</th>
      <th>metadataid</th>
      <th>salesrank</th>
      <th>imurl</th>
      <th>categories</th>
      <th>title</th>
      <th>description</th>
      <th>price</th>
      <th>related</th>
      <th>brand</th>
      <th>positive_helpful</th>
      <th>negative_helpful</th>
      <th>total_helpful</th>
      <th>positive_helpful_ratio</th>
      <th>len_reviewText</th>
      <th>category_derived</th>
      <th>len_summary</th>
      <th>check</th>
      <th>len_summary_bins</th>
      <th>len_reviewText_bins</th>
      <th>reviewText_cleaned</th>
      <th>summary_cleaned</th>
      <th>len_reviewText_cleaned</th>
      <th>len_summary_cleaned</th>
      <th>len_summary_cleaned_bins</th>
      <th>len_reviewText_claned_bins</th>
      <th>price_bins</th>
      <th>salesrank_derived</th>
      <th>date</th>
      <th>month</th>
      <th>asin_reviewer</th>
      <th>pos_neg</th>
      <th>review_nonum</th>
      <th>year</th>
      <th>reviewText_comwords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70999</th>
      <td>70999</td>
      <td>AIVMZ6F8UXRM</td>
      <td>B001Q5QLP6</td>
      <td>2Kids "Mom"</td>
      <td>[0, 0]</td>
      <td>These are really comfortable and true to size....</td>
      <td>5.0</td>
      <td>great shoe</td>
      <td>1369267200</td>
      <td>05 23, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>241.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThesearereallycomfortableandtruetosizeIweara95...</td>
      <td>greatshoe</td>
      <td>184</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-23</td>
      <td>5</td>
      <td>B001Q5QLP6AIVMZ6F8UXRM</td>
      <td>1</td>
      <td>These are really comfortable and true to size ...</td>
      <td>2013</td>
      <td>These are really comfortable and true to size....</td>
    </tr>
    <tr>
      <th>71000</th>
      <td>71000</td>
      <td>A3MGZY6VJSTHOU</td>
      <td>B001Q5QLP6</td>
      <td>A. Haynes "andigirl"</td>
      <td>[0, 0]</td>
      <td>Love these sandals, but my insert kept slippin...</td>
      <td>2.0</td>
      <td>Can't wear with ortho insert</td>
      <td>1401840000</td>
      <td>06 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>125.0</td>
      <td>Shoes</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Lovethesesandalsbutmyinsertkeptslippingouttheb...</td>
      <td>Cantwearwithorthoinsert</td>
      <td>94</td>
      <td>23</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-04</td>
      <td>6</td>
      <td>B001Q5QLP6A3MGZY6VJSTHOU</td>
      <td>0</td>
      <td>Love these sandals but my insert kept slipping...</td>
      <td>2014</td>
      <td>Love these sandals, but my insert kept slippin...</td>
    </tr>
    <tr>
      <th>71001</th>
      <td>71001</td>
      <td>A2YOTQ01MW4JML</td>
      <td>B001Q5QLP6</td>
      <td>Alma</td>
      <td>[3, 4]</td>
      <td>I have very long, slender, narrow feet and I h...</td>
      <td>5.0</td>
      <td>Wish I could afford every color!</td>
      <td>1339977600</td>
      <td>06 18, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>0.428571</td>
      <td>1046.0</td>
      <td>Shoes</td>
      <td>32.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IhaveverylongslendernarrowfeetandIhavebecomefr...</td>
      <td>WishIcouldaffordeverycolor</td>
      <td>810</td>
      <td>26</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-06-18</td>
      <td>6</td>
      <td>B001Q5QLP6A2YOTQ01MW4JML</td>
      <td>1</td>
      <td>I have very long slender narrow feet and I hav...</td>
      <td>2012</td>
      <td>I have very long, slender, narrow feet and I h...</td>
    </tr>
    <tr>
      <th>71002</th>
      <td>71002</td>
      <td>A241HBUTNOTAPB</td>
      <td>B001Q5QLP6</td>
      <td>Amanda</td>
      <td>[1, 1]</td>
      <td>These are unbelievable.  I absolutely love the...</td>
      <td>5.0</td>
      <td>Where have these been all my life!?</td>
      <td>1404000000</td>
      <td>06 29, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>898.0</td>
      <td>Shoes</td>
      <td>35.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>TheseareunbelievableIabsolutelylovethemTheyare...</td>
      <td>Wherehavethesebeenallmylife</td>
      <td>706</td>
      <td>27</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-29</td>
      <td>6</td>
      <td>B001Q5QLP6A241HBUTNOTAPB</td>
      <td>1</td>
      <td>These are unbelievable  I absolutely love them...</td>
      <td>2014</td>
      <td>These are unbelievable.  I absolutely love the...</td>
    </tr>
    <tr>
      <th>71003</th>
      <td>71003</td>
      <td>A2OD8I20PB105B</td>
      <td>B001Q5QLP6</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I needed a sandal that was light, comfortable ...</td>
      <td>4.0</td>
      <td>Comfortable and handsome</td>
      <td>1370908800</td>
      <td>06 11, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>248.0</td>
      <td>Shoes</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Ineededasandalthatwaslightcomfortableandwouldl...</td>
      <td>Comfortableandhandsome</td>
      <td>194</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-11</td>
      <td>6</td>
      <td>B001Q5QLP6A2OD8I20PB105B</td>
      <td>1</td>
      <td>I needed a sandal that was light comfortable a...</td>
      <td>2013</td>
      <td>I needed a sandal that was light, comfortable ...</td>
    </tr>
    <tr>
      <th>71004</th>
      <td>71004</td>
      <td>ASKEOWB4VNF49</td>
      <td>B001Q5QLP6</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>Love these shoes! Easy to put on and very comf...</td>
      <td>5.0</td>
      <td>Love these shoes!</td>
      <td>1404864000</td>
      <td>07 9, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>429.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>LovetheseshoesEasytoputonandverycomfortabletow...</td>
      <td>Lovetheseshoes</td>
      <td>343</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-09</td>
      <td>7</td>
      <td>B001Q5QLP6ASKEOWB4VNF49</td>
      <td>1</td>
      <td>Love these shoes Easy to put on and very comfo...</td>
      <td>2014</td>
      <td>Love these shoes! Easy to put on and very comf...</td>
    </tr>
    <tr>
      <th>71005</th>
      <td>71005</td>
      <td>A25JZRMB0KQ1EI</td>
      <td>B001Q5QLP6</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>These shoes have a great fit.  Will work great...</td>
      <td>5.0</td>
      <td>Whisper Sandal</td>
      <td>1402012800</td>
      <td>06 6, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>200.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>TheseshoeshaveagreatfitWillworkgreatforrunning...</td>
      <td>WhisperSandal</td>
      <td>152</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-06</td>
      <td>6</td>
      <td>B001Q5QLP6A25JZRMB0KQ1EI</td>
      <td>1</td>
      <td>These shoes have a great fit  Will work great ...</td>
      <td>2014</td>
      <td>These shoes have a great fit.  Will work great...</td>
    </tr>
    <tr>
      <th>71006</th>
      <td>71006</td>
      <td>A1S0HYXDPKDDNO</td>
      <td>B001Q5QLP6</td>
      <td>Amazon Customer "kmommy"</td>
      <td>[0, 0]</td>
      <td>I'm giving 3 stars because they work incredibl...</td>
      <td>3.0</td>
      <td>FOR NARROW FEET!</td>
      <td>1401753600</td>
      <td>06 3, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1197.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Imgiving3starsbecausetheyworkincredibleforawat...</td>
      <td>FORNARROWFEET</td>
      <td>923</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-03</td>
      <td>6</td>
      <td>B001Q5QLP6A1S0HYXDPKDDNO</td>
      <td>0</td>
      <td>Im giving  stars because they work incredible ...</td>
      <td>2014</td>
      <td>I'm giving 3 stars because they work incredibl...</td>
    </tr>
    <tr>
      <th>71007</th>
      <td>71007</td>
      <td>A1BZFRYSMNPVYF</td>
      <td>B001Q5QLP6</td>
      <td>Amazon Junkie</td>
      <td>[1, 1]</td>
      <td>I wouldn't run a marathon with these, but if I...</td>
      <td>4.0</td>
      <td>It's great for short term use</td>
      <td>1301097600</td>
      <td>03 26, 2011</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>154.0</td>
      <td>Shoes</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IwouldntrunamarathonwiththesebutifImgoingtothe...</td>
      <td>Itsgreatforshorttermuse</td>
      <td>117</td>
      <td>23</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2011-03-26</td>
      <td>3</td>
      <td>B001Q5QLP6A1BZFRYSMNPVYF</td>
      <td>1</td>
      <td>I wouldnt run a marathon with these but if Im ...</td>
      <td>2011</td>
      <td>I wouldn't run a marathon with these, but if I...</td>
    </tr>
    <tr>
      <th>71008</th>
      <td>71008</td>
      <td>A26HN4UMQCFF6U</td>
      <td>B001Q5QLP6</td>
      <td>Andie</td>
      <td>[27, 40]</td>
      <td>I am working at a summer camp and purchased th...</td>
      <td>5.0</td>
      <td>Awesome sandal!</td>
      <td>1248739200</td>
      <td>07 28, 2009</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>1.000000</td>
      <td>728.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Iamworkingatasummercampandpurchasedthesebecaus...</td>
      <td>Awesomesandal</td>
      <td>565</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2009-07-28</td>
      <td>7</td>
      <td>B001Q5QLP6A26HN4UMQCFF6U</td>
      <td>1</td>
      <td>I am working at a summer camp and purchased th...</td>
      <td>2009</td>
      <td>I am working at a summer camp and purchased th...</td>
    </tr>
    <tr>
      <th>71009</th>
      <td>71009</td>
      <td>A2UFI637FCK3GO</td>
      <td>B001Q5QLP6</td>
      <td>Angela M.</td>
      <td>[0, 0]</td>
      <td>I bought these based onf the reviews and they ...</td>
      <td>5.0</td>
      <td>Love them!</td>
      <td>1402444800</td>
      <td>06 11, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>467.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtthesebasedonfthereviewsandtheydidntdisa...</td>
      <td>Lovethem</td>
      <td>365</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-11</td>
      <td>6</td>
      <td>B001Q5QLP6A2UFI637FCK3GO</td>
      <td>1</td>
      <td>I bought these based onf the reviews and they ...</td>
      <td>2014</td>
      <td>I bought these based onf the reviews and they ...</td>
    </tr>
    <tr>
      <th>71010</th>
      <td>71010</td>
      <td>A1F7YU6O5RU432</td>
      <td>B001Q5QLP6</td>
      <td>Angela Streiff</td>
      <td>[28, 41]</td>
      <td>A few months ago I bought my first pair of Kee...</td>
      <td>5.0</td>
      <td>Whisper vs Newport H2</td>
      <td>1372118400</td>
      <td>06 25, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>0</td>
      <td>2</td>
      <td>1.000000</td>
      <td>1810.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>AfewmonthsagoIboughtmyfirstpairofKeenshoestheK...</td>
      <td>WhispervsNewportH2</td>
      <td>1392</td>
      <td>18</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-25</td>
      <td>6</td>
      <td>B001Q5QLP6A1F7YU6O5RU432</td>
      <td>1</td>
      <td>A few months ago I bought my first pair of Kee...</td>
      <td>2013</td>
      <td>A few months ago I bought my first pair of Kee...</td>
    </tr>
    <tr>
      <th>71011</th>
      <td>71011</td>
      <td>A2F0X4LN9N4O4C</td>
      <td>B001Q5QLP6</td>
      <td>Anna Marie Wendt</td>
      <td>[2, 2]</td>
      <td>I got a great deal on these around Christmas t...</td>
      <td>5.0</td>
      <td>KEEN Sandal</td>
      <td>1394150400</td>
      <td>03 7, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0.500000</td>
      <td>178.0</td>
      <td>Shoes</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IgotagreatdealonthesearoundChristmastimeandIlo...</td>
      <td>KEENSandal</td>
      <td>135</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-07</td>
      <td>3</td>
      <td>B001Q5QLP6A2F0X4LN9N4O4C</td>
      <td>1</td>
      <td>I got a great deal on these around Christmas t...</td>
      <td>2014</td>
      <td>I got a great deal on these around Christmas t...</td>
    </tr>
    <tr>
      <th>71012</th>
      <td>71012</td>
      <td>A319RDF9F8K4DL</td>
      <td>B001Q5QLP6</td>
      <td>A. P. Nessel "Quality not Quantity"</td>
      <td>[0, 0]</td>
      <td>Those sandals are a versatile solution for the...</td>
      <td>5.0</td>
      <td>Very comfy, keep you cool, keep you warm - per...</td>
      <td>1355356800</td>
      <td>12 13, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>521.0</td>
      <td>Shoes</td>
      <td>68.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Thosesandalsareaversatilesolutionforthesummere...</td>
      <td>Verycomfykeepyoucoolkeepyouwarmperfectforsumme...</td>
      <td>410</td>
      <td>53</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-12-13</td>
      <td>12</td>
      <td>B001Q5QLP6A319RDF9F8K4DL</td>
      <td>1</td>
      <td>Those sandals are a versatile solution for the...</td>
      <td>2012</td>
      <td>Those sandals are a versatile solution for the...</td>
    </tr>
    <tr>
      <th>71013</th>
      <td>71013</td>
      <td>A109TXPU8DS85U</td>
      <td>B001Q5QLP6</td>
      <td>AR</td>
      <td>[0, 0]</td>
      <td>These came as advertised. But I returned them ...</td>
      <td>3.0</td>
      <td>Run Small</td>
      <td>1369008000</td>
      <td>05 20, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>359.0</td>
      <td>Shoes</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>ThesecameasadvertisedButIreturnedthembecauseIo...</td>
      <td>RunSmall</td>
      <td>276</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-20</td>
      <td>5</td>
      <td>B001Q5QLP6A109TXPU8DS85U</td>
      <td>0</td>
      <td>These came as advertised But I returned them b...</td>
      <td>2013</td>
      <td>These came as advertised. But I returned them ...</td>
    </tr>
    <tr>
      <th>71014</th>
      <td>71014</td>
      <td>A2B9PH9BUWNAY3</td>
      <td>B001Q5QLP6</td>
      <td>Ariel</td>
      <td>[0, 0]</td>
      <td>These are such great shoes.  I wear them all s...</td>
      <td>5.0</td>
      <td>Love my Keens!</td>
      <td>1384646400</td>
      <td>11 17, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1407.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThesearesuchgreatshoesIwearthemallsummerlongTh...</td>
      <td>LovemyKeens</td>
      <td>1097</td>
      <td>11</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-17</td>
      <td>11</td>
      <td>B001Q5QLP6A2B9PH9BUWNAY3</td>
      <td>1</td>
      <td>These are such great shoes  I wear them all su...</td>
      <td>2013</td>
      <td>These are such great shoes.  I wear them all s...</td>
    </tr>
    <tr>
      <th>71015</th>
      <td>71015</td>
      <td>A2284MUOR64G2F</td>
      <td>B001Q5QLP6</td>
      <td>Aunt Dynee "auntdynee"</td>
      <td>[1, 2]</td>
      <td>Perfect fit. Select she you wear in athletic s...</td>
      <td>5.0</td>
      <td>Right out of the box review...</td>
      <td>1372377600</td>
      <td>06 28, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>161.0</td>
      <td>Shoes</td>
      <td>30.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>PerfectfitSelectsheyouwearinathleticshoesandyo...</td>
      <td>Rightoutoftheboxreview</td>
      <td>127</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-28</td>
      <td>6</td>
      <td>B001Q5QLP6A2284MUOR64G2F</td>
      <td>1</td>
      <td>Perfect fit Select she you wear in athletic sh...</td>
      <td>2013</td>
      <td>Perfect fit. Select she you wear in athletic s...</td>
    </tr>
    <tr>
      <th>71016</th>
      <td>71016</td>
      <td>AUU6TRX7Y6A7A</td>
      <td>B001Q5QLP6</td>
      <td>Barbara</td>
      <td>[0, 0]</td>
      <td>This is my third pair of Keen Whisper sandals ...</td>
      <td>5.0</td>
      <td>Wonderful shoes!</td>
      <td>1385078400</td>
      <td>11 22, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>285.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThisismythirdpairofKeenWhispersandalsandIlovet...</td>
      <td>Wonderfulshoes</td>
      <td>229</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-22</td>
      <td>11</td>
      <td>B001Q5QLP6AUU6TRX7Y6A7A</td>
      <td>1</td>
      <td>This is my third pair of Keen Whisper sandals ...</td>
      <td>2013</td>
      <td>This is my third pair of Keen Whisper sandals ...</td>
    </tr>
    <tr>
      <th>71017</th>
      <td>71017</td>
      <td>A1KOIBT2X2WW6M</td>
      <td>B001Q5QLP6</td>
      <td>BDillon</td>
      <td>[0, 0]</td>
      <td>It's a very comfortable fit and no 'breaking i...</td>
      <td>5.0</td>
      <td>What a comfortable sandal!</td>
      <td>1381017600</td>
      <td>10 6, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>269.0</td>
      <td>Shoes</td>
      <td>26.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ItsaverycomfortablefitandnobreakinginatallItlo...</td>
      <td>Whatacomfortablesandal</td>
      <td>208</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-10-06</td>
      <td>10</td>
      <td>B001Q5QLP6A1KOIBT2X2WW6M</td>
      <td>1</td>
      <td>Its a very comfortable fit and no breaking in ...</td>
      <td>2013</td>
      <td>It's a very comfortable fit and no 'breaking i...</td>
    </tr>
    <tr>
      <th>71018</th>
      <td>71018</td>
      <td>AL5MZ4XI7NW0Y</td>
      <td>B001Q5QLP6</td>
      <td>BonSum</td>
      <td>[0, 0]</td>
      <td>I just got these, tried them on and they fit w...</td>
      <td>5.0</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>1401840000</td>
      <td>06 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>204.0</td>
      <td>Shoes</td>
      <td>27.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IjustgotthesetriedthemonandtheyfitwonderfullyT...</td>
      <td>KEENWomensWhisperSandal</td>
      <td>158</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-04</td>
      <td>6</td>
      <td>B001Q5QLP6AL5MZ4XI7NW0Y</td>
      <td>1</td>
      <td>I just got these tried them on and they fit wo...</td>
      <td>2014</td>
      <td>I just got these, tried them on and they fit w...</td>
    </tr>
    <tr>
      <th>71019</th>
      <td>71019</td>
      <td>A124VIS21EQT8U</td>
      <td>B001Q5QLP6</td>
      <td>Brenda V</td>
      <td>[0, 0]</td>
      <td>These sandals are very comfortable and practic...</td>
      <td>5.0</td>
      <td>Great Sandals</td>
      <td>1368662400</td>
      <td>05 16, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>259.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Thesesandalsareverycomfortableandpracticalfors...</td>
      <td>GreatSandals</td>
      <td>201</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-16</td>
      <td>5</td>
      <td>B001Q5QLP6A124VIS21EQT8U</td>
      <td>1</td>
      <td>These sandals are very comfortable and practic...</td>
      <td>2013</td>
      <td>These sandals are very comfortable and practic...</td>
    </tr>
    <tr>
      <th>71020</th>
      <td>71020</td>
      <td>A3KOIGNM2XCXG5</td>
      <td>B001Q5QLP6</td>
      <td>Buzz Fledderjohn</td>
      <td>[0, 0]</td>
      <td>Perfect fit, very comfortable.</td>
      <td>5.0</td>
      <td>Great water shoes</td>
      <td>1403913600</td>
      <td>06 28, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>30.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Perfectfitverycomfortable</td>
      <td>Greatwatershoes</td>
      <td>25</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-28</td>
      <td>6</td>
      <td>B001Q5QLP6A3KOIGNM2XCXG5</td>
      <td>1</td>
      <td>Perfect fit very comfortable</td>
      <td>2014</td>
      <td>Perfect fit, very comfortable.</td>
    </tr>
    <tr>
      <th>71021</th>
      <td>71021</td>
      <td>A38FO456GIPLDL</td>
      <td>B001Q5QLP6</td>
      <td>Cam Davis "It's a beautiful day!"</td>
      <td>[0, 0]</td>
      <td>I was a little worried about these shoes based...</td>
      <td>5.0</td>
      <td>Light as a whisper, and super-comfortable too!</td>
      <td>1396051200</td>
      <td>03 29, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>899.0</td>
      <td>Shoes</td>
      <td>46.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iwasalittleworriedabouttheseshoesbasedonsomene...</td>
      <td>Lightasawhisperandsupercomfortabletoo</td>
      <td>706</td>
      <td>37</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-29</td>
      <td>3</td>
      <td>B001Q5QLP6A38FO456GIPLDL</td>
      <td>1</td>
      <td>I was a little worried about these shoes based...</td>
      <td>2014</td>
      <td>I was a little worried about these shoes based...</td>
    </tr>
    <tr>
      <th>71022</th>
      <td>71022</td>
      <td>A3IFP7UYZ92207</td>
      <td>B001Q5QLP6</td>
      <td>Cam</td>
      <td>[2, 2]</td>
      <td>I have difficulty finding sandals with good ar...</td>
      <td>5.0</td>
      <td>Wonderfully comfortable from day 1</td>
      <td>1363996800</td>
      <td>03 23, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0.500000</td>
      <td>487.0</td>
      <td>Shoes</td>
      <td>34.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Ihavedifficultyfindingsandalswithgoodarchsuppo...</td>
      <td>Wonderfullycomfortablefromday1</td>
      <td>386</td>
      <td>30</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-03-23</td>
      <td>3</td>
      <td>B001Q5QLP6A3IFP7UYZ92207</td>
      <td>1</td>
      <td>I have difficulty finding sandals with good ar...</td>
      <td>2013</td>
      <td>I have difficulty finding sandals with good ar...</td>
    </tr>
    <tr>
      <th>71023</th>
      <td>71023</td>
      <td>A1I539BXSM7IS8</td>
      <td>B001Q5QLP6</td>
      <td>Campbell Welsh "Campbell"</td>
      <td>[0, 0]</td>
      <td>Love this shoe.  This is the second pair I've ...</td>
      <td>5.0</td>
      <td>Wide Foot? Cant Beat Keen</td>
      <td>1385251200</td>
      <td>11 24, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>255.0</td>
      <td>Shoes</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>LovethisshoeThisisthesecondpairIveorderedIwear...</td>
      <td>WideFootCantBeatKeen</td>
      <td>195</td>
      <td>20</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-24</td>
      <td>11</td>
      <td>B001Q5QLP6A1I539BXSM7IS8</td>
      <td>1</td>
      <td>Love this shoe  This is the second pair Ive or...</td>
      <td>2013</td>
      <td>Love this shoe.  This is the second pair I've ...</td>
    </tr>
    <tr>
      <th>71024</th>
      <td>71024</td>
      <td>A3HDXTJNIIKRMY</td>
      <td>B001Q5QLP6</td>
      <td>Carie Urato "Carie"</td>
      <td>[0, 0]</td>
      <td>I purchased this not too long AGO AND THEN YOU...</td>
      <td>5.0</td>
      <td>Great Shoe</td>
      <td>1401840000</td>
      <td>06 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>211.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IpurchasedthisnottoolongAGOANDTHENYOUDROPTHEPR...</td>
      <td>GreatShoe</td>
      <td>162</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-04</td>
      <td>6</td>
      <td>B001Q5QLP6A3HDXTJNIIKRMY</td>
      <td>1</td>
      <td>I purchased this not too long AGO AND THEN YOU...</td>
      <td>2014</td>
      <td>I purchased this not too long AGO AND THEN YOU...</td>
    </tr>
    <tr>
      <th>71025</th>
      <td>71025</td>
      <td>A3W041GDO02CH3</td>
      <td>B001Q5QLP6</td>
      <td>cassandra renfro</td>
      <td>[0, 0]</td>
      <td>These are versatile sandals. Great for hiking,...</td>
      <td>5.0</td>
      <td>Comfort!!</td>
      <td>1402185600</td>
      <td>06 8, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>131.0</td>
      <td>Shoes</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>TheseareversatilesandalsGreatforhikingwalkingf...</td>
      <td>Comfort</td>
      <td>103</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-08</td>
      <td>6</td>
      <td>B001Q5QLP6A3W041GDO02CH3</td>
      <td>1</td>
      <td>These are versatile sandals Great for hiking w...</td>
      <td>2014</td>
      <td>These are versatile sandals. Great for hiking,...</td>
    </tr>
    <tr>
      <th>71026</th>
      <td>71026</td>
      <td>A2EX67IB48SGLM</td>
      <td>B001Q5QLP6</td>
      <td>Cat Collector</td>
      <td>[1, 1]</td>
      <td>I bought an 8 1/2 and it was way too big.  I s...</td>
      <td>5.0</td>
      <td>Buy these</td>
      <td>1372204800</td>
      <td>06 26, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>377.0</td>
      <td>Shoes</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtan812anditwaswaytoobigIsentitbackyester...</td>
      <td>Buythese</td>
      <td>287</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-26</td>
      <td>6</td>
      <td>B001Q5QLP6A2EX67IB48SGLM</td>
      <td>1</td>
      <td>I bought an   and it was way too big  I sent i...</td>
      <td>2013</td>
      <td>I bought an 8 1/2 and it was way too big.  I s...</td>
    </tr>
    <tr>
      <th>71027</th>
      <td>71027</td>
      <td>A2BG8XXOETAKI4</td>
      <td>B001Q5QLP6</td>
      <td>Catt "Southern Girl"</td>
      <td>[1, 1]</td>
      <td>I have balance issues and cannot wear slides o...</td>
      <td>5.0</td>
      <td>Just what I was looking for</td>
      <td>1367193600</td>
      <td>04 29, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>817.0</td>
      <td>Shoes</td>
      <td>27.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Ihavebalanceissuesandcannotwearslidesorsandals...</td>
      <td>JustwhatIwaslookingfor</td>
      <td>630</td>
      <td>22</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-04-29</td>
      <td>4</td>
      <td>B001Q5QLP6A2BG8XXOETAKI4</td>
      <td>1</td>
      <td>I have balance issues and cannot wear slides o...</td>
      <td>2013</td>
      <td>I have balance issues and cannot wear slides o...</td>
    </tr>
    <tr>
      <th>71028</th>
      <td>71028</td>
      <td>A3NAQCZLTXOJEO</td>
      <td>B001Q5QLP6</td>
      <td>CeeCee</td>
      <td>[0, 0]</td>
      <td>These are very comfortable and supportive.They...</td>
      <td>5.0</td>
      <td>Comfy/Sturdy</td>
      <td>1376438400</td>
      <td>08 14, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>212.0</td>
      <td>Shoes</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>TheseareverycomfortableandsupportiveTheyallowy...</td>
      <td>ComfySturdy</td>
      <td>169</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-14</td>
      <td>8</td>
      <td>B001Q5QLP6A3NAQCZLTXOJEO</td>
      <td>1</td>
      <td>These are very comfortable and supportiveThey ...</td>
      <td>2013</td>
      <td>These are very comfortable and supportive.They...</td>
    </tr>
    <tr>
      <th>71029</th>
      <td>71029</td>
      <td>A11OTLEDSW8ZXD</td>
      <td>B001Q5QLP6</td>
      <td>CGScammell</td>
      <td>[0, 0]</td>
      <td>Some of the reviews about the sizes being off ...</td>
      <td>5.0</td>
      <td>True to size and super comfy</td>
      <td>1384560000</td>
      <td>11 16, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>849.0</td>
      <td>Shoes</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Someofthereviewsaboutthesizesbeingoffhadmeworr...</td>
      <td>Truetosizeandsupercomfy</td>
      <td>661</td>
      <td>23</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-16</td>
      <td>11</td>
      <td>B001Q5QLP6A11OTLEDSW8ZXD</td>
      <td>1</td>
      <td>Some of the reviews about the sizes being off ...</td>
      <td>2013</td>
      <td>Some of the reviews about the sizes being off ...</td>
    </tr>
    <tr>
      <th>71030</th>
      <td>71030</td>
      <td>A3EN4T0JIU931W</td>
      <td>B001Q5QLP6</td>
      <td>cindy aase</td>
      <td>[1, 1]</td>
      <td>I have been happy with most Keen Styles, but a...</td>
      <td>5.0</td>
      <td>Love love LOVE!</td>
      <td>1371686400</td>
      <td>06 20, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>550.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IhavebeenhappywithmostKeenStylesbutasIhavehadt...</td>
      <td>LoveloveLOVE</td>
      <td>429</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-20</td>
      <td>6</td>
      <td>B001Q5QLP6A3EN4T0JIU931W</td>
      <td>1</td>
      <td>I have been happy with most Keen Styles but as...</td>
      <td>2013</td>
      <td>I have been happy with most Keen Styles, but a...</td>
    </tr>
    <tr>
      <th>71031</th>
      <td>71031</td>
      <td>A152Q1C2HRD0RF</td>
      <td>B001Q5QLP6</td>
      <td>C in Yakima</td>
      <td>[0, 0]</td>
      <td>KEEN has changed the foot bed of this years Wh...</td>
      <td>4.0</td>
      <td>Yummie Color</td>
      <td>1377475200</td>
      <td>08 26, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>495.0</td>
      <td>Shoes</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>KEENhaschangedthefootbedofthisyearsWhisperIdon...</td>
      <td>YummieColor</td>
      <td>377</td>
      <td>11</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-26</td>
      <td>8</td>
      <td>B001Q5QLP6A152Q1C2HRD0RF</td>
      <td>1</td>
      <td>KEEN has changed the foot bed of this years Wh...</td>
      <td>2013</td>
      <td>KEEN has changed the foot bed of this years Wh...</td>
    </tr>
    <tr>
      <th>71032</th>
      <td>71032</td>
      <td>AME1QLFSNZVCT</td>
      <td>B001Q5QLP6</td>
      <td>C. J. Fairhurst "Cathy F"</td>
      <td>[0, 0]</td>
      <td>Love these sandals, perfect for hiking across ...</td>
      <td>5.0</td>
      <td>Comfy and cool</td>
      <td>1401840000</td>
      <td>06 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>208.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Lovethesesandalsperfectforhikingacrosslavarock...</td>
      <td>Comfyandcool</td>
      <td>166</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-04</td>
      <td>6</td>
      <td>B001Q5QLP6AME1QLFSNZVCT</td>
      <td>1</td>
      <td>Love these sandals perfect for hiking across l...</td>
      <td>2014</td>
      <td>Love these sandals, perfect for hiking across ...</td>
    </tr>
    <tr>
      <th>71033</th>
      <td>71033</td>
      <td>A3C1G23EIXOVA5</td>
      <td>B001Q5QLP6</td>
      <td>Clare</td>
      <td>[0, 0]</td>
      <td>I was a little worried after reading reviews t...</td>
      <td>5.0</td>
      <td>Perfect fit</td>
      <td>1370304000</td>
      <td>06 4, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>196.0</td>
      <td>Shoes</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iwasalittleworriedafterreadingreviewsthatthese...</td>
      <td>Perfectfit</td>
      <td>153</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-04</td>
      <td>6</td>
      <td>B001Q5QLP6A3C1G23EIXOVA5</td>
      <td>1</td>
      <td>I was a little worried after reading reviews t...</td>
      <td>2013</td>
      <td>I was a little worried after reading reviews t...</td>
    </tr>
    <tr>
      <th>71034</th>
      <td>71034</td>
      <td>A2PRVRKFXLHZAW</td>
      <td>B001Q5QLP6</td>
      <td>Colorado Girl</td>
      <td>[0, 0]</td>
      <td>Anyone that wants an excellent pair of shoes f...</td>
      <td>5.0</td>
      <td>Love these shoes</td>
      <td>1400025600</td>
      <td>05 14, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>295.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>AnyonethatwantsanexcellentpairofshoesforSummer...</td>
      <td>Lovetheseshoes</td>
      <td>230</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-14</td>
      <td>5</td>
      <td>B001Q5QLP6A2PRVRKFXLHZAW</td>
      <td>1</td>
      <td>Anyone that wants an excellent pair of shoes f...</td>
      <td>2014</td>
      <td>Anyone that wants an excellent pair of shoes f...</td>
    </tr>
    <tr>
      <th>71035</th>
      <td>71035</td>
      <td>AM3CX4VOU76MS</td>
      <td>B001Q5QLP6</td>
      <td>---- Covarrubias "jaluvic"</td>
      <td>[0, 0]</td>
      <td>These are actually fairly feminine looking and...</td>
      <td>5.0</td>
      <td>Excellent Fit and super Comfy and Good Looking</td>
      <td>1398902400</td>
      <td>05 1, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>371.0</td>
      <td>Shoes</td>
      <td>46.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Theseareactuallyfairlyfemininelookinganditwasa...</td>
      <td>ExcellentFitandsuperComfyandGoodLooking</td>
      <td>287</td>
      <td>39</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-01</td>
      <td>5</td>
      <td>B001Q5QLP6AM3CX4VOU76MS</td>
      <td>1</td>
      <td>These are actually fairly feminine looking and...</td>
      <td>2014</td>
      <td>These are actually fairly feminine looking and...</td>
    </tr>
    <tr>
      <th>71036</th>
      <td>71036</td>
      <td>A2NZQ7DSJV4AV2</td>
      <td>B001Q5QLP6</td>
      <td>Cyndee</td>
      <td>[0, 0]</td>
      <td>I have been wanting these sandals since last s...</td>
      <td>5.0</td>
      <td>Comfort and great looks</td>
      <td>1394928000</td>
      <td>03 16, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>665.0</td>
      <td>Shoes</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Ihavebeenwantingthesesandalssincelastsummerbut...</td>
      <td>Comfortandgreatlooks</td>
      <td>528</td>
      <td>20</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-16</td>
      <td>3</td>
      <td>B001Q5QLP6A2NZQ7DSJV4AV2</td>
      <td>1</td>
      <td>I have been wanting these sandals since last s...</td>
      <td>2014</td>
      <td>I have been wanting these sandals since last s...</td>
    </tr>
    <tr>
      <th>71037</th>
      <td>71037</td>
      <td>A1N1AL8RQZZ74S</td>
      <td>B001Q5QLP6</td>
      <td>db4r62</td>
      <td>[0, 0]</td>
      <td>I love these sandals there are so comfortable....</td>
      <td>5.0</td>
      <td>Great Sandals</td>
      <td>1384041600</td>
      <td>11 10, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>154.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IlovethesesandalstherearesocomfortableSometime...</td>
      <td>GreatSandals</td>
      <td>122</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-10</td>
      <td>11</td>
      <td>B001Q5QLP6A1N1AL8RQZZ74S</td>
      <td>1</td>
      <td>I love these sandals there are so comfortable ...</td>
      <td>2013</td>
      <td>I love these sandals there are so comfortable....</td>
    </tr>
    <tr>
      <th>71038</th>
      <td>71038</td>
      <td>A3EOMRZFU33I6Z</td>
      <td>B001Q5QLP6</td>
      <td>Debby Lundell</td>
      <td>[0, 0]</td>
      <td>I got the larger size to fit my wide foot.  Ev...</td>
      <td>4.0</td>
      <td>They fit!</td>
      <td>1375488000</td>
      <td>08 3, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>150.0</td>
      <td>Shoes</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IgotthelargersizetofitmywidefootEveryonethatse...</td>
      <td>Theyfit</td>
      <td>118</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-03</td>
      <td>8</td>
      <td>B001Q5QLP6A3EOMRZFU33I6Z</td>
      <td>1</td>
      <td>I got the larger size to fit my wide foot  Eve...</td>
      <td>2013</td>
      <td>I got the larger size to fit my wide foot.  Ev...</td>
    </tr>
    <tr>
      <th>71039</th>
      <td>71039</td>
      <td>A1Y0N2NCM5LCGS</td>
      <td>B001Q5QLP6</td>
      <td>Deb</td>
      <td>[1, 2]</td>
      <td>These are very comfortable, cool shoes for hot...</td>
      <td>5.0</td>
      <td>Love 'em!</td>
      <td>1358899200</td>
      <td>01 23, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>139.0</td>
      <td>Shoes</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Theseareverycomfortablecoolshoesforhotandhumid...</td>
      <td>Loveem</td>
      <td>109</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-01-23</td>
      <td>1</td>
      <td>B001Q5QLP6A1Y0N2NCM5LCGS</td>
      <td>1</td>
      <td>These are very comfortable cool shoes for hot ...</td>
      <td>2013</td>
      <td>These are very comfortable, cool shoes for hot...</td>
    </tr>
    <tr>
      <th>71040</th>
      <td>71040</td>
      <td>A3TL89UYA5D1JJ</td>
      <td>B001Q5QLP6</td>
      <td>Deborah Diehl</td>
      <td>[2, 3]</td>
      <td>keens are much more narrow and smaller than th...</td>
      <td>1.0</td>
      <td>keens have changed</td>
      <td>1401408000</td>
      <td>05 30, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>110.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>keensaremuchmorenarrowandsmallerthantheyusedto...</td>
      <td>keenshavechanged</td>
      <td>87</td>
      <td>16</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-30</td>
      <td>5</td>
      <td>B001Q5QLP6A3TL89UYA5D1JJ</td>
      <td>0</td>
      <td>keens are much more narrow and smaller than th...</td>
      <td>2014</td>
      <td>keens are much more narrow and smaller than th...</td>
    </tr>
    <tr>
      <th>71041</th>
      <td>71041</td>
      <td>A2GOS755C86D8H</td>
      <td>B001Q5QLP6</td>
      <td>DeGrasse</td>
      <td>[1, 1]</td>
      <td>I am normally a size 6.5 or 7, but I ordered a...</td>
      <td>4.0</td>
      <td>Runs small for me!</td>
      <td>1337299200</td>
      <td>05 18, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>939.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Iamnormallyasize65or7butIorderedasize7andmyhee...</td>
      <td>Runssmallforme</td>
      <td>717</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-05-18</td>
      <td>5</td>
      <td>B001Q5QLP6A2GOS755C86D8H</td>
      <td>1</td>
      <td>I am normally a size  or  but I ordered a size...</td>
      <td>2012</td>
      <td>I am normally a size 6.5 or 7, but I ordered a...</td>
    </tr>
    <tr>
      <th>71042</th>
      <td>71042</td>
      <td>A3HKHQT8I1Y4AC</td>
      <td>B001Q5QLP6</td>
      <td>Diane "Diane"</td>
      <td>[0, 0]</td>
      <td>Love these, they are lighter weight, and very ...</td>
      <td>5.0</td>
      <td>Keen Whisper Sandal</td>
      <td>1378166400</td>
      <td>09 3, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>150.0</td>
      <td>Shoes</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Lovethesetheyarelighterweightandverycomfortabl...</td>
      <td>KeenWhisperSandal</td>
      <td>118</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-03</td>
      <td>9</td>
      <td>B001Q5QLP6A3HKHQT8I1Y4AC</td>
      <td>1</td>
      <td>Love these they are lighter weight and very co...</td>
      <td>2013</td>
      <td>Love these, they are lighter weight, and very ...</td>
    </tr>
    <tr>
      <th>71043</th>
      <td>71043</td>
      <td>A3MK1F1Y0SNKAL</td>
      <td>B001Q5QLP6</td>
      <td>dmvrlv</td>
      <td>[1, 1]</td>
      <td>My wife has a very hard time with her feet (VE...</td>
      <td>5.0</td>
      <td>Love 'em</td>
      <td>1401753600</td>
      <td>06 3, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>264.0</td>
      <td>Shoes</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>MywifehasaveryhardtimewithherfeetVERYhigharche...</td>
      <td>Loveem</td>
      <td>204</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-03</td>
      <td>6</td>
      <td>B001Q5QLP6A3MK1F1Y0SNKAL</td>
      <td>1</td>
      <td>My wife has a very hard time with her feet VER...</td>
      <td>2014</td>
      <td>My wife has a very hard time with her feet (VE...</td>
    </tr>
    <tr>
      <th>71044</th>
      <td>71044</td>
      <td>A2SK1KHW6WZ0D6</td>
      <td>B001Q5QLP6</td>
      <td>Dollye</td>
      <td>[0, 1]</td>
      <td>This is the first pair of Keens that I have bo...</td>
      <td>5.0</td>
      <td>Great Little Shoe -</td>
      <td>1349481600</td>
      <td>10 6, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>284.0</td>
      <td>Shoes</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThisisthefirstpairofKeensthatIhaveboughtIlovet...</td>
      <td>GreatLittleShoe</td>
      <td>223</td>
      <td>15</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-10-06</td>
      <td>10</td>
      <td>B001Q5QLP6A2SK1KHW6WZ0D6</td>
      <td>1</td>
      <td>This is the first pair of Keens that I have bo...</td>
      <td>2012</td>
      <td>This is the first pair of Keens that I have bo...</td>
    </tr>
    <tr>
      <th>71045</th>
      <td>71045</td>
      <td>A22Z0FZ6RUNWCB</td>
      <td>B001Q5QLP6</td>
      <td>Donna "Savvy Shopper"</td>
      <td>[0, 0]</td>
      <td>Glad I purchased these as they are very well c...</td>
      <td>5.0</td>
      <td>Very light and. Comfortable</td>
      <td>1398988800</td>
      <td>05 2, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>237.0</td>
      <td>Shoes</td>
      <td>27.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>GladIpurchasedtheseastheyareverywellconstructe...</td>
      <td>VerylightandComfortable</td>
      <td>185</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-02</td>
      <td>5</td>
      <td>B001Q5QLP6A22Z0FZ6RUNWCB</td>
      <td>1</td>
      <td>Glad I purchased these as they are very well c...</td>
      <td>2014</td>
      <td>Glad I purchased these as they are very well c...</td>
    </tr>
    <tr>
      <th>71046</th>
      <td>71046</td>
      <td>A2JXWKX9YY4M8F</td>
      <td>B001Q5QLP6</td>
      <td>Elizabeth A. Thrall "thrallz"</td>
      <td>[1, 1]</td>
      <td>Love these! These were my favorite walking aro...</td>
      <td>5.0</td>
      <td>Keen Woman's Whisper</td>
      <td>1314748800</td>
      <td>08 31, 2011</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>430.0</td>
      <td>Shoes</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>LovetheseTheseweremyfavoritewalkingaroundinDis...</td>
      <td>KeenWomansWhisper</td>
      <td>324</td>
      <td>17</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2011-08-31</td>
      <td>8</td>
      <td>B001Q5QLP6A2JXWKX9YY4M8F</td>
      <td>1</td>
      <td>Love these These were my favorite walking arou...</td>
      <td>2011</td>
      <td>Love these! These were my favorite walking aro...</td>
    </tr>
    <tr>
      <th>71047</th>
      <td>71047</td>
      <td>A1N15KUYZKLAZD</td>
      <td>B001Q5QLP6</td>
      <td>Elizabeth Kanous "super spender"</td>
      <td>[3, 4]</td>
      <td>It took me a long time to accept the nobby toe...</td>
      <td>3.0</td>
      <td>Sliding out the Back</td>
      <td>1339286400</td>
      <td>06 10, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>0.428571</td>
      <td>790.0</td>
      <td>Shoes</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IttookmealongtimetoacceptthenobbytoethatKeensh...</td>
      <td>SlidingouttheBack</td>
      <td>625</td>
      <td>17</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-06-10</td>
      <td>6</td>
      <td>B001Q5QLP6A1N15KUYZKLAZD</td>
      <td>0</td>
      <td>It took me a long time to accept the nobby toe...</td>
      <td>2012</td>
      <td>It took me a long time to accept the nobby toe...</td>
    </tr>
    <tr>
      <th>71048</th>
      <td>71048</td>
      <td>A2MK6IVDI7FGX2</td>
      <td>B001Q5QLP6</td>
      <td>Ellen K. Kremkus "carefulcookkay"</td>
      <td>[2, 3]</td>
      <td>I ordered a 9 1/2 because of the reviews and p...</td>
      <td>5.0</td>
      <td>Light and durable</td>
      <td>1392422400</td>
      <td>02 15, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>483.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Iordereda912becauseofthereviewsandprobablythes...</td>
      <td>Lightanddurable</td>
      <td>373</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-02-15</td>
      <td>2</td>
      <td>B001Q5QLP6A2MK6IVDI7FGX2</td>
      <td>1</td>
      <td>I ordered a   because of the reviews and proba...</td>
      <td>2014</td>
      <td>I ordered a 9 1/2 because of the reviews and p...</td>
    </tr>
    <tr>
      <th>71049</th>
      <td>71049</td>
      <td>A2LO4T2XMR8HSI</td>
      <td>B001Q5QLP6</td>
      <td>ellens</td>
      <td>[0, 0]</td>
      <td>Online it looked like I could adjust the heel ...</td>
      <td>3.0</td>
      <td>Heel too small - no way to really adjust</td>
      <td>1404691200</td>
      <td>07 7, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>139.0</td>
      <td>Shoes</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>OnlineitlookedlikeIcouldadjusttheheelusingthel...</td>
      <td>Heeltoosmallnowaytoreallyadjust</td>
      <td>111</td>
      <td>31</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-07</td>
      <td>7</td>
      <td>B001Q5QLP6A2LO4T2XMR8HSI</td>
      <td>0</td>
      <td>Online it looked like I could adjust the heel ...</td>
      <td>2014</td>
      <td>Online it looked like I could adjust the heel ...</td>
    </tr>
    <tr>
      <th>71050</th>
      <td>71050</td>
      <td>A2CJNNCBCI41EB</td>
      <td>B001Q5QLP6</td>
      <td>Fireflyhaven</td>
      <td>[0, 0]</td>
      <td>I have been a size 10 womens since i was 15. S...</td>
      <td>4.0</td>
      <td>Just a smidge bigger than expected</td>
      <td>1372032000</td>
      <td>06 24, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>560.0</td>
      <td>Shoes</td>
      <td>34.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Ihavebeenasize10womenssinceiwas15Standard95sne...</td>
      <td>Justasmidgebiggerthanexpected</td>
      <td>428</td>
      <td>29</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-24</td>
      <td>6</td>
      <td>B001Q5QLP6A2CJNNCBCI41EB</td>
      <td>1</td>
      <td>I have been a size  womens since i was  Standa...</td>
      <td>2013</td>
      <td>I have been a size 10 womens since i was 15. S...</td>
    </tr>
    <tr>
      <th>71051</th>
      <td>71051</td>
      <td>A1PP3JYGING2XL</td>
      <td>B001Q5QLP6</td>
      <td>Gee Bee</td>
      <td>[0, 0]</td>
      <td>They are soooo comfortable and so light.  The ...</td>
      <td>5.0</td>
      <td>I love these shoes</td>
      <td>1353456000</td>
      <td>11 21, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>142.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>TheyaresoooocomfortableandsolightThesizeistrue...</td>
      <td>Ilovetheseshoes</td>
      <td>108</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-11-21</td>
      <td>11</td>
      <td>B001Q5QLP6A1PP3JYGING2XL</td>
      <td>1</td>
      <td>They are soooo comfortable and so light  The s...</td>
      <td>2012</td>
      <td>They are soooo comfortable and so light.  The ...</td>
    </tr>
    <tr>
      <th>71052</th>
      <td>71052</td>
      <td>ASRQYEYA1C5QB</td>
      <td>B001Q5QLP6</td>
      <td>G  G</td>
      <td>[0, 0]</td>
      <td>These sandals are a perfect fit.  The black ar...</td>
      <td>5.0</td>
      <td>Excellent sandals.</td>
      <td>1368576000</td>
      <td>05 15, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>217.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThesesandalsareaperfectfitTheblackaresmartlook...</td>
      <td>Excellentsandals</td>
      <td>170</td>
      <td>16</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-15</td>
      <td>5</td>
      <td>B001Q5QLP6ASRQYEYA1C5QB</td>
      <td>1</td>
      <td>These sandals are a perfect fit  The black are...</td>
      <td>2013</td>
      <td>These sandals are a perfect fit.  The black ar...</td>
    </tr>
    <tr>
      <th>71053</th>
      <td>71053</td>
      <td>A88BPHHETU0SD</td>
      <td>B001Q5QLP6</td>
      <td>GL</td>
      <td>[0, 0]</td>
      <td>We purchased Keens for the entire family upon ...</td>
      <td>5.0</td>
      <td>Amazing shoes for travel, walking in various e...</td>
      <td>1405123200</td>
      <td>07 12, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>837.0</td>
      <td>Shoes</td>
      <td>53.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>WepurchasedKeensfortheentirefamilyupontherecom...</td>
      <td>Amazingshoesfortravelwalkinginvariouselements</td>
      <td>654</td>
      <td>45</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-12</td>
      <td>7</td>
      <td>B001Q5QLP6A88BPHHETU0SD</td>
      <td>1</td>
      <td>We purchased Keens for the entire family upon ...</td>
      <td>2014</td>
      <td>We purchased Keens for the entire family upon ...</td>
    </tr>
    <tr>
      <th>71054</th>
      <td>71054</td>
      <td>A1HSOIX6YX0UIZ</td>
      <td>B001Q5QLP6</td>
      <td>gooch49</td>
      <td>[1, 1]</td>
      <td>This is my third pair of Keen Whisper Sandal's...</td>
      <td>5.0</td>
      <td>Great Comfort</td>
      <td>1374192000</td>
      <td>07 19, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>248.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThisismythirdpairofKeenWhisperSandalsComfortab...</td>
      <td>GreatComfort</td>
      <td>196</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-07-19</td>
      <td>7</td>
      <td>B001Q5QLP6A1HSOIX6YX0UIZ</td>
      <td>1</td>
      <td>This is my third pair of Keen Whisper Sandals ...</td>
      <td>2013</td>
      <td>This is my third pair of Keen Whisper Sandal's...</td>
    </tr>
    <tr>
      <th>71055</th>
      <td>71055</td>
      <td>AXRT5Z0W7WUSR</td>
      <td>B001Q5QLP6</td>
      <td>Graceonfire</td>
      <td>[0, 0]</td>
      <td>If you don't buy Keens...you are stupid. Proba...</td>
      <td>5.0</td>
      <td>Always the best shoe</td>
      <td>1377388800</td>
      <td>08 25, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>139.0</td>
      <td>Shoes</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IfyoudontbuyKeensyouarestupidProbablythebestfi...</td>
      <td>Alwaysthebestshoe</td>
      <td>111</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-25</td>
      <td>8</td>
      <td>B001Q5QLP6AXRT5Z0W7WUSR</td>
      <td>1</td>
      <td>If you dont buy Keensyou are stupid Probably t...</td>
      <td>2013</td>
      <td>If you don't buy Keens...you are stupid. Proba...</td>
    </tr>
    <tr>
      <th>71056</th>
      <td>71056</td>
      <td>A256FNLX0OPMR5</td>
      <td>B001Q5QLP6</td>
      <td>gswilson</td>
      <td>[0, 0]</td>
      <td>Bought shoe for color combination - love every...</td>
      <td>5.0</td>
      <td>Could wear every day!</td>
      <td>1369267200</td>
      <td>05 23, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>207.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Boughtshoeforcolorcombinationloveeverythingabo...</td>
      <td>Couldweareveryday</td>
      <td>166</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-23</td>
      <td>5</td>
      <td>B001Q5QLP6A256FNLX0OPMR5</td>
      <td>1</td>
      <td>Bought shoe for color combination  love everyt...</td>
      <td>2013</td>
      <td>Bought shoe for color combination - love every...</td>
    </tr>
    <tr>
      <th>71057</th>
      <td>71057</td>
      <td>A382A4DO3XQWVT</td>
      <td>B001Q5QLP6</td>
      <td>Happy Mac User "mb_77"</td>
      <td>[0, 0]</td>
      <td>I love these sandals, they were true to size a...</td>
      <td>4.0</td>
      <td>Great sandals at a great price!</td>
      <td>1386979200</td>
      <td>12 14, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>134.0</td>
      <td>Shoes</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Ilovethesesandalstheyweretruetosizeandlookgrea...</td>
      <td>Greatsandalsatagreatprice</td>
      <td>106</td>
      <td>25</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-12-14</td>
      <td>12</td>
      <td>B001Q5QLP6A382A4DO3XQWVT</td>
      <td>1</td>
      <td>I love these sandals they were true to size an...</td>
      <td>2013</td>
      <td>I love these sandals, they were true to size a...</td>
    </tr>
    <tr>
      <th>71058</th>
      <td>71058</td>
      <td>A2NJSLQAPXXTAS</td>
      <td>B001Q5QLP6</td>
      <td>hopidopi</td>
      <td>[1, 1]</td>
      <td>I have a very wide foot, and these shoes are g...</td>
      <td>5.0</td>
      <td>LOVE these shoes!</td>
      <td>1359417600</td>
      <td>01 29, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>415.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IhaveaverywidefootandtheseshoesaregreatWhenthe...</td>
      <td>LOVEtheseshoes</td>
      <td>318</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-01-29</td>
      <td>1</td>
      <td>B001Q5QLP6A2NJSLQAPXXTAS</td>
      <td>1</td>
      <td>I have a very wide foot and these shoes are gr...</td>
      <td>2013</td>
      <td>I have a very wide foot, and these shoes are g...</td>
    </tr>
    <tr>
      <th>71059</th>
      <td>71059</td>
      <td>A311TT3L5IOMPP</td>
      <td>B001Q5QLP6</td>
      <td>Infiniti Lover</td>
      <td>[0, 0]</td>
      <td>They fit perfectly and this is the first Keen ...</td>
      <td>5.0</td>
      <td>Perfect</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>417.0</td>
      <td>Shoes</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>TheyfitperfectlyandthisisthefirstKeenIhavebeen...</td>
      <td>Perfect</td>
      <td>325</td>
      <td>7</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B001Q5QLP6A311TT3L5IOMPP</td>
      <td>1</td>
      <td>They fit perfectly and this is the first Keen ...</td>
      <td>2013</td>
      <td>They fit perfectly and this is the first Keen ...</td>
    </tr>
    <tr>
      <th>71060</th>
      <td>71060</td>
      <td>A1W7WYGM5AM97S</td>
      <td>B001Q5QLP6</td>
      <td>islandgirl "fran"</td>
      <td>[0, 0]</td>
      <td>Fit well, looks good. One thing I might mentio...</td>
      <td>5.0</td>
      <td>Very nice shoe</td>
      <td>1372982400</td>
      <td>07 5, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>601.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>FitwelllooksgoodOnethingImightmentionisthatthe...</td>
      <td>Veryniceshoe</td>
      <td>465</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-07-05</td>
      <td>7</td>
      <td>B001Q5QLP6A1W7WYGM5AM97S</td>
      <td>1</td>
      <td>Fit well looks good One thing I might mention ...</td>
      <td>2013</td>
      <td>Fit well, looks good. One thing I might mentio...</td>
    </tr>
    <tr>
      <th>71061</th>
      <td>71061</td>
      <td>A4CL3D1XP3JQT</td>
      <td>B001Q5QLP6</td>
      <td>jaslew99</td>
      <td>[0, 0]</td>
      <td>Every single shoe I get with the exception of ...</td>
      <td>5.0</td>
      <td>no blisters</td>
      <td>1379030400</td>
      <td>09 13, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>208.0</td>
      <td>Shoes</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>EverysingleshoeIgetwiththeexceptionofflipflops...</td>
      <td>noblisters</td>
      <td>164</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-13</td>
      <td>9</td>
      <td>B001Q5QLP6A4CL3D1XP3JQT</td>
      <td>1</td>
      <td>Every single shoe I get with the exception of ...</td>
      <td>2013</td>
      <td>Every single shoe I get with the exception of ...</td>
    </tr>
    <tr>
      <th>71062</th>
      <td>71062</td>
      <td>A1EXE4MS0UMWSM</td>
      <td>B001Q5QLP6</td>
      <td>JK</td>
      <td>[0, 0]</td>
      <td>My feet are a Wide size 5, and these were way ...</td>
      <td>3.0</td>
      <td>Size 5 is too small and narrow for my feet</td>
      <td>1401753600</td>
      <td>06 3, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>164.0</td>
      <td>Shoes</td>
      <td>42.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>MyfeetareaWidesize5andthesewerewaytoonarrowfor...</td>
      <td>Size5istoosmallandnarrowformyfeet</td>
      <td>122</td>
      <td>33</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-03</td>
      <td>6</td>
      <td>B001Q5QLP6A1EXE4MS0UMWSM</td>
      <td>0</td>
      <td>My feet are a Wide size  and these were way to...</td>
      <td>2014</td>
      <td>My feet are a Wide size 5, and these were way ...</td>
    </tr>
    <tr>
      <th>71063</th>
      <td>71063</td>
      <td>A2DOK7M6MTOAJQ</td>
      <td>B001Q5QLP6</td>
      <td>Joanne M. Carr</td>
      <td>[1, 1]</td>
      <td>Used my Keen shoes to hike to waterfalls, go k...</td>
      <td>5.0</td>
      <td>Purchased for Hawaii vacation</td>
      <td>1388534400</td>
      <td>01 1, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>516.0</td>
      <td>Shoes</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>UsedmyKeenshoestohiketowaterfallsgokayakingonz...</td>
      <td>PurchasedforHawaiivacation</td>
      <td>408</td>
      <td>26</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-01-01</td>
      <td>1</td>
      <td>B001Q5QLP6A2DOK7M6MTOAJQ</td>
      <td>1</td>
      <td>Used my Keen shoes to hike to waterfalls go ka...</td>
      <td>2014</td>
      <td>Used my Keen shoes to hike to waterfalls, go k...</td>
    </tr>
    <tr>
      <th>71064</th>
      <td>71064</td>
      <td>AM54IIJJVLW0C</td>
      <td>B001Q5QLP6</td>
      <td>Jonathan D. Smith</td>
      <td>[0, 0]</td>
      <td>A good sandal and holding up well so far this ...</td>
      <td>5.0</td>
      <td>Good</td>
      <td>1342656000</td>
      <td>07 19, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>114.0</td>
      <td>Shoes</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>AgoodsandalandholdingupwellsofarthissummerMywi...</td>
      <td>Good</td>
      <td>90</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-07-19</td>
      <td>7</td>
      <td>B001Q5QLP6AM54IIJJVLW0C</td>
      <td>1</td>
      <td>A good sandal and holding up well so far this ...</td>
      <td>2012</td>
      <td>A good sandal and holding up well so far this ...</td>
    </tr>
    <tr>
      <th>71065</th>
      <td>71065</td>
      <td>A1YFSX27LKN9M0</td>
      <td>B001Q5QLP6</td>
      <td>Jordy's Mom</td>
      <td>[0, 0]</td>
      <td>NOTE. ...the color is NOT as pictured.  It is ...</td>
      <td>4.0</td>
      <td>NOT YELLOW/GREY!</td>
      <td>1397347200</td>
      <td>04 13, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>209.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>NOTEthecolorisNOTaspicturedItisNOTyellowcremew...</td>
      <td>NOTYELLOWGREY</td>
      <td>153</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-04-13</td>
      <td>4</td>
      <td>B001Q5QLP6A1YFSX27LKN9M0</td>
      <td>1</td>
      <td>NOTE the color is NOT as pictured  It is NOT y...</td>
      <td>2014</td>
      <td>NOTE. ...the color is NOT as pictured.  It is ...</td>
    </tr>
    <tr>
      <th>71066</th>
      <td>71066</td>
      <td>A1198YWSG4647A</td>
      <td>B001Q5QLP6</td>
      <td>J Rease</td>
      <td>[0, 0]</td>
      <td>They run a little short but I'd read the revie...</td>
      <td>5.0</td>
      <td>Love them</td>
      <td>1402963200</td>
      <td>06 17, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>256.0</td>
      <td>Shoes</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>TheyrunalittleshortbutIdreadthereviewsandorder...</td>
      <td>Lovethem</td>
      <td>202</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-17</td>
      <td>6</td>
      <td>B001Q5QLP6A1198YWSG4647A</td>
      <td>1</td>
      <td>They run a little short but Id read the review...</td>
      <td>2014</td>
      <td>They run a little short but I'd read the revie...</td>
    </tr>
    <tr>
      <th>71067</th>
      <td>71067</td>
      <td>A1UKMT59NN74J5</td>
      <td>B001Q5QLP6</td>
      <td>kaileypete "danopete"</td>
      <td>[0, 0]</td>
      <td>I own several pairs of Keens - sandals, shoes,...</td>
      <td>5.0</td>
      <td>Comfortable and Durable are my Keens</td>
      <td>1375401600</td>
      <td>08 2, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>540.0</td>
      <td>Shoes</td>
      <td>36.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IownseveralpairsofKeenssandalsshoeswatersandal...</td>
      <td>ComfortableandDurablearemyKeens</td>
      <td>425</td>
      <td>31</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-02</td>
      <td>8</td>
      <td>B001Q5QLP6A1UKMT59NN74J5</td>
      <td>1</td>
      <td>I own several pairs of Keens  sandals shoes wa...</td>
      <td>2013</td>
      <td>I own several pairs of Keens - sandals, shoes,...</td>
    </tr>
    <tr>
      <th>71068</th>
      <td>71068</td>
      <td>AW6J9IILGOZY3</td>
      <td>B001Q5QLP6</td>
      <td>Katawampas</td>
      <td>[0, 0]</td>
      <td>These sandals are so comfortable &amp; can go from...</td>
      <td>5.0</td>
      <td>Very Comfortable &amp; Fit Like My Other Keen Shoes</td>
      <td>1384473600</td>
      <td>11 15, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>387.0</td>
      <td>Shoes</td>
      <td>47.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Thesesandalsaresocomfortablecangofromwatertoda...</td>
      <td>VeryComfortableFitLikeMyOtherKeenShoes</td>
      <td>298</td>
      <td>38</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-15</td>
      <td>11</td>
      <td>B001Q5QLP6AW6J9IILGOZY3</td>
      <td>1</td>
      <td>These sandals are so comfortable  can go from ...</td>
      <td>2013</td>
      <td>These sandals are so comfortable &amp; can go from...</td>
    </tr>
    <tr>
      <th>71069</th>
      <td>71069</td>
      <td>AFRKTYRYDVJ7R</td>
      <td>B001Q5QLP6</td>
      <td>Kathleen Delaney "d.d."</td>
      <td>[0, 0]</td>
      <td>This is my second pair.  I loved the first pai...</td>
      <td>5.0</td>
      <td>second pair</td>
      <td>1385942400</td>
      <td>12 2, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>130.0</td>
      <td>Shoes</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisismysecondpairIlovedthefirstpairThedealont...</td>
      <td>secondpair</td>
      <td>96</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-12-02</td>
      <td>12</td>
      <td>B001Q5QLP6AFRKTYRYDVJ7R</td>
      <td>1</td>
      <td>This is my second pair  I loved the first pair...</td>
      <td>2013</td>
      <td>This is my second pair.  I loved the first pai...</td>
    </tr>
    <tr>
      <th>71070</th>
      <td>71070</td>
      <td>A3328AZHVFGA3S</td>
      <td>B001Q5QLP6</td>
      <td>Kathryn</td>
      <td>[0, 0]</td>
      <td>I wear a 6.5 to 7 in normal shoes and a 8 to 8...</td>
      <td>5.0</td>
      <td>Buy like a tennis shoe in size</td>
      <td>1384387200</td>
      <td>11 14, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>451.0</td>
      <td>Shoes</td>
      <td>30.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iweara65to7innormalshoesanda8to85inrunningshoe...</td>
      <td>Buylikeatennisshoeinsize</td>
      <td>342</td>
      <td>24</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-14</td>
      <td>11</td>
      <td>B001Q5QLP6A3328AZHVFGA3S</td>
      <td>1</td>
      <td>I wear a  to  in normal shoes and a  to  in ru...</td>
      <td>2013</td>
      <td>I wear a 6.5 to 7 in normal shoes and a 8 to 8...</td>
    </tr>
    <tr>
      <th>71071</th>
      <td>71071</td>
      <td>A12AMCBUFJYX9H</td>
      <td>B001Q5QLP6</td>
      <td>Kathy Clark</td>
      <td>[0, 0]</td>
      <td>Super comfy, great fit.  And I like that I can...</td>
      <td>5.0</td>
      <td>Love these</td>
      <td>1398297600</td>
      <td>04 24, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SupercomfygreatfitAndIlikethatIcanwashthemoffw...</td>
      <td>Lovethese</td>
      <td>91</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-04-24</td>
      <td>4</td>
      <td>B001Q5QLP6A12AMCBUFJYX9H</td>
      <td>1</td>
      <td>Super comfy great fit  And I like that I can w...</td>
      <td>2014</td>
      <td>Super comfy, great fit.  And I like that I can...</td>
    </tr>
    <tr>
      <th>71072</th>
      <td>71072</td>
      <td>A1YFEYYDFZCLHL</td>
      <td>B001Q5QLP6</td>
      <td>Katt978</td>
      <td>[0, 0]</td>
      <td>I tried these on at a local camping/hiking sto...</td>
      <td>5.0</td>
      <td>Great Sandals!</td>
      <td>1374969600</td>
      <td>07 28, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>482.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Itriedtheseonatalocalcampinghikingstoreandfoun...</td>
      <td>GreatSandals</td>
      <td>372</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-07-28</td>
      <td>7</td>
      <td>B001Q5QLP6A1YFEYYDFZCLHL</td>
      <td>1</td>
      <td>I tried these on at a local campinghiking stor...</td>
      <td>2013</td>
      <td>I tried these on at a local camping/hiking sto...</td>
    </tr>
    <tr>
      <th>71073</th>
      <td>71073</td>
      <td>A15DGG4GJ1WO74</td>
      <td>B001Q5QLP6</td>
      <td>kedimarlon</td>
      <td>[1, 1]</td>
      <td>Keen Women's Whisper...I ordered 8.5 which is ...</td>
      <td>4.0</td>
      <td>So comfortable!</td>
      <td>1347667200</td>
      <td>09 15, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>233.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>KeenWomensWhisperIordered85whichismyshoesizean...</td>
      <td>Socomfortable</td>
      <td>179</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-09-15</td>
      <td>9</td>
      <td>B001Q5QLP6A15DGG4GJ1WO74</td>
      <td>1</td>
      <td>Keen Womens WhisperI ordered  which is my shoe...</td>
      <td>2012</td>
      <td>Keen Women's Whisper...I ordered 8.5 which is ...</td>
    </tr>
    <tr>
      <th>71074</th>
      <td>71074</td>
      <td>A679OAVPIKV9Z</td>
      <td>B001Q5QLP6</td>
      <td>Kindle Customer</td>
      <td>[10, 15]</td>
      <td>Just got these in the mail today and love them...</td>
      <td>5.0</td>
      <td>Comfortable &amp; versatile</td>
      <td>1303948800</td>
      <td>04 28, 2011</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1.000000</td>
      <td>433.0</td>
      <td>Shoes</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>JustgottheseinthemailtodayandlovethemalreadySe...</td>
      <td>Comfortableversatile</td>
      <td>339</td>
      <td>20</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2011-04-28</td>
      <td>4</td>
      <td>B001Q5QLP6A679OAVPIKV9Z</td>
      <td>1</td>
      <td>Just got these in the mail today and love them...</td>
      <td>2011</td>
      <td>Just got these in the mail today and love them...</td>
    </tr>
    <tr>
      <th>71075</th>
      <td>71075</td>
      <td>A3QSPA8SKEKE2K</td>
      <td>B001Q5QLP6</td>
      <td>KMJ</td>
      <td>[1, 1]</td>
      <td>Color is great and the fit is as expected.  On...</td>
      <td>4.0</td>
      <td>Comforable sandal</td>
      <td>1403395200</td>
      <td>06 22, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>299.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ColorisgreatandthefitisasexpectedOnlyobstaclef...</td>
      <td>Comforablesandal</td>
      <td>229</td>
      <td>16</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-22</td>
      <td>6</td>
      <td>B001Q5QLP6A3QSPA8SKEKE2K</td>
      <td>1</td>
      <td>Color is great and the fit is as expected  Onl...</td>
      <td>2014</td>
      <td>Color is great and the fit is as expected.  On...</td>
    </tr>
    <tr>
      <th>71076</th>
      <td>71076</td>
      <td>A1AFXP7V5ROR47</td>
      <td>B001Q5QLP6</td>
      <td>K. Morgan</td>
      <td>[0, 0]</td>
      <td>I bought myself these sandals, as well as the ...</td>
      <td>5.0</td>
      <td>Don't leave home without them!</td>
      <td>1358640000</td>
      <td>01 20, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1008.0</td>
      <td>Shoes</td>
      <td>30.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iboughtmyselfthesesandalsaswellastheyouthonesf...</td>
      <td>Dontleavehomewithoutthem</td>
      <td>789</td>
      <td>24</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-01-20</td>
      <td>1</td>
      <td>B001Q5QLP6A1AFXP7V5ROR47</td>
      <td>1</td>
      <td>I bought myself these sandals as well as the y...</td>
      <td>2013</td>
      <td>I bought myself these sandals, as well as the ...</td>
    </tr>
    <tr>
      <th>71077</th>
      <td>71077</td>
      <td>A278IQIDZ18VS0</td>
      <td>B001Q5QLP6</td>
      <td>Kruiser Kate "KRxby"</td>
      <td>[0, 0]</td>
      <td>I was looking for some good closed-toe hiking ...</td>
      <td>5.0</td>
      <td>Very light weight and super comfortable</td>
      <td>1401494400</td>
      <td>05 31, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>411.0</td>
      <td>Shoes</td>
      <td>39.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IwaslookingforsomegoodclosedtoehikingsandalsIn...</td>
      <td>Verylightweightandsupercomfortable</td>
      <td>326</td>
      <td>34</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-31</td>
      <td>5</td>
      <td>B001Q5QLP6A278IQIDZ18VS0</td>
      <td>1</td>
      <td>I was looking for some good closedtoe hiking s...</td>
      <td>2014</td>
      <td>I was looking for some good closed-toe hiking ...</td>
    </tr>
    <tr>
      <th>71078</th>
      <td>71078</td>
      <td>A39TOXC7IRVEGG</td>
      <td>B001Q5QLP6</td>
      <td>Lakegirl70</td>
      <td>[0, 1]</td>
      <td>I own many pairs of Keen and I'm never disappo...</td>
      <td>5.0</td>
      <td>Keentastic!</td>
      <td>1372032000</td>
      <td>06 24, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>253.0</td>
      <td>Shoes</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IownmanypairsofKeenandImneverdisappointedIneed...</td>
      <td>Keentastic</td>
      <td>185</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-24</td>
      <td>6</td>
      <td>B001Q5QLP6A39TOXC7IRVEGG</td>
      <td>1</td>
      <td>I own many pairs of Keen and Im never disappoi...</td>
      <td>2013</td>
      <td>I own many pairs of Keen and I'm never disappo...</td>
    </tr>
    <tr>
      <th>71079</th>
      <td>71079</td>
      <td>A1GUX6R8DV3ZLY</td>
      <td>B001Q5QLP6</td>
      <td>Lauren A.</td>
      <td>[0, 0]</td>
      <td>I am generally a "fashion first" kind of girl,...</td>
      <td>5.0</td>
      <td>Very comfortable walking sandal</td>
      <td>1368748800</td>
      <td>05 17, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1503.0</td>
      <td>Shoes</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iamgenerallyafashionfirstkindofgirlbutwithanup...</td>
      <td>Verycomfortablewalkingsandal</td>
      <td>1155</td>
      <td>28</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-17</td>
      <td>5</td>
      <td>B001Q5QLP6A1GUX6R8DV3ZLY</td>
      <td>1</td>
      <td>I am generally a fashion first kind of girl bu...</td>
      <td>2013</td>
      <td>I am generally a "fashion first" kind of girl,...</td>
    </tr>
    <tr>
      <th>71080</th>
      <td>71080</td>
      <td>A2F9DHPEUE1TS9</td>
      <td>B001Q5QLP6</td>
      <td>L. D. Hagedorn</td>
      <td>[1, 1]</td>
      <td>After 45 years of running rivers and wearing c...</td>
      <td>5.0</td>
      <td>Favorite river shoe</td>
      <td>1373414400</td>
      <td>07 10, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>595.0</td>
      <td>Shoes</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>After45yearsofrunningriversandwearingcountless...</td>
      <td>Favoriterivershoe</td>
      <td>458</td>
      <td>17</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-07-10</td>
      <td>7</td>
      <td>B001Q5QLP6A2F9DHPEUE1TS9</td>
      <td>1</td>
      <td>After  years of running rivers and wearing cou...</td>
      <td>2013</td>
      <td>After 45 years of running rivers and wearing c...</td>
    </tr>
    <tr>
      <th>71081</th>
      <td>71081</td>
      <td>A1CIQEP3E8L7NC</td>
      <td>B001Q5QLP6</td>
      <td>Leslie</td>
      <td>[4, 6]</td>
      <td>I discovered the Keen brand completely by acci...</td>
      <td>5.0</td>
      <td>LOVE KEEN SHOES!!!</td>
      <td>1329955200</td>
      <td>02 23, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>4</td>
      <td>6</td>
      <td>10</td>
      <td>0.400000</td>
      <td>552.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IdiscoveredtheKeenbrandcompletelybyaccidentIwa...</td>
      <td>LOVEKEENSHOES</td>
      <td>443</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-02-23</td>
      <td>2</td>
      <td>B001Q5QLP6A1CIQEP3E8L7NC</td>
      <td>1</td>
      <td>I discovered the Keen brand completely by acci...</td>
      <td>2012</td>
      <td>I discovered the Keen brand completely by acci...</td>
    </tr>
    <tr>
      <th>71082</th>
      <td>71082</td>
      <td>AN0JQ9QGOFN9S</td>
      <td>B001Q5QLP6</td>
      <td>Lil baby "lovethebooks"</td>
      <td>[0, 0]</td>
      <td>I have a long narrow foot and need lots of sup...</td>
      <td>4.0</td>
      <td>My second pair</td>
      <td>1386201600</td>
      <td>12 5, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>932.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IhavealongnarrowfootandneedlotsofsupportHaving...</td>
      <td>Mysecondpair</td>
      <td>747</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-12-05</td>
      <td>12</td>
      <td>B001Q5QLP6AN0JQ9QGOFN9S</td>
      <td>1</td>
      <td>I have a long narrow foot and need lots of sup...</td>
      <td>2013</td>
      <td>I have a long narrow foot and need lots of sup...</td>
    </tr>
    <tr>
      <th>71083</th>
      <td>71083</td>
      <td>A3N3K9BN1KT86H</td>
      <td>B001Q5QLP6</td>
      <td>Lindsey Comings</td>
      <td>[0, 0]</td>
      <td>I always wanted a pair of Keen's and these are...</td>
      <td>5.0</td>
      <td>LOVE!!</td>
      <td>1402444800</td>
      <td>06 11, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>116.0</td>
      <td>Shoes</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IalwayswantedapairofKeensandtheseareperfectLov...</td>
      <td>LOVE</td>
      <td>89</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-11</td>
      <td>6</td>
      <td>B001Q5QLP6A3N3K9BN1KT86H</td>
      <td>1</td>
      <td>I always wanted a pair of Keens and these are ...</td>
      <td>2014</td>
      <td>I always wanted a pair of Keen's and these are...</td>
    </tr>
    <tr>
      <th>71084</th>
      <td>71084</td>
      <td>A2P1U6RPELLMK6</td>
      <td>B001Q5QLP6</td>
      <td>Lisa Scherber "lisaann9"</td>
      <td>[0, 0]</td>
      <td>This green makes for a great neutral color to ...</td>
      <td>5.0</td>
      <td>Great Neutral</td>
      <td>1391126400</td>
      <td>01 31, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>144.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Thisgreenmakesforagreatneutralcolortowearwithj...</td>
      <td>GreatNeutral</td>
      <td>115</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-01-31</td>
      <td>1</td>
      <td>B001Q5QLP6A2P1U6RPELLMK6</td>
      <td>1</td>
      <td>This green makes for a great neutral color to ...</td>
      <td>2014</td>
      <td>This green makes for a great neutral color to ...</td>
    </tr>
    <tr>
      <th>71085</th>
      <td>71085</td>
      <td>A2SUUFLSEGMD5A</td>
      <td>B001Q5QLP6</td>
      <td>L. Kelly</td>
      <td>[0, 0]</td>
      <td>I wear an 11 medium in womens Keen hiking boot...</td>
      <td>4.0</td>
      <td>long and narrow in size 11 plus little toe hit...</td>
      <td>1404777600</td>
      <td>07 8, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1664.0</td>
      <td>Shoes</td>
      <td>57.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iwearan11mediuminwomensKeenhikingbootsBryceSus...</td>
      <td>longandnarrowinsize11pluslittletoehitsstrangely</td>
      <td>1276</td>
      <td>47</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-08</td>
      <td>7</td>
      <td>B001Q5QLP6A2SUUFLSEGMD5A</td>
      <td>1</td>
      <td>I wear an  medium in womens Keen hiking boots ...</td>
      <td>2014</td>
      <td>I wear an 11 medium in womens Keen hiking boot...</td>
    </tr>
    <tr>
      <th>71086</th>
      <td>71086</td>
      <td>A3NIHYKIC4U9K3</td>
      <td>B001Q5QLP6</td>
      <td>lkp "gracie parra"</td>
      <td>[1, 1]</td>
      <td>I buy KEENS every summer for my daughters.  Th...</td>
      <td>5.0</td>
      <td>wonderful shoes for my kid's growing feet</td>
      <td>1401840000</td>
      <td>06 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>493.0</td>
      <td>Shoes</td>
      <td>41.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IbuyKEENSeverysummerformydaughtersThecomfortan...</td>
      <td>wonderfulshoesformykidsgrowingfeet</td>
      <td>387</td>
      <td>34</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-04</td>
      <td>6</td>
      <td>B001Q5QLP6A3NIHYKIC4U9K3</td>
      <td>1</td>
      <td>I buy KEENS every summer for my daughters  The...</td>
      <td>2014</td>
      <td>I buy KEENS every summer for my daughters.  Th...</td>
    </tr>
    <tr>
      <th>71087</th>
      <td>71087</td>
      <td>A1DIS2BIR5O9J0</td>
      <td>B001Q5QLP6</td>
      <td>LuvsAmazon</td>
      <td>[0, 0]</td>
      <td>I have older Keens in a size 7 (usually wear 7...</td>
      <td>5.0</td>
      <td>Comfy and cushioned...Love them!</td>
      <td>1402963200</td>
      <td>06 17, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>301.0</td>
      <td>Shoes</td>
      <td>32.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IhaveolderKeensinasize7usuallywear7insandalsan...</td>
      <td>ComfyandcushionedLovethem</td>
      <td>226</td>
      <td>25</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-17</td>
      <td>6</td>
      <td>B001Q5QLP6A1DIS2BIR5O9J0</td>
      <td>1</td>
      <td>I have older Keens in a size  usually wear  in...</td>
      <td>2014</td>
      <td>I have older Keens in a size 7 (usually wear 7...</td>
    </tr>
    <tr>
      <th>71088</th>
      <td>71088</td>
      <td>A32ZUD7XZXZHVU</td>
      <td>B001Q5QLP6</td>
      <td>Marilyn A. Cole</td>
      <td>[0, 0]</td>
      <td>I love the shoe and the feel and fit.  Very li...</td>
      <td>2.0</td>
      <td>Product OK, Correctness of Shipment, NOT</td>
      <td>1378339200</td>
      <td>09 5, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>553.0</td>
      <td>Shoes</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IlovetheshoeandthefeelandfitVerylightandcomfor...</td>
      <td>ProductOKCorrectnessofShipmentNOT</td>
      <td>430</td>
      <td>33</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-05</td>
      <td>9</td>
      <td>B001Q5QLP6A32ZUD7XZXZHVU</td>
      <td>0</td>
      <td>I love the shoe and the feel and fit  Very lig...</td>
      <td>2013</td>
      <td>I love the shoe and the feel and fit.  Very li...</td>
    </tr>
    <tr>
      <th>71089</th>
      <td>71089</td>
      <td>A1339KM0F0XQJD</td>
      <td>B001Q5QLP6</td>
      <td>Mark Twain "soul music fan"</td>
      <td>[0, 0]</td>
      <td>Fit is perfect, nice support. No itchy places....</td>
      <td>5.0</td>
      <td>Love this shoe!</td>
      <td>1372550400</td>
      <td>06 30, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>123.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>FitisperfectnicesupportNoitchyplacesFitrightou...</td>
      <td>Lovethisshoe</td>
      <td>93</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-30</td>
      <td>6</td>
      <td>B001Q5QLP6A1339KM0F0XQJD</td>
      <td>1</td>
      <td>Fit is perfect nice support No itchy places Fi...</td>
      <td>2013</td>
      <td>Fit is perfect, nice support. No itchy places....</td>
    </tr>
    <tr>
      <th>71090</th>
      <td>71090</td>
      <td>A37YML33PL1VFV</td>
      <td>B001Q5QLP6</td>
      <td>Marybeth Hicks</td>
      <td>[0, 0]</td>
      <td>These are great shoes.  I have a pair of merre...</td>
      <td>5.0</td>
      <td>great florida sandal</td>
      <td>1385251200</td>
      <td>11 24, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>409.0</td>
      <td>Shoes</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThesearegreatshoesIhaveapairofmerrellswhichhav...</td>
      <td>greatfloridasandal</td>
      <td>321</td>
      <td>18</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-24</td>
      <td>11</td>
      <td>B001Q5QLP6A37YML33PL1VFV</td>
      <td>1</td>
      <td>These are great shoes  I have a pair of merrel...</td>
      <td>2013</td>
      <td>These are great shoes.  I have a pair of merre...</td>
    </tr>
    <tr>
      <th>71091</th>
      <td>71091</td>
      <td>A2LRIOR8IBIW5K</td>
      <td>B001Q5QLP6</td>
      <td>Mary M. Scholten</td>
      <td>[0, 0]</td>
      <td>I have a number of shoes by Keen because of th...</td>
      <td>5.0</td>
      <td>Comfy Keen</td>
      <td>1404604800</td>
      <td>07 6, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>201.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IhaveanumberofshoesbyKeenbecauseoftheircomfort...</td>
      <td>ComfyKeen</td>
      <td>151</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-06</td>
      <td>7</td>
      <td>B001Q5QLP6A2LRIOR8IBIW5K</td>
      <td>1</td>
      <td>I have a number of shoes by Keen because of th...</td>
      <td>2014</td>
      <td>I have a number of shoes by Keen because of th...</td>
    </tr>
    <tr>
      <th>71092</th>
      <td>71092</td>
      <td>A21I9NKCG66B5G</td>
      <td>B001Q5QLP6</td>
      <td>merseyboo</td>
      <td>[2, 2]</td>
      <td>First of all, the sandle is a Keen so you know...</td>
      <td>5.0</td>
      <td>Wonderful Keen Sandle</td>
      <td>1361318400</td>
      <td>02 20, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0.500000</td>
      <td>246.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>FirstofallthesandleisaKeensoyouknowitswonderfu...</td>
      <td>WonderfulKeenSandle</td>
      <td>188</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-02-20</td>
      <td>2</td>
      <td>B001Q5QLP6A21I9NKCG66B5G</td>
      <td>1</td>
      <td>First of all the sandle is a Keen so you know ...</td>
      <td>2013</td>
      <td>First of all, the sandle is a Keen so you know...</td>
    </tr>
    <tr>
      <th>71093</th>
      <td>71093</td>
      <td>A2OBNRYDTITU7F</td>
      <td>B001Q5QLP6</td>
      <td>michelle</td>
      <td>[0, 0]</td>
      <td>Very well constructed sandal offering excellen...</td>
      <td>4.0</td>
      <td>highly recommend</td>
      <td>1348358400</td>
      <td>09 23, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>304.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Verywellconstructedsandalofferingexcellentsupp...</td>
      <td>highlyrecommend</td>
      <td>251</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-09-23</td>
      <td>9</td>
      <td>B001Q5QLP6A2OBNRYDTITU7F</td>
      <td>1</td>
      <td>Very well constructed sandal offering excellen...</td>
      <td>2012</td>
      <td>Very well constructed sandal offering excellen...</td>
    </tr>
    <tr>
      <th>71094</th>
      <td>71094</td>
      <td>A2IMYG68MPGPF9</td>
      <td>B001Q5QLP6</td>
      <td>Mikmity</td>
      <td>[0, 0]</td>
      <td>Wow factor! Not only are these sandals lightwe...</td>
      <td>5.0</td>
      <td>Super Comfy-Love Them!</td>
      <td>1369440000</td>
      <td>05 25, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1386.0</td>
      <td>Shoes</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>WowfactorNotonlyarethesesandalslightweightandc...</td>
      <td>SuperComfyLoveThem</td>
      <td>1086</td>
      <td>18</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-25</td>
      <td>5</td>
      <td>B001Q5QLP6A2IMYG68MPGPF9</td>
      <td>1</td>
      <td>Wow factor Not only are these sandals lightwei...</td>
      <td>2013</td>
      <td>Wow factor! Not only are these sandals lightwe...</td>
    </tr>
    <tr>
      <th>71095</th>
      <td>71095</td>
      <td>A38MTBF5NZWPGS</td>
      <td>B001Q5QLP6</td>
      <td>M. Marks "Melanie"</td>
      <td>[0, 0]</td>
      <td>But...it was a little too small for me and my ...</td>
      <td>5.0</td>
      <td>Love the shoe</td>
      <td>1367107200</td>
      <td>04 28, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Butitwasalittletoosmallformeandmyhealwouldslid...</td>
      <td>Lovetheshoe</td>
      <td>99</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-04-28</td>
      <td>4</td>
      <td>B001Q5QLP6A38MTBF5NZWPGS</td>
      <td>1</td>
      <td>Butit was a little too small for me and my hea...</td>
      <td>2013</td>
      <td>But...it was a little too small for me and my ...</td>
    </tr>
    <tr>
      <th>71096</th>
      <td>71096</td>
      <td>A1A46D270HU3EV</td>
      <td>B001Q5QLP6</td>
      <td>Mooselady "Mooselady"</td>
      <td>[1, 1]</td>
      <td>I have problem feet and always heard about how...</td>
      <td>5.0</td>
      <td>Ahhhh....so comfortable</td>
      <td>1401494400</td>
      <td>05 31, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>287.0</td>
      <td>Shoes</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Ihaveproblemfeetandalwaysheardabouthowwonderfu...</td>
      <td>Ahhhhsocomfortable</td>
      <td>222</td>
      <td>18</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-31</td>
      <td>5</td>
      <td>B001Q5QLP6A1A46D270HU3EV</td>
      <td>1</td>
      <td>I have problem feet and always heard about how...</td>
      <td>2014</td>
      <td>I have problem feet and always heard about how...</td>
    </tr>
    <tr>
      <th>71097</th>
      <td>71097</td>
      <td>AGV9GMEGI5ROW</td>
      <td>B001Q5QLP6</td>
      <td>Mountain Joy</td>
      <td>[1, 1]</td>
      <td>I can't praise these sandals enough.  They've ...</td>
      <td>5.0</td>
      <td>Beach buddy.</td>
      <td>1392336000</td>
      <td>02 14, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>449.0</td>
      <td>Shoes</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>IcantpraisethesesandalsenoughTheyvetakenmearou...</td>
      <td>Beachbuddy</td>
      <td>349</td>
      <td>10</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-02-14</td>
      <td>2</td>
      <td>B001Q5QLP6AGV9GMEGI5ROW</td>
      <td>1</td>
      <td>I cant praise these sandals enough  Theyve tak...</td>
      <td>2014</td>
      <td>I can't praise these sandals enough.  They've ...</td>
    </tr>
    <tr>
      <th>71098</th>
      <td>71098</td>
      <td>ASJK8MIKACBJE</td>
      <td>B001Q5QLP6</td>
      <td>Mrs. S "missbethanyblue"</td>
      <td>[0, 0]</td>
      <td>I had ordered a pair of H2's last summer and r...</td>
      <td>5.0</td>
      <td>So much better!</td>
      <td>1356480000</td>
      <td>12 26, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>424.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IhadorderedapairofH2slastsummerandreturnedthem...</td>
      <td>Somuchbetter</td>
      <td>325</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-12-26</td>
      <td>12</td>
      <td>B001Q5QLP6ASJK8MIKACBJE</td>
      <td>1</td>
      <td>I had ordered a pair of Hs last summer and ret...</td>
      <td>2012</td>
      <td>I had ordered a pair of H2's last summer and r...</td>
    </tr>
    <tr>
      <th>71099</th>
      <td>71099</td>
      <td>A6QMBCFXH09PX</td>
      <td>B001Q5QLP6</td>
      <td>Nancy N. Johnson "Rednana"</td>
      <td>[0, 0]</td>
      <td>I love these shoes. They feel great and look f...</td>
      <td>5.0</td>
      <td>Love my beautiful Keen sandals.</td>
      <td>1379462400</td>
      <td>09 18, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>149.0</td>
      <td>Shoes</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IlovetheseshoesTheyfeelgreatandlookfantasticTh...</td>
      <td>LovemybeautifulKeensandals</td>
      <td>119</td>
      <td>26</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-18</td>
      <td>9</td>
      <td>B001Q5QLP6A6QMBCFXH09PX</td>
      <td>1</td>
      <td>I love these shoes They feel great and look fa...</td>
      <td>2013</td>
      <td>I love these shoes. They feel great and look f...</td>
    </tr>
    <tr>
      <th>71100</th>
      <td>71100</td>
      <td>A1M09JXUQWV1LV</td>
      <td>B001Q5QLP6</td>
      <td>Nancy R Biggs</td>
      <td>[0, 0]</td>
      <td>I LOVE these shoes. They fit perfectly and are...</td>
      <td>5.0</td>
      <td>My Favorite Shoes</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ILOVEtheseshoesTheyfitperfectlyandaregreatfore...</td>
      <td>MyFavoriteShoes</td>
      <td>127</td>
      <td>15</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B001Q5QLP6A1M09JXUQWV1LV</td>
      <td>1</td>
      <td>I LOVE these shoes They fit perfectly and are ...</td>
      <td>2013</td>
      <td>I LOVE these shoes. They fit perfectly and are...</td>
    </tr>
    <tr>
      <th>71101</th>
      <td>71101</td>
      <td>A1M8LW4BBR9YBH</td>
      <td>B001Q5QLP6</td>
      <td>N. Fay</td>
      <td>[0, 0]</td>
      <td>I ordered the 11/11.5 thinking surely it would...</td>
      <td>3.0</td>
      <td>I like the shoe but is too short.</td>
      <td>1376265600</td>
      <td>08 12, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>265.0</td>
      <td>Shoes</td>
      <td>33.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Iorderedthe11115thinkingsurelyitwouldfitIweara...</td>
      <td>Iliketheshoebutistooshort</td>
      <td>202</td>
      <td>25</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-12</td>
      <td>8</td>
      <td>B001Q5QLP6A1M8LW4BBR9YBH</td>
      <td>0</td>
      <td>I ordered the  thinking surely it would fit I ...</td>
      <td>2013</td>
      <td>I ordered the 11/11.5 thinking surely it would...</td>
    </tr>
    <tr>
      <th>71102</th>
      <td>71102</td>
      <td>A3IUV2X4OELLFS</td>
      <td>B001Q5QLP6</td>
      <td>Nic</td>
      <td>[0, 0]</td>
      <td>I gave this shoe 5 stars because it's worth 6 ...</td>
      <td>5.0</td>
      <td>Great hiking shoes</td>
      <td>1396742400</td>
      <td>04 6, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>431.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Igavethisshoe5starsbecauseitsworth6butIonlyget...</td>
      <td>Greathikingshoes</td>
      <td>334</td>
      <td>16</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-04-06</td>
      <td>4</td>
      <td>B001Q5QLP6A3IUV2X4OELLFS</td>
      <td>1</td>
      <td>I gave this shoe  stars because its worth  but...</td>
      <td>2014</td>
      <td>I gave this shoe 5 stars because it's worth 6 ...</td>
    </tr>
    <tr>
      <th>71103</th>
      <td>71103</td>
      <td>A3W3XK1F8YQPMH</td>
      <td>B001Q5QLP6</td>
      <td>Nicole Lynn</td>
      <td>[0, 0]</td>
      <td>I bought these for a cruise my husband and I w...</td>
      <td>4.0</td>
      <td>For me, runs half size large.</td>
      <td>1384214400</td>
      <td>11 12, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>508.0</td>
      <td>Shoes</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IboughttheseforacruisemyhusbandandIweregoingon...</td>
      <td>Formerunshalfsizelarge</td>
      <td>394</td>
      <td>22</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-12</td>
      <td>11</td>
      <td>B001Q5QLP6A3W3XK1F8YQPMH</td>
      <td>1</td>
      <td>I bought these for a cruise my husband and I w...</td>
      <td>2013</td>
      <td>I bought these for a cruise my husband and I w...</td>
    </tr>
    <tr>
      <th>71104</th>
      <td>71104</td>
      <td>AVE7LIB0U69IE</td>
      <td>B001Q5QLP6</td>
      <td>nina</td>
      <td>[0, 0]</td>
      <td>I have a pair of keen Mary Janes that I love, ...</td>
      <td>5.0</td>
      <td>Newest favorite shoes</td>
      <td>1397174400</td>
      <td>04 11, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>162.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IhaveapairofkeenMaryJanesthatIlovebuttheyareal...</td>
      <td>Newestfavoriteshoes</td>
      <td>123</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-04-11</td>
      <td>4</td>
      <td>B001Q5QLP6AVE7LIB0U69IE</td>
      <td>1</td>
      <td>I have a pair of keen Mary Janes that I love b...</td>
      <td>2014</td>
      <td>I have a pair of keen Mary Janes that I love, ...</td>
    </tr>
    <tr>
      <th>71105</th>
      <td>71105</td>
      <td>A1PSQJGV5RQK7S</td>
      <td>B001Q5QLP6</td>
      <td>Oklahoma Wind Sprite</td>
      <td>[0, 1]</td>
      <td>I read another review and dismissed it, well t...</td>
      <td>5.0</td>
      <td>Problem in sizing</td>
      <td>1375833600</td>
      <td>08 7, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>649.0</td>
      <td>Shoes</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Ireadanotherreviewanddismisseditwelltheywereri...</td>
      <td>Probleminsizing</td>
      <td>507</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-07</td>
      <td>8</td>
      <td>B001Q5QLP6A1PSQJGV5RQK7S</td>
      <td>1</td>
      <td>I read another review and dismissed it well th...</td>
      <td>2013</td>
      <td>I read another review and dismissed it, well t...</td>
    </tr>
    <tr>
      <th>71106</th>
      <td>71106</td>
      <td>A2H3PJ2JEXTG3Z</td>
      <td>B001Q5QLP6</td>
      <td>Pamela Talley "donutdoor"</td>
      <td>[0, 0]</td>
      <td>I bought these for my wife. She has back and f...</td>
      <td>4.0</td>
      <td>Good sandals!</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>217.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IboughttheseformywifeShehasbackandfootissuesNo...</td>
      <td>Goodsandals</td>
      <td>166</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B001Q5QLP6A2H3PJ2JEXTG3Z</td>
      <td>1</td>
      <td>I bought these for my wife She has back and fo...</td>
      <td>2013</td>
      <td>I bought these for my wife. She has back and f...</td>
    </tr>
    <tr>
      <th>71107</th>
      <td>71107</td>
      <td>A3R11XXC7MVNYW</td>
      <td>B001Q5QLP6</td>
      <td>Pamela U. Moore</td>
      <td>[0, 0]</td>
      <td>I am usually a tried-and-true Merrell fan, but...</td>
      <td>5.0</td>
      <td>These sandals are soooo comfortable, and right...</td>
      <td>1397088000</td>
      <td>04 10, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>489.0</td>
      <td>Shoes</td>
      <td>62.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IamusuallyatriedandtrueMerrellfanbutthoughtIwo...</td>
      <td>Thesesandalsaresoooocomfortableandrightoutofth...</td>
      <td>372</td>
      <td>50</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-04-10</td>
      <td>4</td>
      <td>B001Q5QLP6A3R11XXC7MVNYW</td>
      <td>1</td>
      <td>I am usually a triedandtrue Merrell fan but th...</td>
      <td>2014</td>
      <td>I am usually a tried-and-true Merrell fan, but...</td>
    </tr>
    <tr>
      <th>71108</th>
      <td>71108</td>
      <td>A2AIZV1VZDL9YL</td>
      <td>B001Q5QLP6</td>
      <td>pevjev</td>
      <td>[0, 0]</td>
      <td>True to Keens sizing. Comfortable from day one...</td>
      <td>5.0</td>
      <td>Comfy and practical</td>
      <td>1364774400</td>
      <td>04 1, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Shoes</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>TruetoKeenssizingComfortablefromdayoneandanice...</td>
      <td>Comfyandpractical</td>
      <td>96</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-04-01</td>
      <td>4</td>
      <td>B001Q5QLP6A2AIZV1VZDL9YL</td>
      <td>1</td>
      <td>True to Keens sizing Comfortable from day one ...</td>
      <td>2013</td>
      <td>True to Keens sizing. Comfortable from day one...</td>
    </tr>
    <tr>
      <th>71109</th>
      <td>71109</td>
      <td>A2QYL4DR8ZWGK9</td>
      <td>B001Q5QLP6</td>
      <td>PJCB</td>
      <td>[0, 0]</td>
      <td>I have other Keen shoes that I like but these ...</td>
      <td>5.0</td>
      <td>Light and Comfortable</td>
      <td>1369785600</td>
      <td>05 29, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>211.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IhaveotherKeenshoesthatIlikebutthesearethebest...</td>
      <td>LightandComfortable</td>
      <td>165</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-05-29</td>
      <td>5</td>
      <td>B001Q5QLP6A2QYL4DR8ZWGK9</td>
      <td>1</td>
      <td>I have other Keen shoes that I like but these ...</td>
      <td>2013</td>
      <td>I have other Keen shoes that I like but these ...</td>
    </tr>
    <tr>
      <th>71110</th>
      <td>71110</td>
      <td>A1I4EPEMTBO8EK</td>
      <td>B001Q5QLP6</td>
      <td>Polishsausag "Polishsausag"</td>
      <td>[0, 1]</td>
      <td>My wife had another pair of these, but pregana...</td>
      <td>5.0</td>
      <td>Excellent build, color, fit, etc</td>
      <td>1376265600</td>
      <td>08 12, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>227.0</td>
      <td>Shoes</td>
      <td>32.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Mywifehadanotherpairofthesebutpreganancychange...</td>
      <td>Excellentbuildcolorfitetc</td>
      <td>177</td>
      <td>25</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-12</td>
      <td>8</td>
      <td>B001Q5QLP6A1I4EPEMTBO8EK</td>
      <td>1</td>
      <td>My wife had another pair of these but preganan...</td>
      <td>2013</td>
      <td>My wife had another pair of these, but pregana...</td>
    </tr>
    <tr>
      <th>71111</th>
      <td>71111</td>
      <td>A3432PZBO4O8AU</td>
      <td>B001Q5QLP6</td>
      <td>Professor G</td>
      <td>[0, 0]</td>
      <td>I bought these for a trip to Hawaii.  They wer...</td>
      <td>5.0</td>
      <td>Fabulous shoe!</td>
      <td>1341705600</td>
      <td>07 8, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>616.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IboughttheseforatriptoHawaiiTheywerefantasticT...</td>
      <td>Fabulousshoe</td>
      <td>467</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-07-08</td>
      <td>7</td>
      <td>B001Q5QLP6A3432PZBO4O8AU</td>
      <td>1</td>
      <td>I bought these for a trip to Hawaii  They were...</td>
      <td>2012</td>
      <td>I bought these for a trip to Hawaii.  They wer...</td>
    </tr>
    <tr>
      <th>71112</th>
      <td>71112</td>
      <td>ALZ8D5293AYYI</td>
      <td>B001Q5QLP6</td>
      <td>razan</td>
      <td>[0, 0]</td>
      <td>this is my first time buying keen... this sana...</td>
      <td>5.0</td>
      <td>perfect buy</td>
      <td>1395792000</td>
      <td>03 26, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>203.0</td>
      <td>Shoes</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>thisismyfirsttimebuyingkeenthissanadalisthebes...</td>
      <td>perfectbuy</td>
      <td>153</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-26</td>
      <td>3</td>
      <td>B001Q5QLP6ALZ8D5293AYYI</td>
      <td>1</td>
      <td>this is my first time buying keen this sanadal...</td>
      <td>2014</td>
      <td>this is my first time buying keen... this sana...</td>
    </tr>
    <tr>
      <th>71113</th>
      <td>71113</td>
      <td>A326D89V011FAZ</td>
      <td>B001Q5QLP6</td>
      <td>Rebecca</td>
      <td>[1, 1]</td>
      <td>These Keen Whisper sandals are great. I bought...</td>
      <td>5.0</td>
      <td>Light and comfortable</td>
      <td>1379894400</td>
      <td>09 23, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>190.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>TheseKeenWhispersandalsaregreatIboughtthemtowe...</td>
      <td>Lightandcomfortable</td>
      <td>150</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-23</td>
      <td>9</td>
      <td>B001Q5QLP6A326D89V011FAZ</td>
      <td>1</td>
      <td>These Keen Whisper sandals are great I bought ...</td>
      <td>2013</td>
      <td>These Keen Whisper sandals are great. I bought...</td>
    </tr>
    <tr>
      <th>71114</th>
      <td>71114</td>
      <td>A2LCG00J6EFCHT</td>
      <td>B001Q5QLP6</td>
      <td>Redeemed</td>
      <td>[0, 0]</td>
      <td>These shoes are very comfortable, fit well, an...</td>
      <td>5.0</td>
      <td>Awesome!</td>
      <td>1386288000</td>
      <td>12 6, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>191.0</td>
      <td>Shoes</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Theseshoesareverycomfortablefitwellandarrivedo...</td>
      <td>Awesome</td>
      <td>148</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-12-06</td>
      <td>12</td>
      <td>B001Q5QLP6A2LCG00J6EFCHT</td>
      <td>1</td>
      <td>These shoes are very comfortable fit well and ...</td>
      <td>2013</td>
      <td>These shoes are very comfortable, fit well, an...</td>
    </tr>
    <tr>
      <th>71115</th>
      <td>71115</td>
      <td>A1JMSXLT23ZLL3</td>
      <td>B001Q5QLP6</td>
      <td>Renaissance human</td>
      <td>[0, 0]</td>
      <td>Bought these after returning the Venice becaus...</td>
      <td>4.0</td>
      <td>Better than the Venice for narrow feet</td>
      <td>1376956800</td>
      <td>08 20, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>457.0</td>
      <td>Shoes</td>
      <td>38.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>BoughttheseafterreturningtheVenicebecauseIhave...</td>
      <td>BetterthantheVenicefornarrowfeet</td>
      <td>361</td>
      <td>32</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-20</td>
      <td>8</td>
      <td>B001Q5QLP6A1JMSXLT23ZLL3</td>
      <td>1</td>
      <td>Bought these after returning the Venice becaus...</td>
      <td>2013</td>
      <td>Bought these after returning the Venice becaus...</td>
    </tr>
    <tr>
      <th>71116</th>
      <td>71116</td>
      <td>A24CS6IB9RYLJ4</td>
      <td>B001Q5QLP6</td>
      <td>robyn</td>
      <td>[1, 1]</td>
      <td>I've had a pair of these before that I loved b...</td>
      <td>5.0</td>
      <td>Perfect dog walking shoe for the summer.</td>
      <td>1401062400</td>
      <td>05 26, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>152.0</td>
      <td>Shoes</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IvehadapairofthesebeforethatIlovedbutmydogatet...</td>
      <td>Perfectdogwalkingshoeforthesummer</td>
      <td>117</td>
      <td>33</td>
      <td>H</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-05-26</td>
      <td>5</td>
      <td>B001Q5QLP6A24CS6IB9RYLJ4</td>
      <td>1</td>
      <td>Ive had a pair of these before that I loved bu...</td>
      <td>2014</td>
      <td>I've had a pair of these before that I loved b...</td>
    </tr>
    <tr>
      <th>71117</th>
      <td>71117</td>
      <td>A5YRIHBRA6D9S</td>
      <td>B001Q5QLP6</td>
      <td>Rochelle L Kunkelmann</td>
      <td>[0, 1]</td>
      <td>My daughter wears a 9-10 running shoe  These r...</td>
      <td>3.0</td>
      <td>Watch the sizing</td>
      <td>1393977600</td>
      <td>03 5, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>152.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Mydaughterwearsa910runningshoeTheserunBIGSheen...</td>
      <td>Watchthesizing</td>
      <td>112</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-05</td>
      <td>3</td>
      <td>B001Q5QLP6A5YRIHBRA6D9S</td>
      <td>0</td>
      <td>My daughter wears a  running shoe  These run B...</td>
      <td>2014</td>
      <td>My daughter wears a 9-10 running shoe  These r...</td>
    </tr>
    <tr>
      <th>71118</th>
      <td>71118</td>
      <td>A3G0F3VRM187KT</td>
      <td>B001Q5QLP6</td>
      <td>Roxanne</td>
      <td>[0, 0]</td>
      <td>When I pulled it out of the box it looked smal...</td>
      <td>5.0</td>
      <td>Surprised!</td>
      <td>1384128000</td>
      <td>11 11, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>211.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>WhenIpulleditoutoftheboxitlookedsmallcomparedt...</td>
      <td>Surprised</td>
      <td>161</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-11</td>
      <td>11</td>
      <td>B001Q5QLP6A3G0F3VRM187KT</td>
      <td>1</td>
      <td>When I pulled it out of the box it looked smal...</td>
      <td>2013</td>
      <td>When I pulled it out of the box it looked smal...</td>
    </tr>
    <tr>
      <th>71119</th>
      <td>71119</td>
      <td>A3UC9WR6Z3UFQ</td>
      <td>B001Q5QLP6</td>
      <td>schweizer</td>
      <td>[0, 0]</td>
      <td>I absolutely love these shoes/sandals. Shandal...</td>
      <td>5.0</td>
      <td>So comfy, so versatile</td>
      <td>1384646400</td>
      <td>11 17, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>665.0</td>
      <td>Shoes</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IabsolutelylovetheseshoessandalsShandalsWhatev...</td>
      <td>Socomfysoversatile</td>
      <td>513</td>
      <td>18</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-17</td>
      <td>11</td>
      <td>B001Q5QLP6A3UC9WR6Z3UFQ</td>
      <td>1</td>
      <td>I absolutely love these shoessandals Shandals ...</td>
      <td>2013</td>
      <td>I absolutely love these shoes/sandals. Shandal...</td>
    </tr>
    <tr>
      <th>71120</th>
      <td>71120</td>
      <td>AQCK0IUYBEBZ2</td>
      <td>B001Q5QLP6</td>
      <td>Scout "Scout Pause"</td>
      <td>[0, 0]</td>
      <td>Keen shoes of all types are durable and above ...</td>
      <td>5.0</td>
      <td>Comfy feet</td>
      <td>1343001600</td>
      <td>07 23, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>114.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Keenshoesofalltypesaredurableandaboveallveryco...</td>
      <td>Comfyfeet</td>
      <td>92</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-07-23</td>
      <td>7</td>
      <td>B001Q5QLP6AQCK0IUYBEBZ2</td>
      <td>1</td>
      <td>Keen shoes of all types are durable and above ...</td>
      <td>2012</td>
      <td>Keen shoes of all types are durable and above ...</td>
    </tr>
    <tr>
      <th>71121</th>
      <td>71121</td>
      <td>AG0UT05GX6BXS</td>
      <td>B001Q5QLP6</td>
      <td>S. Helms</td>
      <td>[0, 0]</td>
      <td>Previous review urged the buyer to go up a siz...</td>
      <td>5.0</td>
      <td>First pair if Keens, won't be the last.</td>
      <td>1378339200</td>
      <td>09 5, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1035.0</td>
      <td>Shoes</td>
      <td>39.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>PreviousreviewurgedthebuyertogoupasizesoIorder...</td>
      <td>FirstpairifKeenswontbethelast</td>
      <td>796</td>
      <td>29</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-05</td>
      <td>9</td>
      <td>B001Q5QLP6AG0UT05GX6BXS</td>
      <td>1</td>
      <td>Previous review urged the buyer to go up a siz...</td>
      <td>2013</td>
      <td>Previous review urged the buyer to go up a siz...</td>
    </tr>
    <tr>
      <th>71122</th>
      <td>71122</td>
      <td>A1GLXERO4SHGM8</td>
      <td>B001Q5QLP6</td>
      <td>Sher Foster Fox</td>
      <td>[0, 1]</td>
      <td>Very pleased with this water shoe! Comfortable...</td>
      <td>5.0</td>
      <td>Great Water Shoe</td>
      <td>1376006400</td>
      <td>08 9, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>263.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>VerypleasedwiththiswatershoeComfortablepractic...</td>
      <td>GreatWaterShoe</td>
      <td>207</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-08-09</td>
      <td>8</td>
      <td>B001Q5QLP6A1GLXERO4SHGM8</td>
      <td>1</td>
      <td>Very pleased with this water shoe Comfortable ...</td>
      <td>2013</td>
      <td>Very pleased with this water shoe! Comfortable...</td>
    </tr>
    <tr>
      <th>71123</th>
      <td>71123</td>
      <td>A3M06PHB1HDGLS</td>
      <td>B001Q5QLP6</td>
      <td>Simba4runner</td>
      <td>[0, 0]</td>
      <td>I just love Keens.  I probably have 13-15 pair...</td>
      <td>5.0</td>
      <td>Keens are the Best</td>
      <td>1378339200</td>
      <td>09 5, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>360.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IjustloveKeensIprobablyhave1315pairbetweenallt...</td>
      <td>KeensaretheBest</td>
      <td>276</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-09-05</td>
      <td>9</td>
      <td>B001Q5QLP6A3M06PHB1HDGLS</td>
      <td>1</td>
      <td>I just love Keens  I probably have  pair betwe...</td>
      <td>2013</td>
      <td>I just love Keens.  I probably have 13-15 pair...</td>
    </tr>
    <tr>
      <th>71124</th>
      <td>71124</td>
      <td>A2G6MJY9C0VAUZ</td>
      <td>B001Q5QLP6</td>
      <td>S. Rainguet "once around"</td>
      <td>[0, 0]</td>
      <td>My Keen Newport's had served me well and I'd r...</td>
      <td>5.0</td>
      <td>Big improvement.</td>
      <td>1403740800</td>
      <td>06 26, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>144.0</td>
      <td>Shoes</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>MyKeenNewportshadservedmewellandIdreadthattheW...</td>
      <td>Bigimprovement</td>
      <td>113</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-06-26</td>
      <td>6</td>
      <td>B001Q5QLP6A2G6MJY9C0VAUZ</td>
      <td>1</td>
      <td>My Keen Newports had served me well and Id rea...</td>
      <td>2014</td>
      <td>My Keen Newport's had served me well and I'd r...</td>
    </tr>
    <tr>
      <th>71125</th>
      <td>71125</td>
      <td>A3GNMSH4PND5L6</td>
      <td>B001Q5QLP6</td>
      <td>Susan C</td>
      <td>[3, 4]</td>
      <td>I just love Keen sandals.  I no longer have fo...</td>
      <td>5.0</td>
      <td>Love these sandals!</td>
      <td>1330560000</td>
      <td>03 1, 2012</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>0.428571</td>
      <td>185.0</td>
      <td>Shoes</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IjustloveKeensandalsInolongerhavefootpainandaf...</td>
      <td>Lovethesesandals</td>
      <td>143</td>
      <td>16</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2012-03-01</td>
      <td>3</td>
      <td>B001Q5QLP6A3GNMSH4PND5L6</td>
      <td>1</td>
      <td>I just love Keen sandals  I no longer have foo...</td>
      <td>2012</td>
      <td>I just love Keen sandals.  I no longer have fo...</td>
    </tr>
    <tr>
      <th>71126</th>
      <td>71126</td>
      <td>A3QYISD9DMD1ID</td>
      <td>B001Q5QLP6</td>
      <td>Suzanne P Gibson</td>
      <td>[1, 1]</td>
      <td>These are my first pair of Keen's.  I was prep...</td>
      <td>5.0</td>
      <td>Perfect sandal</td>
      <td>1393891200</td>
      <td>03 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>293.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThesearemyfirstpairofKeensIwaspreparingforatro...</td>
      <td>Perfectsandal</td>
      <td>231</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-04</td>
      <td>3</td>
      <td>B001Q5QLP6A3QYISD9DMD1ID</td>
      <td>1</td>
      <td>These are my first pair of Keens  I was prepar...</td>
      <td>2014</td>
      <td>These are my first pair of Keen's.  I was prep...</td>
    </tr>
    <tr>
      <th>71127</th>
      <td>71127</td>
      <td>A37LD9AVJMJH8N</td>
      <td>B001Q5QLP6</td>
      <td>Tammy G.</td>
      <td>[0, 0]</td>
      <td>I like the construction of these shoes.  They ...</td>
      <td>5.0</td>
      <td>Wish I had bought these sooner, definitely a k...</td>
      <td>1380758400</td>
      <td>10 3, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>473.0</td>
      <td>Shoes</td>
      <td>52.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IliketheconstructionoftheseshoesTheyoffermores...</td>
      <td>WishIhadboughtthesesoonerdefinitelyakeeper</td>
      <td>363</td>
      <td>42</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-10-03</td>
      <td>10</td>
      <td>B001Q5QLP6A37LD9AVJMJH8N</td>
      <td>1</td>
      <td>I like the construction of these shoes  They o...</td>
      <td>2013</td>
      <td>I like the construction of these shoes.  They ...</td>
    </tr>
    <tr>
      <th>71128</th>
      <td>71128</td>
      <td>A3SYF21Z68XAV3</td>
      <td>B001Q5QLP6</td>
      <td>Terri Eddy</td>
      <td>[2, 2]</td>
      <td>Surprising I like the lavender and beige color...</td>
      <td>5.0</td>
      <td>My third pair</td>
      <td>1393891200</td>
      <td>03 4, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>0.500000</td>
      <td>189.0</td>
      <td>Shoes</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>SurprisingIlikethelavenderandbeigecolorIbought...</td>
      <td>Mythirdpair</td>
      <td>151</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-03-04</td>
      <td>3</td>
      <td>B001Q5QLP6A3SYF21Z68XAV3</td>
      <td>1</td>
      <td>Surprising I like the lavender and beige color...</td>
      <td>2014</td>
      <td>Surprising I like the lavender and beige color...</td>
    </tr>
    <tr>
      <th>71129</th>
      <td>71129</td>
      <td>AZRIYVL8HTYX8</td>
      <td>B001Q5QLP6</td>
      <td>T. Leonard</td>
      <td>[0, 0]</td>
      <td>I have wide feet and they fit great.  The colo...</td>
      <td>3.0</td>
      <td>Color not like it looked on the computer</td>
      <td>1373155200</td>
      <td>07 7, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>256.0</td>
      <td>Shoes</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IhavewidefeetandtheyfitgreatThecolorwasnotasex...</td>
      <td>Colornotlikeitlookedonthecomputer</td>
      <td>197</td>
      <td>33</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-07-07</td>
      <td>7</td>
      <td>B001Q5QLP6AZRIYVL8HTYX8</td>
      <td>0</td>
      <td>I have wide feet and they fit great  The color...</td>
      <td>2013</td>
      <td>I have wide feet and they fit great.  The colo...</td>
    </tr>
    <tr>
      <th>71130</th>
      <td>71130</td>
      <td>A2DT9OLVAPOJL1</td>
      <td>B001Q5QLP6</td>
      <td>Tolokonov</td>
      <td>[0, 0]</td>
      <td>It's a KEEN, guys! :) Very comfortable right f...</td>
      <td>5.0</td>
      <td>It's a KEEN, guys! :)</td>
      <td>1405036800</td>
      <td>07 11, 2014</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Shoes</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ItsaKEENguysVerycomfortablerightfromtheboxhiqu...</td>
      <td>ItsaKEENguys</td>
      <td>82</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-11</td>
      <td>7</td>
      <td>B001Q5QLP6A2DT9OLVAPOJL1</td>
      <td>1</td>
      <td>Its a KEEN guys  Very comfortable right from t...</td>
      <td>2014</td>
      <td>It's a KEEN, guys! :) Very comfortable right f...</td>
    </tr>
    <tr>
      <th>71131</th>
      <td>71131</td>
      <td>A3Z1RAALVL9MV</td>
      <td>B001Q5QLP6</td>
      <td>Torchwood "Boot Collector"</td>
      <td>[5, 7]</td>
      <td>The Keen Whisper is a nice little sports sanda...</td>
      <td>5.0</td>
      <td>keen whisper sandals</td>
      <td>1309046400</td>
      <td>06 26, 2011</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>5</td>
      <td>7</td>
      <td>12</td>
      <td>0.416667</td>
      <td>667.0</td>
      <td>Shoes</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>TheKeenWhisperisanicelittlesportssandalwashabl...</td>
      <td>keenwhispersandals</td>
      <td>528</td>
      <td>18</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2011-06-26</td>
      <td>6</td>
      <td>B001Q5QLP6A3Z1RAALVL9MV</td>
      <td>1</td>
      <td>The Keen Whisper is a nice little sports sanda...</td>
      <td>2011</td>
      <td>The Keen Whisper is a nice little sports sanda...</td>
    </tr>
    <tr>
      <th>71132</th>
      <td>71132</td>
      <td>A7V89Q1UCRRW4</td>
      <td>B001Q5QLP6</td>
      <td>Travel mavn "luvsbooks"</td>
      <td>[0, 0]</td>
      <td>I ended up keeping thtese although a bit long ...</td>
      <td>4.0</td>
      <td>feel good although haven't had a real outing yet</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>649.0</td>
      <td>Shoes</td>
      <td>48.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iendedupkeepingthtesealthoughabitlongabovethet...</td>
      <td>feelgoodalthoughhaventhadarealoutingyet</td>
      <td>509</td>
      <td>39</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B001Q5QLP6A7V89Q1UCRRW4</td>
      <td>1</td>
      <td>I ended up keeping thtese although a bit long ...</td>
      <td>2013</td>
      <td>I ended up keeping thtese although a bit long ...</td>
    </tr>
    <tr>
      <th>71133</th>
      <td>71133</td>
      <td>APJNYZCZSU5A5</td>
      <td>B001Q5QLP6</td>
      <td>turtles6</td>
      <td>[7, 10]</td>
      <td>I got these in the jade color as well as the d...</td>
      <td>5.0</td>
      <td>Love, love, love but order a 1/2 size up</td>
      <td>1358899200</td>
      <td>01 23, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>7</td>
      <td>1</td>
      <td>8</td>
      <td>0.875000</td>
      <td>336.0</td>
      <td>Shoes</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Igottheseinthejadecoloraswellasthedarkshadowan...</td>
      <td>Lovelovelovebutordera12sizeup</td>
      <td>257</td>
      <td>29</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-01-23</td>
      <td>1</td>
      <td>B001Q5QLP6APJNYZCZSU5A5</td>
      <td>1</td>
      <td>I got these in the jade color as well as the d...</td>
      <td>2013</td>
      <td>I got these in the jade color as well as the d...</td>
    </tr>
    <tr>
      <th>71134</th>
      <td>71134</td>
      <td>A36LJXA4FLLXR3</td>
      <td>B001Q5QLP6</td>
      <td>WeeBeaks</td>
      <td>[0, 0]</td>
      <td>I have a few pair of Keens.  These fit as expe...</td>
      <td>4.0</td>
      <td>Excellent shoe</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>236.0</td>
      <td>Shoes</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IhaveafewpairofKeensThesefitasexpectedforKeens...</td>
      <td>Excellentshoe</td>
      <td>182</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B001Q5QLP6A36LJXA4FLLXR3</td>
      <td>1</td>
      <td>I have a few pair of Keens  These fit as expec...</td>
      <td>2013</td>
      <td>I have a few pair of Keens.  These fit as expe...</td>
    </tr>
    <tr>
      <th>71135</th>
      <td>71135</td>
      <td>A39QE08C3E2RJD</td>
      <td>B001Q5QLP6</td>
      <td>witherbeeds</td>
      <td>[0, 0]</td>
      <td>I usually wear 7 1/2 but reading the reviews I...</td>
      <td>4.0</td>
      <td>comfortable walking shoes</td>
      <td>1373068800</td>
      <td>07 6, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>346.0</td>
      <td>Shoes</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iusuallywear712butreadingthereviewsIdecidedtog...</td>
      <td>comfortablewalkingshoes</td>
      <td>264</td>
      <td>23</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-07-06</td>
      <td>7</td>
      <td>B001Q5QLP6A39QE08C3E2RJD</td>
      <td>1</td>
      <td>I usually wear   but reading the reviews I dec...</td>
      <td>2013</td>
      <td>I usually wear 7 1/2 but reading the reviews I...</td>
    </tr>
    <tr>
      <th>71136</th>
      <td>71136</td>
      <td>A3LSSKZJ08O5FY</td>
      <td>B001Q5QLP6</td>
      <td>Yarnspinner13 "Yarnspinner13"</td>
      <td>[0, 0]</td>
      <td>I usually have to wear new shoes a little at a...</td>
      <td>5.0</td>
      <td>Love them!</td>
      <td>1370649600</td>
      <td>06 8, 2013</td>
      <td>3913551</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41bwhM5w...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>530.0</td>
      <td>Shoes</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iusuallyhavetowearnewshoesalittleatatimetogetu...</td>
      <td>Lovethem</td>
      <td>413</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2013-06-08</td>
      <td>6</td>
      <td>B001Q5QLP6A3LSSKZJ08O5FY</td>
      <td>1</td>
      <td>I usually have to wear new shoes a little at a...</td>
      <td>2013</td>
      <td>I usually have to wear new shoes a little at a...</td>
    </tr>
    <tr>
      <th>266683</th>
      <td>266683</td>
      <td>A368PAEL4UV7GE</td>
      <td>B00E0GQQ8A</td>
      <td>camama</td>
      <td>[0, 0]</td>
      <td>As many other reviewers have said, these shoes...</td>
      <td>5.0</td>
      <td>Not bright orange, but VERY comfy</td>
      <td>1405468800</td>
      <td>07 16, 2014</td>
      <td>8588929</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41LsoRcE...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>382.0</td>
      <td>Shoes</td>
      <td>33.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Asmanyotherreviewershavesaidtheseshoesareveryc...</td>
      <td>NotbrightorangebutVERYcomfy</td>
      <td>295</td>
      <td>27</td>
      <td>H</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-16</td>
      <td>7</td>
      <td>B00E0GQQ8AA368PAEL4UV7GE</td>
      <td>1</td>
      <td>As many other reviewers have said these shoes ...</td>
      <td>2014</td>
      <td>As many other reviewers have said, these shoes...</td>
    </tr>
    <tr>
      <th>266684</th>
      <td>266684</td>
      <td>A12HFB9UGYZICB</td>
      <td>B00E0GQQ8A</td>
      <td>Noelle in Minneapolis</td>
      <td>[0, 0]</td>
      <td>This is my second pair of Keen Whisper Sandals...</td>
      <td>5.0</td>
      <td>Love this shoe!</td>
      <td>1405209600</td>
      <td>07 13, 2014</td>
      <td>8588929</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41LsoRcE...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>363.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThisismysecondpairofKeenWhisperSandalsWhisperi...</td>
      <td>Lovethisshoe</td>
      <td>284</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-13</td>
      <td>7</td>
      <td>B00E0GQQ8AA12HFB9UGYZICB</td>
      <td>1</td>
      <td>This is my second pair of Keen Whisper Sandals...</td>
      <td>2014</td>
      <td>This is my second pair of Keen Whisper Sandals...</td>
    </tr>
    <tr>
      <th>266685</th>
      <td>266685</td>
      <td>A2C6CN639N0I6N</td>
      <td>B00E0GQQ8A</td>
      <td>Pink</td>
      <td>[0, 0]</td>
      <td>Love Keen whisper sandals -- this one fits per...</td>
      <td>5.0</td>
      <td>Love Keen whisper sandals -- this one fits per...</td>
      <td>1405296000</td>
      <td>07 14, 2014</td>
      <td>8588929</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41LsoRcE...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>184.0</td>
      <td>Shoes</td>
      <td>60.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>LoveKeenwhispersandalsthisonefitsperfectlyandI...</td>
      <td>LoveKeenwhispersandalsthisonefitsperfectlyand</td>
      <td>141</td>
      <td>45</td>
      <td>H</td>
      <td>M</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-14</td>
      <td>7</td>
      <td>B00E0GQQ8AA2C6CN639N0I6N</td>
      <td>1</td>
      <td>Love Keen whisper sandals  this one fits perfe...</td>
      <td>2014</td>
      <td>Love Keen whisper sandals -- this one fits per...</td>
    </tr>
    <tr>
      <th>266686</th>
      <td>266686</td>
      <td>A25I6ME8FHMTJR</td>
      <td>B00E0GQQ8A</td>
      <td>Susan Prince</td>
      <td>[0, 0]</td>
      <td>I've been a fan of Keen shoes &amp; sandals for ye...</td>
      <td>5.0</td>
      <td>Keen Does It Again</td>
      <td>1405728000</td>
      <td>07 19, 2014</td>
      <td>8588929</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41LsoRcE...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>582.0</td>
      <td>Shoes</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IvebeenafanofKeenshoessandalsforyearswearingth...</td>
      <td>KeenDoesItAgain</td>
      <td>432</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-19</td>
      <td>7</td>
      <td>B00E0GQQ8AA25I6ME8FHMTJR</td>
      <td>1</td>
      <td>Ive been a fan of Keen shoes  sandals for year...</td>
      <td>2014</td>
      <td>I've been a fan of Keen shoes &amp; sandals for ye...</td>
    </tr>
    <tr>
      <th>266687</th>
      <td>266687</td>
      <td>A23YPCAHAAFVXE</td>
      <td>B00E0GQQ8A</td>
      <td>Tahanage</td>
      <td>[0, 0]</td>
      <td>So I buy KEENs every 7 years. My first and las...</td>
      <td>5.0</td>
      <td>My 7 Year KEENs</td>
      <td>1405641600</td>
      <td>07 18, 2014</td>
      <td>8588929</td>
      <td>{'Shoes': 7}</td>
      <td>http://ecx.images-amazon.com/images/I/41LsoRcE...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Shoes &amp; Access...</td>
      <td>KEEN Women's Whisper Sandal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>{'also_bought': ['B0035FE60M', 'B0001MQ60A', '...</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>448.0</td>
      <td>Shoes</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>SoIbuyKEENsevery7yearsMyfirstandlastpairof34am...</td>
      <td>My7YearKEENs</td>
      <td>345</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>NaN</td>
      <td>7</td>
      <td>2014-07-18</td>
      <td>7</td>
      <td>B00E0GQQ8AA23YPCAHAAFVXE</td>
      <td>1</td>
      <td>So I buy KEENs every  years My first and last ...</td>
      <td>2014</td>
      <td>So I buy KEENs every 7 years. My first and las...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_check.groupby('asin').reviewText.nunique().sort_values(ascending=False)
```




    asin
    B005LERHD8    441
    B005GYGD7O    286
    B008WYDP1C    249
    B0058XIMMM    241
    B00CKGB85I    225
                 ... 
    B002C4BTPC      5
    B00D07C73I      5
    B007SBXPR4      5
    B002RWL2OC      4
    B0087115JO      4
    Name: reviewText, Length: 21807, dtype: int64




```python
cloud_check = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['asin']=='B008WYDP1C') & (df_merged_c['pos_neg']==0)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_check);

```


![png](output_173_0.png)



```python
cloud_check = wordcloud.WordCloud(background_color='white', max_font_size=60, 
                                relative_scaling=1).generate(' '.join(df_merged_c[(df_merged_c['asin']=='B008WYDP1C') & (df_merged_c['pos_neg']==1)].total_review_nonum))
fig = plt.figure(figsize=(20, 10))
plt.axis('off')
plt.imshow(cloud_check);

```


![png](output_174_0.png)



```python
set(df_check[(df_check['asin']=='B005LERHD8') & (df_check['pos_neg']==0)]['category_derived'])
```




    {'Jewelry'}




```python
df_check[df_check['asin']=='B005LERHD8']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reviewerID</th>
      <th>asin</th>
      <th>reviewerName</th>
      <th>helpful</th>
      <th>reviewText</th>
      <th>overall</th>
      <th>summary</th>
      <th>unixReviewTime</th>
      <th>reviewTime</th>
      <th>metadataid</th>
      <th>salesrank</th>
      <th>imurl</th>
      <th>categories</th>
      <th>title</th>
      <th>description</th>
      <th>price</th>
      <th>related</th>
      <th>brand</th>
      <th>positive_helpful</th>
      <th>negative_helpful</th>
      <th>total_helpful</th>
      <th>positive_helpful_ratio</th>
      <th>len_reviewText</th>
      <th>category_derived</th>
      <th>len_summary</th>
      <th>check</th>
      <th>len_summary_bins</th>
      <th>len_reviewText_bins</th>
      <th>reviewText_cleaned</th>
      <th>summary_cleaned</th>
      <th>len_reviewText_cleaned</th>
      <th>len_summary_cleaned</th>
      <th>len_summary_cleaned_bins</th>
      <th>len_reviewText_claned_bins</th>
      <th>price_bins</th>
      <th>salesrank_derived</th>
      <th>date</th>
      <th>month</th>
      <th>asin_reviewer</th>
      <th>pos_neg</th>
      <th>review_nonum</th>
      <th>year</th>
      <th>reviewText_comwords</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>161265</th>
      <td>161265</td>
      <td>A1PMGOX24BWDAZ</td>
      <td>B005LERHD8</td>
      <td>0902virgo</td>
      <td>[0, 0]</td>
      <td>I received the necklace a few days ago,i got o...</td>
      <td>5.0</td>
      <td>Really cute</td>
      <td>1354492800</td>
      <td>12 3, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>282.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Ireceivedthenecklaceafewdaysagoigotoneformeand...</td>
      <td>Reallycute</td>
      <td>220</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-03</td>
      <td>12</td>
      <td>B005LERHD8A1PMGOX24BWDAZ</td>
      <td>1</td>
      <td>I received the necklace a few days agoi got on...</td>
      <td>2012</td>
      <td>I received the necklace a few days ago,i got o...</td>
    </tr>
    <tr>
      <th>161266</th>
      <td>161266</td>
      <td>A3FCLEFNZ33BW3</td>
      <td>B005LERHD8</td>
      <td>adversity</td>
      <td>[0, 0]</td>
      <td>I CHOSE THIS FOR MY DAUGHTER ALONG WITH ANOTHE...</td>
      <td>5.0</td>
      <td>GOES WITH ANOTHER ONE</td>
      <td>1364256000</td>
      <td>03 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ICHOSETHISFORMYDAUGHTERALONGWITHANOTHERONELIKE...</td>
      <td>GOESWITHANOTHERONE</td>
      <td>100</td>
      <td>18</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-26</td>
      <td>3</td>
      <td>B005LERHD8A3FCLEFNZ33BW3</td>
      <td>1</td>
      <td>I CHOSE THIS FOR MY DAUGHTER ALONG WITH ANOTHE...</td>
      <td>2013</td>
      <td>I CHOSE THIS FOR MY DAUGHTER ALONG WITH ANOTHE...</td>
    </tr>
    <tr>
      <th>161267</th>
      <td>161267</td>
      <td>A2LESKVQIJC07P</td>
      <td>B005LERHD8</td>
      <td>A. Friscia</td>
      <td>[0, 0]</td>
      <td>I bought one for myself and one for my daughte...</td>
      <td>5.0</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>1368576000</td>
      <td>05 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>250.0</td>
      <td>Jewelry</td>
      <td>53.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IboughtoneformyselfandoneformydaughterWebothwe...</td>
      <td>VintageRetroColorfulCrystalOwlPendantandChain</td>
      <td>196</td>
      <td>45</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-15</td>
      <td>5</td>
      <td>B005LERHD8A2LESKVQIJC07P</td>
      <td>1</td>
      <td>I bought one for myself and one for my daughte...</td>
      <td>2013</td>
      <td>I bought one for myself and one for my daughte...</td>
    </tr>
    <tr>
      <th>161268</th>
      <td>161268</td>
      <td>A37URRNLNUKSAA</td>
      <td>B005LERHD8</td>
      <td>AJccc4Life "AJccc4Life"</td>
      <td>[0, 0]</td>
      <td>These are similar to the ones you see in costu...</td>
      <td>5.0</td>
      <td>Very nice necklace</td>
      <td>1361318400</td>
      <td>02 20, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>259.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Thesearesimilartotheonesyouseeincostumejewelry...</td>
      <td>Verynicenecklace</td>
      <td>205</td>
      <td>16</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-20</td>
      <td>2</td>
      <td>B005LERHD8A37URRNLNUKSAA</td>
      <td>1</td>
      <td>These are similar to the ones you see in costu...</td>
      <td>2013</td>
      <td>These are similar to the ones you see in costu...</td>
    </tr>
    <tr>
      <th>161269</th>
      <td>161269</td>
      <td>A1HFSY6W8LJNJM</td>
      <td>B005LERHD8</td>
      <td>Alicia7tommy "Alicia Andrews"</td>
      <td>[0, 0]</td>
      <td>The owl necklace is really cute but made real ...</td>
      <td>4.0</td>
      <td>Really Cute</td>
      <td>1343001600</td>
      <td>07 23, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>253.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>TheowlnecklaceisreallycutebutmaderealthinItisq...</td>
      <td>ReallyCute</td>
      <td>195</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-07-23</td>
      <td>7</td>
      <td>B005LERHD8A1HFSY6W8LJNJM</td>
      <td>1</td>
      <td>The owl necklace is really cute but made real ...</td>
      <td>2012</td>
      <td>The owl necklace is really cute but made real ...</td>
    </tr>
    <tr>
      <th>161270</th>
      <td>161270</td>
      <td>A168W1XDQRE2IQ</td>
      <td>B005LERHD8</td>
      <td>Alicia Yates</td>
      <td>[0, 0]</td>
      <td>Cute set there's only one piece I did not like...</td>
      <td>4.0</td>
      <td>Nice set</td>
      <td>1402358400</td>
      <td>06 10, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>CutesettheresonlyonepieceIdidnotlikeitisalittl...</td>
      <td>Niceset</td>
      <td>91</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-10</td>
      <td>6</td>
      <td>B005LERHD8A168W1XDQRE2IQ</td>
      <td>1</td>
      <td>Cute set theres only one piece I did not like ...</td>
      <td>2014</td>
      <td>Cute set there's only one piece I did not like...</td>
    </tr>
    <tr>
      <th>161271</th>
      <td>161271</td>
      <td>A2WXIA8LIT5XCD</td>
      <td>B005LERHD8</td>
      <td>ali</td>
      <td>[0, 0]</td>
      <td>would recommend, and was a real bargain,  It g...</td>
      <td>5.0</td>
      <td>loved it</td>
      <td>1394755200</td>
      <td>03 14, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>118.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>wouldrecommendandwasarealbargainItgoeswithalot...</td>
      <td>lovedit</td>
      <td>92</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-14</td>
      <td>3</td>
      <td>B005LERHD8A2WXIA8LIT5XCD</td>
      <td>1</td>
      <td>would recommend and was a real bargain  It goe...</td>
      <td>2014</td>
      <td>would recommend, and was a real bargain,  It g...</td>
    </tr>
    <tr>
      <th>161272</th>
      <td>161272</td>
      <td>A2WKUHVDIFHMY9</td>
      <td>B005LERHD8</td>
      <td>amanda</td>
      <td>[0, 0]</td>
      <td>bought this for a friend and she loved it. the...</td>
      <td>4.0</td>
      <td>love</td>
      <td>1388016000</td>
      <td>12 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>125.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>boughtthisforafriendandshelovedittherewasnothi...</td>
      <td>love</td>
      <td>99</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-26</td>
      <td>12</td>
      <td>B005LERHD8A2WKUHVDIFHMY9</td>
      <td>1</td>
      <td>bought this for a friend and she loved it ther...</td>
      <td>2013</td>
      <td>bought this for a friend and she loved it. the...</td>
    </tr>
    <tr>
      <th>161273</th>
      <td>161273</td>
      <td>A2R42GD26S01S0</td>
      <td>B005LERHD8</td>
      <td>Amanda Simcoe</td>
      <td>[0, 0]</td>
      <td>So cheap! Bought it for myself, gave it to my ...</td>
      <td>1.0</td>
      <td>Cheap</td>
      <td>1389052800</td>
      <td>01 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>152.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SocheapBoughtitformyselfgaveittomydaughterforp...</td>
      <td>Cheap</td>
      <td>119</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-07</td>
      <td>1</td>
      <td>B005LERHD8A2R42GD26S01S0</td>
      <td>0</td>
      <td>So cheap Bought it for myself gave it to my da...</td>
      <td>2014</td>
      <td>So cheap! Bought it for myself, gave it to my ...</td>
    </tr>
    <tr>
      <th>161274</th>
      <td>161274</td>
      <td>A11FNXJY7K666M</td>
      <td>B005LERHD8</td>
      <td>Amanda Starcher</td>
      <td>[0, 0]</td>
      <td>This is a really cute piece of jewelery. The c...</td>
      <td>4.0</td>
      <td>Very cute, larger than it appears</td>
      <td>1390780800</td>
      <td>01 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>531.0</td>
      <td>Jewelry</td>
      <td>33.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>ThisisareallycutepieceofjeweleryThecolorsandap...</td>
      <td>Verycutelargerthanitappears</td>
      <td>415</td>
      <td>27</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-27</td>
      <td>1</td>
      <td>B005LERHD8A11FNXJY7K666M</td>
      <td>1</td>
      <td>This is a really cute piece of jewelery The co...</td>
      <td>2014</td>
      <td>This is a really cute piece of jewelery. The c...</td>
    </tr>
    <tr>
      <th>161275</th>
      <td>161275</td>
      <td>A3HICO8WGUNJGM</td>
      <td>B005LERHD8</td>
      <td>Amanda W.</td>
      <td>[0, 0]</td>
      <td>Cute, nice quality. Nice length.</td>
      <td>5.0</td>
      <td>nice quality. Nice length</td>
      <td>1404777600</td>
      <td>07 8, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>32.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>CutenicequalityNicelength</td>
      <td>nicequalityNicelength</td>
      <td>25</td>
      <td>21</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-08</td>
      <td>7</td>
      <td>B005LERHD8A3HICO8WGUNJGM</td>
      <td>1</td>
      <td>Cute nice quality Nice length</td>
      <td>2014</td>
      <td>Cute, nice quality. Nice length.</td>
    </tr>
    <tr>
      <th>161276</th>
      <td>161276</td>
      <td>A3F5FQ15IE0PDG</td>
      <td>B005LERHD8</td>
      <td>A.Mary</td>
      <td>[0, 0]</td>
      <td>i don't know why, it is prob the size, but i a...</td>
      <td>4.0</td>
      <td>nice except the eyes are a little creepy</td>
      <td>1369094400</td>
      <td>05 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>126.0</td>
      <td>Jewelry</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>idontknowwhyitisprobthesizebutiamalwaysalittle...</td>
      <td>niceexcepttheeyesarealittlecreepy</td>
      <td>93</td>
      <td>33</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-21</td>
      <td>5</td>
      <td>B005LERHD8A3F5FQ15IE0PDG</td>
      <td>1</td>
      <td>i dont know why it is prob the size but i am a...</td>
      <td>2013</td>
      <td>i don't know why, it is prob the size, but i a...</td>
    </tr>
    <tr>
      <th>161277</th>
      <td>161277</td>
      <td>A1WPO8LZHY3YN2</td>
      <td>B005LERHD8</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>Husband got this for me and it's really cute. ...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1399593600</td>
      <td>05 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>HusbandgotthisformeanditsreallycuteDefinitelyc...</td>
      <td>Cute</td>
      <td>95</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-09</td>
      <td>5</td>
      <td>B005LERHD8A1WPO8LZHY3YN2</td>
      <td>1</td>
      <td>Husband got this for me and its really cute  D...</td>
      <td>2014</td>
      <td>Husband got this for me and it's really cute. ...</td>
    </tr>
    <tr>
      <th>161278</th>
      <td>161278</td>
      <td>A2AEFSWJCJ8Q6P</td>
      <td>B005LERHD8</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I am using it as an acessorie on my first day ...</td>
      <td>5.0</td>
      <td>Really pretty!</td>
      <td>1376524800</td>
      <td>08 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Iamusingitasanacessorieonmyfirstdayofschoolout...</td>
      <td>Reallypretty</td>
      <td>128</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-15</td>
      <td>8</td>
      <td>B005LERHD8A2AEFSWJCJ8Q6P</td>
      <td>1</td>
      <td>I am using it as an acessorie on my first day ...</td>
      <td>2013</td>
      <td>I am using it as an acessorie on my first day ...</td>
    </tr>
    <tr>
      <th>161279</th>
      <td>161279</td>
      <td>A1B1YH4TZ326SX</td>
      <td>B005LERHD8</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>I order xmcheap jewelry on amazon all the tone...</td>
      <td>1.0</td>
      <td>Not worth your money</td>
      <td>1393286400</td>
      <td>02 25, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>277.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Iorderxmcheapjewelryonamazonallthetoneanditsus...</td>
      <td>Notworthyourmoney</td>
      <td>216</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-25</td>
      <td>2</td>
      <td>B005LERHD8A1B1YH4TZ326SX</td>
      <td>0</td>
      <td>I order xmcheap jewelry on amazon all the tone...</td>
      <td>2014</td>
      <td>I order xmcheap jewelry on amazon all the tone...</td>
    </tr>
    <tr>
      <th>161280</th>
      <td>161280</td>
      <td>A23L30BKF59BO4</td>
      <td>B005LERHD8</td>
      <td>Amazon Customer</td>
      <td>[0, 0]</td>
      <td>Very pretty.  A lot bigger than I expected.  I...</td>
      <td>4.0</td>
      <td>Very pretty</td>
      <td>1357862400</td>
      <td>01 11, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>158.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VeryprettyAlotbiggerthanIexpectedIreallydontev...</td>
      <td>Verypretty</td>
      <td>121</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-11</td>
      <td>1</td>
      <td>B005LERHD8A23L30BKF59BO4</td>
      <td>1</td>
      <td>Very pretty  A lot bigger than I expected  I r...</td>
      <td>2013</td>
      <td>Very pretty.  A lot bigger than I expected.  I...</td>
    </tr>
    <tr>
      <th>161281</th>
      <td>161281</td>
      <td>A3IH60N0KKTEIH</td>
      <td>B005LERHD8</td>
      <td>Amazon Customer "Kaye Lane"</td>
      <td>[1, 1]</td>
      <td>I am obsessed with Owls, and when I saw this n...</td>
      <td>4.0</td>
      <td>Fun, sparkly, Unique Owl</td>
      <td>1375747200</td>
      <td>08 6, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>991.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IamobsessedwithOwlsandwhenIsawthisnecklaceIkne...</td>
      <td>FunsparklyUniqueOwl</td>
      <td>771</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-06</td>
      <td>8</td>
      <td>B005LERHD8A3IH60N0KKTEIH</td>
      <td>1</td>
      <td>I am obsessed with Owls and when I saw this ne...</td>
      <td>2013</td>
      <td>I am obsessed with Owls, and when I saw this n...</td>
    </tr>
    <tr>
      <th>161282</th>
      <td>161282</td>
      <td>A25J5ZLVS5FGCA</td>
      <td>B005LERHD8</td>
      <td>Amazon Customer "squirlysue"</td>
      <td>[0, 0]</td>
      <td>My five necklaces arrived today.  These owls r...</td>
      <td>5.0</td>
      <td>Owl Necklace</td>
      <td>1387756800</td>
      <td>12 23, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>201.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>MyfivenecklacesarrivedtodayTheseowlsrepresenta...</td>
      <td>OwlNecklace</td>
      <td>160</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-23</td>
      <td>12</td>
      <td>B005LERHD8A25J5ZLVS5FGCA</td>
      <td>1</td>
      <td>My five necklaces arrived today  These owls re...</td>
      <td>2013</td>
      <td>My five necklaces arrived today.  These owls r...</td>
    </tr>
    <tr>
      <th>161283</th>
      <td>161283</td>
      <td>A1J2P8F49G9HQO</td>
      <td>B005LERHD8</td>
      <td>Amber</td>
      <td>[0, 0]</td>
      <td>I love owls, and this is adorable. The length ...</td>
      <td>5.0</td>
      <td>Really cute</td>
      <td>1391040000</td>
      <td>01 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>116.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IloveowlsandthisisadorableThelengthisperfectal...</td>
      <td>Reallycute</td>
      <td>93</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-30</td>
      <td>1</td>
      <td>B005LERHD8A1J2P8F49G9HQO</td>
      <td>1</td>
      <td>I love owls and this is adorable The length is...</td>
      <td>2014</td>
      <td>I love owls, and this is adorable. The length ...</td>
    </tr>
    <tr>
      <th>161284</th>
      <td>161284</td>
      <td>A28R86QYMFFPA0</td>
      <td>B005LERHD8</td>
      <td>amber</td>
      <td>[0, 0]</td>
      <td>i paid 86 cents for this necklace, plus free s...</td>
      <td>5.0</td>
      <td>great deal</td>
      <td>1394150400</td>
      <td>03 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ipaid86centsforthisnecklaceplusfreeshippingifi...</td>
      <td>greatdeal</td>
      <td>130</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-07</td>
      <td>3</td>
      <td>B005LERHD8A28R86QYMFFPA0</td>
      <td>1</td>
      <td>i paid  cents for this necklace plus free ship...</td>
      <td>2014</td>
      <td>i paid 86 cents for this necklace, plus free s...</td>
    </tr>
    <tr>
      <th>161285</th>
      <td>161285</td>
      <td>A2MFNTFPGAKXOL</td>
      <td>B005LERHD8</td>
      <td>Amber</td>
      <td>[0, 0]</td>
      <td>Very cute necklace. Very pretty coloring. Thos...</td>
      <td>5.0</td>
      <td>Nice....</td>
      <td>1395964800</td>
      <td>03 28, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>181.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>VerycutenecklaceVeryprettycoloringThosecolorsa...</td>
      <td>Nice</td>
      <td>139</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-28</td>
      <td>3</td>
      <td>B005LERHD8A2MFNTFPGAKXOL</td>
      <td>1</td>
      <td>Very cute necklace Very pretty coloring Those ...</td>
      <td>2014</td>
      <td>Very cute necklace. Very pretty coloring. Thos...</td>
    </tr>
    <tr>
      <th>161286</th>
      <td>161286</td>
      <td>A45WVAPIFZHTA</td>
      <td>B005LERHD8</td>
      <td>Amber Roper</td>
      <td>[0, 0]</td>
      <td>Cute. Great for the price........ If it was an...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1388966400</td>
      <td>01 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>CuteGreatforthepriceIfitwasanyhigherIwouldsayn...</td>
      <td>Cute</td>
      <td>115</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-06</td>
      <td>1</td>
      <td>B005LERHD8A45WVAPIFZHTA</td>
      <td>1</td>
      <td>Cute Great for the price If it was any higher ...</td>
      <td>2014</td>
      <td>Cute. Great for the price........ If it was an...</td>
    </tr>
    <tr>
      <th>161287</th>
      <td>161287</td>
      <td>A1MPIG72UADQYT</td>
      <td>B005LERHD8</td>
      <td>Amber Spaulding</td>
      <td>[1, 1]</td>
      <td>I like this necklace!  I like the colors.It is...</td>
      <td>4.0</td>
      <td>like!</td>
      <td>1388793600</td>
      <td>01 4, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>130.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlikethisnecklaceIlikethecolorsItissupercutean...</td>
      <td>like</td>
      <td>98</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-04</td>
      <td>1</td>
      <td>B005LERHD8A1MPIG72UADQYT</td>
      <td>1</td>
      <td>I like this necklace  I like the colorsIt is s...</td>
      <td>2014</td>
      <td>I like this necklace!  I like the colors.It is...</td>
    </tr>
    <tr>
      <th>161288</th>
      <td>161288</td>
      <td>A1LGJNC4KJV8SM</td>
      <td>B005LERHD8</td>
      <td>Ameroq01 "Naomi"</td>
      <td>[0, 0]</td>
      <td>This necklace is adorable and so cheap! It loo...</td>
      <td>5.0</td>
      <td>Amazing deal!</td>
      <td>1395014400</td>
      <td>03 17, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>183.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThisnecklaceisadorableandsocheapItlookscuteand...</td>
      <td>Amazingdeal</td>
      <td>145</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-17</td>
      <td>3</td>
      <td>B005LERHD8A1LGJNC4KJV8SM</td>
      <td>1</td>
      <td>This necklace is adorable and so cheap It look...</td>
      <td>2014</td>
      <td>This necklace is adorable and so cheap! It loo...</td>
    </tr>
    <tr>
      <th>161289</th>
      <td>161289</td>
      <td>A1XDE3Z328M3EZ</td>
      <td>B005LERHD8</td>
      <td>Amy Freeman</td>
      <td>[0, 0]</td>
      <td>Gave this to a friend who loves owls - it's no...</td>
      <td>5.0</td>
      <td>Super cute</td>
      <td>1355097600</td>
      <td>12 10, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>130.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Gavethistoafriendwholovesowlsitsnotascheapqual...</td>
      <td>Supercute</td>
      <td>99</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-10</td>
      <td>12</td>
      <td>B005LERHD8A1XDE3Z328M3EZ</td>
      <td>1</td>
      <td>Gave this to a friend who loves owls  its not ...</td>
      <td>2012</td>
      <td>Gave this to a friend who loves owls - it's no...</td>
    </tr>
    <tr>
      <th>161290</th>
      <td>161290</td>
      <td>A2FAHY26BXZFWZ</td>
      <td>B005LERHD8</td>
      <td>ANA</td>
      <td>[0, 0]</td>
      <td>The owl is adorable but this pendant is much l...</td>
      <td>4.0</td>
      <td>very big</td>
      <td>1392681600</td>
      <td>02 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>163.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Theowlisadorablebutthispendantismuchlargerthan...</td>
      <td>verybig</td>
      <td>132</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-18</td>
      <td>2</td>
      <td>B005LERHD8A2FAHY26BXZFWZ</td>
      <td>1</td>
      <td>The owl is adorable but this pendant is much l...</td>
      <td>2014</td>
      <td>The owl is adorable but this pendant is much l...</td>
    </tr>
    <tr>
      <th>161291</th>
      <td>161291</td>
      <td>A1LTUBEOQP4XR1</td>
      <td>B005LERHD8</td>
      <td>Ana Santos</td>
      <td>[0, 0]</td>
      <td>When this arrived i was so excited but after i...</td>
      <td>3.0</td>
      <td>Hmm....Good</td>
      <td>1353628800</td>
      <td>11 23, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>294.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Whenthisarrivediwassoexcitedbutafteriworeitthe...</td>
      <td>HmmGood</td>
      <td>221</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-23</td>
      <td>11</td>
      <td>B005LERHD8A1LTUBEOQP4XR1</td>
      <td>0</td>
      <td>When this arrived i was so excited but after i...</td>
      <td>2012</td>
      <td>When this arrived i was so excited but after i...</td>
    </tr>
    <tr>
      <th>161292</th>
      <td>161292</td>
      <td>AE203EP4EE7XI</td>
      <td>B005LERHD8</td>
      <td>AnayaPapaya</td>
      <td>[0, 0]</td>
      <td>It looks cheap, but I guess its because it is ...</td>
      <td>5.0</td>
      <td>Cheap</td>
      <td>1391040000</td>
      <td>01 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>105.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ItlookscheapbutIguessitsbecauseitischeapGoodfo...</td>
      <td>Cheap</td>
      <td>81</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-30</td>
      <td>1</td>
      <td>B005LERHD8AE203EP4EE7XI</td>
      <td>1</td>
      <td>It looks cheap but I guess its because it is c...</td>
      <td>2014</td>
      <td>It looks cheap, but I guess its because it is ...</td>
    </tr>
    <tr>
      <th>161293</th>
      <td>161293</td>
      <td>A29SM9BXWMMRN8</td>
      <td>B005LERHD8</td>
      <td>Andie Mac</td>
      <td>[0, 0]</td>
      <td>The colors on the owl are beautiful and clear....</td>
      <td>3.0</td>
      <td>Owl necklace</td>
      <td>1373587200</td>
      <td>07 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>97.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThecolorsontheowlarebeautifulandclearTheneckla...</td>
      <td>Owlnecklace</td>
      <td>76</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-12</td>
      <td>7</td>
      <td>B005LERHD8A29SM9BXWMMRN8</td>
      <td>0</td>
      <td>The colors on the owl are beautiful and clear ...</td>
      <td>2013</td>
      <td>The colors on the owl are beautiful and clear....</td>
    </tr>
    <tr>
      <th>161294</th>
      <td>161294</td>
      <td>A1JXY9I578VQ3O</td>
      <td>B005LERHD8</td>
      <td>Angela D. Moore</td>
      <td>[75, 83]</td>
      <td>I paid a very small amount (plus shipping) for...</td>
      <td>5.0</td>
      <td>terrific for the price</td>
      <td>1324857600</td>
      <td>12 26, 2011</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>7</td>
      <td>0</td>
      <td>7</td>
      <td>1.000000</td>
      <td>548.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Ipaidaverysmallamountplusshippingforthisitemso...</td>
      <td>terrificfortheprice</td>
      <td>426</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2011-12-26</td>
      <td>12</td>
      <td>B005LERHD8A1JXY9I578VQ3O</td>
      <td>1</td>
      <td>I paid a very small amount plus shipping for t...</td>
      <td>2011</td>
      <td>I paid a very small amount (plus shipping) for...</td>
    </tr>
    <tr>
      <th>161295</th>
      <td>161295</td>
      <td>A2TJ58Y8SOKBS0</td>
      <td>B005LERHD8</td>
      <td>Angela</td>
      <td>[0, 0]</td>
      <td>This was a very pretty, vintage looking fashio...</td>
      <td>4.0</td>
      <td>Very pretty!</td>
      <td>1400976000</td>
      <td>05 25, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>134.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Thiswasaveryprettyvintagelookingfashionnecklac...</td>
      <td>Verypretty</td>
      <td>103</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-25</td>
      <td>5</td>
      <td>B005LERHD8A2TJ58Y8SOKBS0</td>
      <td>1</td>
      <td>This was a very pretty vintage looking fashion...</td>
      <td>2014</td>
      <td>This was a very pretty, vintage looking fashio...</td>
    </tr>
    <tr>
      <th>161296</th>
      <td>161296</td>
      <td>AO11MSNOPJQ0</td>
      <td>B005LERHD8</td>
      <td>Angela Minaya</td>
      <td>[0, 0]</td>
      <td>love it! they are quite cheap and beauty, i re...</td>
      <td>5.0</td>
      <td>Five Stars</td>
      <td>1405036800</td>
      <td>07 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>87.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>loveittheyarequitecheapandbeautyireallylovethe...</td>
      <td>FiveStars</td>
      <td>68</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-11</td>
      <td>7</td>
      <td>B005LERHD8AO11MSNOPJQ0</td>
      <td>1</td>
      <td>love it they are quite cheap and beauty i real...</td>
      <td>2014</td>
      <td>love it! they are quite cheap and beauty, i re...</td>
    </tr>
    <tr>
      <th>161297</th>
      <td>161297</td>
      <td>A3EHW6DPEYDUYC</td>
      <td>B005LERHD8</td>
      <td>Angel</td>
      <td>[0, 0]</td>
      <td>The price is wonderful!!! The owl is bigger th...</td>
      <td>5.0</td>
      <td>Perfect!</td>
      <td>1355788800</td>
      <td>12 18, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>204.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThepriceiswonderfulTheowlisbiggerthanthepictur...</td>
      <td>Perfect</td>
      <td>155</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-18</td>
      <td>12</td>
      <td>B005LERHD8A3EHW6DPEYDUYC</td>
      <td>1</td>
      <td>The price is wonderful The owl is bigger than ...</td>
      <td>2012</td>
      <td>The price is wonderful!!! The owl is bigger th...</td>
    </tr>
    <tr>
      <th>161298</th>
      <td>161298</td>
      <td>A18DGV8V66Q9C5</td>
      <td>B005LERHD8</td>
      <td>Angelica</td>
      <td>[0, 0]</td>
      <td>Order came way faster and the item was nicely ...</td>
      <td>5.0</td>
      <td>Cute!</td>
      <td>1390003200</td>
      <td>01 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>280.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Ordercamewayfasterandtheitemwasnicelypackageda...</td>
      <td>Cute</td>
      <td>224</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-18</td>
      <td>1</td>
      <td>B005LERHD8A18DGV8V66Q9C5</td>
      <td>1</td>
      <td>Order came way faster and the item was nicely ...</td>
      <td>2014</td>
      <td>Order came way faster and the item was nicely ...</td>
    </tr>
    <tr>
      <th>161299</th>
      <td>161299</td>
      <td>A2Z0MBZKCCO6DU</td>
      <td>B005LERHD8</td>
      <td>angelmimi</td>
      <td>[0, 0]</td>
      <td>Very cute! I have received many compliments wh...</td>
      <td>5.0</td>
      <td>owl necklaces</td>
      <td>1388966400</td>
      <td>01 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>122.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>VerycuteIhavereceivedmanycomplimentswhenIhavew...</td>
      <td>owlnecklaces</td>
      <td>97</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-06</td>
      <td>1</td>
      <td>B005LERHD8A2Z0MBZKCCO6DU</td>
      <td>1</td>
      <td>Very cute I have received many compliments whe...</td>
      <td>2014</td>
      <td>Very cute! I have received many compliments wh...</td>
    </tr>
    <tr>
      <th>161300</th>
      <td>161300</td>
      <td>A9C5ZLYHUWY20</td>
      <td>B005LERHD8</td>
      <td>AnimeMadness</td>
      <td>[0, 0]</td>
      <td>It took a VERRRRY long time for me to receive ...</td>
      <td>5.0</td>
      <td>Love it!</td>
      <td>1355702400</td>
      <td>12 17, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>293.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IttookaVERRRRYlongtimeformetoreceivethisinthem...</td>
      <td>Loveit</td>
      <td>227</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-17</td>
      <td>12</td>
      <td>B005LERHD8A9C5ZLYHUWY20</td>
      <td>1</td>
      <td>It took a VERRRRY long time for me to receive ...</td>
      <td>2012</td>
      <td>It took a VERRRRY long time for me to receive ...</td>
    </tr>
    <tr>
      <th>161301</th>
      <td>161301</td>
      <td>APKNHGY64IKCL</td>
      <td>B005LERHD8</td>
      <td>Ann E. Snowberger</td>
      <td>[0, 0]</td>
      <td>What a surprise, I was not expecting the owl t...</td>
      <td>5.0</td>
      <td>So cute</td>
      <td>1381881600</td>
      <td>10 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>117.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>WhatasurpriseIwasnotexpectingtheowltobethatlar...</td>
      <td>Socute</td>
      <td>89</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-16</td>
      <td>10</td>
      <td>B005LERHD8APKNHGY64IKCL</td>
      <td>1</td>
      <td>What a surprise I was not expecting the owl to...</td>
      <td>2013</td>
      <td>What a surprise, I was not expecting the owl t...</td>
    </tr>
    <tr>
      <th>161302</th>
      <td>161302</td>
      <td>A3FFHFJ9FWOECM</td>
      <td>B005LERHD8</td>
      <td>ANON</td>
      <td>[0, 0]</td>
      <td>I got this much quicker than expected (like te...</td>
      <td>3.0</td>
      <td>very cute</td>
      <td>1355184000</td>
      <td>12 11, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>783.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Igotthismuchquickerthanexpectedliketendaysbefo...</td>
      <td>verycute</td>
      <td>593</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-11</td>
      <td>12</td>
      <td>B005LERHD8A3FFHFJ9FWOECM</td>
      <td>0</td>
      <td>I got this much quicker than expected like ten...</td>
      <td>2012</td>
      <td>I got this much quicker than expected (like te...</td>
    </tr>
    <tr>
      <th>161303</th>
      <td>161303</td>
      <td>A2UTZJR4SM7I4B</td>
      <td>B005LERHD8</td>
      <td>april</td>
      <td>[0, 0]</td>
      <td>could be a lot better, very cheaply made and p...</td>
      <td>3.0</td>
      <td>Cheap</td>
      <td>1356480000</td>
      <td>12 26, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>111.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>couldbealotbetterverycheaplymadeandputtogether...</td>
      <td>Cheap</td>
      <td>87</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-26</td>
      <td>12</td>
      <td>B005LERHD8A2UTZJR4SM7I4B</td>
      <td>0</td>
      <td>could be a lot better very cheaply made and pu...</td>
      <td>2012</td>
      <td>could be a lot better, very cheaply made and p...</td>
    </tr>
    <tr>
      <th>161304</th>
      <td>161304</td>
      <td>A3VFGMYU1F44QJ</td>
      <td>B005LERHD8</td>
      <td>APZ</td>
      <td>[0, 0]</td>
      <td>I got these for my bridesmaids goody bags, the...</td>
      <td>4.0</td>
      <td>It is what you pay for.</td>
      <td>1371168000</td>
      <td>06 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>108.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Igottheseformybridesmaidsgoodybagstheywerewell...</td>
      <td>Itiswhatyoupayfor</td>
      <td>85</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-06-14</td>
      <td>6</td>
      <td>B005LERHD8A3VFGMYU1F44QJ</td>
      <td>1</td>
      <td>I got these for my bridesmaids goody bags they...</td>
      <td>2013</td>
      <td>I got these for my bridesmaids goody bags, the...</td>
    </tr>
    <tr>
      <th>161305</th>
      <td>161305</td>
      <td>A24G5PK4GSEU3T</td>
      <td>B005LERHD8</td>
      <td>Ashlee S.</td>
      <td>[0, 0]</td>
      <td>I am in love with owls, so I thought this woul...</td>
      <td>4.0</td>
      <td>Great necklace</td>
      <td>1383004800</td>
      <td>10 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>561.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IaminlovewithowlssoIthoughtthiswouldbeanicegif...</td>
      <td>Greatnecklace</td>
      <td>424</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-29</td>
      <td>10</td>
      <td>B005LERHD8A24G5PK4GSEU3T</td>
      <td>1</td>
      <td>I am in love with owls so I thought this would...</td>
      <td>2013</td>
      <td>I am in love with owls, so I thought this woul...</td>
    </tr>
    <tr>
      <th>161306</th>
      <td>161306</td>
      <td>A2D2VKIKZ26NZ0</td>
      <td>B005LERHD8</td>
      <td>Ashley Bayer</td>
      <td>[0, 0]</td>
      <td>I loved the necklace when i got it. It is a lo...</td>
      <td>5.0</td>
      <td>So pretty.</td>
      <td>1362009600</td>
      <td>02 28, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>138.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlovedthenecklacewhenigotitItisalongchainwitha...</td>
      <td>Sopretty</td>
      <td>103</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-28</td>
      <td>2</td>
      <td>B005LERHD8A2D2VKIKZ26NZ0</td>
      <td>1</td>
      <td>I loved the necklace when i got it It is a lon...</td>
      <td>2013</td>
      <td>I loved the necklace when i got it. It is a lo...</td>
    </tr>
    <tr>
      <th>161307</th>
      <td>161307</td>
      <td>AO9U85SU9FI7P</td>
      <td>B005LERHD8</td>
      <td>ashley elaine johnson</td>
      <td>[0, 1]</td>
      <td>This is a great buy for a gift or for personal...</td>
      <td>5.0</td>
      <td>Yes!</td>
      <td>1386288000</td>
      <td>12 6, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>139.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisagreatbuyforagiftorforpersonaluseTheyare...</td>
      <td>Yes</td>
      <td>108</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-06</td>
      <td>12</td>
      <td>B005LERHD8AO9U85SU9FI7P</td>
      <td>1</td>
      <td>This is a great buy for a gift or for personal...</td>
      <td>2013</td>
      <td>This is a great buy for a gift or for personal...</td>
    </tr>
    <tr>
      <th>161308</th>
      <td>161308</td>
      <td>AFJITL4YVUB9I</td>
      <td>B005LERHD8</td>
      <td>Ashley</td>
      <td>[0, 0]</td>
      <td>Totally adorbs. Can wear with costume and to w...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1393459200</td>
      <td>02 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>109.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>TotallyadorbsCanwearwithcostumeandtoworkaswell...</td>
      <td>Cute</td>
      <td>86</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-27</td>
      <td>2</td>
      <td>B005LERHD8AFJITL4YVUB9I</td>
      <td>1</td>
      <td>Totally adorbs Can wear with costume and to wo...</td>
      <td>2014</td>
      <td>Totally adorbs. Can wear with costume and to w...</td>
    </tr>
    <tr>
      <th>161309</th>
      <td>161309</td>
      <td>AWAZGG3YJMR06</td>
      <td>B005LERHD8</td>
      <td>atopaz</td>
      <td>[1, 1]</td>
      <td>I was excited to get this, but when it arrived...</td>
      <td>1.0</td>
      <td>broken upon arrival</td>
      <td>1363824000</td>
      <td>03 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>267.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Iwasexcitedtogetthisbutwhenitarrivedthechainwa...</td>
      <td>brokenuponarrival</td>
      <td>215</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-21</td>
      <td>3</td>
      <td>B005LERHD8AWAZGG3YJMR06</td>
      <td>0</td>
      <td>I was excited to get this but when it arrived ...</td>
      <td>2013</td>
      <td>I was excited to get this, but when it arrived...</td>
    </tr>
    <tr>
      <th>161310</th>
      <td>161310</td>
      <td>A386NBHW7C7T32</td>
      <td>B005LERHD8</td>
      <td>Autumn</td>
      <td>[0, 0]</td>
      <td>It looks almost exactly like the picture (bron...</td>
      <td>5.0</td>
      <td>Super cute!</td>
      <td>1390262400</td>
      <td>01 21, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>190.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Itlooksalmostexactlylikethepicturebronzeisdark...</td>
      <td>Supercute</td>
      <td>146</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-21</td>
      <td>1</td>
      <td>B005LERHD8A386NBHW7C7T32</td>
      <td>1</td>
      <td>It looks almost exactly like the picture bronz...</td>
      <td>2014</td>
      <td>It looks almost exactly like the picture (bron...</td>
    </tr>
    <tr>
      <th>161311</th>
      <td>161311</td>
      <td>A32IPFJR0A5XPF</td>
      <td>B005LERHD8</td>
      <td>bao xiong</td>
      <td>[0, 0]</td>
      <td>for the money its ok. got it for the daughter ...</td>
      <td>2.0</td>
      <td>somthing you get at the dollar store</td>
      <td>1392595200</td>
      <td>02 17, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>137.0</td>
      <td>Jewelry</td>
      <td>36.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>forthemoneyitsokgotitforthedaughterbadypartyas...</td>
      <td>somthingyougetatthedollarstore</td>
      <td>106</td>
      <td>30</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-17</td>
      <td>2</td>
      <td>B005LERHD8A32IPFJR0A5XPF</td>
      <td>0</td>
      <td>for the money its ok got it for the daughter b...</td>
      <td>2014</td>
      <td>for the money its ok. got it for the daughter ...</td>
    </tr>
    <tr>
      <th>161312</th>
      <td>161312</td>
      <td>AEKB9BBR4GB8I</td>
      <td>B005LERHD8</td>
      <td>Barbara Jones</td>
      <td>[1, 2]</td>
      <td>Not a fan of this product. I love Owls so that...</td>
      <td>2.0</td>
      <td>Owl Necklace</td>
      <td>1387238400</td>
      <td>12 17, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>202.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>NotafanofthisproductIloveOwlssothatiswhyIrated...</td>
      <td>OwlNecklace</td>
      <td>153</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-17</td>
      <td>12</td>
      <td>B005LERHD8AEKB9BBR4GB8I</td>
      <td>0</td>
      <td>Not a fan of this product I love Owls so that ...</td>
      <td>2013</td>
      <td>Not a fan of this product. I love Owls so that...</td>
    </tr>
    <tr>
      <th>161313</th>
      <td>161313</td>
      <td>A11X7N5RO4H6L9</td>
      <td>B005LERHD8</td>
      <td>Barbara J. Robinson</td>
      <td>[0, 0]</td>
      <td>Such a cute owl, large size will show well ove...</td>
      <td>4.0</td>
      <td>They are a Hoot!</td>
      <td>1382918400</td>
      <td>10 28, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Suchacuteowllargesizewillshowwelloversweatersa...</td>
      <td>TheyareaHoot</td>
      <td>102</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-28</td>
      <td>10</td>
      <td>B005LERHD8A11X7N5RO4H6L9</td>
      <td>1</td>
      <td>Such a cute owl large size will show well over...</td>
      <td>2013</td>
      <td>Such a cute owl, large size will show well ove...</td>
    </tr>
    <tr>
      <th>161314</th>
      <td>161314</td>
      <td>A16A5VFOGBQSDD</td>
      <td>B005LERHD8</td>
      <td>barroyo</td>
      <td>[1, 1]</td>
      <td>Great colors and style. Goes with other owl it...</td>
      <td>5.0</td>
      <td>Owl necklace</td>
      <td>1375142400</td>
      <td>07 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>113.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>GreatcolorsandstyleGoeswithotherowlitemsorjust...</td>
      <td>Owlnecklace</td>
      <td>91</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-30</td>
      <td>7</td>
      <td>B005LERHD8A16A5VFOGBQSDD</td>
      <td>1</td>
      <td>Great colors and style Goes with other owl ite...</td>
      <td>2013</td>
      <td>Great colors and style. Goes with other owl it...</td>
    </tr>
    <tr>
      <th>161315</th>
      <td>161315</td>
      <td>A2J19UTYODZC9Y</td>
      <td>B005LERHD8</td>
      <td>B. Cook</td>
      <td>[0, 0]</td>
      <td>This is a very cute necklace. It looks nice wi...</td>
      <td>5.0</td>
      <td>Versatile, Cute Necklace for a Great Price</td>
      <td>1390348800</td>
      <td>01 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>93.0</td>
      <td>Jewelry</td>
      <td>42.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThisisaverycutenecklaceItlooksnicewithalotofth...</td>
      <td>VersatileCuteNecklaceforaGreatPrice</td>
      <td>69</td>
      <td>35</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-22</td>
      <td>1</td>
      <td>B005LERHD8A2J19UTYODZC9Y</td>
      <td>1</td>
      <td>This is a very cute necklace It looks nice wit...</td>
      <td>2014</td>
      <td>This is a very cute necklace. It looks nice wi...</td>
    </tr>
    <tr>
      <th>161316</th>
      <td>161316</td>
      <td>A1G9H0NUKUH8LQ</td>
      <td>B005LERHD8</td>
      <td>b.donahue "b.donahue"</td>
      <td>[0, 0]</td>
      <td>theyre selling this same exact necklace on thi...</td>
      <td>5.0</td>
      <td>gorgeous</td>
      <td>1368835200</td>
      <td>05 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>152.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>theyresellingthissameexactnecklaceonthisothers...</td>
      <td>gorgeous</td>
      <td>125</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-18</td>
      <td>5</td>
      <td>B005LERHD8A1G9H0NUKUH8LQ</td>
      <td>1</td>
      <td>theyre selling this same exact necklace on thi...</td>
      <td>2013</td>
      <td>theyre selling this same exact necklace on thi...</td>
    </tr>
    <tr>
      <th>161317</th>
      <td>161317</td>
      <td>AY0SP69HCK3B9</td>
      <td>B005LERHD8</td>
      <td>beautiful82</td>
      <td>[0, 0]</td>
      <td>Absolutely beautiful. I love vintage jewelry o...</td>
      <td>5.0</td>
      <td>pendant</td>
      <td>1394496000</td>
      <td>03 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>227.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>AbsolutelybeautifulIlovevintagejewelryorjewelr...</td>
      <td>pendant</td>
      <td>183</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-11</td>
      <td>3</td>
      <td>B005LERHD8AY0SP69HCK3B9</td>
      <td>1</td>
      <td>Absolutely beautiful I love vintage jewelry or...</td>
      <td>2014</td>
      <td>Absolutely beautiful. I love vintage jewelry o...</td>
    </tr>
    <tr>
      <th>161318</th>
      <td>161318</td>
      <td>A2IDJWAS2Q87N6</td>
      <td>B005LERHD8</td>
      <td>becleecan</td>
      <td>[0, 0]</td>
      <td>I thought the chain on this baby would be long...</td>
      <td>3.0</td>
      <td>Shorter than expected</td>
      <td>1390435200</td>
      <td>01 23, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>364.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IthoughtthechainonthisbabywouldbelongerItisonl...</td>
      <td>Shorterthanexpected</td>
      <td>281</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-23</td>
      <td>1</td>
      <td>B005LERHD8A2IDJWAS2Q87N6</td>
      <td>0</td>
      <td>I thought the chain on this baby would be long...</td>
      <td>2014</td>
      <td>I thought the chain on this baby would be long...</td>
    </tr>
    <tr>
      <th>161319</th>
      <td>161319</td>
      <td>A1R8R0ZQB16BGR</td>
      <td>B005LERHD8</td>
      <td>BeeTx</td>
      <td>[0, 0]</td>
      <td>I got it for a gift and it was perfect. She lo...</td>
      <td>5.0</td>
      <td>This is very awesome!</td>
      <td>1394755200</td>
      <td>03 14, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>138.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IgotitforagiftanditwasperfectSheloveditandsodi...</td>
      <td>Thisisveryawesome</td>
      <td>105</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-14</td>
      <td>3</td>
      <td>B005LERHD8A1R8R0ZQB16BGR</td>
      <td>1</td>
      <td>I got it for a gift and it was perfect She lov...</td>
      <td>2014</td>
      <td>I got it for a gift and it was perfect. She lo...</td>
    </tr>
    <tr>
      <th>161320</th>
      <td>161320</td>
      <td>A2841XK79HBCTW</td>
      <td>B005LERHD8</td>
      <td>bellabear5</td>
      <td>[0, 0]</td>
      <td>This came exactly how it was explained and I a...</td>
      <td>5.0</td>
      <td>PERFECT</td>
      <td>1396915200</td>
      <td>04 8, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>161.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThiscameexactlyhowitwasexplainedandIamsohappyI...</td>
      <td>PERFECT</td>
      <td>120</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-08</td>
      <td>4</td>
      <td>B005LERHD8A2841XK79HBCTW</td>
      <td>1</td>
      <td>This came exactly how it was explained and I a...</td>
      <td>2014</td>
      <td>This came exactly how it was explained and I a...</td>
    </tr>
    <tr>
      <th>161321</th>
      <td>161321</td>
      <td>A3GT71XR0WXSBU</td>
      <td>B005LERHD8</td>
      <td>bethany</td>
      <td>[0, 0]</td>
      <td>I bought this as a gift to me i just started c...</td>
      <td>5.0</td>
      <td>For Me</td>
      <td>1387756800</td>
      <td>12 23, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>214.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iboughtthisasagifttomeijuststartedcollectingow...</td>
      <td>ForMe</td>
      <td>169</td>
      <td>5</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-23</td>
      <td>12</td>
      <td>B005LERHD8A3GT71XR0WXSBU</td>
      <td>1</td>
      <td>I bought this as a gift to me i just started c...</td>
      <td>2013</td>
      <td>I bought this as a gift to me i just started c...</td>
    </tr>
    <tr>
      <th>161322</th>
      <td>161322</td>
      <td>A13UXXA6YO0AVK</td>
      <td>B005LERHD8</td>
      <td>Beverly Pomeroy</td>
      <td>[1, 1]</td>
      <td>For the price you can't beat the style! My dau...</td>
      <td>5.0</td>
      <td>Retro owl is a hit</td>
      <td>1385942400</td>
      <td>12 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>192.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ForthepriceyoucantbeatthestyleMydaughterlovest...</td>
      <td>Retroowlisahit</td>
      <td>145</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-02</td>
      <td>12</td>
      <td>B005LERHD8A13UXXA6YO0AVK</td>
      <td>1</td>
      <td>For the price you cant beat the style My daugh...</td>
      <td>2013</td>
      <td>For the price you can't beat the style! My dau...</td>
    </tr>
    <tr>
      <th>161323</th>
      <td>161323</td>
      <td>A3U5M273GGGOB4</td>
      <td>B005LERHD8</td>
      <td>Beverly Rosoff</td>
      <td>[0, 0]</td>
      <td>I wore this to a play, and many people complem...</td>
      <td>5.0</td>
      <td>Very eye-catching</td>
      <td>1355702400</td>
      <td>12 17, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>157.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Iworethistoaplayandmanypeoplecomplementedmeont...</td>
      <td>Veryeyecatching</td>
      <td>122</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-17</td>
      <td>12</td>
      <td>B005LERHD8A3U5M273GGGOB4</td>
      <td>1</td>
      <td>I wore this to a play and many people compleme...</td>
      <td>2012</td>
      <td>I wore this to a play, and many people complem...</td>
    </tr>
    <tr>
      <th>161324</th>
      <td>161324</td>
      <td>A2SKEQT0WTB954</td>
      <td>B005LERHD8</td>
      <td>Big-Z</td>
      <td>[1, 1]</td>
      <td>Considering the price of this gift for a girlf...</td>
      <td>5.0</td>
      <td>Amazing Costume Jewelry</td>
      <td>1361059200</td>
      <td>02 17, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>571.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Consideringthepriceofthisgiftforagirlfrienditi...</td>
      <td>AmazingCostumeJewelry</td>
      <td>447</td>
      <td>21</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-17</td>
      <td>2</td>
      <td>B005LERHD8A2SKEQT0WTB954</td>
      <td>1</td>
      <td>Considering the price of this gift for a girlf...</td>
      <td>2013</td>
      <td>Considering the price of this gift for a girlf...</td>
    </tr>
    <tr>
      <th>161325</th>
      <td>161325</td>
      <td>AOSIE5ITEDVCL</td>
      <td>B005LERHD8</td>
      <td>blair321 "blair"</td>
      <td>[0, 0]</td>
      <td>Get compliments on the necklace, and bought mo...</td>
      <td>5.0</td>
      <td>Very cute, like it</td>
      <td>1394928000</td>
      <td>03 16, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Getcomplimentsonthenecklaceandboughtmoreforfri...</td>
      <td>Verycutelikeit</td>
      <td>100</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-16</td>
      <td>3</td>
      <td>B005LERHD8AOSIE5ITEDVCL</td>
      <td>1</td>
      <td>Get compliments on the necklace and bought mor...</td>
      <td>2014</td>
      <td>Get compliments on the necklace, and bought mo...</td>
    </tr>
    <tr>
      <th>161326</th>
      <td>161326</td>
      <td>ABNUFIO7SJQRL</td>
      <td>B005LERHD8</td>
      <td>blake ducharme</td>
      <td>[3, 4]</td>
      <td>Don't waste your time. Broke apart before gett...</td>
      <td>1.0</td>
      <td>Crap</td>
      <td>1366243200</td>
      <td>04 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>0.428571</td>
      <td>148.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>DontwasteyourtimeBrokeapartbeforegettingitouto...</td>
      <td>Crap</td>
      <td>116</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-18</td>
      <td>4</td>
      <td>B005LERHD8ABNUFIO7SJQRL</td>
      <td>0</td>
      <td>Dont waste your time Broke apart before gettin...</td>
      <td>2013</td>
      <td>Don't waste your time. Broke apart before gett...</td>
    </tr>
    <tr>
      <th>161327</th>
      <td>161327</td>
      <td>A3P1M63XLSY6E2</td>
      <td>B005LERHD8</td>
      <td>BLC Ohio</td>
      <td>[0, 0]</td>
      <td>This little fellow is kind if scary looking!!!...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1392422400</td>
      <td>02 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>107.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThislittlefellowiskindifscarylookingIhavenotwo...</td>
      <td>Cute</td>
      <td>82</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-15</td>
      <td>2</td>
      <td>B005LERHD8A3P1M63XLSY6E2</td>
      <td>1</td>
      <td>This little fellow is kind if scary looking I ...</td>
      <td>2014</td>
      <td>This little fellow is kind if scary looking!!!...</td>
    </tr>
    <tr>
      <th>161328</th>
      <td>161328</td>
      <td>A11DDUTSLAM4HF</td>
      <td>B005LERHD8</td>
      <td>bobbieG</td>
      <td>[0, 0]</td>
      <td>These may have also taken a long time to get b...</td>
      <td>5.0</td>
      <td>Retro Owl Pendant</td>
      <td>1398902400</td>
      <td>05 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>153.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Thesemayhavealsotakenalongtimetogetbutbelievet...</td>
      <td>RetroOwlPendant</td>
      <td>120</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-01</td>
      <td>5</td>
      <td>B005LERHD8A11DDUTSLAM4HF</td>
      <td>1</td>
      <td>These may have also taken a long time to get b...</td>
      <td>2014</td>
      <td>These may have also taken a long time to get b...</td>
    </tr>
    <tr>
      <th>161329</th>
      <td>161329</td>
      <td>A1781C6P9VMU9Q</td>
      <td>B005LERHD8</td>
      <td>Book girl Eva</td>
      <td>[0, 0]</td>
      <td>If found this necklace for a buck with free sh...</td>
      <td>3.0</td>
      <td>You get what you pay for</td>
      <td>1397779200</td>
      <td>04 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>735.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iffoundthisnecklaceforabuckwithfreeshippingand...</td>
      <td>Yougetwhatyoupayfor</td>
      <td>570</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-18</td>
      <td>4</td>
      <td>B005LERHD8A1781C6P9VMU9Q</td>
      <td>0</td>
      <td>If found this necklace for a buck with free sh...</td>
      <td>2014</td>
      <td>If found this necklace for a buck with free sh...</td>
    </tr>
    <tr>
      <th>161330</th>
      <td>161330</td>
      <td>A23CKP5AG4EAWN</td>
      <td>B005LERHD8</td>
      <td>Brandy Durham</td>
      <td>[0, 0]</td>
      <td>I loved My new necklace. It was a great price....</td>
      <td>5.0</td>
      <td>Looks better then picture....</td>
      <td>1380931200</td>
      <td>10 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>173.0</td>
      <td>Jewelry</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IlovedMynewnecklaceItwasagreatpriceAndlotsamaz...</td>
      <td>Looksbetterthenpicture</td>
      <td>134</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-05</td>
      <td>10</td>
      <td>B005LERHD8A23CKP5AG4EAWN</td>
      <td>1</td>
      <td>I loved My new necklace It was a great price A...</td>
      <td>2013</td>
      <td>I loved My new necklace. It was a great price....</td>
    </tr>
    <tr>
      <th>161331</th>
      <td>161331</td>
      <td>A3CM6AH2KNB09O</td>
      <td>B005LERHD8</td>
      <td>Brittanie Bush</td>
      <td>[0, 0]</td>
      <td>SO CUTE! I loved these necklaces! I bought fou...</td>
      <td>5.0</td>
      <td>LOVE</td>
      <td>1388016000</td>
      <td>12 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SOCUTEIlovedthesenecklacesIboughtfouroverthese...</td>
      <td>LOVE</td>
      <td>86</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-26</td>
      <td>12</td>
      <td>B005LERHD8A3CM6AH2KNB09O</td>
      <td>1</td>
      <td>SO CUTE I loved these necklaces I bought four ...</td>
      <td>2013</td>
      <td>SO CUTE! I loved these necklaces! I bought fou...</td>
    </tr>
    <tr>
      <th>161332</th>
      <td>161332</td>
      <td>ASR0WQ9JB4IC1</td>
      <td>B005LERHD8</td>
      <td>Brittany</td>
      <td>[1, 1]</td>
      <td>Looks exactly like the picture. It was a good ...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1375660800</td>
      <td>08 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>92.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>LooksexactlylikethepictureItwasagoodpriceIlove...</td>
      <td>Cute</td>
      <td>71</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-05</td>
      <td>8</td>
      <td>B005LERHD8ASR0WQ9JB4IC1</td>
      <td>1</td>
      <td>Looks exactly like the picture It was a good p...</td>
      <td>2013</td>
      <td>Looks exactly like the picture. It was a good ...</td>
    </tr>
    <tr>
      <th>161333</th>
      <td>161333</td>
      <td>A32O89QR4HUTJN</td>
      <td>B005LERHD8</td>
      <td>BRLA4LSU</td>
      <td>[0, 0]</td>
      <td>I love these, and they are adorable. The chain...</td>
      <td>5.0</td>
      <td>Cannot beat the price for these!</td>
      <td>1396828800</td>
      <td>04 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>229.0</td>
      <td>Jewelry</td>
      <td>32.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IlovetheseandtheyareadorableThechainisalittlef...</td>
      <td>Cannotbeatthepriceforthese</td>
      <td>179</td>
      <td>26</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-07</td>
      <td>4</td>
      <td>B005LERHD8A32O89QR4HUTJN</td>
      <td>1</td>
      <td>I love these and they are adorable The chain i...</td>
      <td>2014</td>
      <td>I love these, and they are adorable. The chain...</td>
    </tr>
    <tr>
      <th>161334</th>
      <td>161334</td>
      <td>A2COK6DKM6QO0O</td>
      <td>B005LERHD8</td>
      <td>Brycen Edwards</td>
      <td>[0, 0]</td>
      <td>You get what you paid for. it is not super wel...</td>
      <td>3.0</td>
      <td>Not bad.</td>
      <td>1383350400</td>
      <td>11 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>376.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>YougetwhatyoupaidforitisnotsuperwellmadebutIpa...</td>
      <td>Notbad</td>
      <td>294</td>
      <td>6</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-02</td>
      <td>11</td>
      <td>B005LERHD8A2COK6DKM6QO0O</td>
      <td>0</td>
      <td>You get what you paid for it is not super well...</td>
      <td>2013</td>
      <td>You get what you paid for. it is not super wel...</td>
    </tr>
    <tr>
      <th>161335</th>
      <td>161335</td>
      <td>ACB85Z7MMFWMY</td>
      <td>B005LERHD8</td>
      <td>B. Sy</td>
      <td>[0, 0]</td>
      <td>Does not look at all cute as the picture. Look...</td>
      <td>3.0</td>
      <td>ehh..</td>
      <td>1384041600</td>
      <td>11 10, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>DoesnotlookatallcuteasthepictureLookstarnished...</td>
      <td>ehh</td>
      <td>92</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-10</td>
      <td>11</td>
      <td>B005LERHD8ACB85Z7MMFWMY</td>
      <td>0</td>
      <td>Does not look at all cute as the picture Looks...</td>
      <td>2013</td>
      <td>Does not look at all cute as the picture. Look...</td>
    </tr>
    <tr>
      <th>161336</th>
      <td>161336</td>
      <td>A22R875US22R70</td>
      <td>B005LERHD8</td>
      <td>Calli Collins</td>
      <td>[0, 0]</td>
      <td>This is cheap, but cute! It breaks very easily...</td>
      <td>3.0</td>
      <td>You get what you pay for</td>
      <td>1356393600</td>
      <td>12 25, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>130.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThisischeapbutcuteItbreaksveryeasilybutifyouar...</td>
      <td>Yougetwhatyoupayfor</td>
      <td>100</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-25</td>
      <td>12</td>
      <td>B005LERHD8A22R875US22R70</td>
      <td>0</td>
      <td>This is cheap but cute It breaks very easily b...</td>
      <td>2012</td>
      <td>This is cheap, but cute! It breaks very easily...</td>
    </tr>
    <tr>
      <th>161337</th>
      <td>161337</td>
      <td>A2Z8MA2XD55HMF</td>
      <td>B005LERHD8</td>
      <td>Candice Hirschman</td>
      <td>[0, 0]</td>
      <td>This is a nice addition to any budding costume...</td>
      <td>5.0</td>
      <td>Gave as an awesome Gift</td>
      <td>1397088000</td>
      <td>04 10, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>193.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Thisisaniceadditiontoanybuddingcostumejewelryc...</td>
      <td>GaveasanawesomeGift</td>
      <td>154</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-10</td>
      <td>4</td>
      <td>B005LERHD8A2Z8MA2XD55HMF</td>
      <td>1</td>
      <td>This is a nice addition to any budding costume...</td>
      <td>2014</td>
      <td>This is a nice addition to any budding costume...</td>
    </tr>
    <tr>
      <th>161338</th>
      <td>161338</td>
      <td>A10RH01V89XHYW</td>
      <td>B005LERHD8</td>
      <td>Carole Mcintyre</td>
      <td>[0, 0]</td>
      <td>I bought 2 and given a gifts. Both people love...</td>
      <td>5.0</td>
      <td>Cute!</td>
      <td>1373760000</td>
      <td>07 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>174.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Ibought2andgivenagiftsBothpeoplelovethemTheyar...</td>
      <td>Cute</td>
      <td>136</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-14</td>
      <td>7</td>
      <td>B005LERHD8A10RH01V89XHYW</td>
      <td>1</td>
      <td>I bought  and given a gifts Both people love t...</td>
      <td>2013</td>
      <td>I bought 2 and given a gifts. Both people love...</td>
    </tr>
    <tr>
      <th>161339</th>
      <td>161339</td>
      <td>A2QSMKSU07K1HV</td>
      <td>B005LERHD8</td>
      <td>Carolen Gray</td>
      <td>[0, 0]</td>
      <td>The necklace is cute but it is of a cheaper ma...</td>
      <td>3.0</td>
      <td>cheaper than I thought</td>
      <td>1359849600</td>
      <td>02 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>145.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Thenecklaceiscutebutitisofacheapermaterialthan...</td>
      <td>cheaperthanIthought</td>
      <td>112</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-03</td>
      <td>2</td>
      <td>B005LERHD8A2QSMKSU07K1HV</td>
      <td>0</td>
      <td>The necklace is cute but it is of a cheaper ma...</td>
      <td>2013</td>
      <td>The necklace is cute but it is of a cheaper ma...</td>
    </tr>
    <tr>
      <th>161340</th>
      <td>161340</td>
      <td>A270Y8MB9VZDW6</td>
      <td>B005LERHD8</td>
      <td>Casey</td>
      <td>[0, 0]</td>
      <td>This chain is long and DOES NOT come with a cl...</td>
      <td>5.0</td>
      <td>Even cuter in person!</td>
      <td>1388016000</td>
      <td>12 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>155.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ThischainislongandDOESNOTcomewithaclaspHowever...</td>
      <td>Evencuterinperson</td>
      <td>119</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-26</td>
      <td>12</td>
      <td>B005LERHD8A270Y8MB9VZDW6</td>
      <td>1</td>
      <td>This chain is long and DOES NOT come with a cl...</td>
      <td>2013</td>
      <td>This chain is long and DOES NOT come with a cl...</td>
    </tr>
    <tr>
      <th>161341</th>
      <td>161341</td>
      <td>APLL7CBHYAGGQ</td>
      <td>B005LERHD8</td>
      <td>Cassandra</td>
      <td>[0, 0]</td>
      <td>Even though this owl is a bit bigger than I ex...</td>
      <td>5.0</td>
      <td>Better than I hoped!</td>
      <td>1359072000</td>
      <td>01 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>502.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>EventhoughthisowlisabitbiggerthanIexpectedthef...</td>
      <td>BetterthanIhoped</td>
      <td>387</td>
      <td>16</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-25</td>
      <td>1</td>
      <td>B005LERHD8APLL7CBHYAGGQ</td>
      <td>1</td>
      <td>Even though this owl is a bit bigger than I ex...</td>
      <td>2013</td>
      <td>Even though this owl is a bit bigger than I ex...</td>
    </tr>
    <tr>
      <th>161342</th>
      <td>161342</td>
      <td>ARF5YAIOVLCR1</td>
      <td>B005LERHD8</td>
      <td>cassie</td>
      <td>[1, 2]</td>
      <td>I loved the overall look of the necklace but I...</td>
      <td>3.0</td>
      <td>It was beautiful but the chain broke :(</td>
      <td>1380758400</td>
      <td>10 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>114.0</td>
      <td>Jewelry</td>
      <td>39.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IlovedtheoveralllookofthenecklacebutInevergott...</td>
      <td>Itwasbeautifulbutthechainbroke</td>
      <td>87</td>
      <td>30</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-03</td>
      <td>10</td>
      <td>B005LERHD8ARF5YAIOVLCR1</td>
      <td>0</td>
      <td>I loved the overall look of the necklace but I...</td>
      <td>2013</td>
      <td>I loved the overall look of the necklace but I...</td>
    </tr>
    <tr>
      <th>161343</th>
      <td>161343</td>
      <td>A2L0XMKSM2E33Y</td>
      <td>B005LERHD8</td>
      <td>C~A~T</td>
      <td>[0, 0]</td>
      <td>This item is cheap like the other reviews say,...</td>
      <td>5.0</td>
      <td>Cheap but totally cute.</td>
      <td>1380240000</td>
      <td>09 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>259.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Thisitemischeapliketheotherreviewssaybutwhatel...</td>
      <td>Cheapbuttotallycute</td>
      <td>206</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-27</td>
      <td>9</td>
      <td>B005LERHD8A2L0XMKSM2E33Y</td>
      <td>1</td>
      <td>This item is cheap like the other reviews say ...</td>
      <td>2013</td>
      <td>This item is cheap like the other reviews say,...</td>
    </tr>
    <tr>
      <th>161344</th>
      <td>161344</td>
      <td>A3B1IKBYRM39Y6</td>
      <td>B005LERHD8</td>
      <td>C. A. Wirfs "Buyer Extraordinaire"</td>
      <td>[0, 0]</td>
      <td>I bought this item really inexpensively and it...</td>
      <td>3.0</td>
      <td>It's cute but not great quality</td>
      <td>1365552000</td>
      <td>04 10, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>301.0</td>
      <td>Jewelry</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iboughtthisitemreallyinexpensivelyanditsreally...</td>
      <td>Itscutebutnotgreatquality</td>
      <td>242</td>
      <td>25</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-10</td>
      <td>4</td>
      <td>B005LERHD8A3B1IKBYRM39Y6</td>
      <td>0</td>
      <td>I bought this item really inexpensively and it...</td>
      <td>2013</td>
      <td>I bought this item really inexpensively and it...</td>
    </tr>
    <tr>
      <th>161345</th>
      <td>161345</td>
      <td>AVUJP7Z6BNT11</td>
      <td>B005LERHD8</td>
      <td>CB</td>
      <td>[0, 0]</td>
      <td>Very eye catching. Jewels need better glue, as...</td>
      <td>4.0</td>
      <td>Better glue needed</td>
      <td>1383609600</td>
      <td>11 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>96.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>VeryeyecatchingJewelsneedbetterglueasitdidnoth...</td>
      <td>Betterglueneeded</td>
      <td>74</td>
      <td>16</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-05</td>
      <td>11</td>
      <td>B005LERHD8AVUJP7Z6BNT11</td>
      <td>1</td>
      <td>Very eye catching Jewels need better glue as i...</td>
      <td>2013</td>
      <td>Very eye catching. Jewels need better glue, as...</td>
    </tr>
    <tr>
      <th>161346</th>
      <td>161346</td>
      <td>A1EOOM1EWVSSA1</td>
      <td>B005LERHD8</td>
      <td>C. C. King</td>
      <td>[0, 0]</td>
      <td>The charm is cute, the jewels are bright. Howe...</td>
      <td>3.0</td>
      <td>no clasp/closure</td>
      <td>1376265600</td>
      <td>08 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>479.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThecharmiscutethejewelsarebrightHoweverthechai...</td>
      <td>noclaspclosure</td>
      <td>365</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-12</td>
      <td>8</td>
      <td>B005LERHD8A1EOOM1EWVSSA1</td>
      <td>0</td>
      <td>The charm is cute the jewels are bright Howeve...</td>
      <td>2013</td>
      <td>The charm is cute, the jewels are bright. Howe...</td>
    </tr>
    <tr>
      <th>161347</th>
      <td>161347</td>
      <td>AGQCN4VIHNW47</td>
      <td>B005LERHD8</td>
      <td>Ccmarinho</td>
      <td>[0, 0]</td>
      <td>This is a fun necklace to add to a plain shirt...</td>
      <td>5.0</td>
      <td>Fun</td>
      <td>1391990400</td>
      <td>02 10, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisafunnecklacetoaddtoaplainshirtThecolorso...</td>
      <td>Fun</td>
      <td>95</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-10</td>
      <td>2</td>
      <td>B005LERHD8AGQCN4VIHNW47</td>
      <td>1</td>
      <td>This is a fun necklace to add to a plain shirt...</td>
      <td>2014</td>
      <td>This is a fun necklace to add to a plain shirt...</td>
    </tr>
    <tr>
      <th>161348</th>
      <td>161348</td>
      <td>A13UGU4VH0JLR</td>
      <td>B005LERHD8</td>
      <td>Celia Valentine</td>
      <td>[0, 2]</td>
      <td>Came fast and exactly as shown in the picture ...</td>
      <td>5.0</td>
      <td>BUY THIS :)</td>
      <td>1380844800</td>
      <td>10 4, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>0.000000</td>
      <td>162.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Camefastandexactlyasshowninthepictureextremely...</td>
      <td>BUYTHIS</td>
      <td>126</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-04</td>
      <td>10</td>
      <td>B005LERHD8A13UGU4VH0JLR</td>
      <td>1</td>
      <td>Came fast and exactly as shown in the picture ...</td>
      <td>2013</td>
      <td>Came fast and exactly as shown in the picture ...</td>
    </tr>
    <tr>
      <th>161349</th>
      <td>161349</td>
      <td>A10KHX41ONY4U1</td>
      <td>B005LERHD8</td>
      <td>C E Matthews</td>
      <td>[0, 0]</td>
      <td>This is super cute and I got it at a great low...</td>
      <td>5.0</td>
      <td>Great Piece of Costume Jewelry.</td>
      <td>1390694400</td>
      <td>01 26, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>236.0</td>
      <td>Jewelry</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisissupercuteandIgotitatagreatlowpriceMyteen...</td>
      <td>GreatPieceofCostumeJewelry</td>
      <td>180</td>
      <td>26</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-26</td>
      <td>1</td>
      <td>B005LERHD8A10KHX41ONY4U1</td>
      <td>1</td>
      <td>This is super cute and I got it at a great low...</td>
      <td>2014</td>
      <td>This is super cute and I got it at a great low...</td>
    </tr>
    <tr>
      <th>161350</th>
      <td>161350</td>
      <td>AE83ZOB7NUZSL</td>
      <td>B005LERHD8</td>
      <td>Cgodwin</td>
      <td>[1, 2]</td>
      <td>This is big and normally I do not wear big jew...</td>
      <td>5.0</td>
      <td>Adorable even for a person who isn't an owl pe...</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>461.0</td>
      <td>Jewelry</td>
      <td>51.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>ThisisbigandnormallyIdonotwearbigjewelryactual...</td>
      <td>Adorableevenforapersonwhoisntanowlperson</td>
      <td>355</td>
      <td>40</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B005LERHD8AE83ZOB7NUZSL</td>
      <td>1</td>
      <td>This is big and normally I do not wear big jew...</td>
      <td>2013</td>
      <td>This is big and normally I do not wear big jew...</td>
    </tr>
    <tr>
      <th>161351</th>
      <td>161351</td>
      <td>A3R8AY1ZQAIC9U</td>
      <td>B005LERHD8</td>
      <td>chef4disney</td>
      <td>[1, 2]</td>
      <td>Cute, very vintage looking, in person, it look...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1385769600</td>
      <td>11 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>137.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Cuteveryvintagelookinginpersonitlooksdarkertha...</td>
      <td>Cute</td>
      <td>107</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-30</td>
      <td>11</td>
      <td>B005LERHD8A3R8AY1ZQAIC9U</td>
      <td>1</td>
      <td>Cute very vintage looking in person it looks d...</td>
      <td>2013</td>
      <td>Cute, very vintage looking, in person, it look...</td>
    </tr>
    <tr>
      <th>161352</th>
      <td>161352</td>
      <td>A19V29WTUN6T0S</td>
      <td>B005LERHD8</td>
      <td>chels_21</td>
      <td>[0, 0]</td>
      <td>I got this for my brother's girlfriend, who lo...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1361836800</td>
      <td>02 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>217.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Igotthisformybrothersgirlfriendwholovesowlsfor...</td>
      <td>Cute</td>
      <td>168</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-26</td>
      <td>2</td>
      <td>B005LERHD8A19V29WTUN6T0S</td>
      <td>1</td>
      <td>I got this for my brothers girlfriend who love...</td>
      <td>2013</td>
      <td>I got this for my brother's girlfriend, who lo...</td>
    </tr>
    <tr>
      <th>161353</th>
      <td>161353</td>
      <td>A22LPY9LAPDQOA</td>
      <td>B005LERHD8</td>
      <td>Chelsea</td>
      <td>[0, 0]</td>
      <td>I should have expected it would be cheap, but ...</td>
      <td>2.0</td>
      <td>Broke the first day I wore it</td>
      <td>1367107200</td>
      <td>04 28, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>230.0</td>
      <td>Jewelry</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Ishouldhaveexpecteditwouldbecheapbutitbrokeont...</td>
      <td>BrokethefirstdayIworeit</td>
      <td>171</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-28</td>
      <td>4</td>
      <td>B005LERHD8A22LPY9LAPDQOA</td>
      <td>0</td>
      <td>I should have expected it would be cheap but i...</td>
      <td>2013</td>
      <td>I should have expected it would be cheap, but ...</td>
    </tr>
    <tr>
      <th>161354</th>
      <td>161354</td>
      <td>A1B00CRK8F5G7I</td>
      <td>B005LERHD8</td>
      <td>Chelsi Lee</td>
      <td>[0, 0]</td>
      <td>Bought it for my friend as a Christmas present...</td>
      <td>5.0</td>
      <td>Really Cute!</td>
      <td>1355356800</td>
      <td>12 13, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>337.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>BoughtitformyfriendasaChristmaspresentItarrive...</td>
      <td>ReallyCute</td>
      <td>261</td>
      <td>10</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-13</td>
      <td>12</td>
      <td>B005LERHD8A1B00CRK8F5G7I</td>
      <td>1</td>
      <td>Bought it for my friend as a Christmas present...</td>
      <td>2012</td>
      <td>Bought it for my friend as a Christmas present...</td>
    </tr>
    <tr>
      <th>161355</th>
      <td>161355</td>
      <td>A2U23FNU67T8KA</td>
      <td>B005LERHD8</td>
      <td>cheryl dantuono</td>
      <td>[0, 0]</td>
      <td>really cute will give to a friend that collect...</td>
      <td>5.0</td>
      <td>cute</td>
      <td>1394323200</td>
      <td>03 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>108.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>reallycutewillgivetoafriendthatcollectsowlswhi...</td>
      <td>cute</td>
      <td>87</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-09</td>
      <td>3</td>
      <td>B005LERHD8A2U23FNU67T8KA</td>
      <td>1</td>
      <td>really cute will give to a friend that collect...</td>
      <td>2014</td>
      <td>really cute will give to a friend that collect...</td>
    </tr>
    <tr>
      <th>161356</th>
      <td>161356</td>
      <td>AKP1DG8T1TQCM</td>
      <td>B005LERHD8</td>
      <td>Cheryl Dennis</td>
      <td>[0, 0]</td>
      <td>This will be a conversation piece.  It is very...</td>
      <td>5.0</td>
      <td>Conversation piece</td>
      <td>1384732800</td>
      <td>11 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>117.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ThiswillbeaconversationpieceItisverynicealthou...</td>
      <td>Conversationpiece</td>
      <td>91</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-18</td>
      <td>11</td>
      <td>B005LERHD8AKP1DG8T1TQCM</td>
      <td>1</td>
      <td>This will be a conversation piece  It is very ...</td>
      <td>2013</td>
      <td>This will be a conversation piece.  It is very...</td>
    </tr>
    <tr>
      <th>161357</th>
      <td>161357</td>
      <td>A1CKPO4W2C5PBK</td>
      <td>B005LERHD8</td>
      <td>Cheryl H.</td>
      <td>[1, 2]</td>
      <td>This is cute, durable, and a great bargain.Bet...</td>
      <td>5.0</td>
      <td>Whoo doesn't like a bargain?</td>
      <td>1376092800</td>
      <td>08 10, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>173.0</td>
      <td>Jewelry</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisiscutedurableandagreatbargainBetterquality...</td>
      <td>Whoodoesntlikeabargain</td>
      <td>138</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-10</td>
      <td>8</td>
      <td>B005LERHD8A1CKPO4W2C5PBK</td>
      <td>1</td>
      <td>This is cute durable and a great bargainBetter...</td>
      <td>2013</td>
      <td>This is cute, durable, and a great bargain.Bet...</td>
    </tr>
    <tr>
      <th>161358</th>
      <td>161358</td>
      <td>ADTPSVFOU5RMT</td>
      <td>B005LERHD8</td>
      <td>Chester_s26</td>
      <td>[0, 0]</td>
      <td>Colors are too bright and make this look like ...</td>
      <td>3.0</td>
      <td>Kid's necklace</td>
      <td>1383436800</td>
      <td>11 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>129.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Colorsaretoobrightandmakethislooklikeakidsneck...</td>
      <td>Kidsnecklace</td>
      <td>101</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-03</td>
      <td>11</td>
      <td>B005LERHD8ADTPSVFOU5RMT</td>
      <td>0</td>
      <td>Colors are too bright and make this look like ...</td>
      <td>2013</td>
      <td>Colors are too bright and make this look like ...</td>
    </tr>
    <tr>
      <th>161359</th>
      <td>161359</td>
      <td>A852I21I0KLM0</td>
      <td>B005LERHD8</td>
      <td>chinagirl3343</td>
      <td>[0, 0]</td>
      <td>I paid $1 for this pendent and no shipping. I ...</td>
      <td>4.0</td>
      <td>Color is darker</td>
      <td>1374710400</td>
      <td>07 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>441.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Ipaid1forthispendentandnoshippingIthinkitscute...</td>
      <td>Colorisdarker</td>
      <td>323</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-25</td>
      <td>7</td>
      <td>B005LERHD8A852I21I0KLM0</td>
      <td>1</td>
      <td>I paid  for this pendent and no shipping I thi...</td>
      <td>2013</td>
      <td>I paid $1 for this pendent and no shipping. I ...</td>
    </tr>
    <tr>
      <th>161360</th>
      <td>161360</td>
      <td>A2R5OBDJPV7M6T</td>
      <td>B005LERHD8</td>
      <td>Christine K. Trease</td>
      <td>[0, 1]</td>
      <td>Not the best quality, but it is a very nice ne...</td>
      <td>5.0</td>
      <td>Nice necklace</td>
      <td>1376524800</td>
      <td>08 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>NotthebestqualitybutitisaverynicenecklaceIboug...</td>
      <td>Nicenecklace</td>
      <td>100</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-15</td>
      <td>8</td>
      <td>B005LERHD8A2R5OBDJPV7M6T</td>
      <td>1</td>
      <td>Not the best quality but it is a very nice nec...</td>
      <td>2013</td>
      <td>Not the best quality, but it is a very nice ne...</td>
    </tr>
    <tr>
      <th>161361</th>
      <td>161361</td>
      <td>A29CEI6U2BLLCK</td>
      <td>B005LERHD8</td>
      <td>Cincymom "Love my kiddos"</td>
      <td>[0, 0]</td>
      <td>Cute little owl. Chain not so great but this i...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1382745600</td>
      <td>10 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>142.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>CutelittleowlChainnotsogreatbutthisiswellworth...</td>
      <td>Cute</td>
      <td>111</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-26</td>
      <td>10</td>
      <td>B005LERHD8A29CEI6U2BLLCK</td>
      <td>1</td>
      <td>Cute little owl Chain not so great but this is...</td>
      <td>2013</td>
      <td>Cute little owl. Chain not so great but this i...</td>
    </tr>
    <tr>
      <th>161362</th>
      <td>161362</td>
      <td>A63SUBOZPI0KQ</td>
      <td>B005LERHD8</td>
      <td>Cindy Stucker</td>
      <td>[0, 0]</td>
      <td>I was pleasantly surprised to receive this nec...</td>
      <td>5.0</td>
      <td>very nice for the price</td>
      <td>1392076800</td>
      <td>02 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>154.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Iwaspleasantlysurprisedtoreceivethisnecklaceit...</td>
      <td>verynicefortheprice</td>
      <td>124</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-11</td>
      <td>2</td>
      <td>B005LERHD8A63SUBOZPI0KQ</td>
      <td>1</td>
      <td>I was pleasantly surprised to receive this nec...</td>
      <td>2014</td>
      <td>I was pleasantly surprised to receive this nec...</td>
    </tr>
    <tr>
      <th>161363</th>
      <td>161363</td>
      <td>A1I2O8IWKYI8IO</td>
      <td>B005LERHD8</td>
      <td>coatzzz</td>
      <td>[0, 0]</td>
      <td>exactly as described and pretty fast shipping....</td>
      <td>5.0</td>
      <td>perfect</td>
      <td>1355011200</td>
      <td>12 9, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>164.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>exactlyasdescribedandprettyfastshippingiloveth...</td>
      <td>perfect</td>
      <td>130</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-09</td>
      <td>12</td>
      <td>B005LERHD8A1I2O8IWKYI8IO</td>
      <td>1</td>
      <td>exactly as described and pretty fast shipping ...</td>
      <td>2012</td>
      <td>exactly as described and pretty fast shipping....</td>
    </tr>
    <tr>
      <th>161364</th>
      <td>161364</td>
      <td>A1XHV2T4TODA51</td>
      <td>B005LERHD8</td>
      <td>Code3Ron</td>
      <td>[0, 0]</td>
      <td>I wouldn't have paid the suggested list price,...</td>
      <td>5.0</td>
      <td>Unbelievable price  - And a nice gift</td>
      <td>1384300800</td>
      <td>11 13, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>197.0</td>
      <td>Jewelry</td>
      <td>37.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Iwouldnthavepaidthesuggestedlistpricebutatamaz...</td>
      <td>UnbelievablepriceAndanicegift</td>
      <td>154</td>
      <td>29</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-13</td>
      <td>11</td>
      <td>B005LERHD8A1XHV2T4TODA51</td>
      <td>1</td>
      <td>I wouldnt have paid the suggested list price b...</td>
      <td>2013</td>
      <td>I wouldn't have paid the suggested list price,...</td>
    </tr>
    <tr>
      <th>161365</th>
      <td>161365</td>
      <td>A2QG84ZEFKUISL</td>
      <td>B005LERHD8</td>
      <td>Colleen Ruch "Colleen Ruch"</td>
      <td>[0, 0]</td>
      <td>i love this necklace. bright colors and good q...</td>
      <td>5.0</td>
      <td>yay</td>
      <td>1382054400</td>
      <td>10 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ilovethisnecklacebrightcolorsandgoodqualitycan...</td>
      <td>yay</td>
      <td>96</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-18</td>
      <td>10</td>
      <td>B005LERHD8A2QG84ZEFKUISL</td>
      <td>1</td>
      <td>i love this necklace bright colors and good qu...</td>
      <td>2013</td>
      <td>i love this necklace. bright colors and good q...</td>
    </tr>
    <tr>
      <th>161366</th>
      <td>161366</td>
      <td>A3TMT0DM8S7LDU</td>
      <td>B005LERHD8</td>
      <td>Colleen Wintz</td>
      <td>[0, 0]</td>
      <td>Very nice piece. Only real downside is it took...</td>
      <td>3.0</td>
      <td>very nice piece</td>
      <td>1388016000</td>
      <td>12 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>472.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>VerynicepieceOnlyrealdownsideisittooktoolongIo...</td>
      <td>verynicepiece</td>
      <td>370</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-26</td>
      <td>12</td>
      <td>B005LERHD8A3TMT0DM8S7LDU</td>
      <td>0</td>
      <td>Very nice piece Only real downside is it took ...</td>
      <td>2013</td>
      <td>Very nice piece. Only real downside is it took...</td>
    </tr>
    <tr>
      <th>161367</th>
      <td>161367</td>
      <td>A3M683NYYU7R4X</td>
      <td>B005LERHD8</td>
      <td>Colly</td>
      <td>[0, 0]</td>
      <td>I like this piece a lot. The colors are nice a...</td>
      <td>4.0</td>
      <td>Very nice</td>
      <td>1360281600</td>
      <td>02 8, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>160.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IlikethispiecealotThecolorsareniceanditsaneyec...</td>
      <td>Verynice</td>
      <td>124</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-08</td>
      <td>2</td>
      <td>B005LERHD8A3M683NYYU7R4X</td>
      <td>1</td>
      <td>I like this piece a lot The colors are nice an...</td>
      <td>2013</td>
      <td>I like this piece a lot. The colors are nice a...</td>
    </tr>
    <tr>
      <th>161368</th>
      <td>161368</td>
      <td>A1FVOVLVU7GDV8</td>
      <td>B005LERHD8</td>
      <td>Connie S. Taff "Love Technology"</td>
      <td>[0, 0]</td>
      <td>I ordered this for a gift for someone else but...</td>
      <td>5.0</td>
      <td>Great Necklace.</td>
      <td>1389744000</td>
      <td>01 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>150.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Iorderedthisforagiftforsomeoneelsebutkeptthisn...</td>
      <td>GreatNecklace</td>
      <td>119</td>
      <td>13</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-15</td>
      <td>1</td>
      <td>B005LERHD8A1FVOVLVU7GDV8</td>
      <td>1</td>
      <td>I ordered this for a gift for someone else but...</td>
      <td>2014</td>
      <td>I ordered this for a gift for someone else but...</td>
    </tr>
    <tr>
      <th>161369</th>
      <td>161369</td>
      <td>AONLQ4H00XKLO</td>
      <td>B005LERHD8</td>
      <td>Constance</td>
      <td>[0, 0]</td>
      <td>Along with everybody else who has reviewed thi...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1382400000</td>
      <td>10 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>302.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Alongwitheverybodyelsewhohasreviewedthistheowl...</td>
      <td>Cute</td>
      <td>235</td>
      <td>4</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-22</td>
      <td>10</td>
      <td>B005LERHD8AONLQ4H00XKLO</td>
      <td>1</td>
      <td>Along with everybody else who has reviewed thi...</td>
      <td>2013</td>
      <td>Along with everybody else who has reviewed thi...</td>
    </tr>
    <tr>
      <th>161370</th>
      <td>161370</td>
      <td>A3FJABXIPXWIY1</td>
      <td>B005LERHD8</td>
      <td>Cookie</td>
      <td>[0, 0]</td>
      <td>This owl goes with all my casual clothes it is...</td>
      <td>5.0</td>
      <td>Great Pendant</td>
      <td>1384819200</td>
      <td>11 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>95.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Thisowlgoeswithallmycasualclothesitisfuntowear...</td>
      <td>GreatPendant</td>
      <td>74</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-19</td>
      <td>11</td>
      <td>B005LERHD8A3FJABXIPXWIY1</td>
      <td>1</td>
      <td>This owl goes with all my casual clothes it is...</td>
      <td>2013</td>
      <td>This owl goes with all my casual clothes it is...</td>
    </tr>
    <tr>
      <th>161371</th>
      <td>161371</td>
      <td>AMMLTH9P315XX</td>
      <td>B005LERHD8</td>
      <td>Coraline Jones</td>
      <td>[0, 0]</td>
      <td>I got this for like $2, for myself, and once I...</td>
      <td>5.0</td>
      <td>Gorgeous gift</td>
      <td>1363046400</td>
      <td>03 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>234.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Igotthisforlike2formyselfandonceIgotitallmygir...</td>
      <td>Gorgeousgift</td>
      <td>181</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-12</td>
      <td>3</td>
      <td>B005LERHD8AMMLTH9P315XX</td>
      <td>1</td>
      <td>I got this for like  for myself and once I got...</td>
      <td>2013</td>
      <td>I got this for like $2, for myself, and once I...</td>
    </tr>
    <tr>
      <th>161372</th>
      <td>161372</td>
      <td>A106GRKSYBW4X4</td>
      <td>B005LERHD8</td>
      <td>courtney</td>
      <td>[0, 0]</td>
      <td>What an adorable owl. Truly cute. Not super we...</td>
      <td>4.0</td>
      <td>Owl Only Have Eyes for You</td>
      <td>1390867200</td>
      <td>01 28, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>106.0</td>
      <td>Jewelry</td>
      <td>26.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>WhatanadorableowlTrulycuteNotsuperwellmadesoit...</td>
      <td>OwlOnlyHaveEyesforYou</td>
      <td>81</td>
      <td>21</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-28</td>
      <td>1</td>
      <td>B005LERHD8A106GRKSYBW4X4</td>
      <td>1</td>
      <td>What an adorable owl Truly cute Not super well...</td>
      <td>2014</td>
      <td>What an adorable owl. Truly cute. Not super we...</td>
    </tr>
    <tr>
      <th>161373</th>
      <td>161373</td>
      <td>A2Q9AEYIBUG2WQ</td>
      <td>B005LERHD8</td>
      <td>crazy4beardies</td>
      <td>[0, 0]</td>
      <td>This vintage owl pendant is so pretty. Its the...</td>
      <td>5.0</td>
      <td>Owl Pendant!</td>
      <td>1364515200</td>
      <td>03 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>182.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThisvintageowlpendantissoprettyItstheperfectle...</td>
      <td>OwlPendant</td>
      <td>144</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-29</td>
      <td>3</td>
      <td>B005LERHD8A2Q9AEYIBUG2WQ</td>
      <td>1</td>
      <td>This vintage owl pendant is so pretty Its the ...</td>
      <td>2013</td>
      <td>This vintage owl pendant is so pretty. Its the...</td>
    </tr>
    <tr>
      <th>161374</th>
      <td>161374</td>
      <td>A1Z1RXWN99W6U7</td>
      <td>B005LERHD8</td>
      <td>Cris</td>
      <td>[0, 0]</td>
      <td>MY GRAND DAUGHTER LOVES OWLS AND THOUGHT THIS ...</td>
      <td>1.0</td>
      <td>GARBAGE</td>
      <td>1401408000</td>
      <td>05 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>174.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>MYGRANDDAUGHTERLOVESOWLSANDTHOUGHTTHISWOULDBEC...</td>
      <td>GARBAGE</td>
      <td>138</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-30</td>
      <td>5</td>
      <td>B005LERHD8A1Z1RXWN99W6U7</td>
      <td>0</td>
      <td>MY GRAND DAUGHTER LOVES OWLS AND THOUGHT THIS ...</td>
      <td>2014</td>
      <td>MY GRAND DAUGHTER LOVES OWLS AND THOUGHT THIS ...</td>
    </tr>
    <tr>
      <th>161375</th>
      <td>161375</td>
      <td>A19R5LCSQUHDB0</td>
      <td>B005LERHD8</td>
      <td>Crystal Barrera</td>
      <td>[1, 1]</td>
      <td>I just wish I could find some earrings that ma...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1377043200</td>
      <td>08 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>226.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IjustwishIcouldfindsomeearringsthatmatchitIamt...</td>
      <td>Cute</td>
      <td>175</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-21</td>
      <td>8</td>
      <td>B005LERHD8A19R5LCSQUHDB0</td>
      <td>1</td>
      <td>I just wish I could find some earrings that ma...</td>
      <td>2013</td>
      <td>I just wish I could find some earrings that ma...</td>
    </tr>
    <tr>
      <th>161376</th>
      <td>161376</td>
      <td>A12RNPBA6RHPIG</td>
      <td>B005LERHD8</td>
      <td>Crystal</td>
      <td>[6, 8]</td>
      <td>I bought this for a friend and she absolutely ...</td>
      <td>5.0</td>
      <td>Cute Necklace for decent price!</td>
      <td>1357344000</td>
      <td>01 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>6</td>
      <td>8</td>
      <td>14</td>
      <td>0.428571</td>
      <td>111.0</td>
      <td>Jewelry</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IboughtthisforafriendandsheabsolutelyloveditIt...</td>
      <td>CuteNecklacefordecentprice</td>
      <td>88</td>
      <td>26</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-05</td>
      <td>1</td>
      <td>B005LERHD8A12RNPBA6RHPIG</td>
      <td>1</td>
      <td>I bought this for a friend and she absolutely ...</td>
      <td>2013</td>
      <td>I bought this for a friend and she absolutely ...</td>
    </tr>
    <tr>
      <th>161377</th>
      <td>161377</td>
      <td>A103H1FRENK1RX</td>
      <td>B005LERHD8</td>
      <td>dallas</td>
      <td>[0, 0]</td>
      <td>This necklace is gorgeous for the small amount...</td>
      <td>5.0</td>
      <td>owls</td>
      <td>1351382400</td>
      <td>10 28, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>242.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Thisnecklaceisgorgeousforthesmallamountwepaidf...</td>
      <td>owls</td>
      <td>179</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-10-28</td>
      <td>10</td>
      <td>B005LERHD8A103H1FRENK1RX</td>
      <td>1</td>
      <td>This necklace is gorgeous for the small amount...</td>
      <td>2012</td>
      <td>This necklace is gorgeous for the small amount...</td>
    </tr>
    <tr>
      <th>161378</th>
      <td>161378</td>
      <td>A24NCFZAQ56ZY5</td>
      <td>B005LERHD8</td>
      <td>Dan</td>
      <td>[0, 0]</td>
      <td>Pretty good for the price.Not the best quality...</td>
      <td>3.0</td>
      <td>Good for the price.</td>
      <td>1377475200</td>
      <td>08 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>200.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>PrettygoodforthepriceNotthebestqualitybutatlea...</td>
      <td>Goodfortheprice</td>
      <td>152</td>
      <td>15</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-26</td>
      <td>8</td>
      <td>B005LERHD8A24NCFZAQ56ZY5</td>
      <td>0</td>
      <td>Pretty good for the priceNot the best quality ...</td>
      <td>2013</td>
      <td>Pretty good for the price.Not the best quality...</td>
    </tr>
    <tr>
      <th>161379</th>
      <td>161379</td>
      <td>A26DRB2MLHDSHP</td>
      <td>B005LERHD8</td>
      <td>Danica Cooper</td>
      <td>[0, 0]</td>
      <td>I love owls, and this one is even cuter now th...</td>
      <td>5.0</td>
      <td>even cuter in person</td>
      <td>1361664000</td>
      <td>02 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>274.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IloveowlsandthisoneisevencuternowthatIhaveitin...</td>
      <td>evencuterinperson</td>
      <td>211</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-24</td>
      <td>2</td>
      <td>B005LERHD8A26DRB2MLHDSHP</td>
      <td>1</td>
      <td>I love owls and this one is even cuter now tha...</td>
      <td>2013</td>
      <td>I love owls, and this one is even cuter now th...</td>
    </tr>
    <tr>
      <th>161380</th>
      <td>161380</td>
      <td>A1NJ8GM0SJP4IB</td>
      <td>B005LERHD8</td>
      <td>Dani</td>
      <td>[0, 0]</td>
      <td>Definitely worth the buy, it's cute, I've actu...</td>
      <td>5.0</td>
      <td>Cute!</td>
      <td>1377129600</td>
      <td>08 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>299.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>DefinitelyworththebuyitscuteIveactuallyneverwo...</td>
      <td>Cute</td>
      <td>222</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-22</td>
      <td>8</td>
      <td>B005LERHD8A1NJ8GM0SJP4IB</td>
      <td>1</td>
      <td>Definitely worth the buy its cute Ive actually...</td>
      <td>2013</td>
      <td>Definitely worth the buy, it's cute, I've actu...</td>
    </tr>
    <tr>
      <th>161381</th>
      <td>161381</td>
      <td>A3SSIBP7BHW13Y</td>
      <td>B005LERHD8</td>
      <td>Darcy Malone</td>
      <td>[0, 0]</td>
      <td>This was an awesome find! It was cheap and I c...</td>
      <td>5.0</td>
      <td>Super Cute!!</td>
      <td>1387152000</td>
      <td>12 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>162.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThiswasanawesomefindItwascheapandIchangedthech...</td>
      <td>SuperCute</td>
      <td>125</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-16</td>
      <td>12</td>
      <td>B005LERHD8A3SSIBP7BHW13Y</td>
      <td>1</td>
      <td>This was an awesome find It was cheap and I ch...</td>
      <td>2013</td>
      <td>This was an awesome find! It was cheap and I c...</td>
    </tr>
    <tr>
      <th>161382</th>
      <td>161382</td>
      <td>A32XP7IIXWPYMY</td>
      <td>B005LERHD8</td>
      <td>David W. Doyle</td>
      <td>[0, 0]</td>
      <td>I bought this for my daughter, who loves to we...</td>
      <td>4.0</td>
      <td>Looks pretty on!</td>
      <td>1388361600</td>
      <td>12 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>107.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Iboughtthisformydaughterwholovestowearitwithhe...</td>
      <td>Looksprettyon</td>
      <td>83</td>
      <td>13</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-30</td>
      <td>12</td>
      <td>B005LERHD8A32XP7IIXWPYMY</td>
      <td>1</td>
      <td>I bought this for my daughter who loves to wea...</td>
      <td>2013</td>
      <td>I bought this for my daughter, who loves to we...</td>
    </tr>
    <tr>
      <th>161383</th>
      <td>161383</td>
      <td>A1S8HPS1UTJ3TV</td>
      <td>B005LERHD8</td>
      <td>Dawn S.</td>
      <td>[0, 0]</td>
      <td>Very cute pendant! The sparkly faux gemstones ...</td>
      <td>5.0</td>
      <td>SPARKLY!</td>
      <td>1363824000</td>
      <td>03 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>141.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VerycutependantThesparklyfauxgemstonescatchyou...</td>
      <td>SPARKLY</td>
      <td>111</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-21</td>
      <td>3</td>
      <td>B005LERHD8A1S8HPS1UTJ3TV</td>
      <td>1</td>
      <td>Very cute pendant The sparkly faux gemstones c...</td>
      <td>2013</td>
      <td>Very cute pendant! The sparkly faux gemstones ...</td>
    </tr>
    <tr>
      <th>161384</th>
      <td>161384</td>
      <td>A2AH4FBVVGMLD0</td>
      <td>B005LERHD8</td>
      <td>debrawidick</td>
      <td>[0, 0]</td>
      <td>Bought this for my Daughter and She Loved It.....</td>
      <td>5.0</td>
      <td>Too Cute</td>
      <td>1368921600</td>
      <td>05 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>BoughtthisformyDaughterandSheLovedItTheStoneCo...</td>
      <td>TooCute</td>
      <td>88</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-19</td>
      <td>5</td>
      <td>B005LERHD8A2AH4FBVVGMLD0</td>
      <td>1</td>
      <td>Bought this for my Daughter and She Loved It T...</td>
      <td>2013</td>
      <td>Bought this for my Daughter and She Loved It.....</td>
    </tr>
    <tr>
      <th>161385</th>
      <td>161385</td>
      <td>A2MC0IMUFSW8RY</td>
      <td>B005LERHD8</td>
      <td>Dee Mautz</td>
      <td>[0, 0]</td>
      <td>not fancy but can jazz up an everyday shirt an...</td>
      <td>3.0</td>
      <td>cute</td>
      <td>1387238400</td>
      <td>12 17, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>102.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>notfancybutcanjazzupaneverydayshirtandIloveowl...</td>
      <td>cute</td>
      <td>79</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-17</td>
      <td>12</td>
      <td>B005LERHD8A2MC0IMUFSW8RY</td>
      <td>0</td>
      <td>not fancy but can jazz up an everyday shirt an...</td>
      <td>2013</td>
      <td>not fancy but can jazz up an everyday shirt an...</td>
    </tr>
    <tr>
      <th>161386</th>
      <td>161386</td>
      <td>A1JLBNDDAJB4OP</td>
      <td>B005LERHD8</td>
      <td>DemeLott</td>
      <td>[1, 1]</td>
      <td>I absolutely love my owl necklace. It's so cut...</td>
      <td>5.0</td>
      <td>Cutest necklace</td>
      <td>1388275200</td>
      <td>12 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>276.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IabsolutelylovemyowlnecklaceItssocuteandtrendy...</td>
      <td>Cutestnecklace</td>
      <td>217</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-29</td>
      <td>12</td>
      <td>B005LERHD8A1JLBNDDAJB4OP</td>
      <td>1</td>
      <td>I absolutely love my owl necklace Its so cute ...</td>
      <td>2013</td>
      <td>I absolutely love my owl necklace. It's so cut...</td>
    </tr>
    <tr>
      <th>161387</th>
      <td>161387</td>
      <td>ACVIBENN5WELA</td>
      <td>B005LERHD8</td>
      <td>Denise Rossi</td>
      <td>[0, 1]</td>
      <td>The owl itself is much larger than what I thou...</td>
      <td>3.0</td>
      <td>You get what you pay for</td>
      <td>1387324800</td>
      <td>12 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>341.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>TheowlitselfismuchlargerthanwhatIthoughtitwoul...</td>
      <td>Yougetwhatyoupayfor</td>
      <td>260</td>
      <td>19</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-18</td>
      <td>12</td>
      <td>B005LERHD8ACVIBENN5WELA</td>
      <td>0</td>
      <td>The owl itself is much larger than what I thou...</td>
      <td>2013</td>
      <td>The owl itself is much larger than what I thou...</td>
    </tr>
    <tr>
      <th>161388</th>
      <td>161388</td>
      <td>A21WVQICXXQVAS</td>
      <td>B005LERHD8</td>
      <td>Denise Thompson</td>
      <td>[0, 0]</td>
      <td>Bought this for my friend for CHRISTmas.  She ...</td>
      <td>4.0</td>
      <td>CHRISTmas gift</td>
      <td>1389398400</td>
      <td>01 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>BoughtthisformyfriendforCHRISTmasSheloveditver...</td>
      <td>CHRISTmasgift</td>
      <td>90</td>
      <td>13</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-11</td>
      <td>1</td>
      <td>B005LERHD8A21WVQICXXQVAS</td>
      <td>1</td>
      <td>Bought this for my friend for CHRISTmas  She l...</td>
      <td>2014</td>
      <td>Bought this for my friend for CHRISTmas.  She ...</td>
    </tr>
    <tr>
      <th>161389</th>
      <td>161389</td>
      <td>A70QG78HDZLY7</td>
      <td>B005LERHD8</td>
      <td>Diane Goodman</td>
      <td>[0, 0]</td>
      <td>For the price I paid for this, I didn't really...</td>
      <td>5.0</td>
      <td>Surprisingly pretty</td>
      <td>1396483200</td>
      <td>04 3, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>195.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ForthepriceIpaidforthisIdidntreallyhavehugeexp...</td>
      <td>Surprisinglypretty</td>
      <td>148</td>
      <td>18</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-03</td>
      <td>4</td>
      <td>B005LERHD8A70QG78HDZLY7</td>
      <td>1</td>
      <td>For the price I paid for this I didnt really h...</td>
      <td>2014</td>
      <td>For the price I paid for this, I didn't really...</td>
    </tr>
    <tr>
      <th>161390</th>
      <td>161390</td>
      <td>AWF3MZW9OG5MV</td>
      <td>B005LERHD8</td>
      <td>Dijah</td>
      <td>[1, 1]</td>
      <td>I purchased this for my niece along with some ...</td>
      <td>5.0</td>
      <td>Great price for this necklace and 'free shipping"</td>
      <td>1385769600</td>
      <td>11 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>100.0</td>
      <td>Jewelry</td>
      <td>49.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Ipurchasedthisformyniecealongwithsomevintageea...</td>
      <td>Greatpriceforthisnecklaceandfreeshipping</td>
      <td>79</td>
      <td>40</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-30</td>
      <td>11</td>
      <td>B005LERHD8AWF3MZW9OG5MV</td>
      <td>1</td>
      <td>I purchased this for my niece along with some ...</td>
      <td>2013</td>
      <td>I purchased this for my niece along with some ...</td>
    </tr>
    <tr>
      <th>161391</th>
      <td>161391</td>
      <td>APC5UWLTPHUYR</td>
      <td>B005LERHD8</td>
      <td>DJ</td>
      <td>[0, 0]</td>
      <td>What you see on the pictures, you won't get.Th...</td>
      <td>2.0</td>
      <td>Not so glossy</td>
      <td>1392508800</td>
      <td>02 16, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>182.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>WhatyouseeonthepicturesyouwontgetThestonesaren...</td>
      <td>Notsoglossy</td>
      <td>139</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-16</td>
      <td>2</td>
      <td>B005LERHD8APC5UWLTPHUYR</td>
      <td>0</td>
      <td>What you see on the pictures you wont getThe s...</td>
      <td>2014</td>
      <td>What you see on the pictures, you won't get.Th...</td>
    </tr>
    <tr>
      <th>161392</th>
      <td>161392</td>
      <td>A1PQJBRZLS0ZWY</td>
      <td>B005LERHD8</td>
      <td>D. Kaiser "Myke xlong"</td>
      <td>[0, 0]</td>
      <td>got this as a gift and they liked it a lot..it...</td>
      <td>5.0</td>
      <td>great gift</td>
      <td>1365638400</td>
      <td>04 11, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>gotthisasagiftandtheylikeditalotitwasawellmade...</td>
      <td>greatgift</td>
      <td>91</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-11</td>
      <td>4</td>
      <td>B005LERHD8A1PQJBRZLS0ZWY</td>
      <td>1</td>
      <td>got this as a gift and they liked it a lotit w...</td>
      <td>2013</td>
      <td>got this as a gift and they liked it a lot..it...</td>
    </tr>
    <tr>
      <th>161393</th>
      <td>161393</td>
      <td>APE685XV6CGBQ</td>
      <td>B005LERHD8</td>
      <td>D. LOVATO "Ring Maven"</td>
      <td>[1, 1]</td>
      <td>I bought this as a gift for one of my sister i...</td>
      <td>5.0</td>
      <td>Very Cute!</td>
      <td>1363564800</td>
      <td>03 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>161.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iboughtthisasagiftforoneofmysisterinlawsthatli...</td>
      <td>VeryCute</td>
      <td>122</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-18</td>
      <td>3</td>
      <td>B005LERHD8APE685XV6CGBQ</td>
      <td>1</td>
      <td>I bought this as a gift for one of my sister i...</td>
      <td>2013</td>
      <td>I bought this as a gift for one of my sister i...</td>
    </tr>
    <tr>
      <th>161394</th>
      <td>161394</td>
      <td>A1Q5O65V2SKM4J</td>
      <td>B005LERHD8</td>
      <td>Donna Friedman</td>
      <td>[0, 0]</td>
      <td>My niece collect all things owl. She was so ha...</td>
      <td>5.0</td>
      <td>Very, very cute</td>
      <td>1371081600</td>
      <td>06 13, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>169.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>MyniececollectallthingsowlShewassohappytogetth...</td>
      <td>Veryverycute</td>
      <td>131</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-06-13</td>
      <td>6</td>
      <td>B005LERHD8A1Q5O65V2SKM4J</td>
      <td>1</td>
      <td>My niece collect all things owl She was so hap...</td>
      <td>2013</td>
      <td>My niece collect all things owl. She was so ha...</td>
    </tr>
    <tr>
      <th>161395</th>
      <td>161395</td>
      <td>A3M1OGVMN786AS</td>
      <td>B005LERHD8</td>
      <td>Dorian</td>
      <td>[0, 0]</td>
      <td>I love the product and so does the person who ...</td>
      <td>5.0</td>
      <td>Vibrant and Vintage!</td>
      <td>1388275200</td>
      <td>12 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>250.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Ilovetheproductandsodoesthepersonwhoreceivedit...</td>
      <td>VibrantandVintage</td>
      <td>195</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-29</td>
      <td>12</td>
      <td>B005LERHD8A3M1OGVMN786AS</td>
      <td>1</td>
      <td>I love the product and so does the person who ...</td>
      <td>2013</td>
      <td>I love the product and so does the person who ...</td>
    </tr>
    <tr>
      <th>161396</th>
      <td>161396</td>
      <td>A2DAZ1G64BEP61</td>
      <td>B005LERHD8</td>
      <td>Dosmastr "dosmastr"</td>
      <td>[0, 0]</td>
      <td>Wife loved it. Its not too heavy and has held ...</td>
      <td>5.0</td>
      <td>Cute and so far durable</td>
      <td>1398124800</td>
      <td>04 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>141.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>WifeloveditItsnottooheavyandhasheldupprettywel...</td>
      <td>Cuteandsofardurable</td>
      <td>110</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-22</td>
      <td>4</td>
      <td>B005LERHD8A2DAZ1G64BEP61</td>
      <td>1</td>
      <td>Wife loved it Its not too heavy and has held u...</td>
      <td>2014</td>
      <td>Wife loved it. Its not too heavy and has held ...</td>
    </tr>
    <tr>
      <th>161397</th>
      <td>161397</td>
      <td>A2VE815L52VZZJ</td>
      <td>B005LERHD8</td>
      <td>dp</td>
      <td>[1, 1]</td>
      <td>I got this for my sister, she collects owls, s...</td>
      <td>5.0</td>
      <td>Nice</td>
      <td>1388275200</td>
      <td>12 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>99.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Igotthisformysistershecollectsowlssheishappywi...</td>
      <td>Nice</td>
      <td>76</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-29</td>
      <td>12</td>
      <td>B005LERHD8A2VE815L52VZZJ</td>
      <td>1</td>
      <td>I got this for my sister she collects owls she...</td>
      <td>2013</td>
      <td>I got this for my sister, she collects owls, s...</td>
    </tr>
    <tr>
      <th>161398</th>
      <td>161398</td>
      <td>A3VMANW8LDJCN5</td>
      <td>B005LERHD8</td>
      <td>Dr of Foot and Ankle</td>
      <td>[2, 3]</td>
      <td>I ordered several of these for gifts.  They ar...</td>
      <td>5.0</td>
      <td>Fun!</td>
      <td>1380153600</td>
      <td>09 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>131.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IorderedseveraloftheseforgiftsTheyaresurprisin...</td>
      <td>Fun</td>
      <td>107</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-26</td>
      <td>9</td>
      <td>B005LERHD8A3VMANW8LDJCN5</td>
      <td>1</td>
      <td>I ordered several of these for gifts  They are...</td>
      <td>2013</td>
      <td>I ordered several of these for gifts.  They ar...</td>
    </tr>
    <tr>
      <th>161399</th>
      <td>161399</td>
      <td>A22A7DLQ7HVZXS</td>
      <td>B005LERHD8</td>
      <td>Dr. S.</td>
      <td>[0, 0]</td>
      <td>This is another beautiful owl pendant. I love ...</td>
      <td>5.0</td>
      <td>Another amazing deal, another amazing gift</td>
      <td>1400371200</td>
      <td>05 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>42.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThisisanotherbeautifulowlpendantIlovethisoneto...</td>
      <td>Anotheramazingdealanotheramazinggift</td>
      <td>89</td>
      <td>36</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-18</td>
      <td>5</td>
      <td>B005LERHD8A22A7DLQ7HVZXS</td>
      <td>1</td>
      <td>This is another beautiful owl pendant I love t...</td>
      <td>2014</td>
      <td>This is another beautiful owl pendant. I love ...</td>
    </tr>
    <tr>
      <th>161400</th>
      <td>161400</td>
      <td>A3AFF6XMHMG9TD</td>
      <td>B005LERHD8</td>
      <td>DweebyChic</td>
      <td>[0, 1]</td>
      <td>I was a bit skeptical about the quality of the...</td>
      <td>4.0</td>
      <td>Larger than pictured, seriously adorable!</td>
      <td>1384992000</td>
      <td>11 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>454.0</td>
      <td>Jewelry</td>
      <td>41.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iwasabitskepticalaboutthequalityofthenecklaces...</td>
      <td>Largerthanpicturedseriouslyadorable</td>
      <td>358</td>
      <td>35</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-21</td>
      <td>11</td>
      <td>B005LERHD8A3AFF6XMHMG9TD</td>
      <td>1</td>
      <td>I was a bit skeptical about the quality of the...</td>
      <td>2013</td>
      <td>I was a bit skeptical about the quality of the...</td>
    </tr>
    <tr>
      <th>161401</th>
      <td>161401</td>
      <td>A1PXCQE1R4403T</td>
      <td>B005LERHD8</td>
      <td>Edward E. Pruett "Old School Military"</td>
      <td>[0, 0]</td>
      <td>These were given as just because gifts. The la...</td>
      <td>5.0</td>
      <td>One better</td>
      <td>1353024000</td>
      <td>11 16, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>121.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>TheseweregivenasjustbecausegiftsTheladiesloved...</td>
      <td>Onebetter</td>
      <td>96</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-16</td>
      <td>11</td>
      <td>B005LERHD8A1PXCQE1R4403T</td>
      <td>1</td>
      <td>These were given as just because gifts The lad...</td>
      <td>2012</td>
      <td>These were given as just because gifts. The la...</td>
    </tr>
    <tr>
      <th>161402</th>
      <td>161402</td>
      <td>A3F3XU38JKR1GU</td>
      <td>B005LERHD8</td>
      <td>Elisabeth Moore "Bitsy"</td>
      <td>[0, 0]</td>
      <td>Great item. Inexpensive but it works with most...</td>
      <td>5.0</td>
      <td>Beautiful</td>
      <td>1378944000</td>
      <td>09 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>134.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>GreatitemInexpensivebutitworkswithmostoutfitsL...</td>
      <td>Beautiful</td>
      <td>108</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-12</td>
      <td>9</td>
      <td>B005LERHD8A3F3XU38JKR1GU</td>
      <td>1</td>
      <td>Great item Inexpensive but it works with most ...</td>
      <td>2013</td>
      <td>Great item. Inexpensive but it works with most...</td>
    </tr>
    <tr>
      <th>161403</th>
      <td>161403</td>
      <td>AXQYYWEECIH54</td>
      <td>B005LERHD8</td>
      <td>Elizabeth Olsen</td>
      <td>[0, 0]</td>
      <td>I love this owl. It's amazing how nice it look...</td>
      <td>5.0</td>
      <td>Vintage, retro colorful crystal owl pendant an...</td>
      <td>1364688000</td>
      <td>03 31, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>69.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IlovethisowlItsamazinghowniceitlooksinpersonIw...</td>
      <td>Vintageretrocolorfulcrystalowlpendantandchainw...</td>
      <td>97</td>
      <td>57</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-31</td>
      <td>3</td>
      <td>B005LERHD8AXQYYWEECIH54</td>
      <td>1</td>
      <td>I love this owl Its amazing how nice it looks ...</td>
      <td>2013</td>
      <td>I love this owl. It's amazing how nice it look...</td>
    </tr>
    <tr>
      <th>161404</th>
      <td>161404</td>
      <td>A39BQMFXMMF5AF</td>
      <td>B005LERHD8</td>
      <td>Ellie "Ellie"</td>
      <td>[0, 0]</td>
      <td>Very cute owl. Doesn't look cheap at all. Cute...</td>
      <td>5.0</td>
      <td>Cute!!</td>
      <td>1361145600</td>
      <td>02 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>257.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>VerycuteowlDoesntlookcheapatallCutedetailIgoti...</td>
      <td>Cute</td>
      <td>194</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-18</td>
      <td>2</td>
      <td>B005LERHD8A39BQMFXMMF5AF</td>
      <td>1</td>
      <td>Very cute owl Doesnt look cheap at all Cute de...</td>
      <td>2013</td>
      <td>Very cute owl. Doesn't look cheap at all. Cute...</td>
    </tr>
    <tr>
      <th>161405</th>
      <td>161405</td>
      <td>A1D8KYAYOT4F1S</td>
      <td>B005LERHD8</td>
      <td>EllyElectricity:)</td>
      <td>[0, 0]</td>
      <td>I got this and I really like it. I tried to or...</td>
      <td>4.0</td>
      <td>Not bad just kinda fimsy.</td>
      <td>1383523200</td>
      <td>11 4, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>126.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IgotthisandIreallylikeitItriedtoorderthesilver...</td>
      <td>Notbadjustkindafimsy</td>
      <td>93</td>
      <td>20</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-04</td>
      <td>11</td>
      <td>B005LERHD8A1D8KYAYOT4F1S</td>
      <td>1</td>
      <td>I got this and I really like it I tried to ord...</td>
      <td>2013</td>
      <td>I got this and I really like it. I tried to or...</td>
    </tr>
    <tr>
      <th>161406</th>
      <td>161406</td>
      <td>A1BNVW2LI29TZT</td>
      <td>B005LERHD8</td>
      <td>E Malatesta</td>
      <td>[0, 0]</td>
      <td>The charm itself is larger than I thought it w...</td>
      <td>4.0</td>
      <td>Very cute Owl!</td>
      <td>1390003200</td>
      <td>01 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>298.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThecharmitselfislargerthanIthoughtitwouldbeThe...</td>
      <td>VerycuteOwl</td>
      <td>231</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-18</td>
      <td>1</td>
      <td>B005LERHD8A1BNVW2LI29TZT</td>
      <td>1</td>
      <td>The charm itself is larger than I thought it w...</td>
      <td>2014</td>
      <td>The charm itself is larger than I thought it w...</td>
    </tr>
    <tr>
      <th>161407</th>
      <td>161407</td>
      <td>A3I5QDNVEZTZ11</td>
      <td>B005LERHD8</td>
      <td>Emily Lawrence</td>
      <td>[0, 0]</td>
      <td>This product broke the first time I wore it. I...</td>
      <td>1.0</td>
      <td>Broken</td>
      <td>1363651200</td>
      <td>03 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>171.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThisproductbrokethefirsttimeIworeitIwasnotroug...</td>
      <td>Broken</td>
      <td>127</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-19</td>
      <td>3</td>
      <td>B005LERHD8A3I5QDNVEZTZ11</td>
      <td>0</td>
      <td>This product broke the first time I wore it I ...</td>
      <td>2013</td>
      <td>This product broke the first time I wore it. I...</td>
    </tr>
    <tr>
      <th>161408</th>
      <td>161408</td>
      <td>A107SEAOVM1W10</td>
      <td>B005LERHD8</td>
      <td>Emmy-Kate</td>
      <td>[0, 0]</td>
      <td>great quality not only for the price, but I'd ...</td>
      <td>5.0</td>
      <td>amazing</td>
      <td>1382140800</td>
      <td>10 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>177.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>greatqualitynotonlyforthepricebutIdhavegotteni...</td>
      <td>amazing</td>
      <td>137</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-19</td>
      <td>10</td>
      <td>B005LERHD8A107SEAOVM1W10</td>
      <td>1</td>
      <td>great quality not only for the price but Id ha...</td>
      <td>2013</td>
      <td>great quality not only for the price, but I'd ...</td>
    </tr>
    <tr>
      <th>161409</th>
      <td>161409</td>
      <td>APLYFIZBJ4AVH</td>
      <td>B005LERHD8</td>
      <td>Erika Martinez</td>
      <td>[0, 0]</td>
      <td>This item was exactly as described and looked ...</td>
      <td>5.0</td>
      <td>Great Christmas gift</td>
      <td>1388620800</td>
      <td>01 2, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>291.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Thisitemwasexactlyasdescribedandlookedabitchea...</td>
      <td>GreatChristmasgift</td>
      <td>232</td>
      <td>18</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-02</td>
      <td>1</td>
      <td>B005LERHD8APLYFIZBJ4AVH</td>
      <td>1</td>
      <td>This item was exactly as described and looked ...</td>
      <td>2014</td>
      <td>This item was exactly as described and looked ...</td>
    </tr>
    <tr>
      <th>161410</th>
      <td>161410</td>
      <td>AB1PEQ3N6MPZ6</td>
      <td>B005LERHD8</td>
      <td>E. Truman</td>
      <td>[0, 0]</td>
      <td>I bought a bunch of these inexpensive necklace...</td>
      <td>3.0</td>
      <td>Ok ... Just ok</td>
      <td>1388707200</td>
      <td>01 3, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>398.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Iboughtabunchoftheseinexpensivenecklacesonawhi...</td>
      <td>OkJustok</td>
      <td>314</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-03</td>
      <td>1</td>
      <td>B005LERHD8AB1PEQ3N6MPZ6</td>
      <td>0</td>
      <td>I bought a bunch of these inexpensive necklace...</td>
      <td>2014</td>
      <td>I bought a bunch of these inexpensive necklace...</td>
    </tr>
    <tr>
      <th>161411</th>
      <td>161411</td>
      <td>A1MOJJMDH2T2M8</td>
      <td>B005LERHD8</td>
      <td>Eva</td>
      <td>[0, 0]</td>
      <td>this is really cute, I really love it and it d...</td>
      <td>5.0</td>
      <td>I love it</td>
      <td>1361923200</td>
      <td>02 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>thisisreallycuteIreallyloveitanditdosentlookch...</td>
      <td>Iloveit</td>
      <td>90</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-27</td>
      <td>2</td>
      <td>B005LERHD8A1MOJJMDH2T2M8</td>
      <td>1</td>
      <td>this is really cute I really love it and it do...</td>
      <td>2013</td>
      <td>this is really cute, I really love it and it d...</td>
    </tr>
    <tr>
      <th>161412</th>
      <td>161412</td>
      <td>A39JTUG0DPCV2X</td>
      <td>B005LERHD8</td>
      <td>Evangelina</td>
      <td>[0, 0]</td>
      <td>Even though the shipping took a few weeks, now...</td>
      <td>5.0</td>
      <td>Love it!</td>
      <td>1359158400</td>
      <td>01 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>365.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>EventhoughtheshippingtookafewweeksnowthatIfina...</td>
      <td>Loveit</td>
      <td>275</td>
      <td>6</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-26</td>
      <td>1</td>
      <td>B005LERHD8A39JTUG0DPCV2X</td>
      <td>1</td>
      <td>Even though the shipping took a few weeks now ...</td>
      <td>2013</td>
      <td>Even though the shipping took a few weeks, now...</td>
    </tr>
    <tr>
      <th>161413</th>
      <td>161413</td>
      <td>ACGPRUGGT0R7Y</td>
      <td>B005LERHD8</td>
      <td>Eva N.</td>
      <td>[0, 0]</td>
      <td>I was so happy when my friend said how much sh...</td>
      <td>5.0</td>
      <td>Gift for a dear friend who is like my sister.....</td>
      <td>1388707200</td>
      <td>01 3, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>1017.0</td>
      <td>Jewelry</td>
      <td>83.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Iwassohappywhenmyfriendsaidhowmuchshelovedhero...</td>
      <td>GiftforadearfriendwhoislikemysisterSHEHASRAVED...</td>
      <td>796</td>
      <td>65</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-03</td>
      <td>1</td>
      <td>B005LERHD8ACGPRUGGT0R7Y</td>
      <td>1</td>
      <td>I was so happy when my friend said how much sh...</td>
      <td>2014</td>
      <td>I was so happy when my friend said how much sh...</td>
    </tr>
    <tr>
      <th>161414</th>
      <td>161414</td>
      <td>A27O26RWSG2NUH</td>
      <td>B005LERHD8</td>
      <td>evelyn</td>
      <td>[0, 1]</td>
      <td>It arrived ahead of schedule, which still took...</td>
      <td>5.0</td>
      <td>Super cute!</td>
      <td>1379203200</td>
      <td>09 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>382.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Itarrivedaheadofschedulewhichstilltookabouttwo...</td>
      <td>Supercute</td>
      <td>293</td>
      <td>9</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-15</td>
      <td>9</td>
      <td>B005LERHD8A27O26RWSG2NUH</td>
      <td>1</td>
      <td>It arrived ahead of schedule which still took ...</td>
      <td>2013</td>
      <td>It arrived ahead of schedule, which still took...</td>
    </tr>
    <tr>
      <th>161415</th>
      <td>161415</td>
      <td>A8TWZ1N4FJW7R</td>
      <td>B005LERHD8</td>
      <td>fabiola</td>
      <td>[0, 0]</td>
      <td>Looks rusty old. I didn't like it i just put i...</td>
      <td>1.0</td>
      <td>ugly ugly ugly.</td>
      <td>1400112000</td>
      <td>05 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>LooksrustyoldIdidntlikeitijustputitinthetrashi...</td>
      <td>uglyuglyugly</td>
      <td>97</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-15</td>
      <td>5</td>
      <td>B005LERHD8A8TWZ1N4FJW7R</td>
      <td>0</td>
      <td>Looks rusty old I didnt like it i just put it ...</td>
      <td>2014</td>
      <td>Looks rusty old. I didn't like it i just put i...</td>
    </tr>
    <tr>
      <th>161416</th>
      <td>161416</td>
      <td>A30WJZP3WY23OW</td>
      <td>B005LERHD8</td>
      <td>FancifulWhimsy</td>
      <td>[0, 0]</td>
      <td>This is one of my absolute favorite pendants. ...</td>
      <td>5.0</td>
      <td>LOVE this pendant!!!</td>
      <td>1400716800</td>
      <td>05 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>745.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThisisoneofmyabsolutefavoritependantsThechaini...</td>
      <td>LOVEthispendant</td>
      <td>562</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-22</td>
      <td>5</td>
      <td>B005LERHD8A30WJZP3WY23OW</td>
      <td>1</td>
      <td>This is one of my absolute favorite pendants  ...</td>
      <td>2014</td>
      <td>This is one of my absolute favorite pendants. ...</td>
    </tr>
    <tr>
      <th>161417</th>
      <td>161417</td>
      <td>A1GMFWYSQ9N0T4</td>
      <td>B005LERHD8</td>
      <td>Fatima</td>
      <td>[0, 0]</td>
      <td>The Product is Tal Cual sign in the picture, I...</td>
      <td>5.0</td>
      <td>very good</td>
      <td>1393027200</td>
      <td>02 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>355.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>TheProductisTalCualsigninthepictureIalsoliketh...</td>
      <td>verygood</td>
      <td>278</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-22</td>
      <td>2</td>
      <td>B005LERHD8A1GMFWYSQ9N0T4</td>
      <td>1</td>
      <td>The Product is Tal Cual sign in the picture I ...</td>
      <td>2014</td>
      <td>The Product is Tal Cual sign in the picture, I...</td>
    </tr>
    <tr>
      <th>161418</th>
      <td>161418</td>
      <td>A1RFZGWX46N8H7</td>
      <td>B005LERHD8</td>
      <td>FlamingoNut "Tracey"</td>
      <td>[0, 0]</td>
      <td>I love owls, and although I knew I wasn't goin...</td>
      <td>4.0</td>
      <td>Great, if you like BIG jewelry, but I prefer i...</td>
      <td>1367193600</td>
      <td>04 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>406.0</td>
      <td>Jewelry</td>
      <td>68.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IloveowlsandalthoughIknewIwasntgoingtowearitIk...</td>
      <td>GreatifyoulikeBIGjewelrybutIpreferitasawindowo...</td>
      <td>317</td>
      <td>53</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-29</td>
      <td>4</td>
      <td>B005LERHD8A1RFZGWX46N8H7</td>
      <td>1</td>
      <td>I love owls and although I knew I wasnt going ...</td>
      <td>2013</td>
      <td>I love owls, and although I knew I wasn't goin...</td>
    </tr>
    <tr>
      <th>161419</th>
      <td>161419</td>
      <td>A10V735AKKTWOR</td>
      <td>B005LERHD8</td>
      <td>FLmommy</td>
      <td>[0, 0]</td>
      <td>Arrived in three weeks. Cuter than the picture...</td>
      <td>5.0</td>
      <td>Cuter than the picture~</td>
      <td>1387411200</td>
      <td>12 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>175.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ArrivedinthreeweeksCuterthanthepictureIwouldlo...</td>
      <td>Cuterthanthepicture</td>
      <td>133</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-19</td>
      <td>12</td>
      <td>B005LERHD8A10V735AKKTWOR</td>
      <td>1</td>
      <td>Arrived in three weeks Cuter than the picture ...</td>
      <td>2013</td>
      <td>Arrived in three weeks. Cuter than the picture...</td>
    </tr>
    <tr>
      <th>161420</th>
      <td>161420</td>
      <td>A5TSRI8S17ZBV</td>
      <td>B005LERHD8</td>
      <td>Forrest</td>
      <td>[0, 0]</td>
      <td>I bought this for my wife. She got it in the m...</td>
      <td>5.0</td>
      <td>Very nice!</td>
      <td>1354147200</td>
      <td>11 29, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>141.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IboughtthisformywifeShegotitinthemailandimmedi...</td>
      <td>Verynice</td>
      <td>109</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-29</td>
      <td>11</td>
      <td>B005LERHD8A5TSRI8S17ZBV</td>
      <td>1</td>
      <td>I bought this for my wife She got it in the ma...</td>
      <td>2012</td>
      <td>I bought this for my wife. She got it in the m...</td>
    </tr>
    <tr>
      <th>161421</th>
      <td>161421</td>
      <td>A117K94NFZEDHT</td>
      <td>B005LERHD8</td>
      <td>Frau Brunlich</td>
      <td>[0, 0]</td>
      <td>The owl charm is super cute and for this price...</td>
      <td>4.0</td>
      <td>Cute!</td>
      <td>1382572800</td>
      <td>10 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>130.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Theowlcharmissupercuteandforthispriceisgoingto...</td>
      <td>Cute</td>
      <td>103</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-24</td>
      <td>10</td>
      <td>B005LERHD8A117K94NFZEDHT</td>
      <td>1</td>
      <td>The owl charm is super cute and for this price...</td>
      <td>2013</td>
      <td>The owl charm is super cute and for this price...</td>
    </tr>
    <tr>
      <th>161422</th>
      <td>161422</td>
      <td>A3I9292W95USCW</td>
      <td>B005LERHD8</td>
      <td>Gabby</td>
      <td>[0, 0]</td>
      <td>I love the look of this bronze owl and it is a...</td>
      <td>5.0</td>
      <td>Golden Owl is Awesome</td>
      <td>1379203200</td>
      <td>09 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>158.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Ilovethelookofthisbronzeowlanditisadecentlengt...</td>
      <td>GoldenOwlisAwesome</td>
      <td>122</td>
      <td>18</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-15</td>
      <td>9</td>
      <td>B005LERHD8A3I9292W95USCW</td>
      <td>1</td>
      <td>I love the look of this bronze owl and it is a...</td>
      <td>2013</td>
      <td>I love the look of this bronze owl and it is a...</td>
    </tr>
    <tr>
      <th>161423</th>
      <td>161423</td>
      <td>A2YI4WRHX5F74S</td>
      <td>B005LERHD8</td>
      <td>Gagsmokefs32</td>
      <td>[0, 0]</td>
      <td>another of my favors items  I am always exchan...</td>
      <td>5.0</td>
      <td>loved it</td>
      <td>1391904000</td>
      <td>02 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>136.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>anotherofmyfavorsitemsIamalwaysexchangingbacka...</td>
      <td>lovedit</td>
      <td>110</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-09</td>
      <td>2</td>
      <td>B005LERHD8A2YI4WRHX5F74S</td>
      <td>1</td>
      <td>another of my favors items  I am always exchan...</td>
      <td>2014</td>
      <td>another of my favors items  I am always exchan...</td>
    </tr>
    <tr>
      <th>161424</th>
      <td>161424</td>
      <td>A3C1HD6PVYV119</td>
      <td>B005LERHD8</td>
      <td>gail capson</td>
      <td>[0, 0]</td>
      <td>I love them I actually sent the bronze one to ...</td>
      <td>5.0</td>
      <td>Beautiful looking pieces</td>
      <td>1396051200</td>
      <td>03 29, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>197.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IlovethemIactuallysentthebronzeonetomydaughter...</td>
      <td>Beautifullookingpieces</td>
      <td>155</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-29</td>
      <td>3</td>
      <td>B005LERHD8A3C1HD6PVYV119</td>
      <td>1</td>
      <td>I love them I actually sent the bronze one to ...</td>
      <td>2014</td>
      <td>I love them I actually sent the bronze one to ...</td>
    </tr>
    <tr>
      <th>161425</th>
      <td>161425</td>
      <td>A391IJ2DH5JJ7O</td>
      <td>B005LERHD8</td>
      <td>Gigi</td>
      <td>[0, 0]</td>
      <td>I bought a few of these for Christmas. The owl...</td>
      <td>4.0</td>
      <td>Nice.</td>
      <td>1392940800</td>
      <td>02 21, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>135.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IboughtafewoftheseforChristmasTheowlitselfisgo...</td>
      <td>Nice</td>
      <td>104</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-21</td>
      <td>2</td>
      <td>B005LERHD8A391IJ2DH5JJ7O</td>
      <td>1</td>
      <td>I bought a few of these for Christmas The owl ...</td>
      <td>2014</td>
      <td>I bought a few of these for Christmas. The owl...</td>
    </tr>
    <tr>
      <th>161426</th>
      <td>161426</td>
      <td>A1QCGYEVWLT6Z9</td>
      <td>B005LERHD8</td>
      <td>Gina Haney</td>
      <td>[0, 0]</td>
      <td>This goes with everything. It is great for eve...</td>
      <td>5.0</td>
      <td>CUTE!</td>
      <td>1381536000</td>
      <td>10 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>110.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisgoeswitheverythingItisgreatforeveryowllove...</td>
      <td>CUTE</td>
      <td>86</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-12</td>
      <td>10</td>
      <td>B005LERHD8A1QCGYEVWLT6Z9</td>
      <td>1</td>
      <td>This goes with everything It is great for ever...</td>
      <td>2013</td>
      <td>This goes with everything. It is great for eve...</td>
    </tr>
    <tr>
      <th>161427</th>
      <td>161427</td>
      <td>A2ZTZM6B8EEKIX</td>
      <td>B005LERHD8</td>
      <td>GlassMelts</td>
      <td>[0, 0]</td>
      <td>I've had this for a while now.  It's holding u...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1391731200</td>
      <td>02 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>203.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IvehadthisforawhilenowItsholdingupgreatthecrys...</td>
      <td>Cute</td>
      <td>151</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-07</td>
      <td>2</td>
      <td>B005LERHD8A2ZTZM6B8EEKIX</td>
      <td>1</td>
      <td>Ive had this for a while now  Its holding up g...</td>
      <td>2014</td>
      <td>I've had this for a while now.  It's holding u...</td>
    </tr>
    <tr>
      <th>161428</th>
      <td>161428</td>
      <td>AJKGF1DFANXE3</td>
      <td>B005LERHD8</td>
      <td>Glenda</td>
      <td>[0, 0]</td>
      <td>Very nice piece of costume jewelry. Goes with ...</td>
      <td>5.0</td>
      <td>Precious</td>
      <td>1398384000</td>
      <td>04 25, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VerynicepieceofcostumejewelryGoeswithmostoutfi...</td>
      <td>Precious</td>
      <td>91</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-25</td>
      <td>4</td>
      <td>B005LERHD8AJKGF1DFANXE3</td>
      <td>1</td>
      <td>Very nice piece of costume jewelry Goes with m...</td>
      <td>2014</td>
      <td>Very nice piece of costume jewelry. Goes with ...</td>
    </tr>
    <tr>
      <th>161429</th>
      <td>161429</td>
      <td>A1ZBY7DVFPPNCP</td>
      <td>B005LERHD8</td>
      <td>Grandma in Louisiana</td>
      <td>[0, 0]</td>
      <td>This pendant is cute.  I really like it.  I do...</td>
      <td>3.0</td>
      <td>Cute Owl Pendant</td>
      <td>1390780800</td>
      <td>01 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>122.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ThispendantiscuteIreallylikeitIdontconsiderita...</td>
      <td>CuteOwlPendant</td>
      <td>89</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-27</td>
      <td>1</td>
      <td>B005LERHD8A1ZBY7DVFPPNCP</td>
      <td>0</td>
      <td>This pendant is cute  I really like it  I dont...</td>
      <td>2014</td>
      <td>This pendant is cute.  I really like it.  I do...</td>
    </tr>
    <tr>
      <th>161430</th>
      <td>161430</td>
      <td>A3P8DF0E4BCG7E</td>
      <td>B005LERHD8</td>
      <td>green.girr</td>
      <td>[0, 0]</td>
      <td>It's a great gift. And it arrived in just a fe...</td>
      <td>5.0</td>
      <td>Love it!!!!!</td>
      <td>1390435200</td>
      <td>01 23, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>224.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ItsagreatgiftAnditarrivedinjustafewdaysItveryb...</td>
      <td>Loveit</td>
      <td>176</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-23</td>
      <td>1</td>
      <td>B005LERHD8A3P8DF0E4BCG7E</td>
      <td>1</td>
      <td>Its a great gift And it arrived in just a few ...</td>
      <td>2014</td>
      <td>It's a great gift. And it arrived in just a fe...</td>
    </tr>
    <tr>
      <th>161431</th>
      <td>161431</td>
      <td>A1M50TCAUWLIBS</td>
      <td>B005LERHD8</td>
      <td>GreenMama "Amanda B"</td>
      <td>[0, 0]</td>
      <td>took 20 days to arrive, bought this for my fri...</td>
      <td>4.0</td>
      <td>Took a while, but worth it!</td>
      <td>1382659200</td>
      <td>10 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>411.0</td>
      <td>Jewelry</td>
      <td>27.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>took20daystoarriveboughtthisformyfriends21stbd...</td>
      <td>Tookawhilebutworthit</td>
      <td>319</td>
      <td>20</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-25</td>
      <td>10</td>
      <td>B005LERHD8A1M50TCAUWLIBS</td>
      <td>1</td>
      <td>took  days to arrive bought this for my friend...</td>
      <td>2013</td>
      <td>took 20 days to arrive, bought this for my fri...</td>
    </tr>
    <tr>
      <th>161432</th>
      <td>161432</td>
      <td>A3KITEYHZF02IK</td>
      <td>B005LERHD8</td>
      <td>grrlonthego10</td>
      <td>[0, 0]</td>
      <td>A little more juvenile than I was expecting.  ...</td>
      <td>3.0</td>
      <td>eh</td>
      <td>1382832000</td>
      <td>10 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>2.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>AlittlemorejuvenilethanIwasexpectingIactuallyh...</td>
      <td>eh</td>
      <td>119</td>
      <td>2</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-27</td>
      <td>10</td>
      <td>B005LERHD8A3KITEYHZF02IK</td>
      <td>0</td>
      <td>A little more juvenile than I was expecting  I...</td>
      <td>2013</td>
      <td>A little more juvenile than I was expecting.  ...</td>
    </tr>
    <tr>
      <th>161433</th>
      <td>161433</td>
      <td>A3RO8N5Y4UF383</td>
      <td>B005LERHD8</td>
      <td>HaanaHail</td>
      <td>[0, 0]</td>
      <td>this was for a friend. and i just loved it. so...</td>
      <td>5.0</td>
      <td>SWEET</td>
      <td>1392336000</td>
      <td>02 14, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>94.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>thiswasforafriendandijustloveditsoyoushouldbut...</td>
      <td>SWEET</td>
      <td>71</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-14</td>
      <td>2</td>
      <td>B005LERHD8A3RO8N5Y4UF383</td>
      <td>1</td>
      <td>this was for a friend and i just loved it so y...</td>
      <td>2014</td>
      <td>this was for a friend. and i just loved it. so...</td>
    </tr>
    <tr>
      <th>161434</th>
      <td>161434</td>
      <td>A36KOXTKN07WRW</td>
      <td>B005LERHD8</td>
      <td>Heather Richards</td>
      <td>[0, 0]</td>
      <td>I got 2 of these - one for each daughter - and...</td>
      <td>4.0</td>
      <td>fun necklace</td>
      <td>1366848000</td>
      <td>04 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Igot2oftheseoneforeachdaughterandtheybothreall...</td>
      <td>funnecklace</td>
      <td>85</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-25</td>
      <td>4</td>
      <td>B005LERHD8A36KOXTKN07WRW</td>
      <td>1</td>
      <td>I got  of these  one for each daughter  and th...</td>
      <td>2013</td>
      <td>I got 2 of these - one for each daughter - and...</td>
    </tr>
    <tr>
      <th>161435</th>
      <td>161435</td>
      <td>A1Z9PVESRHEED5</td>
      <td>B005LERHD8</td>
      <td>Heather S.</td>
      <td>[2, 3]</td>
      <td>I was very skeptical about this piece, for thi...</td>
      <td>5.0</td>
      <td>WOW!</td>
      <td>1383177600</td>
      <td>10 31, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>397.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iwasveryskepticalaboutthispieceforthislowprice...</td>
      <td>WOW</td>
      <td>309</td>
      <td>3</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-31</td>
      <td>10</td>
      <td>B005LERHD8A1Z9PVESRHEED5</td>
      <td>1</td>
      <td>I was very skeptical about this piece for this...</td>
      <td>2013</td>
      <td>I was very skeptical about this piece, for thi...</td>
    </tr>
    <tr>
      <th>161436</th>
      <td>161436</td>
      <td>ACLHE92ZLG8U8</td>
      <td>B005LERHD8</td>
      <td>Heidi</td>
      <td>[0, 0]</td>
      <td>This is a cute necklace, but you can tell when...</td>
      <td>3.0</td>
      <td>good but cheap</td>
      <td>1388361600</td>
      <td>12 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>135.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Thisisacutenecklacebutyoucantellwhenyoufeelitt...</td>
      <td>goodbutcheap</td>
      <td>99</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-30</td>
      <td>12</td>
      <td>B005LERHD8ACLHE92ZLG8U8</td>
      <td>0</td>
      <td>This is a cute necklace but you can tell when ...</td>
      <td>2013</td>
      <td>This is a cute necklace, but you can tell when...</td>
    </tr>
    <tr>
      <th>161437</th>
      <td>161437</td>
      <td>A3VT7821BFWLMO</td>
      <td>B005LERHD8</td>
      <td>heidi</td>
      <td>[0, 1]</td>
      <td>It was cheap and I gave it a shot, why not.......</td>
      <td>1.0</td>
      <td>pass</td>
      <td>1384732800</td>
      <td>11 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>153.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ItwascheapandIgaveitashotwhynotSOOOtackyandCla...</td>
      <td>pass</td>
      <td>113</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-18</td>
      <td>11</td>
      <td>B005LERHD8A3VT7821BFWLMO</td>
      <td>0</td>
      <td>It was cheap and I gave it a shot why notSOOO ...</td>
      <td>2013</td>
      <td>It was cheap and I gave it a shot, why not.......</td>
    </tr>
    <tr>
      <th>161438</th>
      <td>161438</td>
      <td>AGJI67NBALMVK</td>
      <td>B005LERHD8</td>
      <td>helen</td>
      <td>[0, 0]</td>
      <td>costume jewelry, Fun and disposable. Price poi...</td>
      <td>5.0</td>
      <td>product matches pricing.</td>
      <td>1394150400</td>
      <td>03 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>321.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>costumejewelryFunanddisposablePricepointmatche...</td>
      <td>productmatchespricing</td>
      <td>246</td>
      <td>21</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-07</td>
      <td>3</td>
      <td>B005LERHD8AGJI67NBALMVK</td>
      <td>1</td>
      <td>costume jewelry Fun and disposable Price point...</td>
      <td>2014</td>
      <td>costume jewelry, Fun and disposable. Price poi...</td>
    </tr>
    <tr>
      <th>161439</th>
      <td>161439</td>
      <td>A3IN6RPWX5ML94</td>
      <td>B005LERHD8</td>
      <td>H. Marie Picard "Dances With Harleys"</td>
      <td>[0, 0]</td>
      <td>This was my second order as it is sooooo beaut...</td>
      <td>4.0</td>
      <td>Retro Crystal Owl Pendant</td>
      <td>1392249600</td>
      <td>02 13, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>136.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThiswasmysecondorderasitissooooobeautifulIgave...</td>
      <td>RetroCrystalOwlPendant</td>
      <td>105</td>
      <td>22</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-13</td>
      <td>2</td>
      <td>B005LERHD8A3IN6RPWX5ML94</td>
      <td>1</td>
      <td>This was my second order as it is sooooo beaut...</td>
      <td>2014</td>
      <td>This was my second order as it is sooooo beaut...</td>
    </tr>
    <tr>
      <th>161440</th>
      <td>161440</td>
      <td>A1KIUQYH7DT33M</td>
      <td>B005LERHD8</td>
      <td>hteate</td>
      <td>[0, 0]</td>
      <td>I bought 1 and loved it. Unfortunately I lost ...</td>
      <td>5.0</td>
      <td>Buy More</td>
      <td>1359331200</td>
      <td>01 28, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>151.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Ibought1andloveditUnfortunatelyIlostitandIlike...</td>
      <td>BuyMore</td>
      <td>117</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-28</td>
      <td>1</td>
      <td>B005LERHD8A1KIUQYH7DT33M</td>
      <td>1</td>
      <td>I bought  and loved it Unfortunately I lost it...</td>
      <td>2013</td>
      <td>I bought 1 and loved it. Unfortunately I lost ...</td>
    </tr>
    <tr>
      <th>161441</th>
      <td>161441</td>
      <td>AVWCILN9IMEEE</td>
      <td>B005LERHD8</td>
      <td>Ice</td>
      <td>[0, 0]</td>
      <td>I didn't pay attention to the specs on this ne...</td>
      <td>4.0</td>
      <td>Huge</td>
      <td>1396828800</td>
      <td>04 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>200.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Ididntpayattentiontothespecsonthisnecklaceandb...</td>
      <td>Huge</td>
      <td>153</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-07</td>
      <td>4</td>
      <td>B005LERHD8AVWCILN9IMEEE</td>
      <td>1</td>
      <td>I didnt pay attention to the specs on this nec...</td>
      <td>2014</td>
      <td>I didn't pay attention to the specs on this ne...</td>
    </tr>
    <tr>
      <th>161442</th>
      <td>161442</td>
      <td>ANU19469VYBBC</td>
      <td>B005LERHD8</td>
      <td>I.love.frogs</td>
      <td>[0, 0]</td>
      <td>Very cute &amp; adorable. Very colorful. I had ord...</td>
      <td>5.0</td>
      <td>beautiful. perfect for people that love owls</td>
      <td>1399939200</td>
      <td>05 13, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>44.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>VerycuteadorableVerycolorfulIhadorderedthesefo...</td>
      <td>beautifulperfectforpeoplethatloveowls</td>
      <td>124</td>
      <td>37</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-13</td>
      <td>5</td>
      <td>B005LERHD8ANU19469VYBBC</td>
      <td>1</td>
      <td>Very cute  adorable Very colorful I had ordere...</td>
      <td>2014</td>
      <td>Very cute &amp; adorable. Very colorful. I had ord...</td>
    </tr>
    <tr>
      <th>161443</th>
      <td>161443</td>
      <td>A211W8JLJFDIC0</td>
      <td>B005LERHD8</td>
      <td>Injured wing.</td>
      <td>[0, 0]</td>
      <td>This was a gift and it was loved by all. I let...</td>
      <td>5.0</td>
      <td>For an Owl lover and collector</td>
      <td>1370304000</td>
      <td>06 4, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>315.0</td>
      <td>Jewelry</td>
      <td>30.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>ThiswasagiftanditwaslovedbyallIletmyfriendopen...</td>
      <td>ForanOwlloverandcollector</td>
      <td>243</td>
      <td>25</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-06-04</td>
      <td>6</td>
      <td>B005LERHD8A211W8JLJFDIC0</td>
      <td>1</td>
      <td>This was a gift and it was loved by all I let ...</td>
      <td>2013</td>
      <td>This was a gift and it was loved by all. I let...</td>
    </tr>
    <tr>
      <th>161444</th>
      <td>161444</td>
      <td>A37C9JMDE7RKQQ</td>
      <td>B005LERHD8</td>
      <td>Invaderzim</td>
      <td>[0, 1]</td>
      <td>it is cute but it came in broken in the packag...</td>
      <td>1.0</td>
      <td>came in broken</td>
      <td>1384732800</td>
      <td>11 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>94.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>itiscutebutitcameinbrokeninthepackagethenIende...</td>
      <td>cameinbroken</td>
      <td>73</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-18</td>
      <td>11</td>
      <td>B005LERHD8A37C9JMDE7RKQQ</td>
      <td>0</td>
      <td>it is cute but it came in broken in the packag...</td>
      <td>2013</td>
      <td>it is cute but it came in broken in the packag...</td>
    </tr>
    <tr>
      <th>161445</th>
      <td>161445</td>
      <td>A2EBZY1D4B8M5O</td>
      <td>B005LERHD8</td>
      <td>Irayda Tejeda</td>
      <td>[0, 0]</td>
      <td>I got it for a friend and she loved it. I am v...</td>
      <td>4.0</td>
      <td>cute</td>
      <td>1389744000</td>
      <td>01 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>108.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IgotitforafriendandsheloveditIamverypleasewith...</td>
      <td>cute</td>
      <td>82</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-15</td>
      <td>1</td>
      <td>B005LERHD8A2EBZY1D4B8M5O</td>
      <td>1</td>
      <td>I got it for a friend and she loved it I am ve...</td>
      <td>2014</td>
      <td>I got it for a friend and she loved it. I am v...</td>
    </tr>
    <tr>
      <th>161446</th>
      <td>161446</td>
      <td>AY84KEMJB06HX</td>
      <td>B005LERHD8</td>
      <td>Jacqueline Davidson</td>
      <td>[0, 0]</td>
      <td>Loving owls as I do, this pendant caught my ey...</td>
      <td>4.0</td>
      <td>Owl pendant and chain</td>
      <td>1393718400</td>
      <td>03 2, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>202.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>LovingowlsasIdothispendantcaughtmyeyeItlooksol...</td>
      <td>Owlpendantandchain</td>
      <td>154</td>
      <td>18</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-02</td>
      <td>3</td>
      <td>B005LERHD8AY84KEMJB06HX</td>
      <td>1</td>
      <td>Loving owls as I do this pendant caught my eye...</td>
      <td>2014</td>
      <td>Loving owls as I do, this pendant caught my ey...</td>
    </tr>
    <tr>
      <th>161447</th>
      <td>161447</td>
      <td>A36PMHOXOSFX4G</td>
      <td>B005LERHD8</td>
      <td>Jane Thurmond "MsBooksIt"</td>
      <td>[0, 0]</td>
      <td>Love this necklace. Owls are so cute and in st...</td>
      <td>5.0</td>
      <td>Charming little (well, big) necklace</td>
      <td>1376611200</td>
      <td>08 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>306.0</td>
      <td>Jewelry</td>
      <td>36.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>LovethisnecklaceOwlsaresocuteandinstylerightno...</td>
      <td>Charminglittlewellbignecklace</td>
      <td>238</td>
      <td>29</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-16</td>
      <td>8</td>
      <td>B005LERHD8A36PMHOXOSFX4G</td>
      <td>1</td>
      <td>Love this necklace Owls are so cute and in sty...</td>
      <td>2013</td>
      <td>Love this necklace. Owls are so cute and in st...</td>
    </tr>
    <tr>
      <th>161448</th>
      <td>161448</td>
      <td>ALPSHYYHX6Q0O</td>
      <td>B005LERHD8</td>
      <td>Jasmine</td>
      <td>[0, 0]</td>
      <td>I think this is one of the only products I've ...</td>
      <td>5.0</td>
      <td>Exactly as shown</td>
      <td>1390089600</td>
      <td>01 19, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>236.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IthinkthisisoneoftheonlyproductsIveorderedonhe...</td>
      <td>Exactlyasshown</td>
      <td>185</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-19</td>
      <td>1</td>
      <td>B005LERHD8ALPSHYYHX6Q0O</td>
      <td>1</td>
      <td>I think this is one of the only products Ive o...</td>
      <td>2014</td>
      <td>I think this is one of the only products I've ...</td>
    </tr>
    <tr>
      <th>161449</th>
      <td>161449</td>
      <td>A1TWMUCAU35FMV</td>
      <td>B005LERHD8</td>
      <td>Jasmine Moore</td>
      <td>[0, 0]</td>
      <td>Adorable</td>
      <td>5.0</td>
      <td>Five Stars</td>
      <td>1404345600</td>
      <td>07 3, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>8.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Adorable</td>
      <td>FiveStars</td>
      <td>8</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-03</td>
      <td>7</td>
      <td>B005LERHD8A1TWMUCAU35FMV</td>
      <td>1</td>
      <td>Adorable</td>
      <td>2014</td>
      <td>Adorable</td>
    </tr>
    <tr>
      <th>161450</th>
      <td>161450</td>
      <td>A58P1TUC17EL2</td>
      <td>B005LERHD8</td>
      <td>Jason Stanhouse (Jason@stanhouse . com) "J+H ...</td>
      <td>[0, 0]</td>
      <td>I bought this for my wife for 1$ i was not onl...</td>
      <td>5.0</td>
      <td>Great item A+++</td>
      <td>1404518400</td>
      <td>07 5, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>141.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Iboughtthisformywifefor1iwasnotonlyshockedatth...</td>
      <td>GreatitemA</td>
      <td>105</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-05</td>
      <td>7</td>
      <td>B005LERHD8A58P1TUC17EL2</td>
      <td>1</td>
      <td>I bought this for my wife for  i was not only ...</td>
      <td>2014</td>
      <td>I bought this for my wife for 1$ i was not onl...</td>
    </tr>
    <tr>
      <th>161451</th>
      <td>161451</td>
      <td>A18HQ2Z3E9WWG8</td>
      <td>B005LERHD8</td>
      <td>Jaxxosuna</td>
      <td>[0, 0]</td>
      <td>I loooove this necklace !!!!! It's so cute and...</td>
      <td>5.0</td>
      <td>Love it</td>
      <td>1384646400</td>
      <td>11 17, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IloooovethisnecklaceItssocuteanditfeelsheavyit...</td>
      <td>Loveit</td>
      <td>88</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-17</td>
      <td>11</td>
      <td>B005LERHD8A18HQ2Z3E9WWG8</td>
      <td>1</td>
      <td>I loooove this necklace  Its so cute and it fe...</td>
      <td>2013</td>
      <td>I loooove this necklace !!!!! It's so cute and...</td>
    </tr>
    <tr>
      <th>161452</th>
      <td>161452</td>
      <td>A1E1LEVQ9VQNK</td>
      <td>B005LERHD8</td>
      <td>J. Chambers</td>
      <td>[1, 1]</td>
      <td>At the time I ordered the owl pendant and chai...</td>
      <td>5.0</td>
      <td>Remarkably nice costume jewelry for the price</td>
      <td>1390089600</td>
      <td>01 19, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>729.0</td>
      <td>Jewelry</td>
      <td>45.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>AtthetimeIorderedtheowlpendantandchainitcostle...</td>
      <td>Remarkablynicecostumejewelryfortheprice</td>
      <td>571</td>
      <td>39</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-19</td>
      <td>1</td>
      <td>B005LERHD8A1E1LEVQ9VQNK</td>
      <td>1</td>
      <td>At the time I ordered the owl pendant and chai...</td>
      <td>2014</td>
      <td>At the time I ordered the owl pendant and chai...</td>
    </tr>
    <tr>
      <th>161453</th>
      <td>161453</td>
      <td>AVWYFE169YDNS</td>
      <td>B005LERHD8</td>
      <td>Jeanette Spalliero</td>
      <td>[0, 0]</td>
      <td>Beautiful necklaces.  Exactly as pictured.</td>
      <td>5.0</td>
      <td>Five Stars</td>
      <td>1404691200</td>
      <td>07 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>42.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>BeautifulnecklacesExactlyaspictured</td>
      <td>FiveStars</td>
      <td>35</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-07</td>
      <td>7</td>
      <td>B005LERHD8AVWYFE169YDNS</td>
      <td>1</td>
      <td>Beautiful necklaces  Exactly as pictured</td>
      <td>2014</td>
      <td>Beautiful necklaces.  Exactly as pictured.</td>
    </tr>
    <tr>
      <th>161454</th>
      <td>161454</td>
      <td>A1EW8OWJ0BM3VO</td>
      <td>B005LERHD8</td>
      <td>Jeannie Kain</td>
      <td>[0, 0]</td>
      <td>Super cute and fun.  not solid, but that helps...</td>
      <td>5.0</td>
      <td>Fun and colorful</td>
      <td>1387929600</td>
      <td>12 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Supercuteandfunnotsolidbutthathelpswiththefree...</td>
      <td>Funandcolorful</td>
      <td>92</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-25</td>
      <td>12</td>
      <td>B005LERHD8A1EW8OWJ0BM3VO</td>
      <td>1</td>
      <td>Super cute and fun  not solid but that helps w...</td>
      <td>2013</td>
      <td>Super cute and fun.  not solid, but that helps...</td>
    </tr>
    <tr>
      <th>161455</th>
      <td>161455</td>
      <td>A11TXTVCFT246T</td>
      <td>B005LERHD8</td>
      <td>Jeffery B.</td>
      <td>[0, 1]</td>
      <td>Love this cute little own wish I had ordered m...</td>
      <td>5.0</td>
      <td>Love it</td>
      <td>1380758400</td>
      <td>10 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>102.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>LovethiscutelittleownwishIhadorderedmorelolIlo...</td>
      <td>Loveit</td>
      <td>81</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-03</td>
      <td>10</td>
      <td>B005LERHD8A11TXTVCFT246T</td>
      <td>1</td>
      <td>Love this cute little own wish I had ordered m...</td>
      <td>2013</td>
      <td>Love this cute little own wish I had ordered m...</td>
    </tr>
    <tr>
      <th>161456</th>
      <td>161456</td>
      <td>A25CUVLNCTDGQO</td>
      <td>B005LERHD8</td>
      <td>Jen</td>
      <td>[0, 0]</td>
      <td>A cute piece of costume jewelry. Looks just li...</td>
      <td>5.0</td>
      <td>Cute!</td>
      <td>1350259200</td>
      <td>10 15, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>146.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>AcutepieceofcostumejewelryLooksjustlikethepict...</td>
      <td>Cute</td>
      <td>114</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-10-15</td>
      <td>10</td>
      <td>B005LERHD8A25CUVLNCTDGQO</td>
      <td>1</td>
      <td>A cute piece of costume jewelry Looks just lik...</td>
      <td>2012</td>
      <td>A cute piece of costume jewelry. Looks just li...</td>
    </tr>
    <tr>
      <th>161457</th>
      <td>161457</td>
      <td>A34861W2UEQKV9</td>
      <td>B005LERHD8</td>
      <td>Jen_m</td>
      <td>[0, 0]</td>
      <td>Love it! Unique and cute, adds a pop to my out...</td>
      <td>5.0</td>
      <td>I get so many compliments on this piece!</td>
      <td>1365984000</td>
      <td>04 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>177.0</td>
      <td>Jewelry</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>LoveitUniqueandcuteaddsapoptomyoutfitsIhavehad...</td>
      <td>Igetsomanycomplimentsonthispiece</td>
      <td>137</td>
      <td>32</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-15</td>
      <td>4</td>
      <td>B005LERHD8A34861W2UEQKV9</td>
      <td>1</td>
      <td>Love it Unique and cute adds a pop to my outfi...</td>
      <td>2013</td>
      <td>Love it! Unique and cute, adds a pop to my out...</td>
    </tr>
    <tr>
      <th>161458</th>
      <td>161458</td>
      <td>A5GPH59NDWJRB</td>
      <td>B005LERHD8</td>
      <td>Jenna of the Jungle</td>
      <td>[0, 0]</td>
      <td>My 5-year-old daughter is really into owls, so...</td>
      <td>3.0</td>
      <td>Garish, But It Works</td>
      <td>1354492800</td>
      <td>12 3, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>802.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>My5yearolddaughterisreallyintoowlssoIwantedtof...</td>
      <td>GarishButItWorks</td>
      <td>614</td>
      <td>16</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-03</td>
      <td>12</td>
      <td>B005LERHD8A5GPH59NDWJRB</td>
      <td>0</td>
      <td>My yearold daughter is really into owls so I w...</td>
      <td>2012</td>
      <td>My 5-year-old daughter is really into owls, so...</td>
    </tr>
    <tr>
      <th>161459</th>
      <td>161459</td>
      <td>A2Z3EOU60YAOO3</td>
      <td>B005LERHD8</td>
      <td>Jennifer Christian</td>
      <td>[0, 0]</td>
      <td>These turned out to be too big and gody for me...</td>
      <td>3.0</td>
      <td>Cute but too big.</td>
      <td>1385510400</td>
      <td>11 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>TheseturnedouttobetoobigandgodyformeIdontreall...</td>
      <td>Cutebuttoobig</td>
      <td>86</td>
      <td>13</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-27</td>
      <td>11</td>
      <td>B005LERHD8A2Z3EOU60YAOO3</td>
      <td>0</td>
      <td>These turned out to be too big and gody for me...</td>
      <td>2013</td>
      <td>These turned out to be too big and gody for me...</td>
    </tr>
    <tr>
      <th>161460</th>
      <td>161460</td>
      <td>A2N4URI1QI12U1</td>
      <td>B005LERHD8</td>
      <td>jennifer</td>
      <td>[0, 0]</td>
      <td>I love the design and shape of this piece. I g...</td>
      <td>5.0</td>
      <td>my favorite piece</td>
      <td>1390348800</td>
      <td>01 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>130.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IlovethedesignandshapeofthispieceIgetalotofcom...</td>
      <td>myfavoritepiece</td>
      <td>101</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-22</td>
      <td>1</td>
      <td>B005LERHD8A2N4URI1QI12U1</td>
      <td>1</td>
      <td>I love the design and shape of this piece I ge...</td>
      <td>2014</td>
      <td>I love the design and shape of this piece. I g...</td>
    </tr>
    <tr>
      <th>161461</th>
      <td>161461</td>
      <td>A2MA0THFV3B2GA</td>
      <td>B005LERHD8</td>
      <td>Jennifer</td>
      <td>[0, 0]</td>
      <td>The necklace itself it adorable, but every tim...</td>
      <td>2.0</td>
      <td>Super cute, but turns around</td>
      <td>1395100800</td>
      <td>03 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>156.0</td>
      <td>Jewelry</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThenecklaceitselfitadorablebuteverytimeIwearit...</td>
      <td>Supercutebutturnsaround</td>
      <td>121</td>
      <td>23</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-18</td>
      <td>3</td>
      <td>B005LERHD8A2MA0THFV3B2GA</td>
      <td>0</td>
      <td>The necklace itself it adorable but every time...</td>
      <td>2014</td>
      <td>The necklace itself it adorable, but every tim...</td>
    </tr>
    <tr>
      <th>161462</th>
      <td>161462</td>
      <td>A3QJR243PD45N5</td>
      <td>B005LERHD8</td>
      <td>Jennifer Mathesz "trinity52607"</td>
      <td>[1, 1]</td>
      <td>This is very cute.  It's not really my style s...</td>
      <td>4.0</td>
      <td>Cute, but bigger than expected</td>
      <td>1388707200</td>
      <td>01 3, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>278.0</td>
      <td>Jewelry</td>
      <td>30.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisisverycuteItsnotreallymystylesoIdontknowho...</td>
      <td>Cutebutbiggerthanexpected</td>
      <td>205</td>
      <td>25</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-03</td>
      <td>1</td>
      <td>B005LERHD8A3QJR243PD45N5</td>
      <td>1</td>
      <td>This is very cute  Its not really my style so ...</td>
      <td>2014</td>
      <td>This is very cute.  It's not really my style s...</td>
    </tr>
    <tr>
      <th>161463</th>
      <td>161463</td>
      <td>AH9D6UNA3HWAA</td>
      <td>B005LERHD8</td>
      <td>jericorn</td>
      <td>[0, 0]</td>
      <td>Very cute, small and has lovely colors. Was ve...</td>
      <td>4.0</td>
      <td>Pretty!</td>
      <td>1392422400</td>
      <td>02 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>116.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VerycutesmallandhaslovelycolorsWasveryimpresse...</td>
      <td>Pretty</td>
      <td>91</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-15</td>
      <td>2</td>
      <td>B005LERHD8AH9D6UNA3HWAA</td>
      <td>1</td>
      <td>Very cute small and has lovely colors Was very...</td>
      <td>2014</td>
      <td>Very cute, small and has lovely colors. Was ve...</td>
    </tr>
    <tr>
      <th>161464</th>
      <td>161464</td>
      <td>A2MCHPS7RXNCL6</td>
      <td>B005LERHD8</td>
      <td>Jessica Biron</td>
      <td>[0, 0]</td>
      <td>I love this little necklace.  Its super cute, ...</td>
      <td>5.0</td>
      <td>Sooo Cute!</td>
      <td>1401148800</td>
      <td>05 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>372.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>IlovethislittlenecklaceItssupercuteandsuperfun...</td>
      <td>SoooCute</td>
      <td>284</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-27</td>
      <td>5</td>
      <td>B005LERHD8A2MCHPS7RXNCL6</td>
      <td>1</td>
      <td>I love this little necklace  Its super cute an...</td>
      <td>2014</td>
      <td>I love this little necklace.  Its super cute, ...</td>
    </tr>
    <tr>
      <th>161465</th>
      <td>161465</td>
      <td>A88YXQIS8RXQ1</td>
      <td>B005LERHD8</td>
      <td>Jessica</td>
      <td>[0, 0]</td>
      <td>Chain and pendant were both better material th...</td>
      <td>5.0</td>
      <td>Cute!</td>
      <td>1390348800</td>
      <td>01 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ChainandpendantwerebothbettermaterialthenIexpe...</td>
      <td>Cute</td>
      <td>92</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-22</td>
      <td>1</td>
      <td>B005LERHD8A88YXQIS8RXQ1</td>
      <td>1</td>
      <td>Chain and pendant were both better material th...</td>
      <td>2014</td>
      <td>Chain and pendant were both better material th...</td>
    </tr>
    <tr>
      <th>161466</th>
      <td>161466</td>
      <td>A2J8MNYB7PMLNE</td>
      <td>B005LERHD8</td>
      <td>Jessica Rose</td>
      <td>[0, 0]</td>
      <td>Lots of compliments on this good necklace supe...</td>
      <td>5.0</td>
      <td>Colorful!!!</td>
      <td>1397692800</td>
      <td>04 17, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>139.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Lotsofcomplimentsonthisgoodnecklacesupercheapf...</td>
      <td>Colorful</td>
      <td>117</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-17</td>
      <td>4</td>
      <td>B005LERHD8A2J8MNYB7PMLNE</td>
      <td>1</td>
      <td>Lots of compliments on this good necklace supe...</td>
      <td>2014</td>
      <td>Lots of compliments on this good necklace supe...</td>
    </tr>
    <tr>
      <th>161467</th>
      <td>161467</td>
      <td>A3LY749Q2Q3W7S</td>
      <td>B005LERHD8</td>
      <td>jessi</td>
      <td>[0, 0]</td>
      <td>Adorable owl piece. Very long and not an adjus...</td>
      <td>4.0</td>
      <td>love owls</td>
      <td>1363910400</td>
      <td>03 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>118.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>AdorableowlpieceVerylongandnotanadjustablechai...</td>
      <td>loveowls</td>
      <td>96</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-22</td>
      <td>3</td>
      <td>B005LERHD8A3LY749Q2Q3W7S</td>
      <td>1</td>
      <td>Adorable owl piece Very long and not an adjust...</td>
      <td>2013</td>
      <td>Adorable owl piece. Very long and not an adjus...</td>
    </tr>
    <tr>
      <th>161468</th>
      <td>161468</td>
      <td>A1T94B0FKJ74QZ</td>
      <td>B005LERHD8</td>
      <td>Jgraley</td>
      <td>[0, 0]</td>
      <td>order this for a gift for a friend pretty good...</td>
      <td>4.0</td>
      <td>good products great price</td>
      <td>1397606400</td>
      <td>04 16, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>172.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>orderthisforagiftforafriendprettygoodsofarImea...</td>
      <td>goodproductsgreatprice</td>
      <td>137</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-16</td>
      <td>4</td>
      <td>B005LERHD8A1T94B0FKJ74QZ</td>
      <td>1</td>
      <td>order this for a gift for a friend pretty good...</td>
      <td>2014</td>
      <td>order this for a gift for a friend pretty good...</td>
    </tr>
    <tr>
      <th>161469</th>
      <td>161469</td>
      <td>A2I6YWMQHJ4BXN</td>
      <td>B005LERHD8</td>
      <td>JivusTurkus "Jive Turkey"</td>
      <td>[0, 0]</td>
      <td>Perfect and reasonably priced small gift for a...</td>
      <td>4.0</td>
      <td>Got it as a gift</td>
      <td>1391385600</td>
      <td>02 3, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>133.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>PerfectandreasonablypricedsmallgiftforaladyCam...</td>
      <td>Gotitasagift</td>
      <td>108</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-03</td>
      <td>2</td>
      <td>B005LERHD8A2I6YWMQHJ4BXN</td>
      <td>1</td>
      <td>Perfect and reasonably priced small gift for a...</td>
      <td>2014</td>
      <td>Perfect and reasonably priced small gift for a...</td>
    </tr>
    <tr>
      <th>161470</th>
      <td>161470</td>
      <td>A4WFQCDSIL95K</td>
      <td>B005LERHD8</td>
      <td>JMelton "JMelton"</td>
      <td>[0, 0]</td>
      <td>I always get compliments on this necklace when...</td>
      <td>5.0</td>
      <td>Love this!</td>
      <td>1353456000</td>
      <td>11 21, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>168.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IalwaysgetcomplimentsonthisnecklacewhenIwearit...</td>
      <td>Lovethis</td>
      <td>133</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-21</td>
      <td>11</td>
      <td>B005LERHD8A4WFQCDSIL95K</td>
      <td>1</td>
      <td>I always get compliments on this necklace when...</td>
      <td>2012</td>
      <td>I always get compliments on this necklace when...</td>
    </tr>
    <tr>
      <th>161471</th>
      <td>161471</td>
      <td>A1RFYZHZP79VC7</td>
      <td>B005LERHD8</td>
      <td>J. Nice</td>
      <td>[1, 1]</td>
      <td>So pretty!! Got this for my best friend as a C...</td>
      <td>5.0</td>
      <td>Owl Necklace</td>
      <td>1385337600</td>
      <td>11 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>103.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SoprettyGotthisformybestfriendasaChristmasgift...</td>
      <td>OwlNecklace</td>
      <td>75</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-25</td>
      <td>11</td>
      <td>B005LERHD8A1RFYZHZP79VC7</td>
      <td>1</td>
      <td>So pretty Got this for my best friend as a Chr...</td>
      <td>2013</td>
      <td>So pretty!! Got this for my best friend as a C...</td>
    </tr>
    <tr>
      <th>161472</th>
      <td>161472</td>
      <td>AB4BTTDRSQTO5</td>
      <td>B005LERHD8</td>
      <td>joanna</td>
      <td>[0, 0]</td>
      <td>cute but tacky liked how light it was and how ...</td>
      <td>5.0</td>
      <td>so cute!</td>
      <td>1402444800</td>
      <td>06 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>111.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>cutebuttackylikedhowlightitwasandhoweasyitwast...</td>
      <td>socute</td>
      <td>88</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-11</td>
      <td>6</td>
      <td>B005LERHD8AB4BTTDRSQTO5</td>
      <td>1</td>
      <td>cute but tacky liked how light it was and how ...</td>
      <td>2014</td>
      <td>cute but tacky liked how light it was and how ...</td>
    </tr>
    <tr>
      <th>161473</th>
      <td>161473</td>
      <td>A183TEV2X7CBCP</td>
      <td>B005LERHD8</td>
      <td>Joann Andersen</td>
      <td>[0, 0]</td>
      <td>I like the necklace but I ordered the earings ...</td>
      <td>3.0</td>
      <td>granddaughters</td>
      <td>1382745600</td>
      <td>10 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>167.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IlikethenecklacebutIorderedtheearingswiththema...</td>
      <td>granddaughters</td>
      <td>133</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-26</td>
      <td>10</td>
      <td>B005LERHD8A183TEV2X7CBCP</td>
      <td>0</td>
      <td>I like the necklace but I ordered the earings ...</td>
      <td>2013</td>
      <td>I like the necklace but I ordered the earings ...</td>
    </tr>
    <tr>
      <th>161474</th>
      <td>161474</td>
      <td>A178A1YMMNF9TH</td>
      <td>B005LERHD8</td>
      <td>Jo Ann Baird</td>
      <td>[1, 1]</td>
      <td>When I opened the package the owl's body was s...</td>
      <td>2.0</td>
      <td>arrived broken</td>
      <td>1359676800</td>
      <td>02 1, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>248.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>WhenIopenedthepackagetheowlsbodywasseparatefro...</td>
      <td>arrivedbroken</td>
      <td>192</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-01</td>
      <td>2</td>
      <td>B005LERHD8A178A1YMMNF9TH</td>
      <td>0</td>
      <td>When I opened the package the owls body was se...</td>
      <td>2013</td>
      <td>When I opened the package the owl's body was s...</td>
    </tr>
    <tr>
      <th>161475</th>
      <td>161475</td>
      <td>ABNBX0GJPT6UI</td>
      <td>B005LERHD8</td>
      <td>JoCee</td>
      <td>[0, 0]</td>
      <td>very cute item.  I purchased this owl for my g...</td>
      <td>5.0</td>
      <td>Exactly what I wanted</td>
      <td>1385942400</td>
      <td>12 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>121.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>verycuteitemIpurchasedthisowlformygrowngrandda...</td>
      <td>ExactlywhatIwanted</td>
      <td>96</td>
      <td>18</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-02</td>
      <td>12</td>
      <td>B005LERHD8ABNBX0GJPT6UI</td>
      <td>1</td>
      <td>very cute item  I purchased this owl for my gr...</td>
      <td>2013</td>
      <td>very cute item.  I purchased this owl for my g...</td>
    </tr>
    <tr>
      <th>161476</th>
      <td>161476</td>
      <td>A1XQYKUVMDUO61</td>
      <td>B005LERHD8</td>
      <td>Joe &amp;amp; Debs</td>
      <td>[0, 0]</td>
      <td>Simply adorable. Very true to colors with an a...</td>
      <td>5.0</td>
      <td>Adorable.</td>
      <td>1373760000</td>
      <td>07 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>632.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>SimplyadorableVerytruetocolorswithanantiquedbr...</td>
      <td>Adorable</td>
      <td>490</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-14</td>
      <td>7</td>
      <td>B005LERHD8A1XQYKUVMDUO61</td>
      <td>1</td>
      <td>Simply adorable Very true to colors with an an...</td>
      <td>2013</td>
      <td>Simply adorable. Very true to colors with an a...</td>
    </tr>
    <tr>
      <th>161477</th>
      <td>161477</td>
      <td>A065995424G4KBBX1V8BO</td>
      <td>B005LERHD8</td>
      <td>johanna sancho</td>
      <td>[0, 0]</td>
      <td>very nice necklace, I love owls and this has s...</td>
      <td>5.0</td>
      <td>love it!!!!</td>
      <td>1363564800</td>
      <td>03 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>118.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>verynicenecklaceIloveowlsandthishassomeverybea...</td>
      <td>loveit</td>
      <td>94</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-18</td>
      <td>3</td>
      <td>B005LERHD8A065995424G4KBBX1V8BO</td>
      <td>1</td>
      <td>very nice necklace I love owls and this has so...</td>
      <td>2013</td>
      <td>very nice necklace, I love owls and this has s...</td>
    </tr>
    <tr>
      <th>161478</th>
      <td>161478</td>
      <td>AXWV0234EG3BN</td>
      <td>B005LERHD8</td>
      <td>Jolene</td>
      <td>[0, 0]</td>
      <td>Cute little necklace for the price... Great co...</td>
      <td>3.0</td>
      <td>Cant get much better than 0.83 cents!!!</td>
      <td>1382313600</td>
      <td>10 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>131.0</td>
      <td>Jewelry</td>
      <td>39.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>CutelittlenecklaceforthepriceGreatcolorsandrea...</td>
      <td>Cantgetmuchbetterthan083cents</td>
      <td>104</td>
      <td>29</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-21</td>
      <td>10</td>
      <td>B005LERHD8AXWV0234EG3BN</td>
      <td>0</td>
      <td>Cute little necklace for the price Great color...</td>
      <td>2013</td>
      <td>Cute little necklace for the price... Great co...</td>
    </tr>
    <tr>
      <th>161479</th>
      <td>161479</td>
      <td>A3GN1MLW5AYPU4</td>
      <td>B005LERHD8</td>
      <td>Jordan</td>
      <td>[0, 0]</td>
      <td>Very cute little owl.  chain unattaches itseld...</td>
      <td>4.0</td>
      <td>love it</td>
      <td>1379721600</td>
      <td>09 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>129.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Verycutelittleowlchainunattachesitseldattheloo...</td>
      <td>loveit</td>
      <td>100</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-21</td>
      <td>9</td>
      <td>B005LERHD8A3GN1MLW5AYPU4</td>
      <td>1</td>
      <td>Very cute little owl  chain unattaches itseld ...</td>
      <td>2013</td>
      <td>Very cute little owl.  chain unattaches itseld...</td>
    </tr>
    <tr>
      <th>161480</th>
      <td>161480</td>
      <td>A1VXKRSRFGBCJ1</td>
      <td>B005LERHD8</td>
      <td>Juanita_Bell</td>
      <td>[0, 1]</td>
      <td>This necklace is gorgeous.  I have gotten so m...</td>
      <td>5.0</td>
      <td>I would but then out!</td>
      <td>1385769600</td>
      <td>11 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>156.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ThisnecklaceisgorgeousIhavegottensomanycomplim...</td>
      <td>Iwouldbutthenout</td>
      <td>117</td>
      <td>16</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-30</td>
      <td>11</td>
      <td>B005LERHD8A1VXKRSRFGBCJ1</td>
      <td>1</td>
      <td>This necklace is gorgeous  I have gotten so ma...</td>
      <td>2013</td>
      <td>This necklace is gorgeous.  I have gotten so m...</td>
    </tr>
    <tr>
      <th>161481</th>
      <td>161481</td>
      <td>A1JPU1KL84URID</td>
      <td>B005LERHD8</td>
      <td>juliehin "{swak}"</td>
      <td>[0, 0]</td>
      <td>Bought as a gift for my niece but I'm thinking...</td>
      <td>5.0</td>
      <td>LOVE</td>
      <td>1353974400</td>
      <td>11 27, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>105.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>BoughtasagiftformyniecebutImthinkingaboutkeepi...</td>
      <td>LOVE</td>
      <td>81</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-27</td>
      <td>11</td>
      <td>B005LERHD8A1JPU1KL84URID</td>
      <td>1</td>
      <td>Bought as a gift for my niece but Im thinking ...</td>
      <td>2012</td>
      <td>Bought as a gift for my niece but I'm thinking...</td>
    </tr>
    <tr>
      <th>161482</th>
      <td>161482</td>
      <td>A9XPC6GC3M78V</td>
      <td>B005LERHD8</td>
      <td>Julie Thornton "Jules"</td>
      <td>[0, 0]</td>
      <td>Very cheaply made as can be expected from the ...</td>
      <td>1.0</td>
      <td>CHEAPLY MADE</td>
      <td>1387152000</td>
      <td>12 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>142.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VerycheaplymadeascanbeexpectedfromthepriceIpai...</td>
      <td>CHEAPLYMADE</td>
      <td>108</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-16</td>
      <td>12</td>
      <td>B005LERHD8A9XPC6GC3M78V</td>
      <td>0</td>
      <td>Very cheaply made as can be expected from the ...</td>
      <td>2013</td>
      <td>Very cheaply made as can be expected from the ...</td>
    </tr>
    <tr>
      <th>161483</th>
      <td>161483</td>
      <td>A3RQIVB0TE5R9J</td>
      <td>B005LERHD8</td>
      <td>June0563</td>
      <td>[0, 0]</td>
      <td>If only ... Well it is!!!  Purchased at .75 li...</td>
      <td>5.0</td>
      <td>Owl who?</td>
      <td>1384560000</td>
      <td>11 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>341.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>IfonlyWellitisPurchasedat75listedat34dollarsce...</td>
      <td>Owlwho</td>
      <td>252</td>
      <td>6</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-16</td>
      <td>11</td>
      <td>B005LERHD8A3RQIVB0TE5R9J</td>
      <td>1</td>
      <td>If only  Well it is  Purchased at  listed at  ...</td>
      <td>2013</td>
      <td>If only ... Well it is!!!  Purchased at .75 li...</td>
    </tr>
    <tr>
      <th>161484</th>
      <td>161484</td>
      <td>A3HHOJDWZSFXDL</td>
      <td>B005LERHD8</td>
      <td>kaisa</td>
      <td>[0, 0]</td>
      <td>Yes it was cheap, and it sure looked it. Its s...</td>
      <td>1.0</td>
      <td>horrible</td>
      <td>1392076800</td>
      <td>02 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>YesitwascheapanditsurelookeditItssobigdonteven...</td>
      <td>horrible</td>
      <td>87</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-11</td>
      <td>2</td>
      <td>B005LERHD8A3HHOJDWZSFXDL</td>
      <td>0</td>
      <td>Yes it was cheap and it sure looked it Its so ...</td>
      <td>2014</td>
      <td>Yes it was cheap, and it sure looked it. Its s...</td>
    </tr>
    <tr>
      <th>161485</th>
      <td>161485</td>
      <td>A2LX3F0DGMNK15</td>
      <td>B005LERHD8</td>
      <td>Kali</td>
      <td>[1, 1]</td>
      <td>I bought three of these necklaces and gave two...</td>
      <td>4.0</td>
      <td>Cute!</td>
      <td>1388880000</td>
      <td>01 5, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>388.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtthreeofthesenecklacesandgavetwoawayasgi...</td>
      <td>Cute</td>
      <td>306</td>
      <td>4</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-05</td>
      <td>1</td>
      <td>B005LERHD8A2LX3F0DGMNK15</td>
      <td>1</td>
      <td>I bought three of these necklaces and gave two...</td>
      <td>2014</td>
      <td>I bought three of these necklaces and gave two...</td>
    </tr>
    <tr>
      <th>161486</th>
      <td>161486</td>
      <td>A5B7KCCZJOLJX</td>
      <td>B005LERHD8</td>
      <td>karen swinford</td>
      <td>[0, 0]</td>
      <td>I bought this as a Christmas gift. my granddau...</td>
      <td>5.0</td>
      <td>owl</td>
      <td>1396656000</td>
      <td>04 5, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>108.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IboughtthisasaChristmasgiftmygranddaughterlove...</td>
      <td>owl</td>
      <td>84</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-05</td>
      <td>4</td>
      <td>B005LERHD8A5B7KCCZJOLJX</td>
      <td>1</td>
      <td>I bought this as a Christmas gift my granddaug...</td>
      <td>2014</td>
      <td>I bought this as a Christmas gift. my granddau...</td>
    </tr>
    <tr>
      <th>161487</th>
      <td>161487</td>
      <td>A1QGQMTEIZY06U</td>
      <td>B005LERHD8</td>
      <td>Kari Giacomelli</td>
      <td>[8, 11]</td>
      <td>This is so cute and such nice quality for the ...</td>
      <td>5.0</td>
      <td>So Cute!!!</td>
      <td>1357516800</td>
      <td>01 7, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>8</td>
      <td>1</td>
      <td>9</td>
      <td>0.888889</td>
      <td>135.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisissocuteandsuchnicequalityforthepriceIjust...</td>
      <td>SoCute</td>
      <td>104</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-07</td>
      <td>1</td>
      <td>B005LERHD8A1QGQMTEIZY06U</td>
      <td>1</td>
      <td>This is so cute and such nice quality for the ...</td>
      <td>2013</td>
      <td>This is so cute and such nice quality for the ...</td>
    </tr>
    <tr>
      <th>161488</th>
      <td>161488</td>
      <td>A2TQLD4MGY07K8</td>
      <td>B005LERHD8</td>
      <td>Kari Taylor</td>
      <td>[0, 0]</td>
      <td>A very cute little necklace. Ordered for my da...</td>
      <td>5.0</td>
      <td>Very cute!</td>
      <td>1391472000</td>
      <td>02 4, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>126.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>AverycutelittlenecklaceOrderedformydaughterbut...</td>
      <td>Verycute</td>
      <td>103</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-04</td>
      <td>2</td>
      <td>B005LERHD8A2TQLD4MGY07K8</td>
      <td>1</td>
      <td>A very cute little necklace Ordered for my dau...</td>
      <td>2014</td>
      <td>A very cute little necklace. Ordered for my da...</td>
    </tr>
    <tr>
      <th>161489</th>
      <td>161489</td>
      <td>A8C7DDIRD8KWA</td>
      <td>B005LERHD8</td>
      <td>Karla S. Howard "karmakorn62"</td>
      <td>[1, 1]</td>
      <td>Tres' cute!  lol  I have a soon to be 22 yr. o...</td>
      <td>5.0</td>
      <td>How cute is this?</td>
      <td>1381795200</td>
      <td>10 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>352.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>TrescutelolIhaveasoontobe22yroldandshesgetting...</td>
      <td>Howcuteisthis</td>
      <td>262</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-15</td>
      <td>10</td>
      <td>B005LERHD8A8C7DDIRD8KWA</td>
      <td>1</td>
      <td>Tres cute  lol  I have a soon to be  yr old an...</td>
      <td>2013</td>
      <td>Tres' cute!  lol  I have a soon to be 22 yr. o...</td>
    </tr>
    <tr>
      <th>161490</th>
      <td>161490</td>
      <td>AZ1QBHUN5OAG</td>
      <td>B005LERHD8</td>
      <td>kate</td>
      <td>[0, 0]</td>
      <td>cheap but cute. it can break easily if not car...</td>
      <td>5.0</td>
      <td>good</td>
      <td>1387843200</td>
      <td>12 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>101.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>cheapbutcuteitcanbreakeasilyifnotcarefulwithit...</td>
      <td>good</td>
      <td>79</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-24</td>
      <td>12</td>
      <td>B005LERHD8AZ1QBHUN5OAG</td>
      <td>1</td>
      <td>cheap but cute it can break easily if not care...</td>
      <td>2013</td>
      <td>cheap but cute. it can break easily if not car...</td>
    </tr>
    <tr>
      <th>161491</th>
      <td>161491</td>
      <td>A2M1WTT6CQ2Z8N</td>
      <td>B005LERHD8</td>
      <td>Katexoxo4</td>
      <td>[0, 0]</td>
      <td>I loved the owel necklace! at first i thought ...</td>
      <td>4.0</td>
      <td>Love it!!</td>
      <td>1361318400</td>
      <td>02 20, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>353.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Ilovedtheowelnecklaceatfirstithoughtitwasgoing...</td>
      <td>Loveit</td>
      <td>274</td>
      <td>6</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-20</td>
      <td>2</td>
      <td>B005LERHD8A2M1WTT6CQ2Z8N</td>
      <td>1</td>
      <td>I loved the owel necklace at first i thought i...</td>
      <td>2013</td>
      <td>I loved the owel necklace! at first i thought ...</td>
    </tr>
    <tr>
      <th>161492</th>
      <td>161492</td>
      <td>A3IVJYOC2EMVKV</td>
      <td>B005LERHD8</td>
      <td>Kat</td>
      <td>[0, 0]</td>
      <td>i love this i gave it to my mom for Christmas ...</td>
      <td>4.0</td>
      <td>its cool</td>
      <td>1390521600</td>
      <td>01 24, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>85.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ilovethisigaveittomymomforChristmasandsheloves...</td>
      <td>itscool</td>
      <td>66</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-24</td>
      <td>1</td>
      <td>B005LERHD8A3IVJYOC2EMVKV</td>
      <td>1</td>
      <td>i love this i gave it to my mom for Christmas ...</td>
      <td>2014</td>
      <td>i love this i gave it to my mom for Christmas ...</td>
    </tr>
    <tr>
      <th>161493</th>
      <td>161493</td>
      <td>A34YXGNJA4SUUQ</td>
      <td>B005LERHD8</td>
      <td>Katie Horkey</td>
      <td>[0, 0]</td>
      <td>It's a bit annoying, the chain is centered on ...</td>
      <td>4.0</td>
      <td>It's okay</td>
      <td>1398384000</td>
      <td>04 25, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>144.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Itsabitannoyingthechainiscenteredonthependents...</td>
      <td>Itsokay</td>
      <td>110</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-25</td>
      <td>4</td>
      <td>B005LERHD8A34YXGNJA4SUUQ</td>
      <td>1</td>
      <td>Its a bit annoying the chain is centered on th...</td>
      <td>2014</td>
      <td>It's a bit annoying, the chain is centered on ...</td>
    </tr>
    <tr>
      <th>161494</th>
      <td>161494</td>
      <td>A15BK5TVPMGOA3</td>
      <td>B005LERHD8</td>
      <td>Katie McCann</td>
      <td>[0, 0]</td>
      <td>You truly get what you pay for. Honestly, its ...</td>
      <td>1.0</td>
      <td>Don't buy</td>
      <td>1398988800</td>
      <td>05 2, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>223.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>YoutrulygetwhatyoupayforHonestlyitsnotworththe...</td>
      <td>Dontbuy</td>
      <td>177</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-02</td>
      <td>5</td>
      <td>B005LERHD8A15BK5TVPMGOA3</td>
      <td>0</td>
      <td>You truly get what you pay for Honestly its no...</td>
      <td>2014</td>
      <td>You truly get what you pay for. Honestly, its ...</td>
    </tr>
    <tr>
      <th>161495</th>
      <td>161495</td>
      <td>AFGTONJH2JYKU</td>
      <td>B005LERHD8</td>
      <td>Kavita</td>
      <td>[0, 0]</td>
      <td>its cheap but it was expected for the price, i...</td>
      <td>3.0</td>
      <td>cheap but expected</td>
      <td>1373846400</td>
      <td>07 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>itscheapbutitwasexpectedforthepriceidontreally...</td>
      <td>cheapbutexpected</td>
      <td>89</td>
      <td>16</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-15</td>
      <td>7</td>
      <td>B005LERHD8AFGTONJH2JYKU</td>
      <td>0</td>
      <td>its cheap but it was expected for the price i ...</td>
      <td>2013</td>
      <td>its cheap but it was expected for the price, i...</td>
    </tr>
    <tr>
      <th>161496</th>
      <td>161496</td>
      <td>A346N0V91WWND8</td>
      <td>B005LERHD8</td>
      <td>Kayce Nadwodny "Aqua"</td>
      <td>[0, 0]</td>
      <td>Nice size and very pretty. This was a gift for...</td>
      <td>5.0</td>
      <td>Pretty</td>
      <td>1388448000</td>
      <td>12 31, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>196.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>NicesizeandveryprettyThiswasagiftformysisteran...</td>
      <td>Pretty</td>
      <td>154</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-31</td>
      <td>12</td>
      <td>B005LERHD8A346N0V91WWND8</td>
      <td>1</td>
      <td>Nice size and very pretty This was a gift for ...</td>
      <td>2013</td>
      <td>Nice size and very pretty. This was a gift for...</td>
    </tr>
    <tr>
      <th>161497</th>
      <td>161497</td>
      <td>A29D2NAKZHUQLQ</td>
      <td>B005LERHD8</td>
      <td>Kayla</td>
      <td>[0, 0]</td>
      <td>I purchase this for a friend.  She says the qu...</td>
      <td>4.0</td>
      <td>Gift for another</td>
      <td>1398384000</td>
      <td>04 25, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>101.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IpurchasethisforafriendShesaysthequalityisgrea...</td>
      <td>Giftforanother</td>
      <td>78</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-25</td>
      <td>4</td>
      <td>B005LERHD8A29D2NAKZHUQLQ</td>
      <td>1</td>
      <td>I purchase this for a friend  She says the qua...</td>
      <td>2014</td>
      <td>I purchase this for a friend.  She says the qu...</td>
    </tr>
    <tr>
      <th>161498</th>
      <td>161498</td>
      <td>A18FA22ZM9RYGZ</td>
      <td>B005LERHD8</td>
      <td>KayteaDoubleyew</td>
      <td>[0, 0]</td>
      <td>Especially for the price.  It is a cute little...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1391040000</td>
      <td>01 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>95.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>EspeciallyforthepriceItisacutelittlegifttoputi...</td>
      <td>Cute</td>
      <td>70</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-30</td>
      <td>1</td>
      <td>B005LERHD8A18FA22ZM9RYGZ</td>
      <td>1</td>
      <td>Especially for the price  It is a cute little ...</td>
      <td>2014</td>
      <td>Especially for the price.  It is a cute little...</td>
    </tr>
    <tr>
      <th>161499</th>
      <td>161499</td>
      <td>A2BQY6J9FCCJ0O</td>
      <td>B005LERHD8</td>
      <td>KERRY M PAWLING</td>
      <td>[0, 0]</td>
      <td>This is a great pendant especially for the val...</td>
      <td>4.0</td>
      <td>Great Necklace, great value</td>
      <td>1384732800</td>
      <td>11 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>144.0</td>
      <td>Jewelry</td>
      <td>27.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThisisagreatpendantespeciallyforthevalueIhadto...</td>
      <td>GreatNecklacegreatvalue</td>
      <td>110</td>
      <td>23</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-18</td>
      <td>11</td>
      <td>B005LERHD8A2BQY6J9FCCJ0O</td>
      <td>1</td>
      <td>This is a great pendant especially for the val...</td>
      <td>2013</td>
      <td>This is a great pendant especially for the val...</td>
    </tr>
    <tr>
      <th>161500</th>
      <td>161500</td>
      <td>AUT0J13VCBUBN</td>
      <td>B005LERHD8</td>
      <td>K Friendzy</td>
      <td>[0, 0]</td>
      <td>This owl is very pretty and colorful!Great pro...</td>
      <td>5.0</td>
      <td>Very Pretty</td>
      <td>1389398400</td>
      <td>01 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisowlisveryprettyandcolorfulGreatproductGrea...</td>
      <td>VeryPretty</td>
      <td>101</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-11</td>
      <td>1</td>
      <td>B005LERHD8AUT0J13VCBUBN</td>
      <td>1</td>
      <td>This owl is very pretty and colorfulGreat prod...</td>
      <td>2014</td>
      <td>This owl is very pretty and colorful!Great pro...</td>
    </tr>
    <tr>
      <th>161501</th>
      <td>161501</td>
      <td>AZUH5XSJ2NLXR</td>
      <td>B005LERHD8</td>
      <td>K. Garrett</td>
      <td>[0, 1]</td>
      <td>You get what you pay for... This necklace look...</td>
      <td>1.0</td>
      <td>Cheap</td>
      <td>1387065600</td>
      <td>12 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>195.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>YougetwhatyoupayforThisnecklacelookscheapfeels...</td>
      <td>Cheap</td>
      <td>151</td>
      <td>5</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-15</td>
      <td>12</td>
      <td>B005LERHD8AZUH5XSJ2NLXR</td>
      <td>0</td>
      <td>You get what you pay for This necklace looks c...</td>
      <td>2013</td>
      <td>You get what you pay for... This necklace look...</td>
    </tr>
    <tr>
      <th>161502</th>
      <td>161502</td>
      <td>AENH50GW3OKDA</td>
      <td>B005LERHD8</td>
      <td>K</td>
      <td>[0, 0]</td>
      <td>If you like owls you will like this Necklace, ...</td>
      <td>5.0</td>
      <td>Vintage Owl Pendant Long Bronze chain Necklace...</td>
      <td>1385078400</td>
      <td>11 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>441.0</td>
      <td>Jewelry</td>
      <td>62.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>IfyoulikeowlsyouwilllikethisNecklaceIboughtone...</td>
      <td>VintageOwlPendantLongBronzechainNecklaceClothe...</td>
      <td>348</td>
      <td>51</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-22</td>
      <td>11</td>
      <td>B005LERHD8AENH50GW3OKDA</td>
      <td>1</td>
      <td>If you like owls you will like this Necklace I...</td>
      <td>2013</td>
      <td>If you like owls you will like this Necklace, ...</td>
    </tr>
    <tr>
      <th>161503</th>
      <td>161503</td>
      <td>A132M4CCT4TFJA</td>
      <td>B005LERHD8</td>
      <td>Kimberly A. Elliott</td>
      <td>[2, 3]</td>
      <td>Bought this on a whim and the stones are very ...</td>
      <td>5.0</td>
      <td>More vibrant in person!</td>
      <td>1379548800</td>
      <td>09 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>BoughtthisonawhimandthestonesareverycolorfulLo...</td>
      <td>Morevibrantinperson</td>
      <td>95</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-19</td>
      <td>9</td>
      <td>B005LERHD8A132M4CCT4TFJA</td>
      <td>1</td>
      <td>Bought this on a whim and the stones are very ...</td>
      <td>2013</td>
      <td>Bought this on a whim and the stones are very ...</td>
    </tr>
    <tr>
      <th>161504</th>
      <td>161504</td>
      <td>A2N6ITYSMAZLJO</td>
      <td>B005LERHD8</td>
      <td>Kimberly Gabbamonte</td>
      <td>[0, 0]</td>
      <td>Bought as a stocking stuffer for my daughter. ...</td>
      <td>5.0</td>
      <td>Owl necklace</td>
      <td>1388361600</td>
      <td>12 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>231.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>BoughtasastockingstufferformydaughterItcamerea...</td>
      <td>Owlnecklace</td>
      <td>175</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-30</td>
      <td>12</td>
      <td>B005LERHD8A2N6ITYSMAZLJO</td>
      <td>1</td>
      <td>Bought as a stocking stuffer for my daughter  ...</td>
      <td>2013</td>
      <td>Bought as a stocking stuffer for my daughter. ...</td>
    </tr>
    <tr>
      <th>161505</th>
      <td>161505</td>
      <td>A39ZW5XJ99VLOR</td>
      <td>B005LERHD8</td>
      <td>KindleOwnerInOregon</td>
      <td>[1, 1]</td>
      <td>Cute little piece!  Dollar store quality but I...</td>
      <td>5.0</td>
      <td>fun novelty owl piece</td>
      <td>1386288000</td>
      <td>12 6, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>145.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>CutelittlepieceDollarstorequalitybutIpaidlessA...</td>
      <td>funnoveltyowlpiece</td>
      <td>114</td>
      <td>18</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-06</td>
      <td>12</td>
      <td>B005LERHD8A39ZW5XJ99VLOR</td>
      <td>1</td>
      <td>Cute little piece  Dollar store quality but I ...</td>
      <td>2013</td>
      <td>Cute little piece!  Dollar store quality but I...</td>
    </tr>
    <tr>
      <th>161506</th>
      <td>161506</td>
      <td>A2E21IKOE7T964</td>
      <td>B005LERHD8</td>
      <td>knitt96</td>
      <td>[0, 0]</td>
      <td>Great service and everything! I get compliment...</td>
      <td>5.0</td>
      <td>LOVE!</td>
      <td>1389657600</td>
      <td>01 14, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>348.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>GreatserviceandeverythingIgetcomplimentswhenIw...</td>
      <td>LOVE</td>
      <td>270</td>
      <td>4</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-14</td>
      <td>1</td>
      <td>B005LERHD8A2E21IKOE7T964</td>
      <td>1</td>
      <td>Great service and everything I get compliments...</td>
      <td>2014</td>
      <td>Great service and everything! I get compliment...</td>
    </tr>
    <tr>
      <th>161507</th>
      <td>161507</td>
      <td>ANKE909QKLM3A</td>
      <td>B005LERHD8</td>
      <td>Krogo</td>
      <td>[0, 0]</td>
      <td>Cute. I get  a lot of compliments when I wear ...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1392681600</td>
      <td>02 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>111.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>CuteIgetalotofcomplimentswhenIwearitNotsurehow...</td>
      <td>Cute</td>
      <td>83</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-18</td>
      <td>2</td>
      <td>B005LERHD8ANKE909QKLM3A</td>
      <td>1</td>
      <td>Cute I get  a lot of compliments when I wear i...</td>
      <td>2014</td>
      <td>Cute. I get  a lot of compliments when I wear ...</td>
    </tr>
    <tr>
      <th>161508</th>
      <td>161508</td>
      <td>A44V99PXB7RCZ</td>
      <td>B005LERHD8</td>
      <td>K. Rosado "Your Call For Help"</td>
      <td>[0, 0]</td>
      <td>I got this here for a buck or two, and I let m...</td>
      <td>4.0</td>
      <td>Pretty cute</td>
      <td>1389830400</td>
      <td>01 16, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>312.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>IgotthishereforabuckortwoandIletmydaughterplay...</td>
      <td>Prettycute</td>
      <td>241</td>
      <td>10</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-16</td>
      <td>1</td>
      <td>B005LERHD8A44V99PXB7RCZ</td>
      <td>1</td>
      <td>I got this here for a buck or two and I let my...</td>
      <td>2014</td>
      <td>I got this here for a buck or two, and I let m...</td>
    </tr>
    <tr>
      <th>161509</th>
      <td>161509</td>
      <td>A287547UH1VBJ7</td>
      <td>B005LERHD8</td>
      <td>K. Smith</td>
      <td>[0, 0]</td>
      <td>It took a long time to come from China. I expe...</td>
      <td>3.0</td>
      <td>Okay</td>
      <td>1356739200</td>
      <td>12 29, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>214.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IttookalongtimetocomefromChinaIexpectedthatIha...</td>
      <td>Okay</td>
      <td>169</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-29</td>
      <td>12</td>
      <td>B005LERHD8A287547UH1VBJ7</td>
      <td>0</td>
      <td>It took a long time to come from China I expec...</td>
      <td>2012</td>
      <td>It took a long time to come from China. I expe...</td>
    </tr>
    <tr>
      <th>161510</th>
      <td>161510</td>
      <td>A1L3VEJ7ZAERKC</td>
      <td>B005LERHD8</td>
      <td>KtB "Clock Lady"</td>
      <td>[0, 0]</td>
      <td>my customers love it everytime i wear this lit...</td>
      <td>5.0</td>
      <td>cute</td>
      <td>1358985600</td>
      <td>01 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>138.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>mycustomersloveiteverytimeiwearthislittleowlit...</td>
      <td>cute</td>
      <td>110</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-24</td>
      <td>1</td>
      <td>B005LERHD8A1L3VEJ7ZAERKC</td>
      <td>1</td>
      <td>my customers love it everytime i wear this lit...</td>
      <td>2013</td>
      <td>my customers love it everytime i wear this lit...</td>
    </tr>
    <tr>
      <th>161511</th>
      <td>161511</td>
      <td>A3KZOQT3GX8KGV</td>
      <td>B005LERHD8</td>
      <td>Kylee</td>
      <td>[0, 0]</td>
      <td>This necklace is really cute. I only paid 79 c...</td>
      <td>5.0</td>
      <td>What a deal!</td>
      <td>1391212800</td>
      <td>02 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>371.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>ThisnecklaceisreallycuteIonlypaid79centsforitb...</td>
      <td>Whatadeal</td>
      <td>289</td>
      <td>9</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-01</td>
      <td>2</td>
      <td>B005LERHD8A3KZOQT3GX8KGV</td>
      <td>1</td>
      <td>This necklace is really cute I only paid  cent...</td>
      <td>2014</td>
      <td>This necklace is really cute. I only paid 79 c...</td>
    </tr>
    <tr>
      <th>161512</th>
      <td>161512</td>
      <td>AHICTKNZUEMSD</td>
      <td>B005LERHD8</td>
      <td>Kyt-10</td>
      <td>[0, 0]</td>
      <td>this little guy is adorable in person, and for...</td>
      <td>4.0</td>
      <td>Cute!</td>
      <td>1391472000</td>
      <td>02 4, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>172.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>thislittleguyisadorableinpersonandforthepricei...</td>
      <td>Cute</td>
      <td>135</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-04</td>
      <td>2</td>
      <td>B005LERHD8AHICTKNZUEMSD</td>
      <td>1</td>
      <td>this little guy is adorable in person and for ...</td>
      <td>2014</td>
      <td>this little guy is adorable in person, and for...</td>
    </tr>
    <tr>
      <th>161513</th>
      <td>161513</td>
      <td>A3GH7JFDZIE9Y3</td>
      <td>B005LERHD8</td>
      <td>Ladybugturtle</td>
      <td>[0, 0]</td>
      <td>got this for my little one to play dress up wi...</td>
      <td>5.0</td>
      <td>decent costume jewelry</td>
      <td>1394582400</td>
      <td>03 12, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>132.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>gotthisformylittleonetoplaydressupwithitischea...</td>
      <td>decentcostumejewelry</td>
      <td>102</td>
      <td>20</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-12</td>
      <td>3</td>
      <td>B005LERHD8A3GH7JFDZIE9Y3</td>
      <td>1</td>
      <td>got this for my little one to play dress up wi...</td>
      <td>2014</td>
      <td>got this for my little one to play dress up wi...</td>
    </tr>
    <tr>
      <th>161514</th>
      <td>161514</td>
      <td>A2O0BED5QP4IFV</td>
      <td>B005LERHD8</td>
      <td>LadyMichelleSendsLove</td>
      <td>[1, 3]</td>
      <td>I'll use it as a stocking stuffer for a little...</td>
      <td>3.0</td>
      <td>OK for kids</td>
      <td>1385424000</td>
      <td>11 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>0.250000</td>
      <td>111.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Illuseitasastockingstufferforalittlegirlnotnic...</td>
      <td>OKforkids</td>
      <td>84</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-26</td>
      <td>11</td>
      <td>B005LERHD8A2O0BED5QP4IFV</td>
      <td>0</td>
      <td>Ill use it as a stocking stuffer for a little ...</td>
      <td>2013</td>
      <td>I'll use it as a stocking stuffer for a little...</td>
    </tr>
    <tr>
      <th>161515</th>
      <td>161515</td>
      <td>A1CJXYT4TBLERF</td>
      <td>B005LERHD8</td>
      <td>Laura</td>
      <td>[0, 0]</td>
      <td>This necklace is adorable, I only received it ...</td>
      <td>5.0</td>
      <td>Love this necklace!!</td>
      <td>1364083200</td>
      <td>03 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>277.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThisnecklaceisadorableIonlyreceivedityesterday...</td>
      <td>Lovethisnecklace</td>
      <td>218</td>
      <td>16</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-24</td>
      <td>3</td>
      <td>B005LERHD8A1CJXYT4TBLERF</td>
      <td>1</td>
      <td>This necklace is adorable I only received it y...</td>
      <td>2013</td>
      <td>This necklace is adorable, I only received it ...</td>
    </tr>
    <tr>
      <th>161516</th>
      <td>161516</td>
      <td>A1QNUZIZ4QL0V5</td>
      <td>B005LERHD8</td>
      <td>lauren</td>
      <td>[0, 0]</td>
      <td>This looks just like the picture other that th...</td>
      <td>5.0</td>
      <td>Great For the Price</td>
      <td>1387324800</td>
      <td>12 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>338.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThislooksjustlikethepictureotherthatthestonesT...</td>
      <td>GreatForthePrice</td>
      <td>255</td>
      <td>16</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-18</td>
      <td>12</td>
      <td>B005LERHD8A1QNUZIZ4QL0V5</td>
      <td>1</td>
      <td>This looks just like the picture other that th...</td>
      <td>2013</td>
      <td>This looks just like the picture other that th...</td>
    </tr>
    <tr>
      <th>161517</th>
      <td>161517</td>
      <td>A3E77MUDV3ZGB</td>
      <td>B005LERHD8</td>
      <td>Lemonia justina Ashton</td>
      <td>[0, 0]</td>
      <td>It was a nice little necklace for the priceVer...</td>
      <td>4.0</td>
      <td>Nice</td>
      <td>1364601600</td>
      <td>03 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ItwasanicelittlenecklaceforthepriceVerycheapTh...</td>
      <td>Nice</td>
      <td>102</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-30</td>
      <td>3</td>
      <td>B005LERHD8A3E77MUDV3ZGB</td>
      <td>1</td>
      <td>It was a nice little necklace for the priceVer...</td>
      <td>2013</td>
      <td>It was a nice little necklace for the priceVer...</td>
    </tr>
    <tr>
      <th>161518</th>
      <td>161518</td>
      <td>A11VQPE740I4VD</td>
      <td>B005LERHD8</td>
      <td>Lexii Newman</td>
      <td>[1, 1]</td>
      <td>Super cute necklace, great ticket price. Looks...</td>
      <td>4.0</td>
      <td>Cute!</td>
      <td>1401926400</td>
      <td>06 5, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SupercutenecklacegreatticketpriceLooksexactlyl...</td>
      <td>Cute</td>
      <td>96</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-05</td>
      <td>6</td>
      <td>B005LERHD8A11VQPE740I4VD</td>
      <td>1</td>
      <td>Super cute necklace great ticket price Looks e...</td>
      <td>2014</td>
      <td>Super cute necklace, great ticket price. Looks...</td>
    </tr>
    <tr>
      <th>161519</th>
      <td>161519</td>
      <td>AT22MB184SFTQ</td>
      <td>B005LERHD8</td>
      <td>limiabal</td>
      <td>[0, 1]</td>
      <td>This is a beautiful owl, the stones are really...</td>
      <td>4.0</td>
      <td>Really Nice, I love it.</td>
      <td>1385337600</td>
      <td>11 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Thisisabeautifulowlthestonesarereallyniceandsh...</td>
      <td>ReallyNiceIloveit</td>
      <td>101</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-25</td>
      <td>11</td>
      <td>B005LERHD8AT22MB184SFTQ</td>
      <td>1</td>
      <td>This is a beautiful owl the stones are really ...</td>
      <td>2013</td>
      <td>This is a beautiful owl, the stones are really...</td>
    </tr>
    <tr>
      <th>161520</th>
      <td>161520</td>
      <td>A1RH2JFGWWNXN5</td>
      <td>B005LERHD8</td>
      <td>Linda Medwid</td>
      <td>[0, 0]</td>
      <td>I love owls &amp; figured how could I go wrong wit...</td>
      <td>2.0</td>
      <td>You get what you pay for</td>
      <td>1396310400</td>
      <td>04 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>153.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>IloveowlsfiguredhowcouldIgowrongwiththisstylis...</td>
      <td>Yougetwhatyoupayfor</td>
      <td>118</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-01</td>
      <td>4</td>
      <td>B005LERHD8A1RH2JFGWWNXN5</td>
      <td>0</td>
      <td>I love owls  figured how could I go wrong with...</td>
      <td>2014</td>
      <td>I love owls &amp; figured how could I go wrong wit...</td>
    </tr>
    <tr>
      <th>161521</th>
      <td>161521</td>
      <td>A2OMCA6N50QGUY</td>
      <td>B005LERHD8</td>
      <td>Lindsay Roberts "Lindsay"</td>
      <td>[0, 0]</td>
      <td>Cute necklace for wearing with a plain sweater...</td>
      <td>4.0</td>
      <td>long chain</td>
      <td>1400716800</td>
      <td>05 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Cutenecklaceforwearingwithaplainsweaterthechai...</td>
      <td>longchain</td>
      <td>89</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-22</td>
      <td>5</td>
      <td>B005LERHD8A2OMCA6N50QGUY</td>
      <td>1</td>
      <td>Cute necklace for wearing with a plain sweater...</td>
      <td>2014</td>
      <td>Cute necklace for wearing with a plain sweater...</td>
    </tr>
    <tr>
      <th>161522</th>
      <td>161522</td>
      <td>A3E5KPDJ9OMGL3</td>
      <td>B005LERHD8</td>
      <td>linrick</td>
      <td>[0, 0]</td>
      <td>The owl is 1.75 inches tall and about 1.5 inch...</td>
      <td>4.0</td>
      <td>Nicer in person</td>
      <td>1349827200</td>
      <td>10 10, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>325.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Theowlis175inchestallandabout15incheswidelovet...</td>
      <td>Nicerinperson</td>
      <td>245</td>
      <td>13</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-10-10</td>
      <td>10</td>
      <td>B005LERHD8A3E5KPDJ9OMGL3</td>
      <td>1</td>
      <td>The owl is  inches tall and about  inches wide...</td>
      <td>2012</td>
      <td>The owl is 1.75 inches tall and about 1.5 inch...</td>
    </tr>
    <tr>
      <th>161523</th>
      <td>161523</td>
      <td>A3444KR41N5A1P</td>
      <td>B005LERHD8</td>
      <td>Lisa Knisely</td>
      <td>[1, 1]</td>
      <td>Loved these.  It was so beautiful  I sent a fe...</td>
      <td>5.0</td>
      <td>Super cute</td>
      <td>1363910400</td>
      <td>03 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>116.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>LovedtheseItwassobeautifulIsentafewasgiftsandy...</td>
      <td>Supercute</td>
      <td>87</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-22</td>
      <td>3</td>
      <td>B005LERHD8A3444KR41N5A1P</td>
      <td>1</td>
      <td>Loved these  It was so beautiful  I sent a few...</td>
      <td>2013</td>
      <td>Loved these.  It was so beautiful  I sent a fe...</td>
    </tr>
    <tr>
      <th>161524</th>
      <td>161524</td>
      <td>A2KMHO4RO7PPO8</td>
      <td>B005LERHD8</td>
      <td>little lady</td>
      <td>[0, 0]</td>
      <td>really cute necklace! it had a weird plastic s...</td>
      <td>4.0</td>
      <td>cute necklace</td>
      <td>1363564800</td>
      <td>03 18, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>185.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>reallycutenecklaceithadaweirdplasticsmellwheni...</td>
      <td>cutenecklace</td>
      <td>145</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-18</td>
      <td>3</td>
      <td>B005LERHD8A2KMHO4RO7PPO8</td>
      <td>1</td>
      <td>really cute necklace it had a weird plastic sm...</td>
      <td>2013</td>
      <td>really cute necklace! it had a weird plastic s...</td>
    </tr>
    <tr>
      <th>161525</th>
      <td>161525</td>
      <td>AAQS9OXYU19ST</td>
      <td>B005LERHD8</td>
      <td>Lola</td>
      <td>[2, 3]</td>
      <td>It's just as pictured! got this for my middle ...</td>
      <td>5.0</td>
      <td>Holding up so far.</td>
      <td>1379635200</td>
      <td>09 20, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>197.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Itsjustaspicturedgotthisformymiddleschoolagedd...</td>
      <td>Holdingupsofar</td>
      <td>156</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-20</td>
      <td>9</td>
      <td>B005LERHD8AAQS9OXYU19ST</td>
      <td>1</td>
      <td>Its just as pictured got this for my middle sc...</td>
      <td>2013</td>
      <td>It's just as pictured! got this for my middle ...</td>
    </tr>
    <tr>
      <th>161526</th>
      <td>161526</td>
      <td>AJYAL268A59ON</td>
      <td>B005LERHD8</td>
      <td>Loose Leaf "book nut"</td>
      <td>[0, 0]</td>
      <td>Pretty eh. The antiquing is very dark and it''...</td>
      <td>1.0</td>
      <td>Junky</td>
      <td>1387065600</td>
      <td>12 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>106.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>PrettyehTheantiquingisverydarkanditsverycheapl...</td>
      <td>Junky</td>
      <td>80</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-15</td>
      <td>12</td>
      <td>B005LERHD8AJYAL268A59ON</td>
      <td>0</td>
      <td>Pretty eh The antiquing is very dark and its v...</td>
      <td>2013</td>
      <td>Pretty eh. The antiquing is very dark and it''...</td>
    </tr>
    <tr>
      <th>161527</th>
      <td>161527</td>
      <td>A3IT21VQ9E5JC6</td>
      <td>B005LERHD8</td>
      <td>Lori Edwards</td>
      <td>[0, 0]</td>
      <td>Another one of my great finds. I try to keep l...</td>
      <td>5.0</td>
      <td>Love it</td>
      <td>1389398400</td>
      <td>01 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>219.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>AnotheroneofmygreatfindsItrytokeeplittlethings...</td>
      <td>Loveit</td>
      <td>171</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-11</td>
      <td>1</td>
      <td>B005LERHD8A3IT21VQ9E5JC6</td>
      <td>1</td>
      <td>Another one of my great finds I try to keep li...</td>
      <td>2014</td>
      <td>Another one of my great finds. I try to keep l...</td>
    </tr>
    <tr>
      <th>161528</th>
      <td>161528</td>
      <td>A2VSYKTPNM520D</td>
      <td>B005LERHD8</td>
      <td>Lourdes Pion</td>
      <td>[0, 1]</td>
      <td>Necklace is very cheap. You have to be very ca...</td>
      <td>1.0</td>
      <td>Not Satisfied.</td>
      <td>1362096000</td>
      <td>03 1, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>178.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>NecklaceisverycheapYouhavetobeverycarefultakin...</td>
      <td>NotSatisfied</td>
      <td>143</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-01</td>
      <td>3</td>
      <td>B005LERHD8A2VSYKTPNM520D</td>
      <td>0</td>
      <td>Necklace is very cheap You have to be very car...</td>
      <td>2013</td>
      <td>Necklace is very cheap. You have to be very ca...</td>
    </tr>
    <tr>
      <th>161529</th>
      <td>161529</td>
      <td>A3PSH91YKGP4IV</td>
      <td>B005LERHD8</td>
      <td>Lucila Maria Roggio</td>
      <td>[0, 0]</td>
      <td>I love this necklace, I rated it four stars on...</td>
      <td>4.0</td>
      <td>good item</td>
      <td>1364774400</td>
      <td>04 1, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>191.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IlovethisnecklaceIrateditfourstarsonlybecauset...</td>
      <td>gooditem</td>
      <td>147</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-01</td>
      <td>4</td>
      <td>B005LERHD8A3PSH91YKGP4IV</td>
      <td>1</td>
      <td>I love this necklace I rated it four stars onl...</td>
      <td>2013</td>
      <td>I love this necklace, I rated it four stars on...</td>
    </tr>
    <tr>
      <th>161530</th>
      <td>161530</td>
      <td>A27JCLMIGZ8CDF</td>
      <td>B005LERHD8</td>
      <td>Lucyjcms</td>
      <td>[0, 0]</td>
      <td>goes with so many outfits, good quality...love...</td>
      <td>5.0</td>
      <td>Gets tons of compliments!</td>
      <td>1359763200</td>
      <td>02 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>135.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>goeswithsomanyoutfitsgoodqualityloveitOwlsares...</td>
      <td>Getstonsofcompliments</td>
      <td>104</td>
      <td>21</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-02</td>
      <td>2</td>
      <td>B005LERHD8A27JCLMIGZ8CDF</td>
      <td>1</td>
      <td>goes with so many outfits good qualitylove it ...</td>
      <td>2013</td>
      <td>goes with so many outfits, good quality...love...</td>
    </tr>
    <tr>
      <th>161531</th>
      <td>161531</td>
      <td>A34IS8UWEQLWOL</td>
      <td>B005LERHD8</td>
      <td>Luz</td>
      <td>[1, 1]</td>
      <td>this was agreat item, very light and cute it f...</td>
      <td>5.0</td>
      <td>Crystal owl</td>
      <td>1376352000</td>
      <td>08 13, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>99.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>thiswasagreatitemverylightandcuteitfitperfecta...</td>
      <td>Crystalowl</td>
      <td>78</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-13</td>
      <td>8</td>
      <td>B005LERHD8A34IS8UWEQLWOL</td>
      <td>1</td>
      <td>this was agreat item very light and cute it fi...</td>
      <td>2013</td>
      <td>this was agreat item, very light and cute it f...</td>
    </tr>
    <tr>
      <th>161532</th>
      <td>161532</td>
      <td>A2P5GAQDJS9C5O</td>
      <td>B005LERHD8</td>
      <td>Lynda Vice</td>
      <td>[0, 0]</td>
      <td>The price was incredible I got so much more th...</td>
      <td>5.0</td>
      <td>Darling!</td>
      <td>1390003200</td>
      <td>01 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>182.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThepricewasincredibleIgotsomuchmorethanIexpect...</td>
      <td>Darling</td>
      <td>144</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-18</td>
      <td>1</td>
      <td>B005LERHD8A2P5GAQDJS9C5O</td>
      <td>1</td>
      <td>The price was incredible I got so much more th...</td>
      <td>2014</td>
      <td>The price was incredible I got so much more th...</td>
    </tr>
    <tr>
      <th>161533</th>
      <td>161533</td>
      <td>A1C8H1E7U2WWFF</td>
      <td>B005LERHD8</td>
      <td>Lynette Gartner "BHCISHELL"</td>
      <td>[0, 0]</td>
      <td>My sister is into owls, as soon as I saw this ...</td>
      <td>5.0</td>
      <td>Great Buy!</td>
      <td>1389052800</td>
      <td>01 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>282.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>MysisterisintoowlsassoonasIsawthisnecklaceandt...</td>
      <td>GreatBuy</td>
      <td>217</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-07</td>
      <td>1</td>
      <td>B005LERHD8A1C8H1E7U2WWFF</td>
      <td>1</td>
      <td>My sister is into owls as soon as I saw this n...</td>
      <td>2014</td>
      <td>My sister is into owls, as soon as I saw this ...</td>
    </tr>
    <tr>
      <th>161534</th>
      <td>161534</td>
      <td>A3CNNP2XRBSYSV</td>
      <td>B005LERHD8</td>
      <td>Maddy</td>
      <td>[0, 0]</td>
      <td>This item is very useful and adorable; I reviv...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1376092800</td>
      <td>08 10, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>223.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThisitemisveryusefulandadorableIrevivedthisnec...</td>
      <td>Cute</td>
      <td>180</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-10</td>
      <td>8</td>
      <td>B005LERHD8A3CNNP2XRBSYSV</td>
      <td>1</td>
      <td>This item is very useful and adorable I revive...</td>
      <td>2013</td>
      <td>This item is very useful and adorable; I reviv...</td>
    </tr>
    <tr>
      <th>161535</th>
      <td>161535</td>
      <td>A2DFR4K08CFXVM</td>
      <td>B005LERHD8</td>
      <td>Maghan</td>
      <td>[0, 0]</td>
      <td>Very cute. Can't beat the price. Took about 3 ...</td>
      <td>5.0</td>
      <td>A steal.</td>
      <td>1389225600</td>
      <td>01 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>148.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VerycuteCantbeatthepriceTookabout3weekstorecei...</td>
      <td>Asteal</td>
      <td>111</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-09</td>
      <td>1</td>
      <td>B005LERHD8A2DFR4K08CFXVM</td>
      <td>1</td>
      <td>Very cute Cant beat the price Took about  week...</td>
      <td>2014</td>
      <td>Very cute. Can't beat the price. Took about 3 ...</td>
    </tr>
    <tr>
      <th>161536</th>
      <td>161536</td>
      <td>A2TZZVEC9B3AKM</td>
      <td>B005LERHD8</td>
      <td>Mandy Flannery</td>
      <td>[0, 0]</td>
      <td>The necklace is light and thin. It is really c...</td>
      <td>4.0</td>
      <td>Cute!</td>
      <td>1388361600</td>
      <td>12 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>114.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThenecklaceislightandthinItisreallycuteandthec...</td>
      <td>Cute</td>
      <td>89</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-30</td>
      <td>12</td>
      <td>B005LERHD8A2TZZVEC9B3AKM</td>
      <td>1</td>
      <td>The necklace is light and thin It is really cu...</td>
      <td>2013</td>
      <td>The necklace is light and thin. It is really c...</td>
    </tr>
    <tr>
      <th>161537</th>
      <td>161537</td>
      <td>A1FSFYP29DRI4L</td>
      <td>B005LERHD8</td>
      <td>Maria</td>
      <td>[0, 0]</td>
      <td>It is a nice necklace, but not really well don...</td>
      <td>3.0</td>
      <td>Not too bad after all</td>
      <td>1391126400</td>
      <td>01 31, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>214.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Itisanicenecklacebutnotreallywelldonethestones...</td>
      <td>Nottoobadafterall</td>
      <td>162</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-31</td>
      <td>1</td>
      <td>B005LERHD8A1FSFYP29DRI4L</td>
      <td>0</td>
      <td>It is a nice necklace but not really well done...</td>
      <td>2014</td>
      <td>It is a nice necklace, but not really well don...</td>
    </tr>
    <tr>
      <th>161538</th>
      <td>161538</td>
      <td>A3BH4PY9D92M1T</td>
      <td>B005LERHD8</td>
      <td>Marianna</td>
      <td>[0, 0]</td>
      <td>It's the year of the owl.  The owl theme is ev...</td>
      <td>5.0</td>
      <td>Order 2</td>
      <td>1396742400</td>
      <td>04 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>236.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ItstheyearoftheowlTheowlthemeiseverywhereIfyou...</td>
      <td>Order2</td>
      <td>177</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-06</td>
      <td>4</td>
      <td>B005LERHD8A3BH4PY9D92M1T</td>
      <td>1</td>
      <td>Its the year of the owl  The owl theme is ever...</td>
      <td>2014</td>
      <td>It's the year of the owl.  The owl theme is ev...</td>
    </tr>
    <tr>
      <th>161539</th>
      <td>161539</td>
      <td>AX0JCXP95QPKB</td>
      <td>B005LERHD8</td>
      <td>maria shelton</td>
      <td>[0, 0]</td>
      <td>I was disapointed in this pendant It did not s...</td>
      <td>3.0</td>
      <td>tarnished</td>
      <td>1398729600</td>
      <td>04 29, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>183.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IwasdisapointedinthispendantItdidnotsayitwould...</td>
      <td>tarnished</td>
      <td>145</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-29</td>
      <td>4</td>
      <td>B005LERHD8AX0JCXP95QPKB</td>
      <td>0</td>
      <td>I was disapointed in this pendant It did not s...</td>
      <td>2014</td>
      <td>I was disapointed in this pendant It did not s...</td>
    </tr>
    <tr>
      <th>161540</th>
      <td>161540</td>
      <td>A3MWKRG8IGCILW</td>
      <td>B005LERHD8</td>
      <td>Maria Williams</td>
      <td>[1, 2]</td>
      <td>Nice trendy piece ..worth the money...but has ...</td>
      <td>3.0</td>
      <td>Big owl</td>
      <td>1379289600</td>
      <td>09 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Nicetrendypieceworththemoneybuthasbigcrystalst...</td>
      <td>Bigowl</td>
      <td>93</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-16</td>
      <td>9</td>
      <td>B005LERHD8A3MWKRG8IGCILW</td>
      <td>0</td>
      <td>Nice trendy piece worth the moneybut has big c...</td>
      <td>2013</td>
      <td>Nice trendy piece ..worth the money...but has ...</td>
    </tr>
    <tr>
      <th>161541</th>
      <td>161541</td>
      <td>AG2UVZ9NJQZ7W</td>
      <td>B005LERHD8</td>
      <td>Marion Ladd</td>
      <td>[0, 0]</td>
      <td>This owl necklace isn't what I expected.  The ...</td>
      <td>2.0</td>
      <td>Bigger than I expected</td>
      <td>1382745600</td>
      <td>10 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>148.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ThisowlnecklaceisntwhatIexpectedThechainisreal...</td>
      <td>BiggerthanIexpected</td>
      <td>114</td>
      <td>19</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-26</td>
      <td>10</td>
      <td>B005LERHD8AG2UVZ9NJQZ7W</td>
      <td>0</td>
      <td>This owl necklace isnt what I expected  The ch...</td>
      <td>2013</td>
      <td>This owl necklace isn't what I expected.  The ...</td>
    </tr>
    <tr>
      <th>161542</th>
      <td>161542</td>
      <td>AZNUD20EBXPH1</td>
      <td>B005LERHD8</td>
      <td>Mark Gikey</td>
      <td>[0, 0]</td>
      <td>BOUGHT THIS FOR MY WIFE FOR CHRISTMAS AND SHE ...</td>
      <td>5.0</td>
      <td>OWL PENDANT</td>
      <td>1388880000</td>
      <td>01 5, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>BOUGHTTHISFORMYWIFEFORCHRISTMASANDSHELOVEDITSH...</td>
      <td>OWLPENDANT</td>
      <td>90</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-05</td>
      <td>1</td>
      <td>B005LERHD8AZNUD20EBXPH1</td>
      <td>1</td>
      <td>BOUGHT THIS FOR MY WIFE FOR CHRISTMAS AND SHE ...</td>
      <td>2014</td>
      <td>BOUGHT THIS FOR MY WIFE FOR CHRISTMAS AND SHE ...</td>
    </tr>
    <tr>
      <th>161543</th>
      <td>161543</td>
      <td>AWFA4158DDDWC</td>
      <td>B005LERHD8</td>
      <td>Marney</td>
      <td>[0, 0]</td>
      <td>One side of the owls head was lose from the bo...</td>
      <td>3.0</td>
      <td>Weak link</td>
      <td>1358812800</td>
      <td>01 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>129.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>OnesideoftheowlsheadwaslosefromthebodyTherewas...</td>
      <td>Weaklink</td>
      <td>100</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-22</td>
      <td>1</td>
      <td>B005LERHD8AWFA4158DDDWC</td>
      <td>0</td>
      <td>One side of the owls head was lose from the bo...</td>
      <td>2013</td>
      <td>One side of the owls head was lose from the bo...</td>
    </tr>
    <tr>
      <th>161544</th>
      <td>161544</td>
      <td>A335PGKOXLAKMW</td>
      <td>B005LERHD8</td>
      <td>marta f. lukowski</td>
      <td>[0, 1]</td>
      <td>As to the owl:-  I judge that this is VERY lik...</td>
      <td>3.0</td>
      <td>I should of left my grandchildren at home. The...</td>
      <td>1398902400</td>
      <td>05 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>764.0</td>
      <td>Jewelry</td>
      <td>83.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>AstotheowlIjudgethatthisisVERYlikelydesignedou...</td>
      <td>IshouldofleftmygrandchildrenathomeTheydrovemen...</td>
      <td>580</td>
      <td>66</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-01</td>
      <td>5</td>
      <td>B005LERHD8A335PGKOXLAKMW</td>
      <td>0</td>
      <td>As to the owl  I judge that this is VERY likel...</td>
      <td>2014</td>
      <td>As to the owl:-  I judge that this is VERY lik...</td>
    </tr>
    <tr>
      <th>161545</th>
      <td>161545</td>
      <td>A2QVI7NBBXGKGP</td>
      <td>B005LERHD8</td>
      <td>maryam theresa</td>
      <td>[0, 0]</td>
      <td>Very cute necklace, especially for the price. ...</td>
      <td>5.0</td>
      <td>Great value and pretty.</td>
      <td>1391212800</td>
      <td>02 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>163.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>VerycutenecklaceespeciallyforthepriceShippingt...</td>
      <td>Greatvalueandpretty</td>
      <td>126</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-01</td>
      <td>2</td>
      <td>B005LERHD8A2QVI7NBBXGKGP</td>
      <td>1</td>
      <td>Very cute necklace especially for the price  S...</td>
      <td>2014</td>
      <td>Very cute necklace, especially for the price. ...</td>
    </tr>
    <tr>
      <th>161546</th>
      <td>161546</td>
      <td>A1HCO5ZNXRGAGA</td>
      <td>B005LERHD8</td>
      <td>Mary</td>
      <td>[0, 0]</td>
      <td>I LOVE THIS. I wear it a lot and I get complim...</td>
      <td>5.0</td>
      <td>SOO CUTE</td>
      <td>1390867200</td>
      <td>01 28, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>96.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ILOVETHISIwearitalotandIgetcomplimentsonitallt...</td>
      <td>SOOCUTE</td>
      <td>71</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-28</td>
      <td>1</td>
      <td>B005LERHD8A1HCO5ZNXRGAGA</td>
      <td>1</td>
      <td>I LOVE THIS I wear it a lot and I get complime...</td>
      <td>2014</td>
      <td>I LOVE THIS. I wear it a lot and I get complim...</td>
    </tr>
    <tr>
      <th>161547</th>
      <td>161547</td>
      <td>A15PNIMFUHBW83</td>
      <td>B005LERHD8</td>
      <td>mary</td>
      <td>[0, 0]</td>
      <td>So glad i bought this. I love it. I bet the pe...</td>
      <td>5.0</td>
      <td>Love Owls</td>
      <td>1395100800</td>
      <td>03 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>91.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SogladiboughtthisIloveitIbetthepersonIgiveitto...</td>
      <td>LoveOwls</td>
      <td>66</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-18</td>
      <td>3</td>
      <td>B005LERHD8A15PNIMFUHBW83</td>
      <td>1</td>
      <td>So glad i bought this I love it I bet the pers...</td>
      <td>2014</td>
      <td>So glad i bought this. I love it. I bet the pe...</td>
    </tr>
    <tr>
      <th>161548</th>
      <td>161548</td>
      <td>A3FJQDMK3S5RT</td>
      <td>B005LERHD8</td>
      <td>MATT</td>
      <td>[0, 0]</td>
      <td>Great cheap addon item for your little girl or...</td>
      <td>5.0</td>
      <td>let her know you were thinking of her...</td>
      <td>1402963200</td>
      <td>06 17, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>328.0</td>
      <td>Jewelry</td>
      <td>40.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Greatcheapaddonitemforyourlittlegirlorgiftfory...</td>
      <td>letherknowyouwerethinkingofher</td>
      <td>254</td>
      <td>30</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-17</td>
      <td>6</td>
      <td>B005LERHD8A3FJQDMK3S5RT</td>
      <td>1</td>
      <td>Great cheap addon item for your little girl or...</td>
      <td>2014</td>
      <td>Great cheap addon item for your little girl or...</td>
    </tr>
    <tr>
      <th>161549</th>
      <td>161549</td>
      <td>A3JZC24TNOOJSV</td>
      <td>B005LERHD8</td>
      <td>Matt</td>
      <td>[0, 0]</td>
      <td>The owl is perfect, but the chain makes it loo...</td>
      <td>5.0</td>
      <td>Super cute!</td>
      <td>1389916800</td>
      <td>01 17, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>183.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>TheowlisperfectbutthechainmakesitlookcheapIjus...</td>
      <td>Supercute</td>
      <td>144</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-17</td>
      <td>1</td>
      <td>B005LERHD8A3JZC24TNOOJSV</td>
      <td>1</td>
      <td>The owl is perfect but the chain makes it look...</td>
      <td>2014</td>
      <td>The owl is perfect, but the chain makes it loo...</td>
    </tr>
    <tr>
      <th>161550</th>
      <td>161550</td>
      <td>A1FRVG2241XO6N</td>
      <td>B005LERHD8</td>
      <td>Mbible</td>
      <td>[0, 0]</td>
      <td>Exactly what I paid for... I have another one ...</td>
      <td>4.0</td>
      <td>Super cute</td>
      <td>1356912000</td>
      <td>12 31, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ExactlywhatIpaidforIhaveanotheroneoftheseinsil...</td>
      <td>Supercute</td>
      <td>118</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-31</td>
      <td>12</td>
      <td>B005LERHD8A1FRVG2241XO6N</td>
      <td>1</td>
      <td>Exactly what I paid for I have another one of ...</td>
      <td>2012</td>
      <td>Exactly what I paid for... I have another one ...</td>
    </tr>
    <tr>
      <th>161551</th>
      <td>161551</td>
      <td>A78FK0HQ6JSUV</td>
      <td>B005LERHD8</td>
      <td>M. Casey "misstkc"</td>
      <td>[0, 0]</td>
      <td>This was very inexpensive, so I can hardly giv...</td>
      <td>3.0</td>
      <td>You get what you pay for</td>
      <td>1365897600</td>
      <td>04 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>244.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThiswasveryinexpensivesoIcanhardlygiveitapoorr...</td>
      <td>Yougetwhatyoupayfor</td>
      <td>178</td>
      <td>19</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-14</td>
      <td>4</td>
      <td>B005LERHD8A78FK0HQ6JSUV</td>
      <td>0</td>
      <td>This was very inexpensive so I can hardly give...</td>
      <td>2013</td>
      <td>This was very inexpensive, so I can hardly giv...</td>
    </tr>
    <tr>
      <th>161552</th>
      <td>161552</td>
      <td>AK2FPYNJJ20LP</td>
      <td>B005LERHD8</td>
      <td>MC</td>
      <td>[0, 0]</td>
      <td>I don't know why I have this fascination with ...</td>
      <td>4.0</td>
      <td>Decent quality, but super cute</td>
      <td>1362787200</td>
      <td>03 9, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>247.0</td>
      <td>Jewelry</td>
      <td>30.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>IdontknowwhyIhavethisfascinationwithowlnecklac...</td>
      <td>Decentqualitybutsupercute</td>
      <td>190</td>
      <td>25</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-09</td>
      <td>3</td>
      <td>B005LERHD8AK2FPYNJJ20LP</td>
      <td>1</td>
      <td>I dont know why I have this fascination with o...</td>
      <td>2013</td>
      <td>I don't know why I have this fascination with ...</td>
    </tr>
    <tr>
      <th>161553</th>
      <td>161553</td>
      <td>A3U139EU4OP03A</td>
      <td>B005LERHD8</td>
      <td>M. Darden "Reign of Saturn"</td>
      <td>[0, 0]</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant/Ch...</td>
      <td>5.0</td>
      <td>Hoot the Owl</td>
      <td>1378080000</td>
      <td>09 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>218.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>VintageRetroColorfulCrystalOwlPendantChainwith...</td>
      <td>HoottheOwl</td>
      <td>175</td>
      <td>10</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-02</td>
      <td>9</td>
      <td>B005LERHD8A3U139EU4OP03A</td>
      <td>1</td>
      <td>Vintage Retro Colorful Crystal Owl PendantChai...</td>
      <td>2013</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant/Ch...</td>
    </tr>
    <tr>
      <th>161554</th>
      <td>161554</td>
      <td>A3LRF2D4O0OYDO</td>
      <td>B005LERHD8</td>
      <td>Megan</td>
      <td>[0, 0]</td>
      <td>This is very cute for the price its crazy not ...</td>
      <td>5.0</td>
      <td>AGH CUTE!</td>
      <td>1388966400</td>
      <td>01 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>135.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisverycuteforthepriceitscrazynottotryItsal...</td>
      <td>AGHCUTE</td>
      <td>105</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-06</td>
      <td>1</td>
      <td>B005LERHD8A3LRF2D4O0OYDO</td>
      <td>1</td>
      <td>This is very cute for the price its crazy not ...</td>
      <td>2014</td>
      <td>This is very cute for the price its crazy not ...</td>
    </tr>
    <tr>
      <th>161555</th>
      <td>161555</td>
      <td>A3822GTKXA67LP</td>
      <td>B005LERHD8</td>
      <td>Melinda Atwell</td>
      <td>[1, 1]</td>
      <td>This is super cute, but incredibly flimsy. The...</td>
      <td>2.0</td>
      <td>Cute, but fragile!</td>
      <td>1392422400</td>
      <td>02 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>171.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ThisissupercutebutincrediblyflimsyThebodyofthe...</td>
      <td>Cutebutfragile</td>
      <td>132</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-15</td>
      <td>2</td>
      <td>B005LERHD8A3822GTKXA67LP</td>
      <td>0</td>
      <td>This is super cute but incredibly flimsy The b...</td>
      <td>2014</td>
      <td>This is super cute, but incredibly flimsy. The...</td>
    </tr>
    <tr>
      <th>161556</th>
      <td>161556</td>
      <td>A1NRO9TD2B6AP2</td>
      <td>B005LERHD8</td>
      <td>Melinda Collis</td>
      <td>[0, 0]</td>
      <td>This is cute but very large. If you want a sta...</td>
      <td>3.0</td>
      <td>Big owl!</td>
      <td>1390435200</td>
      <td>01 23, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>116.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisiscutebutverylargeIfyouwantastandoutneckla...</td>
      <td>Bigowl</td>
      <td>88</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-23</td>
      <td>1</td>
      <td>B005LERHD8A1NRO9TD2B6AP2</td>
      <td>0</td>
      <td>This is cute but very large If you want a stan...</td>
      <td>2014</td>
      <td>This is cute but very large. If you want a sta...</td>
    </tr>
    <tr>
      <th>161557</th>
      <td>161557</td>
      <td>A2I2K6T8RHW1Z2</td>
      <td>B005LERHD8</td>
      <td>MelindaDiann</td>
      <td>[0, 0]</td>
      <td>I like it. I think it's really pretty, and it ...</td>
      <td>4.0</td>
      <td>Eh.</td>
      <td>1372291200</td>
      <td>06 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlikeitIthinkitsreallyprettyanditcameearlyitsj...</td>
      <td>Eh</td>
      <td>87</td>
      <td>2</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-06-27</td>
      <td>6</td>
      <td>B005LERHD8A2I2K6T8RHW1Z2</td>
      <td>1</td>
      <td>I like it I think its really pretty and it cam...</td>
      <td>2013</td>
      <td>I like it. I think it's really pretty, and it ...</td>
    </tr>
    <tr>
      <th>161558</th>
      <td>161558</td>
      <td>A2ESLFDVZJVQT4</td>
      <td>B005LERHD8</td>
      <td>Melissa</td>
      <td>[0, 0]</td>
      <td>Its a big oil necklace and its so pretty I got...</td>
      <td>5.0</td>
      <td>Great product!</td>
      <td>1378339200</td>
      <td>09 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ItsabigoilnecklaceanditssoprettyIgotitformysis...</td>
      <td>Greatproduct</td>
      <td>126</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-05</td>
      <td>9</td>
      <td>B005LERHD8A2ESLFDVZJVQT4</td>
      <td>1</td>
      <td>Its a big oil necklace and its so pretty I got...</td>
      <td>2013</td>
      <td>Its a big oil necklace and its so pretty I got...</td>
    </tr>
    <tr>
      <th>161559</th>
      <td>161559</td>
      <td>AJLVHR17O4U8V</td>
      <td>B005LERHD8</td>
      <td>Melly "Viper"</td>
      <td>[0, 0]</td>
      <td>I like the length of this necklace.  It's just...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1355616000</td>
      <td>12 16, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlikethelengthofthisnecklaceItsjustacutepiecea...</td>
      <td>Cute</td>
      <td>89</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-16</td>
      <td>12</td>
      <td>B005LERHD8AJLVHR17O4U8V</td>
      <td>1</td>
      <td>I like the length of this necklace  Its just a...</td>
      <td>2012</td>
      <td>I like the length of this necklace.  It's just...</td>
    </tr>
    <tr>
      <th>161560</th>
      <td>161560</td>
      <td>AWHTG124ZGE66</td>
      <td>B005LERHD8</td>
      <td>Melodie S Corley</td>
      <td>[0, 0]</td>
      <td>I bought this not only because the price was s...</td>
      <td>5.0</td>
      <td>Different</td>
      <td>1387756800</td>
      <td>12 23, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>144.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Iboughtthisnotonlybecausethepricewassooooogood...</td>
      <td>Different</td>
      <td>116</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-23</td>
      <td>12</td>
      <td>B005LERHD8AWHTG124ZGE66</td>
      <td>1</td>
      <td>I bought this not only because the price was s...</td>
      <td>2013</td>
      <td>I bought this not only because the price was s...</td>
    </tr>
    <tr>
      <th>161561</th>
      <td>161561</td>
      <td>A36VE080NBVOUP</td>
      <td>B005LERHD8</td>
      <td>Melody James</td>
      <td>[1, 1]</td>
      <td>Super fun and funky!  People are in love with ...</td>
      <td>5.0</td>
      <td>Fun and funky!</td>
      <td>1385078400</td>
      <td>11 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>130.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>SuperfunandfunkyPeopleareinlovewiththeowltrend...</td>
      <td>Funandfunky</td>
      <td>100</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-22</td>
      <td>11</td>
      <td>B005LERHD8A36VE080NBVOUP</td>
      <td>1</td>
      <td>Super fun and funky  People are in love with t...</td>
      <td>2013</td>
      <td>Super fun and funky!  People are in love with ...</td>
    </tr>
    <tr>
      <th>161562</th>
      <td>161562</td>
      <td>A1B1B68XXFLUGC</td>
      <td>B005LERHD8</td>
      <td>Meow</td>
      <td>[0, 0]</td>
      <td>I have alot of owl chains so it was only right...</td>
      <td>5.0</td>
      <td>Good</td>
      <td>1354320000</td>
      <td>12 1, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>101.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Ihavealotofowlchainssoitwasonlyrighttoaddanoth...</td>
      <td>Good</td>
      <td>79</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-01</td>
      <td>12</td>
      <td>B005LERHD8A1B1B68XXFLUGC</td>
      <td>1</td>
      <td>I have alot of owl chains so it was only right...</td>
      <td>2012</td>
      <td>I have alot of owl chains so it was only right...</td>
    </tr>
    <tr>
      <th>161563</th>
      <td>161563</td>
      <td>A1T5IEKS6SKLO8</td>
      <td>B005LERHD8</td>
      <td>Michaela Haas</td>
      <td>[0, 0]</td>
      <td>I bought this for my best friend because she's...</td>
      <td>5.0</td>
      <td>Very cute.</td>
      <td>1382486400</td>
      <td>10 23, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>268.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iboughtthisformybestfriendbecauseshesobsessedw...</td>
      <td>Verycute</td>
      <td>211</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-23</td>
      <td>10</td>
      <td>B005LERHD8A1T5IEKS6SKLO8</td>
      <td>1</td>
      <td>I bought this for my best friend because shes ...</td>
      <td>2013</td>
      <td>I bought this for my best friend because she's...</td>
    </tr>
    <tr>
      <th>161564</th>
      <td>161564</td>
      <td>A3LKZ2CX7TQJP0</td>
      <td>B005LERHD8</td>
      <td>Michelle L. Munn</td>
      <td>[0, 0]</td>
      <td>once again this was  a great item to add to my...</td>
      <td>5.0</td>
      <td>Great item for the price</td>
      <td>1358294400</td>
      <td>01 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>onceagainthiswasagreatitemtoaddtomyaccessoryco...</td>
      <td>Greatitemfortheprice</td>
      <td>93</td>
      <td>20</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-16</td>
      <td>1</td>
      <td>B005LERHD8A3LKZ2CX7TQJP0</td>
      <td>1</td>
      <td>once again this was  a great item to add to my...</td>
      <td>2013</td>
      <td>once again this was  a great item to add to my...</td>
    </tr>
    <tr>
      <th>161565</th>
      <td>161565</td>
      <td>A2KLRA43CCLIF7</td>
      <td>B005LERHD8</td>
      <td>Michelle Luman "MickeyB"</td>
      <td>[0, 0]</td>
      <td>I absolutely adore this necklace! Not only is ...</td>
      <td>5.0</td>
      <td>Love, love, love!!!</td>
      <td>1391644800</td>
      <td>02 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>185.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IabsolutelyadorethisnecklaceNotonlyisitasupera...</td>
      <td>Lovelovelove</td>
      <td>146</td>
      <td>12</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-06</td>
      <td>2</td>
      <td>B005LERHD8A2KLRA43CCLIF7</td>
      <td>1</td>
      <td>I absolutely adore this necklace Not only is i...</td>
      <td>2014</td>
      <td>I absolutely adore this necklace! Not only is ...</td>
    </tr>
    <tr>
      <th>161566</th>
      <td>161566</td>
      <td>A1R3PQLVKXKHLD</td>
      <td>B005LERHD8</td>
      <td>Millisa Miller</td>
      <td>[0, 0]</td>
      <td>longer than expected but i didn't read the mea...</td>
      <td>4.0</td>
      <td>gift for friend</td>
      <td>1389571200</td>
      <td>01 13, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>243.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>longerthanexpectedbutididntreadthemeasurements...</td>
      <td>giftforfriend</td>
      <td>193</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-13</td>
      <td>1</td>
      <td>B005LERHD8A1R3PQLVKXKHLD</td>
      <td>1</td>
      <td>longer than expected but i didnt read the meas...</td>
      <td>2014</td>
      <td>longer than expected but i didn't read the mea...</td>
    </tr>
    <tr>
      <th>161567</th>
      <td>161567</td>
      <td>AS34283W45T25</td>
      <td>B005LERHD8</td>
      <td>mimo</td>
      <td>[0, 0]</td>
      <td>Average size and a bit to kitschy for me.  Oth...</td>
      <td>3.0</td>
      <td>Looks cheaply made</td>
      <td>1390435200</td>
      <td>01 23, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>129.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>AveragesizeandabittokitschyformeOtherwisethede...</td>
      <td>Lookscheaplymade</td>
      <td>102</td>
      <td>16</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-23</td>
      <td>1</td>
      <td>B005LERHD8AS34283W45T25</td>
      <td>0</td>
      <td>Average size and a bit to kitschy for me  Othe...</td>
      <td>2014</td>
      <td>Average size and a bit to kitschy for me.  Oth...</td>
    </tr>
    <tr>
      <th>161568</th>
      <td>161568</td>
      <td>A3SGBS1DJHT00L</td>
      <td>B005LERHD8</td>
      <td>Miranda Stevenson</td>
      <td>[0, 0]</td>
      <td>I got the necklace in the mail today. It's a v...</td>
      <td>4.0</td>
      <td>Cute owl pendant</td>
      <td>1392163200</td>
      <td>02 12, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>150.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IgotthenecklaceinthemailtodayItsaverycutependa...</td>
      <td>Cuteowlpendant</td>
      <td>116</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-12</td>
      <td>2</td>
      <td>B005LERHD8A3SGBS1DJHT00L</td>
      <td>1</td>
      <td>I got the necklace in the mail today Its a ver...</td>
      <td>2014</td>
      <td>I got the necklace in the mail today. It's a v...</td>
    </tr>
    <tr>
      <th>161569</th>
      <td>161569</td>
      <td>A2F4FJ3BIZ68GJ</td>
      <td>B005LERHD8</td>
      <td>mm springfield</td>
      <td>[2, 4]</td>
      <td>I was very disappointed. It looks super cheap ...</td>
      <td>1.0</td>
      <td>junk</td>
      <td>1380499200</td>
      <td>09 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>0.333333</td>
      <td>123.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IwasverydisappointedItlookssupercheapandcheesy...</td>
      <td>junk</td>
      <td>96</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-30</td>
      <td>9</td>
      <td>B005LERHD8A2F4FJ3BIZ68GJ</td>
      <td>0</td>
      <td>I was very disappointed It looks super cheap a...</td>
      <td>2013</td>
      <td>I was very disappointed. It looks super cheap ...</td>
    </tr>
    <tr>
      <th>161570</th>
      <td>161570</td>
      <td>AHUYX2FP6SYQR</td>
      <td>B005LERHD8</td>
      <td>mn30</td>
      <td>[0, 0]</td>
      <td>always I have to say only that all your produc...</td>
      <td>5.0</td>
      <td>vintage,s retro colors crystal owl pendant and...</td>
      <td>1390348800</td>
      <td>01 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>362.0</td>
      <td>Jewelry</td>
      <td>66.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>alwaysIhavetosayonlythatallyourproductscolorss...</td>
      <td>vintagesretrocolorscrystalowlpendantandchainwi...</td>
      <td>299</td>
      <td>56</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-22</td>
      <td>1</td>
      <td>B005LERHD8AHUYX2FP6SYQR</td>
      <td>1</td>
      <td>always I have to say only that all your produc...</td>
      <td>2014</td>
      <td>always I have to say only that all your produc...</td>
    </tr>
    <tr>
      <th>161571</th>
      <td>161571</td>
      <td>ANVO1550KQHJ9</td>
      <td>B005LERHD8</td>
      <td>MN Girl</td>
      <td>[0, 0]</td>
      <td>For the cost I am thrilled with this necklace!...</td>
      <td>4.0</td>
      <td>Beautiful Bargain</td>
      <td>1355270400</td>
      <td>12 12, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>407.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ForthecostIamthrilledwiththisnecklaceIwasscare...</td>
      <td>BeautifulBargain</td>
      <td>312</td>
      <td>16</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-12</td>
      <td>12</td>
      <td>B005LERHD8ANVO1550KQHJ9</td>
      <td>1</td>
      <td>For the cost I am thrilled with this necklace ...</td>
      <td>2012</td>
      <td>For the cost I am thrilled with this necklace!...</td>
    </tr>
    <tr>
      <th>161572</th>
      <td>161572</td>
      <td>AWA6BBJ4K8PI9</td>
      <td>B005LERHD8</td>
      <td>Mom of 2</td>
      <td>[0, 0]</td>
      <td>These are so cute I bought 4 of them, for my d...</td>
      <td>5.0</td>
      <td>very cute!</td>
      <td>1372809600</td>
      <td>07 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>219.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThesearesocuteIbought4ofthemformydaughtermymom...</td>
      <td>verycute</td>
      <td>166</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-03</td>
      <td>7</td>
      <td>B005LERHD8AWA6BBJ4K8PI9</td>
      <td>1</td>
      <td>These are so cute I bought  of them for my dau...</td>
      <td>2013</td>
      <td>These are so cute I bought 4 of them, for my d...</td>
    </tr>
    <tr>
      <th>161573</th>
      <td>161573</td>
      <td>AHFEZ1KSH93IR</td>
      <td>B005LERHD8</td>
      <td>Mom of 2 in Cali</td>
      <td>[0, 0]</td>
      <td>You could have easily spent $50 at Macy's or N...</td>
      <td>5.0</td>
      <td>Way nicer than I expected</td>
      <td>1365120000</td>
      <td>04 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>140.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Youcouldhaveeasilyspent50atMacysorNordstromfor...</td>
      <td>WaynicerthanIexpected</td>
      <td>109</td>
      <td>21</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-05</td>
      <td>4</td>
      <td>B005LERHD8AHFEZ1KSH93IR</td>
      <td>1</td>
      <td>You could have easily spent  at Macys or Nords...</td>
      <td>2013</td>
      <td>You could have easily spent $50 at Macy's or N...</td>
    </tr>
    <tr>
      <th>161574</th>
      <td>161574</td>
      <td>A3T7UKBUV1W9Y4</td>
      <td>B005LERHD8</td>
      <td>Mom of three beauties</td>
      <td>[0, 0]</td>
      <td>Cute, but I bought two and one came with a bro...</td>
      <td>3.0</td>
      <td>Meh</td>
      <td>1384560000</td>
      <td>11 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>275.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>CutebutIboughttwoandonecamewithabrokenunusable...</td>
      <td>Meh</td>
      <td>209</td>
      <td>3</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-16</td>
      <td>11</td>
      <td>B005LERHD8A3T7UKBUV1W9Y4</td>
      <td>0</td>
      <td>Cute but I bought two and one came with a brok...</td>
      <td>2013</td>
      <td>Cute, but I bought two and one came with a bro...</td>
    </tr>
    <tr>
      <th>161575</th>
      <td>161575</td>
      <td>A10UHQH1YL5Q6B</td>
      <td>B005LERHD8</td>
      <td>MONTYHADES</td>
      <td>[0, 0]</td>
      <td>I got it for my sister and she loved it,of cou...</td>
      <td>5.0</td>
      <td>very nice and pretty..</td>
      <td>1354752000</td>
      <td>12 6, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Igotitformysisterandsheloveditofcoursethechain...</td>
      <td>veryniceandpretty</td>
      <td>123</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-06</td>
      <td>12</td>
      <td>B005LERHD8A10UHQH1YL5Q6B</td>
      <td>1</td>
      <td>I got it for my sister and she loved itof cour...</td>
      <td>2012</td>
      <td>I got it for my sister and she loved it,of cou...</td>
    </tr>
    <tr>
      <th>161576</th>
      <td>161576</td>
      <td>A2RMMIVUO1EH22</td>
      <td>B005LERHD8</td>
      <td>Morgan B. Russell</td>
      <td>[0, 0]</td>
      <td>I expected this necklace to be cheap because o...</td>
      <td>3.0</td>
      <td>Cheap</td>
      <td>1390348800</td>
      <td>01 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>256.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iexpectedthisnecklacetobecheapbecauseoftherevi...</td>
      <td>Cheap</td>
      <td>195</td>
      <td>5</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-22</td>
      <td>1</td>
      <td>B005LERHD8A2RMMIVUO1EH22</td>
      <td>0</td>
      <td>I expected this necklace to be cheap because o...</td>
      <td>2014</td>
      <td>I expected this necklace to be cheap because o...</td>
    </tr>
    <tr>
      <th>161577</th>
      <td>161577</td>
      <td>AB15M1ZP6GQAW</td>
      <td>B005LERHD8</td>
      <td>mostly pleased</td>
      <td>[0, 1]</td>
      <td>I went to a store once and I saw few long chai...</td>
      <td>5.0</td>
      <td>Cute and cheap</td>
      <td>1380672000</td>
      <td>10 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>356.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IwenttoastoreonceandIsawfewlongchainnecklacesa...</td>
      <td>Cuteandcheap</td>
      <td>279</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-02</td>
      <td>10</td>
      <td>B005LERHD8AB15M1ZP6GQAW</td>
      <td>1</td>
      <td>I went to a store once and I saw few long chai...</td>
      <td>2013</td>
      <td>I went to a store once and I saw few long chai...</td>
    </tr>
    <tr>
      <th>161578</th>
      <td>161578</td>
      <td>A2BB6AX0AZ7FRL</td>
      <td>B005LERHD8</td>
      <td>Ms. Charles</td>
      <td>[0, 0]</td>
      <td>I got this for my best friend to add into my g...</td>
      <td>5.0</td>
      <td>Present</td>
      <td>1377302400</td>
      <td>08 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>143.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Igotthisformybestfriendtoaddintomygiftbagprese...</td>
      <td>Present</td>
      <td>110</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-24</td>
      <td>8</td>
      <td>B005LERHD8A2BB6AX0AZ7FRL</td>
      <td>1</td>
      <td>I got this for my best friend to add into my g...</td>
      <td>2013</td>
      <td>I got this for my best friend to add into my g...</td>
    </tr>
    <tr>
      <th>161579</th>
      <td>161579</td>
      <td>A6Q9J59WP9LQK</td>
      <td>B005LERHD8</td>
      <td>Ms. Diana Gurzadyan</td>
      <td>[2, 3]</td>
      <td>This necklace smells badly and when you touch ...</td>
      <td>1.0</td>
      <td>smells badly</td>
      <td>1361404800</td>
      <td>02 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>149.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Thisnecklacesmellsbadlyandwhenyoutouchitthesme...</td>
      <td>smellsbadly</td>
      <td>121</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-21</td>
      <td>2</td>
      <td>B005LERHD8A6Q9J59WP9LQK</td>
      <td>0</td>
      <td>This necklace smells badly and when you touch ...</td>
      <td>2013</td>
      <td>This necklace smells badly and when you touch ...</td>
    </tr>
    <tr>
      <th>161580</th>
      <td>161580</td>
      <td>A2LKE0SEQBP6PD</td>
      <td>B005LERHD8</td>
      <td>Ms. Hill "CH"</td>
      <td>[0, 0]</td>
      <td>I bought this as a gift for a female relative ...</td>
      <td>5.0</td>
      <td>Cute</td>
      <td>1371081600</td>
      <td>06 13, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>118.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Iboughtthisasagiftforafemalerelativeandwaswell...</td>
      <td>Cute</td>
      <td>95</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-06-13</td>
      <td>6</td>
      <td>B005LERHD8A2LKE0SEQBP6PD</td>
      <td>1</td>
      <td>I bought this as a gift for a female relative ...</td>
      <td>2013</td>
      <td>I bought this as a gift for a female relative ...</td>
    </tr>
    <tr>
      <th>161581</th>
      <td>161581</td>
      <td>A1Z7Y2GMAP9SRY</td>
      <td>B005LERHD8</td>
      <td>M. Thompson "Dyson Diva"</td>
      <td>[0, 0]</td>
      <td>This is really cute especially for the price. ...</td>
      <td>5.0</td>
      <td>So cute</td>
      <td>1389398400</td>
      <td>01 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>126.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisreallycuteespeciallyforthepriceIthasheld...</td>
      <td>Socute</td>
      <td>97</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-11</td>
      <td>1</td>
      <td>B005LERHD8A1Z7Y2GMAP9SRY</td>
      <td>1</td>
      <td>This is really cute especially for the price  ...</td>
      <td>2014</td>
      <td>This is really cute especially for the price. ...</td>
    </tr>
    <tr>
      <th>161582</th>
      <td>161582</td>
      <td>A30JTOC8FB9VVD</td>
      <td>B005LERHD8</td>
      <td>Mykaela</td>
      <td>[0, 0]</td>
      <td>I got this in the mail earlier than expected a...</td>
      <td>5.0</td>
      <td>Exactly Like It's Pictured</td>
      <td>1390780800</td>
      <td>01 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>302.0</td>
      <td>Jewelry</td>
      <td>26.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Igotthisinthemailearlierthanexpectedanditsexac...</td>
      <td>ExactlyLikeItsPictured</td>
      <td>236</td>
      <td>22</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-27</td>
      <td>1</td>
      <td>B005LERHD8A30JTOC8FB9VVD</td>
      <td>1</td>
      <td>I got this in the mail earlier than expected a...</td>
      <td>2014</td>
      <td>I got this in the mail earlier than expected a...</td>
    </tr>
    <tr>
      <th>161583</th>
      <td>161583</td>
      <td>A1OH54Q0N3I3OY</td>
      <td>B005LERHD8</td>
      <td>myopinions</td>
      <td>[0, 0]</td>
      <td>Came quickly and it looks just like it does on...</td>
      <td>4.0</td>
      <td>love it</td>
      <td>1390176000</td>
      <td>01 20, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>96.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Camequicklyanditlooksjustlikeitdoesonthepictur...</td>
      <td>loveit</td>
      <td>75</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-20</td>
      <td>1</td>
      <td>B005LERHD8A1OH54Q0N3I3OY</td>
      <td>1</td>
      <td>Came quickly and it looks just like it does on...</td>
      <td>2014</td>
      <td>Came quickly and it looks just like it does on...</td>
    </tr>
    <tr>
      <th>161584</th>
      <td>161584</td>
      <td>A39T51LZYXGC06</td>
      <td>B005LERHD8</td>
      <td>Namaste</td>
      <td>[1, 1]</td>
      <td>I bought two of these as a gift for two people...</td>
      <td>5.0</td>
      <td>Bought as gift</td>
      <td>1393545600</td>
      <td>02 28, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>137.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IboughttwooftheseasagiftfortwopeopleatRiceUniv...</td>
      <td>Boughtasgift</td>
      <td>108</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-28</td>
      <td>2</td>
      <td>B005LERHD8A39T51LZYXGC06</td>
      <td>1</td>
      <td>I bought two of these as a gift for two people...</td>
      <td>2014</td>
      <td>I bought two of these as a gift for two people...</td>
    </tr>
    <tr>
      <th>161585</th>
      <td>161585</td>
      <td>A32Z22ZL58XULT</td>
      <td>B005LERHD8</td>
      <td>Nancy Eubanks</td>
      <td>[0, 0]</td>
      <td>This is a darling necklace and I hope the teen...</td>
      <td>5.0</td>
      <td>Very cute item for teenagers</td>
      <td>1390176000</td>
      <td>01 20, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>99.0</td>
      <td>Jewelry</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThisisadarlingnecklaceandIhopetheteensthatwill...</td>
      <td>Verycuteitemforteenagers</td>
      <td>79</td>
      <td>24</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-20</td>
      <td>1</td>
      <td>B005LERHD8A32Z22ZL58XULT</td>
      <td>1</td>
      <td>This is a darling necklace and I hope the teen...</td>
      <td>2014</td>
      <td>This is a darling necklace and I hope the teen...</td>
    </tr>
    <tr>
      <th>161586</th>
      <td>161586</td>
      <td>A3DTZTXDHK08EF</td>
      <td>B005LERHD8</td>
      <td>Natalie</td>
      <td>[0, 0]</td>
      <td>What a lovely necklace! It is quite large but ...</td>
      <td>5.0</td>
      <td>Great</td>
      <td>1381190400</td>
      <td>10 8, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>205.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>WhatalovelynecklaceItisquitelargebutthatiswhat...</td>
      <td>Great</td>
      <td>158</td>
      <td>5</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-08</td>
      <td>10</td>
      <td>B005LERHD8A3DTZTXDHK08EF</td>
      <td>1</td>
      <td>What a lovely necklace It is quite large but t...</td>
      <td>2013</td>
      <td>What a lovely necklace! It is quite large but ...</td>
    </tr>
    <tr>
      <th>161587</th>
      <td>161587</td>
      <td>AFNDFG39I5L5</td>
      <td>B005LERHD8</td>
      <td>Nia Gill</td>
      <td>[0, 0]</td>
      <td>Got it for a friend, and she apparently loves ...</td>
      <td>4.0</td>
      <td>.</td>
      <td>1394668800</td>
      <td>03 13, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>1.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>GotitforafriendandsheapparentlylovesitSoIlltak...</td>
      <td></td>
      <td>83</td>
      <td>0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-13</td>
      <td>3</td>
      <td>B005LERHD8AFNDFG39I5L5</td>
      <td>1</td>
      <td>Got it for a friend and she apparently loves i...</td>
      <td>2014</td>
      <td>Got it for a friend, and she apparently loves ...</td>
    </tr>
    <tr>
      <th>161588</th>
      <td>161588</td>
      <td>ACKMT8MT9BU52</td>
      <td>B005LERHD8</td>
      <td>Nicanor</td>
      <td>[0, 0]</td>
      <td>great product better than what I imaginedI kno...</td>
      <td>5.0</td>
      <td>owl</td>
      <td>1390694400</td>
      <td>01 26, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>123.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>greatproductbetterthanwhatIimaginedIknowmydaug...</td>
      <td>owl</td>
      <td>100</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-26</td>
      <td>1</td>
      <td>B005LERHD8ACKMT8MT9BU52</td>
      <td>1</td>
      <td>great product better than what I imaginedI kno...</td>
      <td>2014</td>
      <td>great product better than what I imaginedI kno...</td>
    </tr>
    <tr>
      <th>161589</th>
      <td>161589</td>
      <td>A6JW3CRTK6CZZ</td>
      <td>B005LERHD8</td>
      <td>nickel</td>
      <td>[0, 0]</td>
      <td>Great price, I love wearing it, and it is the ...</td>
      <td>5.0</td>
      <td>owl necklace</td>
      <td>1392422400</td>
      <td>02 15, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>110.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>GreatpriceIlovewearingitanditistheperfectlengt...</td>
      <td>owlnecklace</td>
      <td>86</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-15</td>
      <td>2</td>
      <td>B005LERHD8A6JW3CRTK6CZZ</td>
      <td>1</td>
      <td>Great price I love wearing it and it is the pe...</td>
      <td>2014</td>
      <td>Great price, I love wearing it, and it is the ...</td>
    </tr>
    <tr>
      <th>161590</th>
      <td>161590</td>
      <td>A2ZPU3QHD1DTYT</td>
      <td>B005LERHD8</td>
      <td>Nicole Manes</td>
      <td>[0, 0]</td>
      <td>I loved this necklace. It is pretty good quali...</td>
      <td>5.0</td>
      <td>SO PRETTY!</td>
      <td>1389571200</td>
      <td>01 13, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>127.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlovedthisnecklaceItisprettygoodqualityandsupe...</td>
      <td>SOPRETTY</td>
      <td>99</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-13</td>
      <td>1</td>
      <td>B005LERHD8A2ZPU3QHD1DTYT</td>
      <td>1</td>
      <td>I loved this necklace It is pretty good qualit...</td>
      <td>2014</td>
      <td>I loved this necklace. It is pretty good quali...</td>
    </tr>
    <tr>
      <th>161591</th>
      <td>161591</td>
      <td>A3T6U5NFR55X6D</td>
      <td>B005LERHD8</td>
      <td>Nicole Reyna</td>
      <td>[0, 0]</td>
      <td>I'm actually wearing this necklace AGAIN to wo...</td>
      <td>5.0</td>
      <td>I wear it all the time!</td>
      <td>1378339200</td>
      <td>09 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>113.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ImactuallywearingthisnecklaceAGAINtoworkbcitma...</td>
      <td>Iwearitallthetime</td>
      <td>88</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-05</td>
      <td>9</td>
      <td>B005LERHD8A3T6U5NFR55X6D</td>
      <td>1</td>
      <td>Im actually wearing this necklace AGAIN to wor...</td>
      <td>2013</td>
      <td>I'm actually wearing this necklace AGAIN to wo...</td>
    </tr>
    <tr>
      <th>161592</th>
      <td>161592</td>
      <td>A32UCS8155TK6Q</td>
      <td>B005LERHD8</td>
      <td>N.R.</td>
      <td>[0, 0]</td>
      <td>Just as expected. It is affordable and I have ...</td>
      <td>4.0</td>
      <td>cool owl necklace</td>
      <td>1402272000</td>
      <td>06 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>133.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>JustasexpectedItisaffordableandIhavegottenseve...</td>
      <td>coolowlnecklace</td>
      <td>109</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-09</td>
      <td>6</td>
      <td>B005LERHD8A32UCS8155TK6Q</td>
      <td>1</td>
      <td>Just as expected It is affordable and I have g...</td>
      <td>2014</td>
      <td>Just as expected. It is affordable and I have ...</td>
    </tr>
    <tr>
      <th>161593</th>
      <td>161593</td>
      <td>ASDEJ8NCJP1IH</td>
      <td>B005LERHD8</td>
      <td>nwklee</td>
      <td>[0, 0]</td>
      <td>For someone who likes owls.  This owls were be...</td>
      <td>4.0</td>
      <td>Nice Owl pendant !</td>
      <td>1389571200</td>
      <td>01 13, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>255.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>ForsomeonewholikesowlsThisowlswerebeautifulspa...</td>
      <td>NiceOwlpendant</td>
      <td>199</td>
      <td>14</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-13</td>
      <td>1</td>
      <td>B005LERHD8ASDEJ8NCJP1IH</td>
      <td>1</td>
      <td>For someone who likes owls  This owls were bea...</td>
      <td>2014</td>
      <td>For someone who likes owls.  This owls were be...</td>
    </tr>
    <tr>
      <th>161594</th>
      <td>161594</td>
      <td>ASBIEY56AC2RE</td>
      <td>B005LERHD8</td>
      <td>Ola</td>
      <td>[0, 0]</td>
      <td>It's very light. Much lighter than I thought w...</td>
      <td>3.0</td>
      <td>I like it!</td>
      <td>1389139200</td>
      <td>01 8, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>114.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ItsverylightMuchlighterthanIthoughtwouldbeButi...</td>
      <td>Ilikeit</td>
      <td>88</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-08</td>
      <td>1</td>
      <td>B005LERHD8ASBIEY56AC2RE</td>
      <td>0</td>
      <td>Its very light Much lighter than I thought wou...</td>
      <td>2014</td>
      <td>It's very light. Much lighter than I thought w...</td>
    </tr>
    <tr>
      <th>161595</th>
      <td>161595</td>
      <td>A2Q1UZTJQUOQXK</td>
      <td>B005LERHD8</td>
      <td>Olivia English</td>
      <td>[0, 0]</td>
      <td>I love this necklace! I bought it as a gift fo...</td>
      <td>5.0</td>
      <td>love</td>
      <td>1395878400</td>
      <td>03 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlovethisnecklaceIboughtitasagiftformysisterbe...</td>
      <td>love</td>
      <td>86</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-27</td>
      <td>3</td>
      <td>B005LERHD8A2Q1UZTJQUOQXK</td>
      <td>1</td>
      <td>I love this necklace I bought it as a gift for...</td>
      <td>2014</td>
      <td>I love this necklace! I bought it as a gift fo...</td>
    </tr>
    <tr>
      <th>161596</th>
      <td>161596</td>
      <td>A1CVQNHWSCYX68</td>
      <td>B005LERHD8</td>
      <td>Orange Juice</td>
      <td>[0, 0]</td>
      <td>It came exactly as said, nothing wrong at all....</td>
      <td>5.0</td>
      <td>It is great</td>
      <td>1390089600</td>
      <td>01 19, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ItcameexactlyassaidnothingwrongatallIwouldbuya...</td>
      <td>Itisgreat</td>
      <td>123</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-19</td>
      <td>1</td>
      <td>B005LERHD8A1CVQNHWSCYX68</td>
      <td>1</td>
      <td>It came exactly as said nothing wrong at all I...</td>
      <td>2014</td>
      <td>It came exactly as said, nothing wrong at all....</td>
    </tr>
    <tr>
      <th>161597</th>
      <td>161597</td>
      <td>A3B1HS1LF0PPQZ</td>
      <td>B005LERHD8</td>
      <td>PacNwMomOfThree</td>
      <td>[0, 0]</td>
      <td>Quick shipping, it came in one piece and looks...</td>
      <td>4.0</td>
      <td>Very cute!</td>
      <td>1391040000</td>
      <td>01 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Quickshippingitcameinonepieceandlookslikethepi...</td>
      <td>Verycute</td>
      <td>98</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-30</td>
      <td>1</td>
      <td>B005LERHD8A3B1HS1LF0PPQZ</td>
      <td>1</td>
      <td>Quick shipping it came in one piece and looks ...</td>
      <td>2014</td>
      <td>Quick shipping, it came in one piece and looks...</td>
    </tr>
    <tr>
      <th>161598</th>
      <td>161598</td>
      <td>A18O52WNBOBJAT</td>
      <td>B005LERHD8</td>
      <td>pamela smith</td>
      <td>[0, 0]</td>
      <td>I had some difficulty receiving my pendant and...</td>
      <td>5.0</td>
      <td>Really cute pendant on a long, matching chain.</td>
      <td>1395878400</td>
      <td>03 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>283.0</td>
      <td>Jewelry</td>
      <td>46.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Ihadsomedifficultyreceivingmypendantandemailed...</td>
      <td>Reallycutependantonalongmatchingchain</td>
      <td>231</td>
      <td>37</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-27</td>
      <td>3</td>
      <td>B005LERHD8A18O52WNBOBJAT</td>
      <td>1</td>
      <td>I had some difficulty receiving my pendant and...</td>
      <td>2014</td>
      <td>I had some difficulty receiving my pendant and...</td>
    </tr>
    <tr>
      <th>161599</th>
      <td>161599</td>
      <td>A3B4XU398QW4Z0</td>
      <td>B005LERHD8</td>
      <td>Patrick V.</td>
      <td>[0, 0]</td>
      <td>I also ordered this chain b/c of the cheap pri...</td>
      <td>4.0</td>
      <td>super cute</td>
      <td>1388016000</td>
      <td>12 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>206.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IalsoorderedthischainbcofthecheappriceIloveita...</td>
      <td>supercute</td>
      <td>154</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-26</td>
      <td>12</td>
      <td>B005LERHD8A3B4XU398QW4Z0</td>
      <td>1</td>
      <td>I also ordered this chain bc of the cheap pric...</td>
      <td>2013</td>
      <td>I also ordered this chain b/c of the cheap pri...</td>
    </tr>
    <tr>
      <th>161600</th>
      <td>161600</td>
      <td>A1M7MKIC7GSD8Z</td>
      <td>B005LERHD8</td>
      <td>Patti E.</td>
      <td>[0, 0]</td>
      <td>the eyes look like onyx beadsso goes nice with...</td>
      <td>5.0</td>
      <td>fun!!!</td>
      <td>1394582400</td>
      <td>03 12, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>theeyeslooklikeonyxbeadssogoesnicewithonyxearr...</td>
      <td>fun</td>
      <td>100</td>
      <td>3</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-12</td>
      <td>3</td>
      <td>B005LERHD8A1M7MKIC7GSD8Z</td>
      <td>1</td>
      <td>the eyes look like onyx beadsso goes nice with...</td>
      <td>2014</td>
      <td>the eyes look like onyx beadsso goes nice with...</td>
    </tr>
    <tr>
      <th>161601</th>
      <td>161601</td>
      <td>A1ZM3GJ1KTIQX0</td>
      <td>B005LERHD8</td>
      <td>pattyisroxxy</td>
      <td>[0, 0]</td>
      <td>This is the cutest necklace. It's the perfect ...</td>
      <td>5.0</td>
      <td>Perfect</td>
      <td>1354060800</td>
      <td>11 28, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>128.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisthecutestnecklaceItstheperfectsizetheper...</td>
      <td>Perfect</td>
      <td>97</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-28</td>
      <td>11</td>
      <td>B005LERHD8A1ZM3GJ1KTIQX0</td>
      <td>1</td>
      <td>This is the cutest necklace Its the perfect si...</td>
      <td>2012</td>
      <td>This is the cutest necklace. It's the perfect ...</td>
    </tr>
    <tr>
      <th>161602</th>
      <td>161602</td>
      <td>AZDKF2JQG3JRB</td>
      <td>B005LERHD8</td>
      <td>Paul C. Whipple "Mr_Whipple"</td>
      <td>[0, 0]</td>
      <td>She seems to like it.  Thats all that matters,...</td>
      <td>5.0</td>
      <td>Wifey Wears it Everywhere</td>
      <td>1389139200</td>
      <td>01 8, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>133.0</td>
      <td>Jewelry</td>
      <td>25.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>SheseemstolikeitThatsallthatmattersRightILovey...</td>
      <td>WifeyWearsitEverywhere</td>
      <td>100</td>
      <td>22</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-08</td>
      <td>1</td>
      <td>B005LERHD8AZDKF2JQG3JRB</td>
      <td>1</td>
      <td>She seems to like it  Thats all that matters R...</td>
      <td>2014</td>
      <td>She seems to like it.  Thats all that matters,...</td>
    </tr>
    <tr>
      <th>161603</th>
      <td>161603</td>
      <td>A2CYSK76Z9PS64</td>
      <td>B005LERHD8</td>
      <td>Peggy M. Lewis "gatelady"</td>
      <td>[0, 0]</td>
      <td>My daughter loves owls and when she received t...</td>
      <td>5.0</td>
      <td>Such fun</td>
      <td>1374019200</td>
      <td>07 17, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>153.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Mydaughterlovesowlsandwhenshereceivedthisshewa...</td>
      <td>Suchfun</td>
      <td>121</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-17</td>
      <td>7</td>
      <td>B005LERHD8A2CYSK76Z9PS64</td>
      <td>1</td>
      <td>My daughter loves owls and when she received t...</td>
      <td>2013</td>
      <td>My daughter loves owls and when she received t...</td>
    </tr>
    <tr>
      <th>161604</th>
      <td>161604</td>
      <td>A6Y7658A04MTT</td>
      <td>B005LERHD8</td>
      <td>Perry M. Rogers</td>
      <td>[1, 1]</td>
      <td>I paid $0.75 for this and it it perfect for ho...</td>
      <td>5.0</td>
      <td>Amazing for the price.</td>
      <td>1385942400</td>
      <td>12 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>235.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Ipaid075forthisandititperfectforhowmuchyoupayI...</td>
      <td>Amazingfortheprice</td>
      <td>177</td>
      <td>18</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-02</td>
      <td>12</td>
      <td>B005LERHD8A6Y7658A04MTT</td>
      <td>1</td>
      <td>I paid  for this and it it perfect for how muc...</td>
      <td>2013</td>
      <td>I paid $0.75 for this and it it perfect for ho...</td>
    </tr>
    <tr>
      <th>161605</th>
      <td>161605</td>
      <td>A1S28L6LVIVPV3</td>
      <td>B005LERHD8</td>
      <td>piptastic</td>
      <td>[0, 0]</td>
      <td>First, the price. Wonderful! Seriously. Wonder...</td>
      <td>5.0</td>
      <td>Owls! Necklaces!</td>
      <td>1367280000</td>
      <td>04 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>239.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>FirstthepriceWonderfulSeriouslyWonderfulIfyoul...</td>
      <td>OwlsNecklaces</td>
      <td>189</td>
      <td>13</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-30</td>
      <td>4</td>
      <td>B005LERHD8A1S28L6LVIVPV3</td>
      <td>1</td>
      <td>First the price Wonderful Seriously WonderfulI...</td>
      <td>2013</td>
      <td>First, the price. Wonderful! Seriously. Wonder...</td>
    </tr>
    <tr>
      <th>161606</th>
      <td>161606</td>
      <td>A3CKWKLURZWPRP</td>
      <td>B005LERHD8</td>
      <td>policeman's wife</td>
      <td>[0, 0]</td>
      <td>The chain is cute but not sturdy so be careful...</td>
      <td>5.0</td>
      <td>LOVE this necklace</td>
      <td>1357344000</td>
      <td>01 5, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>198.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Thechainiscutebutnotsturdysobecarefulwhilewear...</td>
      <td>LOVEthisnecklace</td>
      <td>159</td>
      <td>16</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-05</td>
      <td>1</td>
      <td>B005LERHD8A3CKWKLURZWPRP</td>
      <td>1</td>
      <td>The chain is cute but not sturdy so be careful...</td>
      <td>2013</td>
      <td>The chain is cute but not sturdy so be careful...</td>
    </tr>
    <tr>
      <th>161607</th>
      <td>161607</td>
      <td>A1M5VDKXHMVJYQ</td>
      <td>B005LERHD8</td>
      <td>Poppyngrl</td>
      <td>[0, 0]</td>
      <td>Exactly what I wanted! The necklace is way cut...</td>
      <td>5.0</td>
      <td>Happy Girl!</td>
      <td>1361404800</td>
      <td>02 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>430.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>ExactlywhatIwantedThenecklaceiswaycuteronIreal...</td>
      <td>HappyGirl</td>
      <td>328</td>
      <td>9</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-21</td>
      <td>2</td>
      <td>B005LERHD8A1M5VDKXHMVJYQ</td>
      <td>1</td>
      <td>Exactly what I wanted The necklace is way cute...</td>
      <td>2013</td>
      <td>Exactly what I wanted! The necklace is way cut...</td>
    </tr>
    <tr>
      <th>161608</th>
      <td>161608</td>
      <td>A3APCBD7D7SW4Y</td>
      <td>B005LERHD8</td>
      <td>Princesita "Princesita"</td>
      <td>[0, 0]</td>
      <td>Runs small, is also kind of weak looking, but ...</td>
      <td>5.0</td>
      <td>nice</td>
      <td>1392940800</td>
      <td>02 21, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>149.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Runssmallisalsokindofweaklookingbutitissonicet...</td>
      <td>nice</td>
      <td>114</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-21</td>
      <td>2</td>
      <td>B005LERHD8A3APCBD7D7SW4Y</td>
      <td>1</td>
      <td>Runs small is also kind of weak looking but it...</td>
      <td>2014</td>
      <td>Runs small, is also kind of weak looking, but ...</td>
    </tr>
    <tr>
      <th>161609</th>
      <td>161609</td>
      <td>A0508575POGBTVG7AGWP</td>
      <td>B005LERHD8</td>
      <td>Puffpuff</td>
      <td>[0, 0]</td>
      <td>it's kinda thin and there's more gap space vis...</td>
      <td>4.0</td>
      <td>doesn't really look like the picture</td>
      <td>1357084800</td>
      <td>01 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>182.0</td>
      <td>Jewelry</td>
      <td>36.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>itskindathinandtheresmoregapspacevisibalwheret...</td>
      <td>doesntreallylooklikethepicture</td>
      <td>142</td>
      <td>30</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-02</td>
      <td>1</td>
      <td>B005LERHD8A0508575POGBTVG7AGWP</td>
      <td>1</td>
      <td>its kinda thin and theres more gap space visib...</td>
      <td>2013</td>
      <td>it's kinda thin and there's more gap space vis...</td>
    </tr>
    <tr>
      <th>161610</th>
      <td>161610</td>
      <td>A2Z0AHNVKZ2JPE</td>
      <td>B005LERHD8</td>
      <td>RAINY</td>
      <td>[0, 0]</td>
      <td>only .60 and wow what a good deal i love this ...</td>
      <td>5.0</td>
      <td>love love love it</td>
      <td>1389139200</td>
      <td>01 8, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>99.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>only60andwowwhatagooddealilovethisandsodoesthe...</td>
      <td>loveloveloveit</td>
      <td>72</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-08</td>
      <td>1</td>
      <td>B005LERHD8A2Z0AHNVKZ2JPE</td>
      <td>1</td>
      <td>only  and wow what a good deal i love this and...</td>
      <td>2014</td>
      <td>only .60 and wow what a good deal i love this ...</td>
    </tr>
    <tr>
      <th>161611</th>
      <td>161611</td>
      <td>A3T5YCAQ2VAPUQ</td>
      <td>B005LERHD8</td>
      <td>Raisa</td>
      <td>[0, 1]</td>
      <td>I bought this as a gift. it came early in the ...</td>
      <td>4.0</td>
      <td>nice</td>
      <td>1374192000</td>
      <td>07 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>373.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Iboughtthisasagiftitcameearlyinthemailwellpack...</td>
      <td>nice</td>
      <td>289</td>
      <td>4</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-19</td>
      <td>7</td>
      <td>B005LERHD8A3T5YCAQ2VAPUQ</td>
      <td>1</td>
      <td>I bought this as a gift it came early in the m...</td>
      <td>2013</td>
      <td>I bought this as a gift. it came early in the ...</td>
    </tr>
    <tr>
      <th>161612</th>
      <td>161612</td>
      <td>AGQ6TI2F0PJV5</td>
      <td>B005LERHD8</td>
      <td>Randolph the wolf "Skullbuster"</td>
      <td>[0, 0]</td>
      <td>very cute necklace . The chain doesn't have a ...</td>
      <td>3.0</td>
      <td>Pretty necklace</td>
      <td>1360195200</td>
      <td>02 7, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>137.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>verycutenecklaceThechaindoesnthaveaclaspwhichi...</td>
      <td>Prettynecklace</td>
      <td>103</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-07</td>
      <td>2</td>
      <td>B005LERHD8AGQ6TI2F0PJV5</td>
      <td>0</td>
      <td>very cute necklace  The chain doesnt have a cl...</td>
      <td>2013</td>
      <td>very cute necklace . The chain doesn't have a ...</td>
    </tr>
    <tr>
      <th>161613</th>
      <td>161613</td>
      <td>A8DU56URCL1IP</td>
      <td>B005LERHD8</td>
      <td>Randy A. Feagans "Randy Feagans"</td>
      <td>[0, 0]</td>
      <td>very pretty. It's an owl with jewels for eyes....</td>
      <td>5.0</td>
      <td>very pretty</td>
      <td>1387065600</td>
      <td>12 15, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>103.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>veryprettyItsanowlwithjewelsforeyesandjewelson...</td>
      <td>verypretty</td>
      <td>77</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-15</td>
      <td>12</td>
      <td>B005LERHD8A8DU56URCL1IP</td>
      <td>1</td>
      <td>very pretty Its an owl with jewels for eyes an...</td>
      <td>2013</td>
      <td>very pretty. It's an owl with jewels for eyes....</td>
    </tr>
    <tr>
      <th>161614</th>
      <td>161614</td>
      <td>AQ8EFEPCB7NHJ</td>
      <td>B005LERHD8</td>
      <td>Ray A Miller</td>
      <td>[0, 0]</td>
      <td>I think I paid around $3.00 for this necklace....</td>
      <td>4.0</td>
      <td>Good for the money</td>
      <td>1371168000</td>
      <td>06 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>152.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IthinkIpaidaround300forthisnecklaceIttookabitl...</td>
      <td>Goodforthemoney</td>
      <td>112</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-06-14</td>
      <td>6</td>
      <td>B005LERHD8AQ8EFEPCB7NHJ</td>
      <td>1</td>
      <td>I think I paid around  for this necklace It to...</td>
      <td>2013</td>
      <td>I think I paid around $3.00 for this necklace....</td>
    </tr>
    <tr>
      <th>161615</th>
      <td>161615</td>
      <td>AID0HI4KG7YUF</td>
      <td>B005LERHD8</td>
      <td>Ray</td>
      <td>[0, 0]</td>
      <td>This was actually a gift, but I have seen it w...</td>
      <td>5.0</td>
      <td>Perfect</td>
      <td>1361577600</td>
      <td>02 23, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>254.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThiswasactuallyagiftbutIhaveseenitwornanditsve...</td>
      <td>Perfect</td>
      <td>197</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-23</td>
      <td>2</td>
      <td>B005LERHD8AID0HI4KG7YUF</td>
      <td>1</td>
      <td>This was actually a gift but I have seen it wo...</td>
      <td>2013</td>
      <td>This was actually a gift, but I have seen it w...</td>
    </tr>
    <tr>
      <th>161616</th>
      <td>161616</td>
      <td>A215600781TUD1</td>
      <td>B005LERHD8</td>
      <td>Rebecca</td>
      <td>[0, 0]</td>
      <td>This is a cute little necklace.I ordered them ...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1396915200</td>
      <td>04 8, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>124.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisacutelittlenecklaceIorderedthemforalittl...</td>
      <td>Cute</td>
      <td>97</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-08</td>
      <td>4</td>
      <td>B005LERHD8A215600781TUD1</td>
      <td>1</td>
      <td>This is a cute little necklaceI ordered them f...</td>
      <td>2014</td>
      <td>This is a cute little necklace.I ordered them ...</td>
    </tr>
    <tr>
      <th>161617</th>
      <td>161617</td>
      <td>A1W0DROQTFUT8P</td>
      <td>B005LERHD8</td>
      <td>Rena Mae</td>
      <td>[0, 0]</td>
      <td>Had to close the rings holding the owl togethe...</td>
      <td>5.0</td>
      <td>Give a hoot</td>
      <td>1386288000</td>
      <td>12 6, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>112.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Hadtoclosetheringsholdingtheowltogetherstraigh...</td>
      <td>Giveahoot</td>
      <td>88</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-06</td>
      <td>12</td>
      <td>B005LERHD8A1W0DROQTFUT8P</td>
      <td>1</td>
      <td>Had to close the rings holding the owl togethe...</td>
      <td>2013</td>
      <td>Had to close the rings holding the owl togethe...</td>
    </tr>
    <tr>
      <th>161618</th>
      <td>161618</td>
      <td>A4OGAHOVIP594</td>
      <td>B005LERHD8</td>
      <td>Rhonda L Rust</td>
      <td>[0, 0]</td>
      <td>the rhinestones are plastic and not straight w...</td>
      <td>1.0</td>
      <td>extremely cheap</td>
      <td>1388102400</td>
      <td>12 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>131.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>therhinestonesareplasticandnotstraightwhenGLUE...</td>
      <td>extremelycheap</td>
      <td>104</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-27</td>
      <td>12</td>
      <td>B005LERHD8A4OGAHOVIP594</td>
      <td>0</td>
      <td>the rhinestones are plastic and not straight w...</td>
      <td>2013</td>
      <td>the rhinestones are plastic and not straight w...</td>
    </tr>
    <tr>
      <th>161619</th>
      <td>161619</td>
      <td>A1DGVCCQQYHGCE</td>
      <td>B005LERHD8</td>
      <td>rmjaxon</td>
      <td>[0, 0]</td>
      <td>I bought this as a present, and I am very impr...</td>
      <td>5.0</td>
      <td>Perfect!</td>
      <td>1357084800</td>
      <td>01 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>252.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IboughtthisasapresentandIamveryimpressedwithth...</td>
      <td>Perfect</td>
      <td>192</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-02</td>
      <td>1</td>
      <td>B005LERHD8A1DGVCCQQYHGCE</td>
      <td>1</td>
      <td>I bought this as a present and I am very impre...</td>
      <td>2013</td>
      <td>I bought this as a present, and I am very impr...</td>
    </tr>
    <tr>
      <th>161620</th>
      <td>161620</td>
      <td>A34NAKADPNT3HA</td>
      <td>B005LERHD8</td>
      <td>Roberta Wise</td>
      <td>[0, 0]</td>
      <td>Love this little pendant.  Ordered more than o...</td>
      <td>5.0</td>
      <td>DARLING OWL!</td>
      <td>1388448000</td>
      <td>12 31, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>158.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>LovethislittlependantOrderedmorethanonePlantog...</td>
      <td>DARLINGOWL</td>
      <td>117</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-31</td>
      <td>12</td>
      <td>B005LERHD8A34NAKADPNT3HA</td>
      <td>1</td>
      <td>Love this little pendant  Ordered more than on...</td>
      <td>2013</td>
      <td>Love this little pendant.  Ordered more than o...</td>
    </tr>
    <tr>
      <th>161621</th>
      <td>161621</td>
      <td>A4BA6M0HBU56A</td>
      <td>B005LERHD8</td>
      <td>Romeo</td>
      <td>[0, 0]</td>
      <td>very nice necklace. the owl is really nice and...</td>
      <td>5.0</td>
      <td>Great buy</td>
      <td>1365206400</td>
      <td>04 6, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>140.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>verynicenecklacetheowlisreallyniceandhasverygo...</td>
      <td>Greatbuy</td>
      <td>109</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-06</td>
      <td>4</td>
      <td>B005LERHD8A4BA6M0HBU56A</td>
      <td>1</td>
      <td>very nice necklace the owl is really nice and ...</td>
      <td>2013</td>
      <td>very nice necklace. the owl is really nice and...</td>
    </tr>
    <tr>
      <th>161622</th>
      <td>161622</td>
      <td>ARVKRZJQGOT0U</td>
      <td>B005LERHD8</td>
      <td>rosaury lopez</td>
      <td>[0, 0]</td>
      <td>I love this necklace!!! It's really pretty, a ...</td>
      <td>5.0</td>
      <td>Soooo cute!</td>
      <td>1357084800</td>
      <td>01 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>194.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IlovethisnecklaceItsreallyprettyagoodsizeIwish...</td>
      <td>Soooocute</td>
      <td>144</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-02</td>
      <td>1</td>
      <td>B005LERHD8ARVKRZJQGOT0U</td>
      <td>1</td>
      <td>I love this necklace Its really pretty a good ...</td>
      <td>2013</td>
      <td>I love this necklace!!! It's really pretty, a ...</td>
    </tr>
    <tr>
      <th>161623</th>
      <td>161623</td>
      <td>A3SETPJ4RE36OM</td>
      <td>B005LERHD8</td>
      <td>Rose Murphy "rm"</td>
      <td>[0, 0]</td>
      <td>Pretty in color and also quite large in size. ...</td>
      <td>5.0</td>
      <td>Owl necklace</td>
      <td>1383004800</td>
      <td>10 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>104.0</td>
      <td>Jewelry</td>
      <td>12.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>PrettyincolorandalsoquitelargeinsizeThecolorsa...</td>
      <td>Owlnecklace</td>
      <td>82</td>
      <td>11</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-29</td>
      <td>10</td>
      <td>B005LERHD8A3SETPJ4RE36OM</td>
      <td>1</td>
      <td>Pretty in color and also quite large in size T...</td>
      <td>2013</td>
      <td>Pretty in color and also quite large in size. ...</td>
    </tr>
    <tr>
      <th>161624</th>
      <td>161624</td>
      <td>A1VWQLRSPS4W0A</td>
      <td>B005LERHD8</td>
      <td>Rose N</td>
      <td>[1, 1]</td>
      <td>I couldn't believe the price so I wasn't expec...</td>
      <td>5.0</td>
      <td>Beautiful</td>
      <td>1359417600</td>
      <td>01 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>243.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>IcouldntbelievethepricesoIwasntexpectinganicep...</td>
      <td>Beautiful</td>
      <td>192</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-29</td>
      <td>1</td>
      <td>B005LERHD8A1VWQLRSPS4W0A</td>
      <td>1</td>
      <td>I couldnt believe the price so I wasnt expecti...</td>
      <td>2013</td>
      <td>I couldn't believe the price so I wasn't expec...</td>
    </tr>
    <tr>
      <th>161625</th>
      <td>161625</td>
      <td>A1E5P5P8MO41BJ</td>
      <td>B005LERHD8</td>
      <td>Sabrina Sutton</td>
      <td>[0, 0]</td>
      <td>I thought that the gems would be a little more...</td>
      <td>4.0</td>
      <td>Like it</td>
      <td>1381363200</td>
      <td>10 10, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>164.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Ithoughtthatthegemswouldbealittlemoresparklyth...</td>
      <td>Likeit</td>
      <td>131</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-10</td>
      <td>10</td>
      <td>B005LERHD8A1E5P5P8MO41BJ</td>
      <td>1</td>
      <td>I thought that the gems would be a little more...</td>
      <td>2013</td>
      <td>I thought that the gems would be a little more...</td>
    </tr>
    <tr>
      <th>161626</th>
      <td>161626</td>
      <td>A7OCJ1ZTDZXUZ</td>
      <td>B005LERHD8</td>
      <td>Sage Rowan</td>
      <td>[0, 0]</td>
      <td>I ordered this piece on 11/15 &amp; received it on...</td>
      <td>5.0</td>
      <td>Darling piece!!</td>
      <td>1354752000</td>
      <td>12 6, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>346.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Iorderedthispieceon1115receivediton126earliert...</td>
      <td>Darlingpiece</td>
      <td>260</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-06</td>
      <td>12</td>
      <td>B005LERHD8A7OCJ1ZTDZXUZ</td>
      <td>1</td>
      <td>I ordered this piece on   received it on  earl...</td>
      <td>2012</td>
      <td>I ordered this piece on 11/15 &amp; received it on...</td>
    </tr>
    <tr>
      <th>161627</th>
      <td>161627</td>
      <td>A2ZGFG276Z2IT2</td>
      <td>B005LERHD8</td>
      <td>Samantha Keen "Scowt23"</td>
      <td>[0, 0]</td>
      <td>Super cute and for the price you really can't ...</td>
      <td>5.0</td>
      <td>Super cute!</td>
      <td>1391731200</td>
      <td>02 7, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>SupercuteandforthepriceyoureallycantbeatitBoug...</td>
      <td>Supercute</td>
      <td>125</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-07</td>
      <td>2</td>
      <td>B005LERHD8A2ZGFG276Z2IT2</td>
      <td>1</td>
      <td>Super cute and for the price you really cant b...</td>
      <td>2014</td>
      <td>Super cute and for the price you really can't ...</td>
    </tr>
    <tr>
      <th>161628</th>
      <td>161628</td>
      <td>A1MA2ZT8YB9ZM1</td>
      <td>B005LERHD8</td>
      <td>sandra</td>
      <td>[0, 0]</td>
      <td>when i got this at the under one dollar price ...</td>
      <td>5.0</td>
      <td>cute</td>
      <td>1392076800</td>
      <td>02 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>120.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>whenigotthisattheunderonedollarpriceithoughtfo...</td>
      <td>cute</td>
      <td>93</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-11</td>
      <td>2</td>
      <td>B005LERHD8A1MA2ZT8YB9ZM1</td>
      <td>1</td>
      <td>when i got this at the under one dollar price ...</td>
      <td>2014</td>
      <td>when i got this at the under one dollar price ...</td>
    </tr>
    <tr>
      <th>161629</th>
      <td>161629</td>
      <td>AUFJRMYL1K9OZ</td>
      <td>B005LERHD8</td>
      <td>Sandy2035</td>
      <td>[0, 0]</td>
      <td>This is a very different piece of jewelry that...</td>
      <td>5.0</td>
      <td>very cool</td>
      <td>1388102400</td>
      <td>12 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>139.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Thisisaverydifferentpieceofjewelrythatlooksnic...</td>
      <td>verycool</td>
      <td>110</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-27</td>
      <td>12</td>
      <td>B005LERHD8AUFJRMYL1K9OZ</td>
      <td>1</td>
      <td>This is a very different piece of jewelry that...</td>
      <td>2013</td>
      <td>This is a very different piece of jewelry that...</td>
    </tr>
    <tr>
      <th>161630</th>
      <td>161630</td>
      <td>A218Y4UECWNS8L</td>
      <td>B005LERHD8</td>
      <td>Sandy</td>
      <td>[0, 0]</td>
      <td>I bought this as a gift for a friend and she l...</td>
      <td>5.0</td>
      <td>Great</td>
      <td>1364428800</td>
      <td>03 28, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>114.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Iboughtthisasagiftforafriendandsheloveditbette...</td>
      <td>Great</td>
      <td>87</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-28</td>
      <td>3</td>
      <td>B005LERHD8A218Y4UECWNS8L</td>
      <td>1</td>
      <td>I bought this as a gift for a friend and she l...</td>
      <td>2013</td>
      <td>I bought this as a gift for a friend and she l...</td>
    </tr>
    <tr>
      <th>161631</th>
      <td>161631</td>
      <td>AWXNJ01KHLU3B</td>
      <td>B005LERHD8</td>
      <td>Sannam</td>
      <td>[0, 0]</td>
      <td>This necklace is sooo cute. I pair it with my ...</td>
      <td>4.0</td>
      <td>I love this necklace!</td>
      <td>1364947200</td>
      <td>04 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>430.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ThisnecklaceissooocuteIpairitwithmydressesandi...</td>
      <td>Ilovethisnecklace</td>
      <td>340</td>
      <td>17</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-04-03</td>
      <td>4</td>
      <td>B005LERHD8AWXNJ01KHLU3B</td>
      <td>1</td>
      <td>This necklace is sooo cute I pair it with my d...</td>
      <td>2013</td>
      <td>This necklace is sooo cute. I pair it with my ...</td>
    </tr>
    <tr>
      <th>161632</th>
      <td>161632</td>
      <td>A2QKTD9UUF0PMW</td>
      <td>B005LERHD8</td>
      <td>sapphire116</td>
      <td>[0, 0]</td>
      <td>Bought a bunch of these to give as gifts at $0...</td>
      <td>4.0</td>
      <td>Don't Pay More than $1!</td>
      <td>1398816000</td>
      <td>04 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>319.0</td>
      <td>Jewelry</td>
      <td>23.0</td>
      <td>H</td>
      <td>H</td>
      <td>H</td>
      <td>Boughtabunchofthesetogiveasgiftsat085eachwithf...</td>
      <td>DontPayMorethan1</td>
      <td>241</td>
      <td>16</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-30</td>
      <td>4</td>
      <td>B005LERHD8A2QKTD9UUF0PMW</td>
      <td>1</td>
      <td>Bought a bunch of these to give as gifts at ea...</td>
      <td>2014</td>
      <td>Bought a bunch of these to give as gifts at $0...</td>
    </tr>
    <tr>
      <th>161633</th>
      <td>161633</td>
      <td>AL05PE3JZI8VN</td>
      <td>B005LERHD8</td>
      <td>SaraG2003</td>
      <td>[0, 0]</td>
      <td>Ordered a few of these as teacher gifts.  Defi...</td>
      <td>5.0</td>
      <td>Great teacher gifts!</td>
      <td>1353283200</td>
      <td>11 19, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>109.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>OrderedafewoftheseasteachergiftsDefinitelywort...</td>
      <td>Greatteachergifts</td>
      <td>85</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-19</td>
      <td>11</td>
      <td>B005LERHD8AL05PE3JZI8VN</td>
      <td>1</td>
      <td>Ordered a few of these as teacher gifts  Defin...</td>
      <td>2012</td>
      <td>Ordered a few of these as teacher gifts.  Defi...</td>
    </tr>
    <tr>
      <th>161634</th>
      <td>161634</td>
      <td>A3SNZPUALWI73A</td>
      <td>B005LERHD8</td>
      <td>sarah</td>
      <td>[0, 0]</td>
      <td>I like this necklace because I like owls  dd21...</td>
      <td>4.0</td>
      <td>compliments</td>
      <td>1395792000</td>
      <td>03 26, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlikethisnecklacebecauseIlikeowlsdd214thisonew...</td>
      <td>compliments</td>
      <td>126</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-26</td>
      <td>3</td>
      <td>B005LERHD8A3SNZPUALWI73A</td>
      <td>1</td>
      <td>I like this necklace because I like owls  dd t...</td>
      <td>2014</td>
      <td>I like this necklace because I like owls  dd21...</td>
    </tr>
    <tr>
      <th>161635</th>
      <td>161635</td>
      <td>A37P26N2AC8WKS</td>
      <td>B005LERHD8</td>
      <td>Sarah</td>
      <td>[0, 0]</td>
      <td>Very cute and for as big as they are they are ...</td>
      <td>5.0</td>
      <td>cute!</td>
      <td>1399334400</td>
      <td>05 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>94.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>VerycuteandforasbigastheyaretheyareverylightIw...</td>
      <td>cute</td>
      <td>72</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-06</td>
      <td>5</td>
      <td>B005LERHD8A37P26N2AC8WKS</td>
      <td>1</td>
      <td>Very cute and for as big as they are they are ...</td>
      <td>2014</td>
      <td>Very cute and for as big as they are they are ...</td>
    </tr>
    <tr>
      <th>161636</th>
      <td>161636</td>
      <td>A3S2LNW0HGKD7M</td>
      <td>B005LERHD8</td>
      <td>Sarah Mains</td>
      <td>[0, 0]</td>
      <td>Not the best construction but what to be expec...</td>
      <td>5.0</td>
      <td>Nice size and pretty</td>
      <td>1391472000</td>
      <td>02 4, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>109.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Notthebestconstructionbutwhattobeexpectedatthi...</td>
      <td>Nicesizeandpretty</td>
      <td>87</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-04</td>
      <td>2</td>
      <td>B005LERHD8A3S2LNW0HGKD7M</td>
      <td>1</td>
      <td>Not the best construction but what to be expec...</td>
      <td>2014</td>
      <td>Not the best construction but what to be expec...</td>
    </tr>
    <tr>
      <th>161637</th>
      <td>161637</td>
      <td>A34QZXG3D5RI5C</td>
      <td>B005LERHD8</td>
      <td>Saunawong</td>
      <td>[0, 0]</td>
      <td>It's look pretty and the price is cheap , it i...</td>
      <td>4.0</td>
      <td>Pretty</td>
      <td>1388534400</td>
      <td>01 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>98.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Itslookprettyandthepriceischeapitisgoodgiftfor...</td>
      <td>Pretty</td>
      <td>73</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-01</td>
      <td>1</td>
      <td>B005LERHD8A34QZXG3D5RI5C</td>
      <td>1</td>
      <td>Its look pretty and the price is cheap  it is ...</td>
      <td>2014</td>
      <td>It's look pretty and the price is cheap , it i...</td>
    </tr>
    <tr>
      <th>161638</th>
      <td>161638</td>
      <td>A3303E6ZH9T5SM</td>
      <td>B005LERHD8</td>
      <td>Savannah Hyde</td>
      <td>[0, 0]</td>
      <td>Chain was a bit shorter than I expected, and t...</td>
      <td>3.0</td>
      <td>Short chain</td>
      <td>1395878400</td>
      <td>03 27, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>144.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ChainwasabitshorterthanIexpectedandthependantf...</td>
      <td>Shortchain</td>
      <td>113</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-27</td>
      <td>3</td>
      <td>B005LERHD8A3303E6ZH9T5SM</td>
      <td>0</td>
      <td>Chain was a bit shorter than I expected and th...</td>
      <td>2014</td>
      <td>Chain was a bit shorter than I expected, and t...</td>
    </tr>
    <tr>
      <th>161639</th>
      <td>161639</td>
      <td>A16X8MOL9BFX1R</td>
      <td>B005LERHD8</td>
      <td>savvy jacox</td>
      <td>[1, 1]</td>
      <td>I was sad that the chain broke but other than ...</td>
      <td>4.0</td>
      <td>ok</td>
      <td>1386547200</td>
      <td>12 9, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>106.0</td>
      <td>Jewelry</td>
      <td>2.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Iwassadthatthechainbrokebutotherthanthatitsrea...</td>
      <td>ok</td>
      <td>84</td>
      <td>2</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-09</td>
      <td>12</td>
      <td>B005LERHD8A16X8MOL9BFX1R</td>
      <td>1</td>
      <td>I was sad that the chain broke but other than ...</td>
      <td>2013</td>
      <td>I was sad that the chain broke but other than ...</td>
    </tr>
    <tr>
      <th>161640</th>
      <td>161640</td>
      <td>A82HDHO6IJWRE</td>
      <td>B005LERHD8</td>
      <td>Savy</td>
      <td>[1, 1]</td>
      <td>I bought this item for my sister in law and sh...</td>
      <td>5.0</td>
      <td>perfect!</td>
      <td>1376611200</td>
      <td>08 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>184.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iboughtthisitemformysisterinlawandsheabsolutel...</td>
      <td>perfect</td>
      <td>145</td>
      <td>7</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-16</td>
      <td>8</td>
      <td>B005LERHD8A82HDHO6IJWRE</td>
      <td>1</td>
      <td>I bought this item for my sister in law and sh...</td>
      <td>2013</td>
      <td>I bought this item for my sister in law and sh...</td>
    </tr>
    <tr>
      <th>161641</th>
      <td>161641</td>
      <td>A1P5VCJVV6JA0Z</td>
      <td>B005LERHD8</td>
      <td>S. Capel</td>
      <td>[0, 0]</td>
      <td>The quality isn't good, but for the price you ...</td>
      <td>4.0</td>
      <td>Can't Complain for the Price</td>
      <td>1361836800</td>
      <td>02 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>132.0</td>
      <td>Jewelry</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Thequalityisntgoodbutforthepriceyoucantcomplai...</td>
      <td>CantComplainforthePrice</td>
      <td>101</td>
      <td>23</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-26</td>
      <td>2</td>
      <td>B005LERHD8A1P5VCJVV6JA0Z</td>
      <td>1</td>
      <td>The quality isnt good but for the price you ca...</td>
      <td>2013</td>
      <td>The quality isn't good, but for the price you ...</td>
    </tr>
    <tr>
      <th>161642</th>
      <td>161642</td>
      <td>A37UK5P85F0OC</td>
      <td>B005LERHD8</td>
      <td>selen</td>
      <td>[1, 1]</td>
      <td>very very good for the price. its bigger than ...</td>
      <td>5.0</td>
      <td>Love it. cheapest and cutest</td>
      <td>1388102400</td>
      <td>12 27, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>116.0</td>
      <td>Jewelry</td>
      <td>28.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>veryverygoodforthepriceitsbiggerthanitseemsIwi...</td>
      <td>Loveitcheapestandcutest</td>
      <td>91</td>
      <td>23</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-27</td>
      <td>12</td>
      <td>B005LERHD8A37UK5P85F0OC</td>
      <td>1</td>
      <td>very very good for the price its bigger than i...</td>
      <td>2013</td>
      <td>very very good for the price. its bigger than ...</td>
    </tr>
    <tr>
      <th>161643</th>
      <td>161643</td>
      <td>A37MOE0DXWE40R</td>
      <td>B005LERHD8</td>
      <td>Shannon Cahill</td>
      <td>[0, 0]</td>
      <td>Loves owls. So this product is cute. It is not...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1389398400</td>
      <td>01 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>129.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>LovesowlsSothisproductiscuteItisnotmadeofthebe...</td>
      <td>Cute</td>
      <td>99</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-11</td>
      <td>1</td>
      <td>B005LERHD8A37MOE0DXWE40R</td>
      <td>1</td>
      <td>Loves owls So this product is cute It is not m...</td>
      <td>2014</td>
      <td>Loves owls. So this product is cute. It is not...</td>
    </tr>
    <tr>
      <th>161644</th>
      <td>161644</td>
      <td>A10H6RT7OL6LRW</td>
      <td>B005LERHD8</td>
      <td>Sharon</td>
      <td>[0, 0]</td>
      <td>Cute but the stones are very sharp  lucky im h...</td>
      <td>1.0</td>
      <td>could be i got bad one</td>
      <td>1396051200</td>
      <td>03 29, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>136.0</td>
      <td>Jewelry</td>
      <td>22.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Cutebutthestonesareverysharpluckyimhandyneeded...</td>
      <td>couldbeigotbadone</td>
      <td>108</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-29</td>
      <td>3</td>
      <td>B005LERHD8A10H6RT7OL6LRW</td>
      <td>0</td>
      <td>Cute but the stones are very sharp  lucky im h...</td>
      <td>2014</td>
      <td>Cute but the stones are very sharp  lucky im h...</td>
    </tr>
    <tr>
      <th>161645</th>
      <td>161645</td>
      <td>A1JI7PVMVR03YE</td>
      <td>B005LERHD8</td>
      <td>Sharon M.T.</td>
      <td>[1, 1]</td>
      <td>This is a fantastic deal and the owl is so cut...</td>
      <td>4.0</td>
      <td>Cute!</td>
      <td>1393718400</td>
      <td>03 2, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>149.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisafantasticdealandtheowlissocuteIlovethel...</td>
      <td>Cute</td>
      <td>112</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-02</td>
      <td>3</td>
      <td>B005LERHD8A1JI7PVMVR03YE</td>
      <td>1</td>
      <td>This is a fantastic deal and the owl is so cut...</td>
      <td>2014</td>
      <td>This is a fantastic deal and the owl is so cut...</td>
    </tr>
    <tr>
      <th>161646</th>
      <td>161646</td>
      <td>A1VKH3IS099L3E</td>
      <td>B005LERHD8</td>
      <td>Shasara</td>
      <td>[0, 0]</td>
      <td>I bought this because it was so inexpensive an...</td>
      <td>5.0</td>
      <td>Absolutely adorable!</td>
      <td>1356652800</td>
      <td>12 28, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>235.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>IboughtthisbecauseitwassoinexpensiveandIfigure...</td>
      <td>Absolutelyadorable</td>
      <td>180</td>
      <td>18</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-28</td>
      <td>12</td>
      <td>B005LERHD8A1VKH3IS099L3E</td>
      <td>1</td>
      <td>I bought this because it was so inexpensive an...</td>
      <td>2012</td>
      <td>I bought this because it was so inexpensive an...</td>
    </tr>
    <tr>
      <th>161647</th>
      <td>161647</td>
      <td>A1MLYGLBB5JYYA</td>
      <td>B005LERHD8</td>
      <td>Shelby Nicole</td>
      <td>[0, 0]</td>
      <td>Came just as pictured. Adorable! I love it. If...</td>
      <td>5.0</td>
      <td>Great!</td>
      <td>1390348800</td>
      <td>01 22, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>156.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>CamejustaspicturedAdorableIloveitIfyourelookin...</td>
      <td>Great</td>
      <td>120</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-22</td>
      <td>1</td>
      <td>B005LERHD8A1MLYGLBB5JYYA</td>
      <td>1</td>
      <td>Came just as pictured Adorable I love it If yo...</td>
      <td>2014</td>
      <td>Came just as pictured. Adorable! I love it. If...</td>
    </tr>
    <tr>
      <th>161648</th>
      <td>161648</td>
      <td>AGOR9P22JLV8H</td>
      <td>B005LERHD8</td>
      <td>Shoes!!!</td>
      <td>[0, 1]</td>
      <td>I bought this and then found the same one with...</td>
      <td>3.0</td>
      <td>Different seller offers earring too</td>
      <td>1381881600</td>
      <td>10 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0.000000</td>
      <td>281.0</td>
      <td>Jewelry</td>
      <td>35.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Iboughtthisandthenfoundthesameonewithmatchinge...</td>
      <td>Differentselleroffersearringtoo</td>
      <td>222</td>
      <td>31</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-16</td>
      <td>10</td>
      <td>B005LERHD8AGOR9P22JLV8H</td>
      <td>0</td>
      <td>I bought this and then found the same one with...</td>
      <td>2013</td>
      <td>I bought this and then found the same one with...</td>
    </tr>
    <tr>
      <th>161649</th>
      <td>161649</td>
      <td>A237M100LDW445</td>
      <td>B005LERHD8</td>
      <td>Simply ME</td>
      <td>[0, 0]</td>
      <td>For the money you can not go wrong if you love...</td>
      <td>5.0</td>
      <td>very colorful</td>
      <td>1392940800</td>
      <td>02 21, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>122.0</td>
      <td>Jewelry</td>
      <td>13.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ForthemoneyyoucannotgowrongifyouloveowlsIwasha...</td>
      <td>verycolorful</td>
      <td>92</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-21</td>
      <td>2</td>
      <td>B005LERHD8A237M100LDW445</td>
      <td>1</td>
      <td>For the money you can not go wrong if you love...</td>
      <td>2014</td>
      <td>For the money you can not go wrong if you love...</td>
    </tr>
    <tr>
      <th>161650</th>
      <td>161650</td>
      <td>A2UF3D96TBYYV3</td>
      <td>B005LERHD8</td>
      <td>Sinister Serenade "Sweet Nightmares"</td>
      <td>[1, 2]</td>
      <td>I love this necklace! It arrived in perfect co...</td>
      <td>5.0</td>
      <td>GORGEOUS!</td>
      <td>1379376000</td>
      <td>09 17, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0.333333</td>
      <td>567.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>IlovethisnecklaceItarrivedinperfectconditionan...</td>
      <td>GORGEOUS</td>
      <td>433</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-17</td>
      <td>9</td>
      <td>B005LERHD8A2UF3D96TBYYV3</td>
      <td>1</td>
      <td>I love this necklace It arrived in perfect con...</td>
      <td>2013</td>
      <td>I love this necklace! It arrived in perfect co...</td>
    </tr>
    <tr>
      <th>161651</th>
      <td>161651</td>
      <td>A2OBAX0SBTE86K</td>
      <td>B005LERHD8</td>
      <td>skfit</td>
      <td>[2, 3]</td>
      <td>I bought 3 of the owl charm necklace, 1 for me...</td>
      <td>4.0</td>
      <td>Cute necklace...</td>
      <td>1357689600</td>
      <td>01 9, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>777.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>Ibought3oftheowlcharmnecklace1forme1forbothofm...</td>
      <td>Cutenecklace</td>
      <td>561</td>
      <td>12</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-09</td>
      <td>1</td>
      <td>B005LERHD8A2OBAX0SBTE86K</td>
      <td>1</td>
      <td>I bought  of the owl charm necklace  for me   ...</td>
      <td>2013</td>
      <td>I bought 3 of the owl charm necklace, 1 for me...</td>
    </tr>
    <tr>
      <th>161652</th>
      <td>161652</td>
      <td>A30H8ACW807Q2F</td>
      <td>B005LERHD8</td>
      <td>S-N-D "Layford"</td>
      <td>[0, 0]</td>
      <td>Don't know how the seller could do it. For mer...</td>
      <td>5.0</td>
      <td>Good and very inexpensive.</td>
      <td>1387152000</td>
      <td>12 16, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>239.0</td>
      <td>Jewelry</td>
      <td>26.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>DontknowhowthesellercoulddoitFormerely085andsh...</td>
      <td>Goodandveryinexpensive</td>
      <td>184</td>
      <td>22</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-16</td>
      <td>12</td>
      <td>B005LERHD8A30H8ACW807Q2F</td>
      <td>1</td>
      <td>Dont know how the seller could do it For merel...</td>
      <td>2013</td>
      <td>Don't know how the seller could do it. For mer...</td>
    </tr>
    <tr>
      <th>161653</th>
      <td>161653</td>
      <td>A3BRKYSUHFWSW7</td>
      <td>B005LERHD8</td>
      <td>Sophie M. Matera "SOPHIE (SOPH_EYE)"</td>
      <td>[0, 0]</td>
      <td>Sturdy chain and cute owl design. Theres no cl...</td>
      <td>3.0</td>
      <td>Good for the Price</td>
      <td>1358726400</td>
      <td>01 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>100.0</td>
      <td>Jewelry</td>
      <td>18.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>SturdychainandcuteowldesignTheresnoclaspforthe...</td>
      <td>GoodforthePrice</td>
      <td>79</td>
      <td>15</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-21</td>
      <td>1</td>
      <td>B005LERHD8A3BRKYSUHFWSW7</td>
      <td>0</td>
      <td>Sturdy chain and cute owl design Theres no cla...</td>
      <td>2013</td>
      <td>Sturdy chain and cute owl design. Theres no cl...</td>
    </tr>
    <tr>
      <th>161654</th>
      <td>161654</td>
      <td>A1TGX98768Z3Y2</td>
      <td>B005LERHD8</td>
      <td>SouthernJill</td>
      <td>[0, 0]</td>
      <td>I may be a little old for this. It's cutesy. I...</td>
      <td>3.0</td>
      <td>Cute</td>
      <td>1368921600</td>
      <td>05 19, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>204.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ImaybealittleoldforthisItscutesyItsIceLooksali...</td>
      <td>Cute</td>
      <td>150</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-19</td>
      <td>5</td>
      <td>B005LERHD8A1TGX98768Z3Y2</td>
      <td>0</td>
      <td>I may be a little old for this Its cutesy Its ...</td>
      <td>2013</td>
      <td>I may be a little old for this. It's cutesy. I...</td>
    </tr>
    <tr>
      <th>161655</th>
      <td>161655</td>
      <td>ADX7OJDLEUL6R</td>
      <td>B005LERHD8</td>
      <td>Sparx</td>
      <td>[0, 0]</td>
      <td>cheaply made and so light i feel that I am goi...</td>
      <td>2.0</td>
      <td>pretty but</td>
      <td>1369872000</td>
      <td>05 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>85.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>cheaplymadeandsolightifeelthatIamgoingtobreaki...</td>
      <td>prettybut</td>
      <td>65</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-30</td>
      <td>5</td>
      <td>B005LERHD8ADX7OJDLEUL6R</td>
      <td>0</td>
      <td>cheaply made and so light i feel that I am goi...</td>
      <td>2013</td>
      <td>cheaply made and so light i feel that I am goi...</td>
    </tr>
    <tr>
      <th>161656</th>
      <td>161656</td>
      <td>A1THSBWV04YAIK</td>
      <td>B005LERHD8</td>
      <td>Speechless</td>
      <td>[0, 0]</td>
      <td>The owl is smaller than I expected, but I was ...</td>
      <td>5.0</td>
      <td>Love it!</td>
      <td>1381708800</td>
      <td>10 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>612.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>TheowlissmallerthanIexpectedbutIwashappyaboutt...</td>
      <td>Loveit</td>
      <td>457</td>
      <td>6</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-14</td>
      <td>10</td>
      <td>B005LERHD8A1THSBWV04YAIK</td>
      <td>1</td>
      <td>The owl is smaller than I expected but I was h...</td>
      <td>2013</td>
      <td>The owl is smaller than I expected, but I was ...</td>
    </tr>
    <tr>
      <th>161657</th>
      <td>161657</td>
      <td>AHCI6ZIQY1PZQ</td>
      <td>B005LERHD8</td>
      <td>S. Swist</td>
      <td>[0, 0]</td>
      <td>purchased for a friend, has a bit of weight to...</td>
      <td>5.0</td>
      <td>bronze owl necklace</td>
      <td>1377475200</td>
      <td>08 26, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>106.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>purchasedforafriendhasabitofweighttoitsoyoukno...</td>
      <td>bronzeowlnecklace</td>
      <td>82</td>
      <td>17</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-26</td>
      <td>8</td>
      <td>B005LERHD8AHCI6ZIQY1PZQ</td>
      <td>1</td>
      <td>purchased for a friend has a bit of weight to ...</td>
      <td>2013</td>
      <td>purchased for a friend, has a bit of weight to...</td>
    </tr>
    <tr>
      <th>161658</th>
      <td>161658</td>
      <td>A3V1N9K3BHHGJY</td>
      <td>B005LERHD8</td>
      <td>Stephanie</td>
      <td>[0, 0]</td>
      <td>Really like this necklace but swap out the cha...</td>
      <td>3.0</td>
      <td>Get a new chain!</td>
      <td>1388361600</td>
      <td>12 30, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>151.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Reallylikethisnecklacebutswapoutthechainifyoub...</td>
      <td>Getanewchain</td>
      <td>116</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-30</td>
      <td>12</td>
      <td>B005LERHD8A3V1N9K3BHHGJY</td>
      <td>0</td>
      <td>Really like this necklace but swap out the cha...</td>
      <td>2013</td>
      <td>Really like this necklace but swap out the cha...</td>
    </tr>
    <tr>
      <th>161659</th>
      <td>161659</td>
      <td>A1Q4V5G4S00Q7M</td>
      <td>B005LERHD8</td>
      <td>Stephanie</td>
      <td>[12, 13]</td>
      <td>This is exactly as it looks and big and pretty...</td>
      <td>5.0</td>
      <td>LOVE</td>
      <td>1376956800</td>
      <td>08 20, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThisisexactlyasitlooksandbigandprettyandniceIt...</td>
      <td>LOVE</td>
      <td>125</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-08-20</td>
      <td>8</td>
      <td>B005LERHD8A1Q4V5G4S00Q7M</td>
      <td>1</td>
      <td>This is exactly as it looks and big and pretty...</td>
      <td>2013</td>
      <td>This is exactly as it looks and big and pretty...</td>
    </tr>
    <tr>
      <th>161660</th>
      <td>161660</td>
      <td>A2Z2PB561J4NI7</td>
      <td>B005LERHD8</td>
      <td>Stephanie Sherwood</td>
      <td>[0, 0]</td>
      <td>Its an amazing necklace for the price. If you ...</td>
      <td>5.0</td>
      <td>Love it!</td>
      <td>1396742400</td>
      <td>04 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>122.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ItsanamazingnecklaceforthepriceIfyouareanowlco...</td>
      <td>Loveit</td>
      <td>97</td>
      <td>6</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-04-06</td>
      <td>4</td>
      <td>B005LERHD8A2Z2PB561J4NI7</td>
      <td>1</td>
      <td>Its an amazing necklace for the price If you a...</td>
      <td>2014</td>
      <td>Its an amazing necklace for the price. If you ...</td>
    </tr>
    <tr>
      <th>161661</th>
      <td>161661</td>
      <td>A29Q46ODD8TOLZ</td>
      <td>B005LERHD8</td>
      <td>Steph L Jones "Steph"</td>
      <td>[0, 0]</td>
      <td>This owl arrived exactly as described. It is a...</td>
      <td>5.0</td>
      <td>Great, fun piece of costume jewelry.</td>
      <td>1354838400</td>
      <td>12 7, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>211.0</td>
      <td>Jewelry</td>
      <td>36.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>ThisowlarrivedexactlyasdescribedItisaveryfunpi...</td>
      <td>Greatfunpieceofcostumejewelry</td>
      <td>167</td>
      <td>29</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-07</td>
      <td>12</td>
      <td>B005LERHD8A29Q46ODD8TOLZ</td>
      <td>1</td>
      <td>This owl arrived exactly as described It is a ...</td>
      <td>2012</td>
      <td>This owl arrived exactly as described. It is a...</td>
    </tr>
    <tr>
      <th>161662</th>
      <td>161662</td>
      <td>A25Y9I1WPFM63X</td>
      <td>B005LERHD8</td>
      <td>Steven</td>
      <td>[0, 0]</td>
      <td>wayyyy bigger than i thought. the product seem...</td>
      <td>2.0</td>
      <td>eh</td>
      <td>1361404800</td>
      <td>02 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>133.0</td>
      <td>Jewelry</td>
      <td>2.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>wayyyybiggerthanithoughttheproductseemsnicebut...</td>
      <td>eh</td>
      <td>107</td>
      <td>2</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-21</td>
      <td>2</td>
      <td>B005LERHD8A25Y9I1WPFM63X</td>
      <td>0</td>
      <td>wayyyy bigger than i thought the product seems...</td>
      <td>2013</td>
      <td>wayyyy bigger than i thought. the product seem...</td>
    </tr>
    <tr>
      <th>161663</th>
      <td>161663</td>
      <td>A24WKOS7B5SLVA</td>
      <td>B005LERHD8</td>
      <td>Stucci</td>
      <td>[0, 0]</td>
      <td>This is a very cute and lovely necklace.  It i...</td>
      <td>4.0</td>
      <td>Very cute</td>
      <td>1359676800</td>
      <td>02 1, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>257.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThisisaverycuteandlovelynecklaceItismoreofabra...</td>
      <td>Verycute</td>
      <td>194</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-01</td>
      <td>2</td>
      <td>B005LERHD8A24WKOS7B5SLVA</td>
      <td>1</td>
      <td>This is a very cute and lovely necklace  It is...</td>
      <td>2013</td>
      <td>This is a very cute and lovely necklace.  It i...</td>
    </tr>
    <tr>
      <th>161664</th>
      <td>161664</td>
      <td>A2DQV7OZ9YIWWK</td>
      <td>B005LERHD8</td>
      <td>Susan Bailey</td>
      <td>[0, 0]</td>
      <td>the owl is very nice, it just took a long time...</td>
      <td>4.0</td>
      <td>Nice</td>
      <td>1392595200</td>
      <td>02 17, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>95.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>theowlisveryniceitjusttookalongtimetoshipwhich...</td>
      <td>Nice</td>
      <td>72</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-17</td>
      <td>2</td>
      <td>B005LERHD8A2DQV7OZ9YIWWK</td>
      <td>1</td>
      <td>the owl is very nice it just took a long time ...</td>
      <td>2014</td>
      <td>the owl is very nice, it just took a long time...</td>
    </tr>
    <tr>
      <th>161665</th>
      <td>161665</td>
      <td>ACZ795QWHGPF7</td>
      <td>B005LERHD8</td>
      <td>Susan C Wilson</td>
      <td>[0, 0]</td>
      <td>Owls are so fun and this looks great with my v...</td>
      <td>5.0</td>
      <td>Really darling necklace!</td>
      <td>1369094400</td>
      <td>05 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>142.0</td>
      <td>Jewelry</td>
      <td>24.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>Owlsaresofunandthislooksgreatwithmyvintagedeni...</td>
      <td>Reallydarlingnecklace</td>
      <td>113</td>
      <td>21</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-21</td>
      <td>5</td>
      <td>B005LERHD8ACZ795QWHGPF7</td>
      <td>1</td>
      <td>Owls are so fun and this looks great with my v...</td>
      <td>2013</td>
      <td>Owls are so fun and this looks great with my v...</td>
    </tr>
    <tr>
      <th>161666</th>
      <td>161666</td>
      <td>A153CXP3E8EGIP</td>
      <td>B005LERHD8</td>
      <td>Susanne Brase "seltenonline"</td>
      <td>[1, 1]</td>
      <td>The best u get for this price, but u have to w...</td>
      <td>2.0</td>
      <td>so so</td>
      <td>1355097600</td>
      <td>12 10, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>123.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Thebestugetforthispricebutuhavetowaitforalongl...</td>
      <td>soso</td>
      <td>95</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-10</td>
      <td>12</td>
      <td>B005LERHD8A153CXP3E8EGIP</td>
      <td>0</td>
      <td>The best u get for this price but u have to wa...</td>
      <td>2012</td>
      <td>The best u get for this price, but u have to w...</td>
    </tr>
    <tr>
      <th>161667</th>
      <td>161667</td>
      <td>AA3JO5MX1VAUF</td>
      <td>B005LERHD8</td>
      <td>Susan Sarver</td>
      <td>[0, 0]</td>
      <td>I'm giving the Owl Necklace to my niece for Ch...</td>
      <td>5.0</td>
      <td>Christmas</td>
      <td>1378512000</td>
      <td>09 7, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>109.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ImgivingtheOwlNecklacetomynieceforChristmasshe...</td>
      <td>Christmas</td>
      <td>85</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-07</td>
      <td>9</td>
      <td>B005LERHD8AA3JO5MX1VAUF</td>
      <td>1</td>
      <td>Im giving the Owl Necklace to my niece for Chr...</td>
      <td>2013</td>
      <td>I'm giving the Owl Necklace to my niece for Ch...</td>
    </tr>
    <tr>
      <th>161668</th>
      <td>161668</td>
      <td>A1TPTRMYHOFPES</td>
      <td>B005LERHD8</td>
      <td>Susie Fair "fairlady"</td>
      <td>[0, 0]</td>
      <td>The metal on this is very thin and I am not su...</td>
      <td>4.0</td>
      <td>Thin Metal</td>
      <td>1382572800</td>
      <td>10 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>390.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>ThemetalonthisisverythinandIamnotsurehowlongit...</td>
      <td>ThinMetal</td>
      <td>292</td>
      <td>9</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-24</td>
      <td>10</td>
      <td>B005LERHD8A1TPTRMYHOFPES</td>
      <td>1</td>
      <td>The metal on this is very thin and I am not su...</td>
      <td>2013</td>
      <td>The metal on this is very thin and I am not su...</td>
    </tr>
    <tr>
      <th>161669</th>
      <td>161669</td>
      <td>A2XL8GPL563XRK</td>
      <td>B005LERHD8</td>
      <td>SweetJ</td>
      <td>[0, 0]</td>
      <td>Love it so cute! Tones of compliments on it. I...</td>
      <td>5.0</td>
      <td>Bronze owl</td>
      <td>1385942400</td>
      <td>12 2, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>150.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>LoveitsocuteTonesofcomplimentsonitItgoesgreatw...</td>
      <td>Bronzeowl</td>
      <td>116</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-02</td>
      <td>12</td>
      <td>B005LERHD8A2XL8GPL563XRK</td>
      <td>1</td>
      <td>Love it so cute Tones of compliments on it It ...</td>
      <td>2013</td>
      <td>Love it so cute! Tones of compliments on it. I...</td>
    </tr>
    <tr>
      <th>161670</th>
      <td>161670</td>
      <td>A1OIP4HU97J11</td>
      <td>B005LERHD8</td>
      <td>sweet pea "peachy"</td>
      <td>[0, 0]</td>
      <td>received this a little early but i love my nec...</td>
      <td>5.0</td>
      <td>vintage necklace</td>
      <td>1390521600</td>
      <td>01 24, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>165.0</td>
      <td>Jewelry</td>
      <td>16.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>receivedthisalittleearlybutilovemynecklacevery...</td>
      <td>vintagenecklace</td>
      <td>133</td>
      <td>15</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-24</td>
      <td>1</td>
      <td>B005LERHD8A1OIP4HU97J11</td>
      <td>1</td>
      <td>received this a little early but i love my nec...</td>
      <td>2014</td>
      <td>received this a little early but i love my nec...</td>
    </tr>
    <tr>
      <th>161671</th>
      <td>161671</td>
      <td>A3TYCQ2Y083FR2</td>
      <td>B005LERHD8</td>
      <td>S. Whipp</td>
      <td>[0, 0]</td>
      <td>So cute!  I have one good hand &amp; hate claps! (...</td>
      <td>5.0</td>
      <td>Hot &amp; Spiffy!!</td>
      <td>1374624000</td>
      <td>07 24, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>302.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>SocuteIhaveonegoodhandhateclapsTheygethunginst...</td>
      <td>HotSpiffy</td>
      <td>219</td>
      <td>9</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-24</td>
      <td>7</td>
      <td>B005LERHD8A3TYCQ2Y083FR2</td>
      <td>1</td>
      <td>So cute  I have one good hand  hate claps They...</td>
      <td>2013</td>
      <td>So cute!  I have one good hand &amp; hate claps! (...</td>
    </tr>
    <tr>
      <th>161672</th>
      <td>161672</td>
      <td>AY6I0YNS3QAMM</td>
      <td>B005LERHD8</td>
      <td>sylviamae88</td>
      <td>[0, 0]</td>
      <td>Very cute and my mom loved it! I got us both o...</td>
      <td>5.0</td>
      <td>Very cute!</td>
      <td>1359849600</td>
      <td>02 3, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>214.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>VerycuteandmymomloveditIgotusbothoneandthecolo...</td>
      <td>Verycute</td>
      <td>166</td>
      <td>8</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-03</td>
      <td>2</td>
      <td>B005LERHD8AY6I0YNS3QAMM</td>
      <td>1</td>
      <td>Very cute and my mom loved it I got us both on...</td>
      <td>2013</td>
      <td>Very cute and my mom loved it! I got us both o...</td>
    </tr>
    <tr>
      <th>161673</th>
      <td>161673</td>
      <td>A24QJT338UJ7PV</td>
      <td>B005LERHD8</td>
      <td>Tabitha Woods</td>
      <td>[0, 0]</td>
      <td>Great item!  I get tons of compliments and hav...</td>
      <td>5.0</td>
      <td>LOVE!</td>
      <td>1402272000</td>
      <td>06 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>268.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>GreatitemIgettonsofcomplimentsandhavehadsomany...</td>
      <td>LOVE</td>
      <td>206</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-09</td>
      <td>6</td>
      <td>B005LERHD8A24QJT338UJ7PV</td>
      <td>1</td>
      <td>Great item  I get tons of compliments and have...</td>
      <td>2014</td>
      <td>Great item!  I get tons of compliments and hav...</td>
    </tr>
    <tr>
      <th>161674</th>
      <td>161674</td>
      <td>A1ZCH4CLZDZCMH</td>
      <td>B005LERHD8</td>
      <td>taks</td>
      <td>[0, 0]</td>
      <td>Cute Costume jewelry. bought it for my pre-tee...</td>
      <td>4.0</td>
      <td>cute</td>
      <td>1393891200</td>
      <td>03 4, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>121.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>CuteCostumejewelryboughtitformypreteendaughter...</td>
      <td>cute</td>
      <td>94</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-04</td>
      <td>3</td>
      <td>B005LERHD8A1ZCH4CLZDZCMH</td>
      <td>1</td>
      <td>Cute Costume jewelry bought it for my preteen ...</td>
      <td>2014</td>
      <td>Cute Costume jewelry. bought it for my pre-tee...</td>
    </tr>
    <tr>
      <th>161675</th>
      <td>161675</td>
      <td>A1IUADOR80DZTO</td>
      <td>B005LERHD8</td>
      <td>terilynn fenderson</td>
      <td>[0, 0]</td>
      <td>Stones and owl were different colors than show...</td>
      <td>5.0</td>
      <td>so cute!</td>
      <td>1383523200</td>
      <td>11 4, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>227.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Stonesandowlweredifferentcolorsthanshownbuttha...</td>
      <td>socute</td>
      <td>176</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-04</td>
      <td>11</td>
      <td>B005LERHD8A1IUADOR80DZTO</td>
      <td>1</td>
      <td>Stones and owl were different colors than show...</td>
      <td>2013</td>
      <td>Stones and owl were different colors than show...</td>
    </tr>
    <tr>
      <th>161676</th>
      <td>161676</td>
      <td>A202WUJ5CPIJYA</td>
      <td>B005LERHD8</td>
      <td>Terry Dean</td>
      <td>[0, 0]</td>
      <td>This is well built and bright.  It seems a bit...</td>
      <td>5.0</td>
      <td>A lot af necklace for the money</td>
      <td>1400371200</td>
      <td>05 18, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>153.0</td>
      <td>Jewelry</td>
      <td>31.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThisiswellbuiltandbrightItseemsabitbigforsomep...</td>
      <td>Alotafnecklaceforthemoney</td>
      <td>116</td>
      <td>25</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-18</td>
      <td>5</td>
      <td>B005LERHD8A202WUJ5CPIJYA</td>
      <td>1</td>
      <td>This is well built and bright  It seems a bit ...</td>
      <td>2014</td>
      <td>This is well built and bright.  It seems a bit...</td>
    </tr>
    <tr>
      <th>161677</th>
      <td>161677</td>
      <td>A3L512XC4X1C76</td>
      <td>B005LERHD8</td>
      <td>that one girl</td>
      <td>[0, 0]</td>
      <td>The pictures do not do this necklace justice i...</td>
      <td>5.0</td>
      <td>love love love</td>
      <td>1383955200</td>
      <td>11 9, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>141.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Thepicturesdonotdothisnecklacejusticeitissocut...</td>
      <td>lovelovelove</td>
      <td>107</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-09</td>
      <td>11</td>
      <td>B005LERHD8A3L512XC4X1C76</td>
      <td>1</td>
      <td>The pictures do not do this necklace justice i...</td>
      <td>2013</td>
      <td>The pictures do not do this necklace justice i...</td>
    </tr>
    <tr>
      <th>161678</th>
      <td>161678</td>
      <td>A1S21UVMN61AZF</td>
      <td>B005LERHD8</td>
      <td>The Direct Beader "Andrea I Thayer"</td>
      <td>[0, 0]</td>
      <td>Thank-you Spire Arts for not letting me down. ...</td>
      <td>5.0</td>
      <td>;-)</td>
      <td>1401580800</td>
      <td>06 1, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>113.0</td>
      <td>Jewelry</td>
      <td>3.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThankyouSpireArtsfornotlettingmedownItwaswhatI...</td>
      <td></td>
      <td>89</td>
      <td>0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-06-01</td>
      <td>6</td>
      <td>B005LERHD8A1S21UVMN61AZF</td>
      <td>1</td>
      <td>Thankyou Spire Arts for not letting me down It...</td>
      <td>2014</td>
      <td>Thank-you Spire Arts for not letting me down. ...</td>
    </tr>
    <tr>
      <th>161679</th>
      <td>161679</td>
      <td>A2PGJWH9BMX9LT</td>
      <td>B005LERHD8</td>
      <td>TheRedNinja</td>
      <td>[0, 0]</td>
      <td>Super cute and not bad for the price. I ended ...</td>
      <td>5.0</td>
      <td>cute</td>
      <td>1373760000</td>
      <td>07 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>135.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>SupercuteandnotbadforthepriceIendedupgluingsom...</td>
      <td>cute</td>
      <td>107</td>
      <td>4</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-14</td>
      <td>7</td>
      <td>B005LERHD8A2PGJWH9BMX9LT</td>
      <td>1</td>
      <td>Super cute and not bad for the price I ended u...</td>
      <td>2013</td>
      <td>Super cute and not bad for the price. I ended ...</td>
    </tr>
    <tr>
      <th>161680</th>
      <td>161680</td>
      <td>A2QKR3PFJY6XCM</td>
      <td>B005LERHD8</td>
      <td>thetattooedlady</td>
      <td>[0, 0]</td>
      <td>I was expecting something that was much lower ...</td>
      <td>4.0</td>
      <td>Great quality for the price</td>
      <td>1353369600</td>
      <td>11 20, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>272.0</td>
      <td>Jewelry</td>
      <td>27.0</td>
      <td>H</td>
      <td>H</td>
      <td>M</td>
      <td>Iwasexpectingsomethingthatwasmuchlowerqualityc...</td>
      <td>Greatqualityfortheprice</td>
      <td>218</td>
      <td>23</td>
      <td>H</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-20</td>
      <td>11</td>
      <td>B005LERHD8A2QKR3PFJY6XCM</td>
      <td>1</td>
      <td>I was expecting something that was much lower ...</td>
      <td>2012</td>
      <td>I was expecting something that was much lower ...</td>
    </tr>
    <tr>
      <th>161681</th>
      <td>161681</td>
      <td>AD3QONCT8C302</td>
      <td>B005LERHD8</td>
      <td>Tiffany Gray</td>
      <td>[0, 0]</td>
      <td>I love this item. Colors arent the same as pic...</td>
      <td>5.0</td>
      <td>my favorite</td>
      <td>1388966400</td>
      <td>01 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>136.0</td>
      <td>Jewelry</td>
      <td>11.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>IlovethisitemColorsarentthesameaspicturebutIli...</td>
      <td>myfavorite</td>
      <td>106</td>
      <td>10</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-06</td>
      <td>1</td>
      <td>B005LERHD8AD3QONCT8C302</td>
      <td>1</td>
      <td>I love this item Colors arent the same as pict...</td>
      <td>2014</td>
      <td>I love this item. Colors arent the same as pic...</td>
    </tr>
    <tr>
      <th>161682</th>
      <td>161682</td>
      <td>A3TWSE14G5PNCW</td>
      <td>B005LERHD8</td>
      <td>Timpee</td>
      <td>[0, 0]</td>
      <td>Everyone really loved getting one from me for ...</td>
      <td>5.0</td>
      <td>Amazing looking</td>
      <td>1389225600</td>
      <td>01 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>107.0</td>
      <td>Jewelry</td>
      <td>15.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>Everyonereallylovedgettingonefrommefortheholid...</td>
      <td>Amazinglooking</td>
      <td>84</td>
      <td>14</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-01-09</td>
      <td>1</td>
      <td>B005LERHD8A3TWSE14G5PNCW</td>
      <td>1</td>
      <td>Everyone really loved getting one from me for ...</td>
      <td>2014</td>
      <td>Everyone really loved getting one from me for ...</td>
    </tr>
    <tr>
      <th>161683</th>
      <td>161683</td>
      <td>AZC097NSZCUQ8</td>
      <td>B005LERHD8</td>
      <td>Tosha Evans</td>
      <td>[0, 0]</td>
      <td>I love this Vintage Bronze Owl necklace.It is ...</td>
      <td>5.0</td>
      <td>Simply beautiful :)</td>
      <td>1378512000</td>
      <td>09 7, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>392.0</td>
      <td>Jewelry</td>
      <td>19.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IlovethisVintageBronzeOwlnecklaceItissimplyfab...</td>
      <td>Simplybeautiful</td>
      <td>314</td>
      <td>15</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-07</td>
      <td>9</td>
      <td>B005LERHD8AZC097NSZCUQ8</td>
      <td>1</td>
      <td>I love this Vintage Bronze Owl necklaceIt is s...</td>
      <td>2013</td>
      <td>I love this Vintage Bronze Owl necklace.It is ...</td>
    </tr>
    <tr>
      <th>161684</th>
      <td>161684</td>
      <td>A1QYE76M7E4ZK4</td>
      <td>B005LERHD8</td>
      <td>Tracy</td>
      <td>[0, 0]</td>
      <td>It's cute, in a kitsch-y way. The whole owl lo...</td>
      <td>4.0</td>
      <td>NOT FINE JEWELRY!</td>
      <td>1356480000</td>
      <td>12 26, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>513.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>ItscuteinakitschywayThewholeowllookisratherinr...</td>
      <td>NOTFINEJEWELRY</td>
      <td>389</td>
      <td>14</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-26</td>
      <td>12</td>
      <td>B005LERHD8A1QYE76M7E4ZK4</td>
      <td>1</td>
      <td>Its cute in a kitschy way The whole owl look i...</td>
      <td>2012</td>
      <td>It's cute, in a kitsch-y way. The whole owl lo...</td>
    </tr>
    <tr>
      <th>161685</th>
      <td>161685</td>
      <td>A3EAHMM1Y6JTRK</td>
      <td>B005LERHD8</td>
      <td>Travis Blackwell</td>
      <td>[0, 0]</td>
      <td>I got it for a friend that loves owls! She wea...</td>
      <td>5.0</td>
      <td>Cheap and Chic</td>
      <td>1381536000</td>
      <td>10 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>159.0</td>
      <td>Jewelry</td>
      <td>14.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>IgotitforafriendthatlovesowlsShewearsitallthet...</td>
      <td>CheapandChic</td>
      <td>120</td>
      <td>12</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-12</td>
      <td>10</td>
      <td>B005LERHD8A3EAHMM1Y6JTRK</td>
      <td>1</td>
      <td>I got it for a friend that loves owls She wear...</td>
      <td>2013</td>
      <td>I got it for a friend that loves owls! She wea...</td>
    </tr>
    <tr>
      <th>161686</th>
      <td>161686</td>
      <td>A3G6DMMDSOMI99</td>
      <td>B005LERHD8</td>
      <td>Tricia Cartinez</td>
      <td>[0, 0]</td>
      <td>Cuter than expected and excellent price, very ...</td>
      <td>5.0</td>
      <td>too cute</td>
      <td>1391644800</td>
      <td>02 6, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>119.0</td>
      <td>Jewelry</td>
      <td>8.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Cuterthanexpectedandexcellentpriceverypleasedw...</td>
      <td>toocute</td>
      <td>95</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-06</td>
      <td>2</td>
      <td>B005LERHD8A3G6DMMDSOMI99</td>
      <td>1</td>
      <td>Cuter than expected and excellent price very p...</td>
      <td>2014</td>
      <td>Cuter than expected and excellent price, very ...</td>
    </tr>
    <tr>
      <th>161687</th>
      <td>161687</td>
      <td>A2SJNS7S6ECGWN</td>
      <td>B005LERHD8</td>
      <td>Troy Culbreth</td>
      <td>[0, 0]</td>
      <td>Let the sellers know I wasn't completely happy...</td>
      <td>5.0</td>
      <td>Awesome to Deal with.</td>
      <td>1368403200</td>
      <td>05 13, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>223.0</td>
      <td>Jewelry</td>
      <td>21.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>LetthesellersknowIwasntcompletelyhappywiththep...</td>
      <td>AwesometoDealwith</td>
      <td>178</td>
      <td>17</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-05-13</td>
      <td>5</td>
      <td>B005LERHD8A2SJNS7S6ECGWN</td>
      <td>1</td>
      <td>Let the sellers know I wasnt completely happy ...</td>
      <td>2013</td>
      <td>Let the sellers know I wasn't completely happy...</td>
    </tr>
    <tr>
      <th>161688</th>
      <td>161688</td>
      <td>A3KHOFC9GOWQY7</td>
      <td>B005LERHD8</td>
      <td>UrbanFangrl</td>
      <td>[1, 1]</td>
      <td>This is a great necklace! It arrived promptly ...</td>
      <td>5.0</td>
      <td>Great!</td>
      <td>1374451200</td>
      <td>07 22, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>121.0</td>
      <td>Jewelry</td>
      <td>6.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisisagreatnecklaceItarrivedpromptlyandinperf...</td>
      <td>Great</td>
      <td>96</td>
      <td>5</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-22</td>
      <td>7</td>
      <td>B005LERHD8A3KHOFC9GOWQY7</td>
      <td>1</td>
      <td>This is a great necklace It arrived promptly a...</td>
      <td>2013</td>
      <td>This is a great necklace! It arrived promptly ...</td>
    </tr>
    <tr>
      <th>161689</th>
      <td>161689</td>
      <td>A1QM3IBH8SS6VU</td>
      <td>B005LERHD8</td>
      <td>Valdora</td>
      <td>[0, 0]</td>
      <td>My chain is long enough, about 32" so I can sl...</td>
      <td>4.0</td>
      <td>Very cute</td>
      <td>1373068800</td>
      <td>07 6, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>395.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>Mychainislongenoughabout32soIcanslipitovermyhe...</td>
      <td>Verycute</td>
      <td>302</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-06</td>
      <td>7</td>
      <td>B005LERHD8A1QM3IBH8SS6VU</td>
      <td>1</td>
      <td>My chain is long enough about  so I can slip i...</td>
      <td>2013</td>
      <td>My chain is long enough, about 32" so I can sl...</td>
    </tr>
    <tr>
      <th>161690</th>
      <td>161690</td>
      <td>A2G4CKVW5G0K7G</td>
      <td>B005LERHD8</td>
      <td>Valerie Carpenter</td>
      <td>[2, 3]</td>
      <td>Super cute! The pendant is larger than I expec...</td>
      <td>5.0</td>
      <td>Adorable owl pendant</td>
      <td>1379721600</td>
      <td>09 21, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>0.400000</td>
      <td>133.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>SupercuteThependantislargerthanIexpectedwhichw...</td>
      <td>Adorableowlpendant</td>
      <td>106</td>
      <td>18</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-09-21</td>
      <td>9</td>
      <td>B005LERHD8A2G4CKVW5G0K7G</td>
      <td>1</td>
      <td>Super cute The pendant is larger than I expect...</td>
      <td>2013</td>
      <td>Super cute! The pendant is larger than I expec...</td>
    </tr>
    <tr>
      <th>161691</th>
      <td>161691</td>
      <td>A2DPHKB60JGENT</td>
      <td>B005LERHD8</td>
      <td>veronica</td>
      <td>[0, 0]</td>
      <td>Thought the chain would be a little longer on ...</td>
      <td>4.0</td>
      <td>Cute</td>
      <td>1382659200</td>
      <td>10 25, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>239.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Thoughtthechainwouldbealittlelongeronmebutitss...</td>
      <td>Cute</td>
      <td>184</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-10-25</td>
      <td>10</td>
      <td>B005LERHD8A2DPHKB60JGENT</td>
      <td>1</td>
      <td>Thought the chain would be a little longer on ...</td>
      <td>2013</td>
      <td>Thought the chain would be a little longer on ...</td>
    </tr>
    <tr>
      <th>161692</th>
      <td>161692</td>
      <td>A1KCZKMWZGNJMD</td>
      <td>B005LERHD8</td>
      <td>Vickster</td>
      <td>[1, 1]</td>
      <td>I do like this necklace. It looks more brushed...</td>
      <td>4.0</td>
      <td>Nice item</td>
      <td>1355702400</td>
      <td>12 17, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>537.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>H</td>
      <td>IdolikethisnecklaceItlooksmorebrushedthanpictu...</td>
      <td>Niceitem</td>
      <td>422</td>
      <td>8</td>
      <td>L</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2012-12-17</td>
      <td>12</td>
      <td>B005LERHD8A1KCZKMWZGNJMD</td>
      <td>1</td>
      <td>I do like this necklace It looks more brushed ...</td>
      <td>2012</td>
      <td>I do like this necklace. It looks more brushed...</td>
    </tr>
    <tr>
      <th>161693</th>
      <td>161693</td>
      <td>A27GAMYJC1U5IC</td>
      <td>B005LERHD8</td>
      <td>victoria1993</td>
      <td>[0, 0]</td>
      <td>i was pleased with this purchase! bought it as...</td>
      <td>5.0</td>
      <td>what a cute lil owl!</td>
      <td>1401408000</td>
      <td>05 30, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>238.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>iwaspleasedwiththispurchaseboughtitasapresenta...</td>
      <td>whatacutelilowl</td>
      <td>183</td>
      <td>15</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-05-30</td>
      <td>5</td>
      <td>B005LERHD8A27GAMYJC1U5IC</td>
      <td>1</td>
      <td>i was pleased with this purchase bought it as ...</td>
      <td>2014</td>
      <td>i was pleased with this purchase! bought it as...</td>
    </tr>
    <tr>
      <th>161694</th>
      <td>161694</td>
      <td>A2NEV5LKP08N01</td>
      <td>B005LERHD8</td>
      <td>Victoria Engelen</td>
      <td>[0, 0]</td>
      <td>got this as a gift and she loved it. it's a cu...</td>
      <td>5.0</td>
      <td>good gift</td>
      <td>1386806400</td>
      <td>12 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>129.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>gotthisasagiftandshelovedititsacutelittleowlan...</td>
      <td>goodgift</td>
      <td>95</td>
      <td>8</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-12</td>
      <td>12</td>
      <td>B005LERHD8A2NEV5LKP08N01</td>
      <td>1</td>
      <td>got this as a gift and she loved it its a cute...</td>
      <td>2013</td>
      <td>got this as a gift and she loved it. it's a cu...</td>
    </tr>
    <tr>
      <th>161695</th>
      <td>161695</td>
      <td>A1EHNNMTB08S2P</td>
      <td>B005LERHD8</td>
      <td>Vincent D.</td>
      <td>[0, 0]</td>
      <td>My friends will love them and I might just buy...</td>
      <td>5.0</td>
      <td>WHO WHO!!!</td>
      <td>1386806400</td>
      <td>12 12, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>169.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>MyfriendswilllovethemandImightjustbuymorePrett...</td>
      <td>WHOWHO</td>
      <td>131</td>
      <td>6</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-12-12</td>
      <td>12</td>
      <td>B005LERHD8A1EHNNMTB08S2P</td>
      <td>1</td>
      <td>My friends will love them and I might just buy...</td>
      <td>2013</td>
      <td>My friends will love them and I might just buy...</td>
    </tr>
    <tr>
      <th>161696</th>
      <td>161696</td>
      <td>A5O9USKDYRKVK</td>
      <td>B005LERHD8</td>
      <td>vmeans</td>
      <td>[0, 0]</td>
      <td>This necklace is good for the price it was, I ...</td>
      <td>3.0</td>
      <td>Alright</td>
      <td>1359936000</td>
      <td>02 4, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>121.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>ThisnecklaceisgoodforthepriceitwasIguessIttook...</td>
      <td>Alright</td>
      <td>90</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-02-04</td>
      <td>2</td>
      <td>B005LERHD8A5O9USKDYRKVK</td>
      <td>0</td>
      <td>This necklace is good for the price it was I g...</td>
      <td>2013</td>
      <td>This necklace is good for the price it was, I ...</td>
    </tr>
    <tr>
      <th>161697</th>
      <td>161697</td>
      <td>A1MO713GHGJXZD</td>
      <td>B005LERHD8</td>
      <td>V. Rivera "tbell"</td>
      <td>[0, 0]</td>
      <td>It is a really preatty and looks good..came on...</td>
      <td>4.0</td>
      <td>Nice preatty chain..</td>
      <td>1373760000</td>
      <td>07 14, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>115.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>L</td>
      <td>ItisareallypreattyandlooksgoodcameontimeReally...</td>
      <td>Nicepreattychain</td>
      <td>90</td>
      <td>16</td>
      <td>M</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2013-07-14</td>
      <td>7</td>
      <td>B005LERHD8A1MO713GHGJXZD</td>
      <td>1</td>
      <td>It is a really preatty and looks goodcame on t...</td>
      <td>2013</td>
      <td>It is a really preatty and looks good..came on...</td>
    </tr>
    <tr>
      <th>161698</th>
      <td>161698</td>
      <td>A19GYKRVE3SP00</td>
      <td>B005LERHD8</td>
      <td>wanderlust "wavelette"</td>
      <td>[0, 0]</td>
      <td>This was a waste of money. The size was too la...</td>
      <td>2.0</td>
      <td>Way too big and unattractive.</td>
      <td>1353974400</td>
      <td>11 27, 2012</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>149.0</td>
      <td>Jewelry</td>
      <td>29.0</td>
      <td>H</td>
      <td>H</td>
      <td>L</td>
      <td>ThiswasawasteofmoneyThesizewastoolargeandthepe...</td>
      <td>Waytoobigandunattractive</td>
      <td>119</td>
      <td>24</td>
      <td>H</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2012-11-27</td>
      <td>11</td>
      <td>B005LERHD8A19GYKRVE3SP00</td>
      <td>0</td>
      <td>This was a waste of money The size was too lar...</td>
      <td>2012</td>
      <td>This was a waste of money. The size was too la...</td>
    </tr>
    <tr>
      <th>161699</th>
      <td>161699</td>
      <td>A32QDAKOPWYW17</td>
      <td>B005LERHD8</td>
      <td>WillowJule</td>
      <td>[0, 0]</td>
      <td>I love the length of the chain (which I had pr...</td>
      <td>5.0</td>
      <td>Absolutely gorgeous!</td>
      <td>1362096000</td>
      <td>03 1, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>614.0</td>
      <td>Jewelry</td>
      <td>20.0</td>
      <td>M</td>
      <td>M</td>
      <td>H</td>
      <td>IlovethelengthofthechainwhichIhadpreviouslyrea...</td>
      <td>Absolutelygorgeous</td>
      <td>468</td>
      <td>18</td>
      <td>M</td>
      <td>H</td>
      <td>L</td>
      <td>214</td>
      <td>2013-03-01</td>
      <td>3</td>
      <td>B005LERHD8A32QDAKOPWYW17</td>
      <td>1</td>
      <td>I love the length of the chain which I had pre...</td>
      <td>2013</td>
      <td>I love the length of the chain (which I had pr...</td>
    </tr>
    <tr>
      <th>161700</th>
      <td>161700</td>
      <td>A205ZO9KZY2ZD2</td>
      <td>B005LERHD8</td>
      <td>Winnie</td>
      <td>[0, 0]</td>
      <td>I was expecting it to be more of a gold tint w...</td>
      <td>4.0</td>
      <td>It's ok</td>
      <td>1357776000</td>
      <td>01 10, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>255.0</td>
      <td>Jewelry</td>
      <td>7.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>Iwasexpectingittobemoreofagoldtintwhenitgother...</td>
      <td>Itsok</td>
      <td>195</td>
      <td>5</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-01-10</td>
      <td>1</td>
      <td>B005LERHD8A205ZO9KZY2ZD2</td>
      <td>1</td>
      <td>I was expecting it to be more of a gold tint w...</td>
      <td>2013</td>
      <td>I was expecting it to be more of a gold tint w...</td>
    </tr>
    <tr>
      <th>161701</th>
      <td>161701</td>
      <td>APFTQJGB3TFND</td>
      <td>B005LERHD8</td>
      <td>yblirt</td>
      <td>[0, 0]</td>
      <td>These are just so cute, I even wear one and ha...</td>
      <td>5.0</td>
      <td>cute</td>
      <td>1392076800</td>
      <td>02 11, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>294.0</td>
      <td>Jewelry</td>
      <td>4.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>ThesearejustsocuteIevenwearoneandhaveneverworn...</td>
      <td>cute</td>
      <td>229</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-02-11</td>
      <td>2</td>
      <td>B005LERHD8APFTQJGB3TFND</td>
      <td>1</td>
      <td>These are just so cute I even wear one and hav...</td>
      <td>2014</td>
      <td>These are just so cute, I even wear one and ha...</td>
    </tr>
    <tr>
      <th>161702</th>
      <td>161702</td>
      <td>ARUAJ7VWW3KCI</td>
      <td>B005LERHD8</td>
      <td>Yuma, AZ</td>
      <td>[1, 1]</td>
      <td>The pendant is very cute but the rhinestones a...</td>
      <td>4.0</td>
      <td>Great for the $$$</td>
      <td>1385683200</td>
      <td>11 29, 2013</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.500000</td>
      <td>178.0</td>
      <td>Jewelry</td>
      <td>17.0</td>
      <td>M</td>
      <td>M</td>
      <td>M</td>
      <td>Thependantisverycutebuttherhinestonesarejustth...</td>
      <td>Greatforthe</td>
      <td>137</td>
      <td>11</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2013-11-29</td>
      <td>11</td>
      <td>B005LERHD8ARUAJ7VWW3KCI</td>
      <td>1</td>
      <td>The pendant is very cute but the rhinestones a...</td>
      <td>2013</td>
      <td>The pendant is very cute but the rhinestones a...</td>
    </tr>
    <tr>
      <th>161703</th>
      <td>161703</td>
      <td>A1UJ9PL8CQ5TEQ</td>
      <td>B005LERHD8</td>
      <td>Zayettcy</td>
      <td>[0, 0]</td>
      <td>Very cute!</td>
      <td>4.0</td>
      <td>Four Stars</td>
      <td>1405123200</td>
      <td>07 12, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>10.0</td>
      <td>Jewelry</td>
      <td>10.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Verycute</td>
      <td>FourStars</td>
      <td>8</td>
      <td>9</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-12</td>
      <td>7</td>
      <td>B005LERHD8A1UJ9PL8CQ5TEQ</td>
      <td>1</td>
      <td>Very cute</td>
      <td>2014</td>
      <td>Very cute!</td>
    </tr>
    <tr>
      <th>161704</th>
      <td>161704</td>
      <td>A1OHOGJK6QJJZP</td>
      <td>B005LERHD8</td>
      <td>Zoe</td>
      <td>[0, 0]</td>
      <td>Breaks very easily but is easily fixed. There ...</td>
      <td>3.0</td>
      <td>Ehhh.</td>
      <td>1404864000</td>
      <td>07 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>255.0</td>
      <td>Jewelry</td>
      <td>5.0</td>
      <td>L</td>
      <td>L</td>
      <td>M</td>
      <td>BreaksveryeasilybutiseasilyfixedThereisnoclasp...</td>
      <td>Ehhh</td>
      <td>199</td>
      <td>4</td>
      <td>L</td>
      <td>M</td>
      <td>L</td>
      <td>214</td>
      <td>2014-07-09</td>
      <td>7</td>
      <td>B005LERHD8A1OHOGJK6QJJZP</td>
      <td>0</td>
      <td>Breaks very easily but is easily fixed There i...</td>
      <td>2014</td>
      <td>Breaks very easily but is easily fixed. There ...</td>
    </tr>
    <tr>
      <th>161705</th>
      <td>161705</td>
      <td>A23TVM6UI5ULUD</td>
      <td>B005LERHD8</td>
      <td>Zuri Gandy</td>
      <td>[0, 0]</td>
      <td>This necklace looks just like they say, it's t...</td>
      <td>4.0</td>
      <td>I love it</td>
      <td>1394323200</td>
      <td>03 9, 2014</td>
      <td>5995774</td>
      <td>{'Jewelry': 214}</td>
      <td>http://ecx.images-amazon.com/images/I/41b7ttDx...</td>
      <td>[['Clothing, Shoes &amp; Jewelry', 'Women'], ['Clo...</td>
      <td>Vintage, Retro Colorful Crystal Owl Pendant an...</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>{'also_bought': ['B00JZPUIPS', 'B00FF3O6IO', '...</td>
      <td>JewelrieShop</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0.000000</td>
      <td>125.0</td>
      <td>Jewelry</td>
      <td>9.0</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>Thisnecklacelooksjustliketheysayitstocuteandgo...</td>
      <td>Iloveit</td>
      <td>98</td>
      <td>7</td>
      <td>L</td>
      <td>L</td>
      <td>L</td>
      <td>214</td>
      <td>2014-03-09</td>
      <td>3</td>
      <td>B005LERHD8A23TVM6UI5ULUD</td>
      <td>1</td>
      <td>This necklace looks just like they say its to ...</td>
      <td>2014</td>
      <td>This necklace looks just like they say, it's t...</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_merged_c.shape
```




    (278677, 47)




```python
df_merged_c.groupby('year').asin.nunique()
```




    year
    2003        2
    2004        6
    2005       23
    2006       91
    2007      338
    2008      628
    2009     1153
    2010     2242
    2011     5099
    2012    12240
    2013    21328
    2014    19693
    Name: asin, dtype: int64




```python
min(df_merged_c['date'])
```




    '2003-03-29'




```python

```
