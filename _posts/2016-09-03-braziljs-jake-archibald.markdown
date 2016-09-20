---
layout:     post
comments:   true
title:      "Jake Archibald's talk on BrazilJS"
subtitle:   "Instant loading offline-first progressive web apps - the next generation - part II uncovered "
date:       2016-09-03 16:13:53
author:     "Mauricio Vieira"
header-img: "img/braziljs-bg.jpg"
---

<h2 class="section-heading">The invitation</h2>

I think the first video I watched of this conference, back in March was:

{% include youtube.html id="lthear99Snc" %}

<blockquote>Jake Archibald's invitation to the event.</blockquote>

Just a misterious talk about the _future of web performance_. I got excited to attend to the conference because of his and Mattias Johansson's invitations. 

<h2 class="section-heading">The talk</h2>

[Jake Archibald](https://jakearchibald.com) opened the conference with a Game of Thrones Google World video about London, where he works, and Carslile, his hometown. He is a developer advocate at Google Chrome.

Then he presented [Emojoy!](http://jakearchibald-gcm.appspot.com) to introduce how a [progressive webapp](https://developers.google.com/web/progressive-web-apps/) is built. What's basically needed is an <code>index.html</code> and a <code>manifest.json</code> for setting up the app.

So, the app runs on the mobile browser and when the phone is offline (and worse on _Lie-fie_, that is when the phone has a connection but is so weak that doesn't get anything). When offline or on _Lie-fie_, the experience of a web app can be terrible.

<h2 class="section-heading">Service Worker</h2>

To the rescue, the new kid on the block is the [Service Worker](http://www.html5rocks.com/en/tutorials/service-worker/introduction/), a resource that is available on all modern browsers and is accessed through javascript.

<code>on the page:</code>
{% highlight javascript %}
if (navigator.serviceWorker) {
  navigator.serviceWorker.register('/sw.js')
}
{% endhighlight %}

ServiceWorker controls the flow between the browser and the server and thus is able to make _offline-first_ work.

First, the app registers some files to the cache:

<code>sw.js:</code>
{% highlight javascript %}
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('static-v1')
      .then(cache => cache.addAll([
        '/shell-b2a6d8f0.html',
        '/styles-8d723caf.css',
        '/script-4b38af25.js'
      ]))
  )
})
{% endhighlight %}
<blockquote>Sample javascript code I copied from the presentation.</blockquote>

But to create an _offline-first_ experience, the <code>fetch</code> event must be setup.

<code>sw.js:</code>
{% highlight javascript %}
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url)

  if (url.origin == location.origin && url.pathname == '/') {
    event.respondWith(caches.match('/shell-b2a6d8f0.html'))
    return
  }

  event.respondWith(
    caches.match(event.request).
      then(response => response || fetch(event.request))
  )
})
{% endhighlight %}

This way, the cache is the primary resource of data and is falling back to the network. The user always has a good experience, even on _Lie-fie_. And this is called _offline first_.


<h2 class="section-heading">Full talk:</h2>

<b>Update:</b> BrazilJS organizers just published the recordings:

{% include youtube.html id="k6P9ndFNarg" %}

<h2 class="section-heading">Further Reading</h2>

The talk was also about [Streams](https://jakearchibald.com/2016/streams-ftw/), but I won't cover here, except the fact that he was the first one to play with the poo emoji (💩).

<s>I did not find his slides...</s> <b>Update:</b> Jake [published](https://twitter.com/jaffathecake/status/772211953460707328) the slides:

Part I:
<script async class="speakerdeck-embed" data-id="f3406bb4c82744738ede2f3d2ab1bb74" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

Part II - uncovered:
<script async class="speakerdeck-embed" data-id="ef3764c11dbf4091b1bcaf2750f9372b" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

The official [tutorial](https://developers.google.com/web/fundamentals/getting-started/) about progressive webapps and the Emojoy! [source code](https://github.com/jakearchibald/emojoy/) are also available. 😃

{% include series/braziljs2016.html %}
