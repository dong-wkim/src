import pandas as pd
import numpy as np
import re

def search(file = os.getcwd()):

    file = os.getcwd()
    here = Path(file).resolve().parent
    root = here
    while not (root / "research").exists():
        root = root.parent
    
    pm_cols = {'PMID': 'id',
     'DOI': 'doi',
     'Authors': 'authors',
     'Title': 'title',
     'Publication Year': 'year',
     'Journal/Book': 'journal'}
     
    em_cols = {'Embase Link': 'id',
     'DOI':'doi',
     'Author Names': 'authors',
     'Title': 'title',
     'Publication Year': 'year',
     'Source': 'journal'}
    
    wos_cols = {'UT (Unique WOS ID)':'id',
     'DOI':'doi',
     'Authors': 'authors',
     'Article Title':  'title',
     'Publication Year':  'year',
     'Source Title': 'journal'}
    
    pm_bptb = pd.read_csv('./rct/pubmed/pm_bptb.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    pm_ht = pd.read_csv('./rct/pubmed/pm_ht.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    pm_qt = pd.read_csv('./rct/pubmed/pm_qt.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    pm_plt = pd.read_csv('./rct/pubmed/pm_plt.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    pm_at = pd.read_csv('./rct/pubmed/pm_at.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    pm_ta = pd.read_csv('./rct/pubmed/pm_ta.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    
    pm_bptb['subgroup'] = 'BPTB'
    pm_ht['subgroup'] = 'HT'
    pm_qt['subgroup'] = 'QT'
    pm_plt['subgroup'] = 'PLT'
    pm_at['subgroup'] = 'AT'
    pm_ta['subgroup'] = 'TA'
    
    pubmed = pd.concat([pm_bptb, pm_ht, pm_qt, pm_plt, pm_at, pm_ta])
    pubmed['source'] = 'PubMed/MEDLINE'
    pubmed.to_csv('./rct/pubmed/pubmed.csv', encoding = 'utf-8')
    
    em_bptb = pd.read_csv('./rct/embase/em_bptb.csv', encoding = 'utf-8', usecols =['Embase Link', 'DOI', 'Author Names', 'Title', 'Publication Year', 'Source']).rename(columns = em_cols)
    em_ht = pd.read_csv('./rct/embase/em_ht.csv', encoding = 'utf-8', usecols = ['Embase Link', 'DOI', 'Author Names', 'Title', 'Publication Year', 'Source']).rename(columns = em_cols)
    em_qt = pd.read_csv('./rct/embase/em_qt.csv', encoding = 'utf-8', usecols = ['Embase Link', 'DOI', 'Author Names', 'Title', 'Publication Year', 'Source']).rename(columns = em_cols)
    em_plt = pd.read_csv('./rct/embase/em_plt.csv', encoding = 'utf-8', usecols = ['Embase Link', 'DOI', 'Author Names', 'Title', 'Publication Year', 'Source']).rename(columns = em_cols)
    em_at = pd.read_csv('./rct/embase/em_at.csv', encoding = 'utf-8', usecols = ['Embase Link', 'DOI', 'Author Names', 'Title', 'Publication Year', 'Source']).rename(columns = em_cols)
    em_ta = pd.read_csv('./rct/embase/em_ta.csv', encoding = 'utf-8', usecols = ['Embase Link', 'DOI', 'Author Names', 'Title', 'Publication Year', 'Source']).rename(columns = em_cols)
    
    em_bptb['subgroup'] = 'BPTB'
    em_ht['subgroup'] = 'HT'
    em_qt['subgroup'] = 'QT'
    em_plt['subgroup'] = 'PLT'
    em_at['subgroup'] = 'AT'
    em_ta['subgroup'] = 'TA'
    
    embase = pd.concat([em_bptb, em_ht, em_qt, em_plt, em_at, em_ta])
    embase['source'] = 'Embase'
    embase.to_csv('./rct/embase/embase.csv', encoding = 'utf-8')
    
    wos_bptb = pd.read_csv('./rct/wos/wos_bptb.csv', encoding = 'latin-1', usecols = ['UT (Unique WOS ID)', 'DOI', 'Authors', 'Article Title', 'Publication Year', 'Source Title']).rename(columns = wos_cols)
    wos_ht = pd.read_csv('./rct/wos/wos_ht.csv', encoding = 'latin-1', usecols = ['UT (Unique WOS ID)', 'DOI', 'Authors', 'Article Title', 'Publication Year', 'Source Title']).rename(columns = wos_cols)
    wos_qt = pd.read_csv('./rct/wos/wos_qt.csv', encoding = 'latin-1', usecols = ['UT (Unique WOS ID)', 'DOI', 'Authors', 'Article Title', 'Publication Year', 'Source Title']).rename(columns = wos_cols)
    wos_plt = pd.read_csv('./rct/wos/wos_plt.csv', encoding = 'latin-1', usecols = ['UT (Unique WOS ID)', 'DOI', 'Authors', 'Article Title', 'Publication Year', 'Source Title']).rename(columns = wos_cols)
    
    wos_bptb['subgroup'] = 'BPTB'
    wos_ht['subgroup'] = 'HT'
    wos_qt['subgroup'] = 'QT'
    wos_plt['subgroup'] = 'PLT'
    
    wos = pd.concat([wos_bptb, wos_ht, wos_qt, wos_plt])
    wos['source'] = 'Web of Science'
    wos.to_csv('./rct/embase/wos.csv', encoding = 'latin-1')
    
    records = pd.concat([pubmed, embase, wos])
    records['first_author'] = records['authors'].str.replace(r'[,.;]','', regex = True).str.split().str[0]
    records['short_title'] = records['title'].str.replace(r'[\[\]\s,.;-]','',regex = True).str.lower()
    records['key'] = records['first_author'] + '+' + records['short_title'] + '+' + records['year'].astype(str)
    
    records.to_csv('./records.csv')
    records.head()
    
    rev_pm_bptb = pd.read_csv('./reviews/bptb.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    rev_pm_ht = pd.read_csv('./reviews/ht.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    rev_pm_qt = pd.read_csv('./reviews/qt.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    rev_pm_plt = pd.read_csv('./reviews/plt.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    rev_pm_at = pd.read_csv('./reviews/at.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    rev_pm_ta = pd.read_csv('./reviews/ta.csv', encoding = 'utf-8', usecols = ['PMID', 'DOI', 'Authors', 'Title', 'Publication Year', 'Journal/Book']).rename(columns = pm_cols)
    rev_pubmed = pd.concat([rev_pm_bptb, rev_pm_ht, rev_pm_qt, rev_pm_plt, rev_pm_at, rev_pm_ta])
    
    rev_pubmed['first_author'] = rev_pubmed['authors'].str.replace(r'[,.;]','', regex = True).str.split().str[0]
    rev_pubmed['short_title'] = rev_pubmed['title'].str.replace(r'[\[\]\s,.;-]','',regex = True).str.lower()
    rev_pubmed['key'] = rev_pubmed['first_author'] + '+' + rev_pubmed['short_title'] + '+' + rev_pubmed['year'].astype(str)
    rev_pubmed.to_csv('./reviews.csv', encoding = 'utf-8')

    return records, reviews
