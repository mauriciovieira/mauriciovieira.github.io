---
layout:     post
title:      "Running jekyll"
subtitle:   "A short howto for future myself."
date:       2016-09-01 06:35:55
author:     "Mauricio Vieira"
header-img: "img/post-bg-03.jpg"
---

<p><a href="http://pages.github.com">Github pages</a> supports <a href="https://jekyllrb.com/">jekyll</a>, a static blog generator written in Ruby.</p>

<p>I got this <a href="http://blackrockdigital.github.io/startbootstrap-clean-blog-jekyll/">blog template</a> after I read a <a href="https://iamtrask.github.io/2016/08/17/grokking-deep-learning/">blog post</a> about <a href="https://en.wikipedia.org/wiki/Deep_learning">deep learning</a>. And here are the steps.</p>

<h2 class="section-heading">Requirements installation</h2>

<p>Firstly, you'll need Ruby installed. I use <a href="http://rvm.io/">Ruby Version Manager</a> (some people prefer <a href="http://rbenv.org/">rbenv</a>). A basic RVM installation should come with <a href="http://rubygems.org/">Rubygems</a>, the ruby packaging system and <a href="http://bundler.io/">bundler</a>, a tool to locally manage your gems.</p>

<p>You should check your installed versions. Currently I'm using:</p>

Ruby:

<pre>
$ ruby --version
ruby 2.2.2p95 (2015-04-13 revision 50295) [x86_64-darwin14]
</pre>

Gem:

<pre>
$ gem --version
2.4.8
</pre>

Bundler:

<pre>
$ bundle --version
Bundler version 1.10.6
</pre>

<h2 class="section-heading">Jekyll installation</h2>

All you need to install jekyll is a Gemfile (i.e. a text file named Gemfile) with the following lines:

<pre>
source 'https://rubygems.org'

gem "jekyll"
</pre>

But I got a sample installation by cloning <a href="http://blackrockdigital.github.io/startbootstrap-clean-blog-jekyll/">Clean Blog</a>.

To install the packages, just go to the directory where Gemfile is and run

<pre>
$ bundle install --path .bundle
</pre>

<p>Bundler makes a local environment for your gems, so you don't have to globally install packages (and mess with your system). Also for production, normally you don't have access or don't want to install ruby gems globally. So I always use bundler.</p>

<p>The <code>--path</code> parameter should point to any <i>dot-name</i> (like <code>.bundle</code>) because jekyll tries to compile itself if it's on it's way (any subdirectory the blog has).</p>

And take look at the versions:

<pre>
$ bundle exec jekyll --version
jekyll 3.2.1
</pre>

<blockquote>I believe that listing the versions now will help myself in the future :-)</blockquote>


<h2 class="section-heading">Writting</h2>

Jekyll has it's conventions for generating posts. Basically, your files should be named <code>YEAR-MONTH-DAY-title.MARKUP</code> inside the <code>_posts</code> directory. For instance, this blog post's source is at <code>_posts/2019-09-01-running-jekyll.markdown</code>.

To run locally before pushing to github:

<pre>
$ bundle exec jekyll serve --watch
</pre> 

And it opens a local server on port <code>4000</code> with the contents.

<h2 class="section-heading">More information</h2>

You just should read <a href="https://jekyllrb.com/docs/quickstart/">jekyll's documentation</a>.
