import plotly.express as px
import pandas as pd
data=pd.read_excel("Book1.xlsx")


names = data.loc[data["marks"] > 30, "name"]
fig = px.bar(names, x="name",)

print(names)
print(fig)


