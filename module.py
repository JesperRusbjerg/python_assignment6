import urllib.request as request
import gzip
import shutil
import networkx as nx
import matplotlib.pyplot as plt

data_url = "https://snap.stanford.edu/data/facebook_combined.txt.gz"
request.urlretrieve(data_url, "data.txt.gz")

with gzip.open('data.txt.gz', 'rb') as f_in:
    with open('data.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


G = nx.read_edgelist("./data.txt")
print(nx.info(G))

nx.draw(G, node_size=20)
plt.show()

top10 = sorted(G.degree, key=lambda x: x[1], reverse=True)[:10]
print(top10)