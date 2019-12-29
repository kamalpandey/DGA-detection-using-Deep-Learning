import pandas as pd
from sklearn.utils import shuffle

df_dga = pd.read_csv("./dga_feed.csv")
df_alexa = pd.read_csv("./top-1m.csv")

# DGA labels
dga_labels_dict = {'alexa':0, 'banjori':1, 'tinba':2, 'Post':3, 'ramnit':4, 'necurs':5, 'murofet':6, 'qakbot':7, 'shiotob/urlzone/bebloh':8, 'simda':9,
              'pykspa':10, 'ranbyus':11, 'dyre':12, 'kraken':13, 'Cryptolocker':14, 'nymaim':15, 'locky':16, 'vawtrak':17, 'shifu':18,
              'ramdo':19, 'P2P':20 }

# Process DGA data
dga_label= []
dga_domains = []
z = 0
for x in df_dga['source'].tolist():
    if x in dga_labels_dict:
        dga_label.append(dga_labels_dict[x])
        dga_domains.append(df_dga['domain'].tolist()[z])
    z = z + 1

# Data columns("domain", "class")
dga_archive = pd.DataFrame(columns=['domain'])
dga_archive["domain"] = dga_domains
dga_archive['class'] = dga_label

# Process Alexa data
alexa_domains = df_alexa['domain'].tolist()
alexa_labels = []
for x in alexa_domains:
    alexa_labels.append(0)

alexa_archive = pd.DataFrame(columns=['domain'])
alexa_archive["domain"] = alexa_domains
alexa_archive['class'] = alexa_labels

# Combine DGA and Alexa data
result = pd.concat([dga_archive, alexa_archive])

# Shuffle the data
result = shuffle(result)
result.to_csv("./dga_label.csv",mode='w',index=False)

