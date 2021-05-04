title: Starting This Site - Adding a Favicon
publish-datetime: 2021-04-29 12:00:00
publish: true
previous-post: introduction
next-post: do-not-register-a-dot-us

This will also serve as a test of page sequencing. I should be able to navigate to this from the introduction.

It works! We should see navigation links to the others in the sequence at the bottom of this page. There was an interesting trade-off to consider. I put the next and previous post information in the metadata within the Markdown. I chose to put only the basic filename, and not the full path, which means I need to infer the file is within the same path as the other pages within the sequence. I did this to minimize the impact should I need to change a folder name or topic. I also figure if
I _do_ need to link across folders/topics, I can do so with an additional parameter that is ignored if `Null`.

The generated favicon was added following the thorough instructions from the [generator](https://favicon.io/favicon-generator/ "John Sorrentino's Favicon Generator"), though I did sequester it to its own directory.

I'll be interested to see if my static structure translates after using Freeze to build the site.
