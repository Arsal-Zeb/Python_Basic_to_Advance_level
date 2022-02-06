# # import pandas as pd

# # data=pd.read_csv("data_viz.csv")
# # data.head()
# # print (data)


# import pandas as pd
# import seaborn as sns
# import matplotlib as plt
# import plotly
# import plotly.express as px

# #import chilla data
# data_chilla1=pd.read_csv("Chilla_data2_for_plots.csv")


# fig = px.bar( x="Gender",  y= "Qualification_completed", data= data_chilla1, color='field_of_study')
# fig.show()
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()