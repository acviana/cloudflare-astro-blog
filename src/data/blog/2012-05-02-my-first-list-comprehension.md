---
author: acv
pubDatetime: 2012-05-02T13:50:00
title: "My First List Comprehension "
slug: my-first-list-comprehension
featured: false
draft: false
tags:
  - tumblr-blog
  - python
  - text
description: "My First List Comprehension"
originalUrl: https://theothersideofthescreen-blog.tumblr.com/post/22265982572/my-first-list-comprehension
---

I've been programming in Python for over 4 years. That's how long it took me to use [list comprehensions](http://docs.python.org/tutorial/datastructures.html#list-comprehensions). I'm a little embarrassed about this.

To be fair I've known about list comprehensions for years but just never used them. It's one of those nice bits of syntactic sugar that you can get by without. This is especially true if you're off in the corner reinventing the wheel, as I was the first couple of years I was programming. I knew they existed, I had a rough Idea of what they were for, but I just didn't see the use for them. Like learning most things in software development, it was just a matter of having the right problem.

In my case I was refactoring some of my code so my officemate could more effectively collaborate with me and I didn't like the way I was modifying lists. Let's say I had a list of names and wanted to remove all the names that didn't start with b. I was doing something like this:
    
    
    name_list = ['bill', 'bob', 'brian', 'betty', 'farnsworth']
    b_name_only_list = []
    for name in name_list:
        if name[0] == 'b':
            b_name_only_list.append(name)
    

This would create a list of the names that start with 'b'. For smaller projects this worked. But it felt dumb to have to make a new list to do this. What if I didn't want two lists? What I just wanted to chuck the non-b names? I tried to do this by modifing the list "in-place" with something like this:
    
    
    for name in name_list:
        if name[0] != 'b':
            name_list.remove(name)
    

But modifying a list as you are iterating over it creates errors and other weirdness such as this little guy:
    
    
    a = [1, 2, 3]
    for item in a:
        a.remove(item)
    print a
    

Which prints `2`. (Explained [here](http://stackoverflow.com/questions/7226997/removing-items-from-a-list-in-a-loop).)

I got the feeling I was barking up the wrong tree. So after a little searching on StackOverflow I remembered, "oh yeah, list comprehensions, I should try that." Sure enough I can just do something like this:
    
    
     name_list = [name for name in name_list if name[0] == 'b']
    

Sweet.