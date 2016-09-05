---
layout:     post
comments:   true
title:      "Ruth John's talk on BrazilJS"
subtitle:   "Let's talk about midi"
date:       2016-09-04 23:26:10
author:     "Mauricio Vieira"
header-img: "img/braziljs-bg.jpg"
---

[Ruth](http://rumyrashead.com/)'s talk was about [MIDI](https://en.wikipedia.org/wiki/MIDI). She introduced [Cameron's World](http://www.cameronsworld.net/) to say it's not MIDI but digital audio. 

There is a [Web Midi API](https://webaudio.github.io/web-midi-api/) that allows midi to be played by Javascript (and I had no idea of that before this talk) along with [Web Audio API](https://webaudio.github.io/).

Also there is an specification for [Timing Object](http://webtiming.github.io/timingobject/) that enables a user to overload and configure and compose instruments using javascript.

She did a [live demo](https://mididemos.herokuapp.com/) with a keyboard for participants to try the notes and they were played live (although overload).

I found the [MIDI.js](https://galacticmilk.com/midi-js/) lib that provides an easier way for using all these things. [Watch this demo](https://galacticmilk.com/piano/). 

<h2 class="section-heading">Further information</h2>

I saw a similar talk on [JSConf Uruguay](https://jsconf.uy/) too. This is better than [BrazilJS conference video](https://www.youtube.com/watch?v=tJ0XV9W4nHw) because it is cut.

{% include youtube.html id="khsBjXKJOPs" %}

(and on [Web progressions](https://www.youtube.com/watch?v=x2v3mQOvOms)).

But couldn't find the slides on [speakerdeck](https://speakerdeck.com/rumyra).

PS: She was the second speaker to mention the poo emoji (💩), and actually she played the emoji (that is a 4 characters UTF-8 word) as midi on her talk.

{% include series/braziljs2016.html %}
