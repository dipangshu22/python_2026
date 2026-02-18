import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Hours": [1,2,3,4,5],
    "Score": [50,55,65,70,80]
})

sns.lineplot(x="Hours", y="Score", data=data)

plt.show()
