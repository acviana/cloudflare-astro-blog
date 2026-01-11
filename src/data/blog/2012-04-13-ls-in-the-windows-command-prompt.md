---
author: acv
pubDatetime: 2012-04-13T15:59:51
title: "`ls` in the Windows Command Prompt"
slug: ls-in-the-windows-command-prompt
featured: false
draft: false
tags:
  - tumblr-blog
  - Windows
  - Cygwin
  - text
description: "`ls` in the Windows Command Prompt"
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/21041091800/ls-in-the-windows-command-prompt
---

Right now to interact with Windows Command Prompt I use a wrapper called Console2. It adds some basic functionality to the Command Prompt like tabs, and copy/paste. It's an improvement but not great because it's still just a wrapper around the primitive command prompt.

So I've been slowly transitioning over to Cygwin. Last week one of my buddies [showed me](http://theothersideofthescreen.tumblr.com/post/20543972366/getting-cygwin-to-see-my-local-file-system) what to add to my Windows `PATH` variable to to allow Cygwin to see the local filespace. I was, and still am, confused about why adding paths _inside_ of the Cygwin filespace allowed Cygwin to see the rest of the drive, but it worked.

But today I noticed something interesting. One of the minor annoyances of having to use the Windows Command Prompt at home and OSX at work is that in windows you have to use `dir` instead of `ls` to view the contents of a folder and I have to remember to switch back and forth.

But today, `ls` worked! It was such a little thing that I didn't even notice till I had done it a few times. I realized (I think) this is because the paths I added to the `PATH` variable mapped the functions from Cygwin to rest of the Windows environment.

Neat! A nice surprise.