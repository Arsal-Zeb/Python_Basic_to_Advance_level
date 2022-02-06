#Use Seaborn and matplotlib to plot titanic data (built-in data in seaborn library)
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes="true")

titanic=sns.load_dataset("titanic")
# p1=sns.catplot(x="who",y="survived", hue="class", kind="bar" , data=titanic)
# print (titanic)
p1=sns.countplot(x='who',data=titanic, hue='alone' )
p1.set_title("plot for counting")
plt.show()


# #Scatter Plot 
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes="true")

# titanic=sns.load_dataset("titanic")
# h=sns.FacetGrid(titanic,row="sex" ,hue="alone")
# h=(h.map(plt.scatter, "age", "fare").add_legend())
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes="true")

# titanic=sns.load_dataset("titanic")
# # p1=sns.catplot(x="sex",y="survived", hue="class", kind="bar" , data=titanic)
# p1=sns.countplot(x='sex',data=titanic, hue='class' )
# p1.set_title("plot for counting")
