title: Starting This Site - Initial Deploy with Netlify
page-description: A recap of deploying this Flask site with Netlify
publish-datetime: 2021-04-30 12:00:00
updated-datetime: 2021-05-04 12:00:00
publish: true
previous-post: do-not-register-a-dot-us
next-post: ordering-and-categorizing-posts


I'll tackle this <s>tomorrow</s> May 2nd.

##### 2021-05-04 Update

The basic deployment is not working. The Posts and Pages load fine, but the home page is not loading the correct template or including the links to all the posts.

The issue does not present at all in dev. I suspect it's happening somewhere in the freeze process?

I also removed the register generator, since I added the links from post to post, it _should_ no longer be necessary.

##### Post-Commit Update

Hey, it worked! The generator must have been causing the issue with the home page. Of course now all the posts are out of order on the home page.
