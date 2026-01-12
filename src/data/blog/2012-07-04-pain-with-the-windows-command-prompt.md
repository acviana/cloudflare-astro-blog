---
author: acv
pubDatetime: 2012-07-04T16:54:06
title: "Pain with the Windows Command Prompt"
slug: pain-with-the-windows-command-prompt
featured: false
draft: false
tags:
  - source-tumblr-blog
  - windows
  - dropbox
  - SQLite
  - Command Line
  - text
description: "Pain with the Windows Command Prompt"
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/26516553909/pain-with-the-windows-command-prompt
---

_[I wrote this post a few months but never posted it for some reason. Ah, the joys of trying to develop on Windows.]_

I love my trusty IBM Thinkpad. It's coming up on 5 years old and other than a some fan buzz and a RAM card that needed to be replaced it runs just fine.

But the Windows Command Prompt can just ruin my day.

So I run my code to ingest the data into the database. No problem. But then I need to see if it made it into the database. I try just typing `sqlite3` in the Command Prompt. No dice. No big deal, I just download the SQLite3 windows shell. But the problem with this tool is is just launches. You can't do something like:
    
    
    sqlite3 mydatabse.db
    

Bummer. In hindsight I should have tried to called the full path to `sqlite3.exe` in the folder with my database. But since SQLite was just firing up in the folder where `sqlite3.exe` lives I focused on trying to open the database from within the SQLite3 shell.

Enter my next problem. There is no tab completion or copy/paste functionality in the SQLite3 shell. So now I have to type the full path out. No big deal right?

Wrong. My database lives with my code in a folder in my dropbox area. On a windows machine the Dropbox root folder is called `My Dropbox`, with the space. This creates a minor headache because now I have to get SQLite to accept a path name with space in it. After some playing with quotes, and forward and back slashes I decided that the space in the `My Dropbox` path element was annoying enough in general I should just change it altogether (it's just `Dropbox` on my OSX system at work).

It turns out this is a known 'non-issue' with Dropbox that is intentionally configured that was to avoid confusing non-technical Dropbox users. Around the time I was reading about scripts and redownloading instructions to change this I realized I had gone much too far afield wresting with this.

I the end I hacked a solution by just making a copy of `sqlite3.exe` in the same folder as my database. Then I can use the `.restore` command inside the SQLite3 shell without worrying about the full path. Definitely a hack but it worked and I was able to get it to work.