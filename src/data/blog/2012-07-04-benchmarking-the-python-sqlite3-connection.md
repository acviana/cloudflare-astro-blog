---
author: acv
pubDatetime: 2012-07-04T16:51:00
title: "Benchmarking the Python SQLite3 Connection"
slug: benchmarking-the-python-sqlite3-connection
featured: false
draft: false
tags:
  - source-tumblr-blog
  - python
  - SQLite
  - text
description: "Benchmarking the Python SQLite3 Connection"
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/26516364196/benchmarking-the-python-sqlite3-connection
---

We have several SQLite calls in our pipeline that look something like this
    
    
    for file in file_list:
        conn = sqlite3.connect(database)
        c = conn.cursor()
        command = 'SELECT * FROM table'
        c.execute(command)
        conn.close()
    

I originally wrote our database calls this way because at the time (this was about 2 years ago), I was worried about the code crashing with an open database connection. I thought this would be vaguely "bad" so I was over enthusiastic about keeping connections closed. The design pattern stuck.

But someone pointed out to us that it would be faster to do something like this:
    
    
    conn = sqlite3.connect(database)
    c = conn.cursor()
    for file in file_list:
        command = 'SELECT * FROM table'
        c.execute(command)
    conn.close()
    

The reason being that there is some overhead involved when opening a Python SQLite3 connection. When you loop over the connection opening/closing steps you multiply this overhead.

My officemate went ahead and tested the overhead for running both design patterns over a test set of queries. Based on our results you can infer a connection overhead of 0.0134s. I took that data and assumed a linear increase for the overhead time for each additional query to extrapolate the results up to scale of our filesystem. The results are below. The first row are the real results and the next two are the extrapolated predictions.

Multiple | Single | Delta | Delta % | Records | Factor | Notes  
---|---|---|---|---|---|---  
0:02:23 | 0:02:05 | 0:00:18 | 12.59% | 9300 | 1 | wfc3g flt files  
0:19:13 | 0:16:48 | 0:02:25 | 12.59% | 75000 | 8.0645 | All flt files  
3:31:25 | 3:04:48 | 0:26:36 | 12.59% | 825000 | 88.7097 | All fits files  
  
As you can see, we achieve a 13% speed up, which if we are querying the entire database saves us almost 30 min. Since we are running this process overnight this isn't a huge deal. Going forward it would be smart to use the faster form. However, I'm not sure if it's worth it to go back and fix our old SQLite calls as we have more pressing issues.

All in all, this was an interesting exercise and will probably lead to some more detailed profiling of our pipeline in the future.