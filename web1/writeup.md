Check out duckrice404's writeup here: <https://deyixtan.github.io/posts/wxmctf2023/web1-the-maze/>

Author note:
- We were able to mess with the URL using `history.pushState` in the JS file. You can read about it
  [here](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState). Large sites like YouTube
  use it all the time, though usually to load another page on top of the current page to create a
  seamless page loading experience.
- Making the doors use `onclick` instead of `href` was another way I tried to make the challenge
  slightly less trivial: usually if you hover over a link, a link preview shows in your browser, but
  with `onclick`, no such thing occurs.
- This is one of the only web challenges that is solvable using just a phone: you should be able to
  catch the `pushState` shenanigans going on with even mobile Chrome.
