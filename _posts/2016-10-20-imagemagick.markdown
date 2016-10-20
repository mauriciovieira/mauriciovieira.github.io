---
layout:     post
title:      "Using imagemagick"
subtitle:   "To make background images"
date:       2016-10-20 10:50:00
author:     "Mauricio Vieira"
header-img: "img/post-bg-04.jpg"
---

I don't know how to use imaging software. I mean, I used to use Gimp and
Inkscape when I was a more frequent Debian user, but since when I switched to
MacOSx, I just stopped. A few days ago I wanted to create a new background
image for all python-related posts.

The only package needed is <a href="http://www.imagemagick.org/">ImageMagick</a>.

### 1. First I got to find an image labeled for reuse 

I used Google Image search _labeled for use_ filter and got pointed to <a href="https://commons.wikimedia.org/wiki/File:Python_natalensis_Smith_1840.jpg">some python wikimedia image</a>. As it is labeled as public domain, I am free to do anything with it :-).

```
$ wget https://upload.wikimedia.org/wikipedia/commons/a/ab/Python_natalensis_Smith_1840.jpg
$ mv Python_natalensis_Smith_1840.jpg post-bg-python-01.jpg
```

<img src="{{ site.baseurl }}/img/2016-10-20-imagemagick/post-bg-python-01-20perc.jpg" alt="Python_natalensis_Smith_1840">
<span class="caption text-muted">The "original" image (resized to 20%).</span>

### 2. Resizing

ImageMagick allows us to <a href="http://www.imagemagick.org/Usage/resize/">resize the image</a> in many ways.

```
$ convert post-bg-python-01.jpg -resize 1900x600 post-bg-python-01-1900.jpg
$ identify post-bg-python-*
post-bg-python-01-1900.jpg JPEG 1469x600 1469x600+0+0 8-bit sRGB 823KB 0.010u 0:00.000
post-bg-python-01.jpg JPEG 2941x1201 2941x1201+0+0 8-bit sRGB 2.396MB 0.000u 0:00.000
```

### 3. Changing colors

Finally, it is possible to _negate_ the colors.

```
$ convert post-bg-python-01-1900.jpg -negate post-bg-python-01-negate.jpg
```

<img src="{{ site.baseurl }}/img/2016-10-20-imagemagick/post-bg-python-01-negate-20perc.jpg" alt="Inverted color">
<span class="caption text-muted">The final image.</span>

### Real life example

The first post I used this background image was the post about [anaconda]({% post_url 2016-10-15-anaconda %}).
