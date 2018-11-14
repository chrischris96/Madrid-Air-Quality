# Madrid Air Quality
 Analysing the air quality in the Madrid central area with
 data from the last two decades. For the beginning the
 stations are plotted to show where the data is recorded.
 
 The calleavdandctra_madrid_huge.png shows the output of the code, plotting all infrastructure in Madrid named 
 "calle", "avenia" or "carretera" in one image. If you look closly you can see red dots in the city center.
 Those dots refer to the points where the air measurements took place.
 
 ## Exploring the data
 
 The dataset consists of a huge matrix. However there is a lot of missing data i.e. nan values. As part of the exploration we first have a look at the carbon dioxid values of the stations and plot it in one plot. In the merged the green values are particularly interesting, since it seems like the stations measured a relatively high value of carbon dioxid all year long. A further look at the single station underlines the assumption. The plot of the single station is shown in another plot as a .png file.
 
 In a further analysis we can seperate the stations in different groups and analysis the values of air pollution in groups. What is a interesting ansatz to seperate the stations in different groups? Maybe we can merge them in different neigborhoods, or stations on main roads or just by cardinal points.

