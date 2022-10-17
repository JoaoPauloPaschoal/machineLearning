import numpy as np
import pandas as pd
import plotly.express as px

dados = pd.read_csv(r'F:\Python\Machine Learning\heart.csv', sep=',', encoding='iso-8859-1')

dados.head()
#print(dados['Age'].value_counts().sort_index())


hist1 =  px.histogram(dados, x="Age", nbins=60)
hist1.update_layout(width=800, height=500,title_text="Distribuição das idades")
hist1.show()