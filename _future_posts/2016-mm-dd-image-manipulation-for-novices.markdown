---
layout:     post
title:      "Image manipulation for novices"
subtitle:   "Using imagemagick to transform an image to be the new background"
date:       2016-xx-yy 12:00:00
author:     "Mauricio Vieira"
header-img: "img/home-bg.jpg"
---

I don't know how to use imaging software. I mean, I used to use Gimp and Inkscape when I was a Debian user, but since when I switched to MacOSx, I just stopped. Inkscape 

<h2 class="section-heading">The Problem</h2>

<p>Create a background image for my this blog</p>

<h2 class="section-heading">The Solution</h2>

<p>First I got to find an image. 

https://search.creativecommons.org/

<a href="#">
    <img src="{{ site.baseurl }}/img/post-sample-image.jpg" alt="Post Sample Image">
</a>
<span class="caption text-muted">The original image.</span>

<p>Reduce the size:

<pre>
convert pexels-photo-139135.jpeg -resize 1900x872 home-bg2.jpg
</pre>

<p>Invert the colors.

<pre>
convert home-bg2.jpg -negate home-bg.jpg
</pre>

<a href="#">
    <img src="{{ site.baseurl }}/img/post-sample-image.jpg" alt="Post Sample Image">
</a>
<span class="caption text-muted">The final image.</span>

You can find more about ImageMagick...
