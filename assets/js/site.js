/* ============================================================================
   BiomE Lab — site behaviour
   Everything here is progressive: the pages still read fine without JavaScript,
   this file adds the navigation toggle, the interactive cladogram, and renders
   the lists that come from the files in /data.
   ========================================================================== */
(function () {
  "use strict";

  /* --- Navigation --------------------------------------------------------- */
  function initNav() {
    var toggle = document.querySelector(".nav-toggle");
    var nav = document.getElementById("primary-nav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }
    // Mark the current page in the nav.
    var here = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".nav a").forEach(function (a) {
      var target = a.getAttribute("href");
      if (target === here || (here === "index.html" && target === "index.html")) {
        a.setAttribute("aria-current", "page");
      }
    });
    var y = document.getElementById("year");
    if (y) y.textContent = new Date().getFullYear();
  }

  /* --- Cladogram ----------------------------------------------------------
     Sets each branch's dash length so the draw-on animation is proportional,
     and wires the tips to the note line underneath. */
  function initTree() {
    var tree = document.querySelector(".tree");
    if (!tree) return;

    tree.querySelectorAll(".branch-line").forEach(function (path, i) {
      var len = 0;
      try { len = path.getTotalLength(); } catch (e) { len = 1200; }
      path.style.setProperty("--len", len);
      path.style.animationDelay = (i * 0.16) + "s";
    });

    var note = document.querySelector(".tree-note");
    var defaultNote = note ? note.innerHTML : "";
    var tips = tree.querySelectorAll(".tip-group");

    tips.forEach(function (tip, i) {
      tip.style.animationDelay = (0.7 + i * 0.05) + "s";

      function show() {
        tips.forEach(function (t) { t.classList.remove("is-active"); });
        tip.classList.add("is-active");
        if (note) {
          var count = tip.dataset.count
            ? ' <span class="note-count">about ' + tip.dataset.count + " described species.</span> "
            : " ";
          note.innerHTML = "<strong>" + tip.dataset.name + "</strong>" + count + tip.dataset.note;
        }
      }
      function clear() {
        tip.classList.remove("is-active");
        if (note) note.innerHTML = defaultNote;
      }

      tip.addEventListener("mouseenter", show);
      tip.addEventListener("mouseleave", clear);
      tip.addEventListener("focus", show);
      tip.addEventListener("blur", clear);
      tip.addEventListener("click", show);
      tip.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(); }
      });
    });
  }

  /* --- News --------------------------------------------------------------- */
  function renderNews() {
    var host = document.querySelector("[data-news]");
    if (!host || !window.NEWS) return;
    var limit = parseInt(host.dataset.news, 10);
    var items = window.NEWS.slice().sort(function (a, b) { return b.sort - a.sort; });
    if (limit) items = items.slice(0, limit);

    host.innerHTML = items.map(function (it, i) {
      return '<li class="entry' + (i === 0 ? " is-recent" : "") + '">' +
        '<div class="entry-date">' + it.date + "</div>" +
        '<p class="entry-body">' + it.body + "</p></li>";
    }).join("");
  }

  /* --- People ------------------------------------------------------------- */
  function initials(name) {
    return name.split(/\s+/).filter(Boolean).slice(0, 2)
      .map(function (w) { return w[0]; }).join("").toUpperCase();
  }

  function photoBlock(person, dir) {
    // The initials sit behind the photo, so a missing or broken image file
    // degrades to initials instead of an empty box.
    var fallback = '<span class="initials" aria-hidden="true">' + initials(person.name) + "</span>";
    if (person.photo) {
      return '<div class="person-photo">' + fallback + '<img src="assets/img/' + dir + "/" +
        person.photo + '" alt="' + person.name +
        '" loading="lazy" onerror="this.remove()"></div>';
    }
    return '<div class="person-photo">' + fallback + "</div>";
  }

  function renderPI() {
    var host = document.querySelector("[data-pi]");
    if (!host || !window.PI) return;
    var pi = window.PI;

    var titles = (pi.titles || []).join(" &middot; ");
    var bio = (pi.bio || []).map(function (para) { return "<p>" + para + "</p>"; }).join("");
    var links = (pi.links || []).map(function (l) {
      return '<a href="' + l.url + '">' + l.label + "</a>";
    });
    links.push('<a href="mailto:siddharth@csirccmb.org">Email</a>');

    host.innerHTML =
      photoBlock(pi, "people") +
      "<div>" +
        "<h2>" + pi.name + "</h2>" +
        '<p class="person-role">' + pi.role + "</p>" +
        (titles ? '<p class="small muted">' + titles + "</p>" : "") +
        bio +
        '<p class="small">' + links.join(" &nbsp; ") + "</p>" +
      "</div>";
  }

  function renderPeople() {
    var host = document.querySelector("[data-people]");
    if (!host || !window.GROUPS) return;

    host.innerHTML = window.GROUPS.map(function (g) {
      var cards = g.people.map(function (p) {
        var links = (p.links || []).map(function (l) {
          return '<a href="' + l.url + '">' + l.label + "</a>";
        }).join("");
        // Tenure can be given as since (a start year), AY (an academic year
        // range for a dissertation trainee), or Summer (a summer internship
        // year) — whichever is present is shown after the role.
        var tenure = p.since ? " · since " + p.since
          : p.AY ? " · AY " + p.AY
          : p.Summer ? " · Summer " + p.Summer
          : "";
        return '<article class="person" id="' + p.name.toLowerCase().replace(/[^a-z]+/g, "-") + '">' +
          photoBlock(p, "people") +
          '<div class="person-body">' +
            "<h3>" + p.name + "</h3>" +
            '<p class="person-role">' + p.role + tenure + "</p>" +
            (p.note ? '<p class="person-note">' + p.note + "</p>" : "") +
            (links ? '<div class="person-links">' + links + "</div>" : "") +
          "</div></article>";
      }).join("");

      return '<section class="roster-group" id="' + g.id + '">' +
        "<h3>" + g.title + "</h3><p>" + g.blurb + "</p>" +
        '<div class="grid grid-4">' + cards + "</div></section>";
    }).join("");

    var alum = document.querySelector("[data-alumni]");
    if (alum && window.ALUMNI) {
      alum.innerHTML = window.ALUMNI.map(function (a) {
        return "<li><strong>" + a.name + "</strong> <span>" + a.detail + "</span></li>";
      }).join("");
    }
  }

  /* --- Projects ----------------------------------------------------------- */
  function renderProjects() {
    var host = document.querySelector("[data-projects]");
    if (!host || !window.PROJECTS) return;

    host.innerHTML = window.PROJECTS.map(function (p) {
      var meta = "<div>" + p.years + "</div>" +
        (p.funder ? "<div>" + p.funder + "</div>" : "") +
        (p.amount ? "<div>" + p.amount + "</div>" : "") +
        '<div><span class="project-status' + (p.status === "live" ? " live" : "") + '">' +
          (p.status === "live" ? "Running" : "Continuing") + "</span></div>";

      return '<article class="project">' +
        '<div class="project-meta">' + meta + "</div>" +
        "<div><h3>" + p.title + "</h3><p>" + p.summary + "</p>" +
        (p.people ? '<p class="small muted" style="margin-top:.6rem">' + p.people + "</p>" : "") +
        (p.link ? '<p style="margin-top:.6rem"><a href="' + p.link.url + '">' + p.link.label + "</a></p>" : "") +
        "</div></article>";
    }).join("");
  }

  /* --- Publications ------------------------------------------------------- */
  var TAG_LABELS = {
    all: "Everything",
    genomics: "Genomics",
    phylogenomics: "Phylogenomics",
    taxonomy: "Taxonomy",
    spiders: "Spiders",
    acari: "Ticks and mites",
    solifugae: "Camel spiders",
    amblypygi: "Whip spiders",
    community: "Community science"
  };

  function pubHTML(p) {
    var title = p.url
      ? '<a href="' + p.url + '">' + p.title + "</a>"
      : p.title;
    var flag = p.status ? ' <span class="pub-flag">' + p.status + "</span>" : "";
    return '<article class="pub">' +
      '<p class="pub-title">' + title + flag + "</p>" +
      '<p class="pub-authors">' + p.authors + "</p>" +
      '<p class="pub-venue"><em>' + p.venue + "</em>" + (p.detail ? " " + p.detail : "") + "</p>" +
      "</article>";
  }

  function renderPublications() {
    var host = document.querySelector("[data-publications]");
    if (!host || !window.PUBLICATIONS) return;

    var controls = document.querySelector("[data-pub-controls]");
    var state = { tag: "all", q: "" };

    if (controls) {
      var used = ["all"];
      window.PUBLICATIONS.forEach(function (p) {
        (p.tags || []).forEach(function (t) { if (used.indexOf(t) === -1) used.push(t); });
      });
      used = used.filter(function (t) { return TAG_LABELS[t]; });

      controls.innerHTML =
        '<label class="visually-hidden" for="pub-q">Search publications</label>' +
        '<input class="pub-search" id="pub-q" type="search" placeholder="Search titles, authors, journals">' +
        used.map(function (t) {
          return '<button class="chip" type="button" data-tag="' + t + '" aria-pressed="' +
            (t === "all") + '">' + TAG_LABELS[t] + "</button>";
        }).join("");

      controls.addEventListener("click", function (e) {
        var btn = e.target.closest(".chip");
        if (!btn) return;
        state.tag = btn.dataset.tag;
        controls.querySelectorAll(".chip").forEach(function (c) {
          c.setAttribute("aria-pressed", c === btn ? "true" : "false");
        });
        draw();
      });
      controls.addEventListener("input", function (e) {
        if (e.target.id === "pub-q") { state.q = e.target.value.toLowerCase().trim(); draw(); }
      });
    }

    function draw() {
      var list = window.PUBLICATIONS.filter(function (p) {
        var okTag = state.tag === "all" || (p.tags || []).indexOf(state.tag) !== -1;
        var hay = (p.title + " " + p.authors + " " + p.venue).replace(/<[^>]+>/g, "").toLowerCase();
        return okTag && (!state.q || hay.indexOf(state.q) !== -1);
      });

      if (!list.length) {
        host.innerHTML = '<p class="empty">No papers match that. Try a different word, or choose Everything.</p>';
        return;
      }

      var years = [];
      list.forEach(function (p) { if (years.indexOf(p.year) === -1) years.push(p.year); });
      years.sort(function (a, b) { return b - a; });

      host.innerHTML = years.map(function (y) {
        var group = list.filter(function (p) { return p.year === y; });
        return '<section class="pub-year"><h3>' + y + "</h3><div>" +
          group.map(pubHTML).join("") + "</div></section>";
      }).join("");

      var count = document.querySelector("[data-pub-count]");
      if (count) {
        count.textContent = list.length === window.PUBLICATIONS.length
          ? list.length + " papers"
          : list.length + " of " + window.PUBLICATIONS.length + " papers";
      }
    }

    draw();
  }

  function renderBooks() {
    var host = document.querySelector("[data-books]");
    if (!host || !window.BOOKS) return;
    host.innerHTML = window.BOOKS.map(function (b) {
      return '<article class="pub">' +
        '<p class="pub-title">' + (b.url ? '<a href="' + b.url + '">' + b.title + "</a>" : b.title) + "</p>" +
        '<p class="pub-authors">' + b.authors + "</p>" +
        '<p class="pub-venue"><em>' + b.venue + "</em> · " + b.year + "</p></article>";
    }).join("");
  }

  /* --- Featured publication on the home page ------------------------------
     Looks for the one entry in PUBLICATIONS with featured: true. Shows a
     figure + blurb card if it has an image; falls back to a full-width text
     card if figure is empty or the file fails to load, so a missing image
     never looks broken. */
  function renderFeaturedPub() {
    var host = document.querySelector("[data-featured-pub]");
    if (!host || !window.PUBLICATIONS) return;
    var p = window.PUBLICATIONS.find(function (pub) { return pub.featured; });
    if (!p) { host.closest("section").style.display = "none"; return; }

    var titleLink = p.url ? '<a href="' + p.url + '">' + p.title + "</a>" : p.title;
    var venueLine = '<p class="pub-venue"><em>' + p.venue + "</em>" +
      (p.detail ? " " + p.detail : "") + (p.status ? " · " + p.status : "") + "</p>";
    var text =
      '<div class="featured-pub-text">' +
        '<p class="featured-pub-kicker">Latest publication</p>' +
        "<h3>" + titleLink + "</h3>" +
        '<p class="pub-authors">' + p.authors + "</p>" +
        venueLine +
        (p.blurb ? "<p>" + p.blurb + "</p>" : "") +
        (p.url ? '<p><a class="btn btn-solid" href="' + p.url + '">Read the paper</a></p>' : "") +
      "</div>";

    if (p.figure) {
      host.innerHTML =
        '<div class="featured-pub-figure">' +
          '<img src="assets/img/publications/' + p.figure + '" alt="" loading="lazy" ' +
          'onerror="this.closest(\'.featured-pub\').classList.add(\'no-figure\'); this.remove();">' +
        "</div>" + text;
      host.classList.remove("no-figure");
    } else {
      host.innerHTML = text;
      host.classList.add("no-figure");
    }
  }

  /* --- Recent papers on the home page ------------------------------------- */
  function renderHighlights() {
    var host = document.querySelector("[data-highlights]");
    if (!host || !window.PUBLICATIONS) return;
    host.innerHTML = window.PUBLICATIONS.slice(0, 3).map(function (p) {
      return '<article class="card">' +
        "<h3>" + (p.url ? '<a href="' + p.url + '">' + p.title + "</a>" : p.title) + "</h3>" +
        '<p class="pub-venue"><em>' + p.venue + "</em>" + (p.status ? " · " + p.status : "") + "</p>" +
        "</article>";
    }).join("");
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initTree();
    renderNews();
    renderPI();
    renderPeople();
    renderProjects();
    renderPublications();
    renderBooks();
    renderHighlights();
    renderFeaturedPub();
  });
})();
