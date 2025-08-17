---
layout: page
title: "News"
permalink: /news/
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<p>Highlights, newest first.</p>

<ul>
{% assign items = site.data.news | sort: 'date' | reverse %}
{% for n in items %}
  <li class="news-item"><strong>{{ n.date | date: "%b %Y" }}</strong> — {{ n.text }}</li>
{% endfor %}
</ul>