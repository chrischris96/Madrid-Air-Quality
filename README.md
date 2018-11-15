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
 
 ## Usage of the right estimator
 
 After having a first look at the data, let's beginn predicting. For the beginning we stick to predicting the carbon dioxid values of 2018 by using the data from the previous years. A question arises: What is the right estimator? With a sample size of  <200,000 we stand a good chance to find a suitable estimator. Since we use a supervised algorithm and want to predit a quantity with a great sample size and few important features, I would personally choose ElasticNet. If it is really a match, we should have a look at the data. For ElasticNet, the features should strongly correlate which is the case. For comparison, we will also have a the linear model calles Lasso that estimates sparse coefficients. 
