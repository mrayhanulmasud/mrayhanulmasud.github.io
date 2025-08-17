---
layout: page
title: "Projects"
permalink: /projects/
---

<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">

<p>Selected repositories (recently updated). For a full list, see my <a href="https://github.com/mrayhanulmasud">GitHub profile</a>.</p>

<div id="repos" class="grid-two"></div>

<script>
async function loadRepos() {
  const user = "mrayhanulmasud"; // change if needed
  const res = await fetch(`https://api.github.com/users/${user}/repos?per_page=12&sort=updated`);
  const data = await res.json();
  const container = document.getElementById("repos");
  container.innerHTML = "";
  (data || []).forEach(r => {
    const card = document.createElement("div");
    card.className = "pub";
    const name = document.createElement("div");
    name.innerHTML = `<strong><a href="${r.html_url}" target="_blank" rel="noopener">${r.name}</a></strong>`;
    const desc = document.createElement("p");
    desc.textContent = r.description || "—";
    const meta = document.createElement("div");
    meta.innerHTML = `<small class="note">★ ${r.stargazers_count} • Updated ${new Date(r.updated_at).toLocaleDateString()}</small>`;
    card.appendChild(name); card.appendChild(desc); card.appendChild(meta);
    container.appendChild(card);
  });
}
loadRepos();
</script>