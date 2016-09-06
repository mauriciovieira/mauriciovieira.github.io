---
layout:     post
comments:   true
title:      "Nolan Dawson's talk on BrazilJS"
subtitle:   "We Can Work It Out: from Web Workers to Service Workers"
date:       2016-09-05 09:15:10
author:     "Mauricio Vieira"
header-img: "img/braziljs-bg.jpg"
---

[Nolan Lawson](https://nolanlawson.com/) is part of [Microsoft Edge](//edge.ms) team and also talked about ServiceWorkers and WebWorkers.

<h2 class="section-heading">Motivation</h2>

According to him, all these stuff blocks the DOM somehow (_those APIs block the DOM, but [not 100%](https://twitter.com/nolanlawson/status/772984268804939777) and also heavily dependent upon the browser and usage_):

<ul>
  <li>[IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/)</li>
  <li> [XHR](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)</li>
  <li> JSON.parse</li>
  <li> fetch</li>
  <li> Garbage collection</li>
  <li> Javascript!</li>
</ul>

Basically, everything made in Javascript blocks the browser because it's single threaded, unless you use something else.

<h2 class="section-heading">WebWorkers</h2>

[Web Workers](https://html.spec.whatwg.org/multipage/workers.html) have been around since, at least, [2009](http://ejohn.org/blog/web-workers/), and is almost ubiquituous right now according to [Can I use](http://caniuse.com/#feat=webworkers):

<img src="{{ site.baseurl }}/img/2016-09-05-braziljs-nolan-lawson/can-i-use-web-workers.jpg" alt="Can I Use: Web Workers?">

The anatomy of the WebWorker is:

{% highlight javascript %}
// index.js

var worker = new Worker('worker.js');
worker.postMessage('ping');
worker.onmessage = function (e) {
  console.log(e.data); // 'pong'
};
{% endhighlight %}

{% highlight javascript %}
// worker.js

self.onmessage = function (e) {
  console.log(e.data); // 'ping'
  self.postMessage('pong');
};
{% endhighlight %}

But WebWorker has some limitations, and then W3C created ServiceWorkers (also described on [Jake Archibald's talk]({% post_url 2016-09-03-braziljs-jake-archibald %})), and then he showed a comparison table for both (and gave some tips).

<img src="{{ site.baseurl }}/img/2016-09-05-braziljs-nolan-lawson/web-workers-versus-service-workers.jpg" alt="Web Workers versus Service Workers">
<blockquote>Shamelessly copied from <a href="https://nolanlawson.github.io/cascadia-2016/#/35">his slides</a>.</blockquote>

<h2 class="section-heading">Further Reading</h2>

He published [his slides](https://nolanlawson.github.io/cascadia-2016/) from [Cascadia Fest 2016](http://2016.cascadiafest.org/) (and the talk seem to be the same, [more or less](https://twitter.com/nolanlawson/status/772984020107866113?cn=cmVwbHk%3D&refsrc=email)) and the [talk](http://2016.cascadiafest.org/speakers/nolan-lawson/) was published too:

Also, Nolan has a post about IndexedDB, stating that [Edge and Safari get less blocked than Firefox and Chrome](https://nolanlawson.com/2015/09/29/indexeddb-websql-localstorage-what-blocks-the-dom/).

{% include youtube.html id="OgLemdR65pE" %}

{% include series/braziljs2016.html %}

