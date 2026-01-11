---
author: acv
pubDatetime: 2012-08-21T16:28:09
title: "I'm on-site today at Southern Illinois University - Edwardsville working on Space Telescope's collaboration with..."
slug: im-on-site-today-at-southern-illinois-university
featured: false
draft: false
tags:
  - tumblr-blog
  - photo
description: "I'm on-site today at Southern Illinois University - Edwardsville working on Space Telescope's collaboration with..."
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/29919504208/im-on-site-today-at-southern-illinois-university
---

![Photo](/assets/tumblr/im-on-site-today-at-southern-illinois-university/tumblr_m94jmx7CBQ1rt9cjfo1_1280.png) 

I'm on-site today at Southern Illinois University - Edwardsville working on Space Telescope's collaboration with [CosmoQuest](http://cosmoquest.org/) on an exciting crowd-sourcing project for citizen-scientists.

I'm providing the back-end pipeline to produce the images for the web app (I'll share the GitHub onces it's a little further along). Right now I'm using a little imaging tool I created (below) to examine the steps in the image scaling. The three row are the original image, the image after the step was applied (in this case the log of original image) and a delta image. Each row has an image and a histogram. In this case you can see there is single pixel pulling the stretch way out of whack so I'm working a function to trim the lowest outliers.