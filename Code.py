import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv('Iris.csv')
print(df)

sns.violinplot(x=df["species"], y=df["sepal_length"])
plt.show()
