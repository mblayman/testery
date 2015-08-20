Design Thoughts
===============

testery will be a webapp
with a hard separation between the frontend and the backend.

My initial thought was to use Django.
During my prototype phase,
I discovered that my JavaScript was a horrid mess.
This led me to Ember.

Ember really wants to own the whole application experience.
Because of Ember's philosophy,
using a full stack like Django makes little sense to me.
Django is full of features
and there would be a massive amount that I don't need.

The downside to this approach is that I lose out on server side rendering.
But I think the truth is that matching server side rendering
and client side rendering is a dream
or a very hamstrung reality
if I used just the right subset of templating languages.

Phase 0
-------

Bootstrap everything.

The problem of making a full webapp by yourself
is that you're making a full webapp by yourself.

Since I am not going with an all-in-one framework like Django,
the stack of technology is huge and varied.

My MVP for this phase must be the thinnest of features
fleshed out with most of the stack.
For this portion,
I can probably punt on many things.
There is no need for HA,
backend workers,
caching,
authentication,
and probably a lot of other things.
The core focus is on the application backend
and the application frontend.

Thankfully, I think the core backend will be very light anyway.
