title: Starting This Site - Ordering and Categorizing Posts
page-description: Ordering and categorizing the flat pages on the Flask app home page
publish-datetime: 2021-05-04 21:00:00
updated-datetime: 
publish: true
previous-post: initial-deploy-with-netlify
next-post: 
code-examples: true

Currently, the home page shows the posts in a seemingly random order. Also, all posts written thus far are under "Starting This Site," and I do not expect that to be the only grouping for long.

Here we'll try to order the posts by the meta field `publish-datetime`.

##### First Try Update

I first adopted my `get_active_posts` function to take two new parameters beyond the list of pages, `sort` and `sort_by_meta`.

Shown here
```
:::python hl_lines="1 3 4"
def get_active_posts(pages, sort=True, sort_by_meta="publish-datetime"):
    // omitted
    if sort:
        active_posts.sort(key=lambda x: x.meta[sort_by_meta])
    return active_posts
```

##### Configuration Issues

I was trying to show that I made a function that did two things, and I really need to abstract the above code to have a separate function for sorting. _However_, depending on when you're reading this you'll notice how... plain, the code above looks.

In trying to solve that, `app.py` is getting a bit cluttered. I am going to refactor some of that out.
