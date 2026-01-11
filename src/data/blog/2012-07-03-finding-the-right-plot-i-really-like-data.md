---
author: acv
pubDatetime: 2012-07-03T18:31:13
title: "_Finding the Right Plot_

I really like data visualization, even if I can't claim to be any an expert at it. Today I wanted to..."
slug: finding-the-right-plot-i-really-like-data
featured: false
draft: false
tags:
  - tumblr-blog
  - python
  - matplotlib
  - visualization
  - photo
description: "_Finding the Right Plot_

I really like data visualization, even if I can't claim to be any an expert at it. Today I wanted to..."
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/26452519547/finding-the-right-plot-i-really-like-data
---

![Photo](/assets/tumblr/finding-the-right-plot-i-really-like-data/tumblr_m6lyo1p5dg1rt9cjfo1_1280.png) 

_Finding the Right Plot_

I really like data visualization, even if I can't claim to be any an expert at it. Today I wanted to plot some data in a flat file a coworker had generated. I first tried this with Google Docs because I just wanted something quick and dirty. But while I discovered some nice new features I wasn't quite able to do what I wanted; so I switched to Python with the Matplotlib module.

In Matplotlib I was pretty quickly able to get what I wanted, but then there was the matter of deciding what I wanted. I went through the 4 plots above.

The first was the standard scatter plot, this is no good because close fluctuations in February just look scattered and hard to follow. Then I tried a line plot, but now I felt that it was hard to pick out the individual points. Since the data points are non-uniformly distributed this is key information. Next I tried a plot with both lines and points (actually the two plots overlaid). This produced the best of both worlds, you could see the individual data points as well as follow their progression.

But then I noticed there was a problem with this chart as well. The use of the line implies an interpolation between the data points that might not be true. For example the increase shown on the plot from mid-May to mid-June actually occurred suddenly, not gradually as the line implies.

Finally I settled on a bar plot. This allows us to see that the data is non-uniformly distributed. We can pick out each individual point, as well as follow the flow of data. Lastly, nothing about data markers is misleading about the nature of the data. Areas with no data look "empty", which is exactly what they are.

Fun little project for the end of the workday.