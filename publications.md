---
layout: page
title: "Publications"
permalink: /publications/
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<h3>Selected publications & demos</h3>
<p class="note"><small class="note">(*) indicates first-author.</small></p>

{% assign pubs = site.data.publications | sort: 'year' | reverse %}
{% for pub in pubs %}
  {% include publication.html pub=pub %}
{% endfor %}