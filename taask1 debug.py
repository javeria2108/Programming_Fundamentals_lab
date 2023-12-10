# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:00:57 2022

@author: Marry
"""
try:
    blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},  {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5,  'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4,  'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1},  {'Photos': 3, 'Likes': 19, 'Comments': 3}] 
    total_likes = 0 
    for post in blog_posts: 
      total_likes = total_likes + post['Likes'] 
except KeyError:
    print('there is a key error')