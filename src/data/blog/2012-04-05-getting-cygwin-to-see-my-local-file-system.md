---
author: acv
pubDatetime: 2012-04-05T15:41:09
title: "Getting Cygwin to see my local file system. "
slug: getting-cygwin-to-see-my-local-file-system
featured: false
draft: false
tags:
  - tumblr-blog
  - cygwin
  - windows
  - text
description: "Getting Cygwin to see my local file system."
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/20543972366/getting-cygwin-to-see-my-local-file-system
---

My friend showed me how to see my local file system on my windows Vista machine. I added the following paths to my windows PATH variable:
    
    
    C:\Cygwin\bin;
    C:\Cygwin\usr\bin;
    C:\Cygwin\usr\local\bin;
    C:\Cygwin\lib;
    C:\Cygwin\usr\lib
    

Then I can see the local file system with:
    
    
    cd c:/
    

I'm not sure what adding these path to this variable changed though. Cygwin was already working so I'm not sure why adding paths that point to it's own directory structure allows me to see the local file structure.