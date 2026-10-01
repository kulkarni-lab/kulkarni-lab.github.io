# -*- coding: utf-8 -*-
"""Page bodies for build.py. Each entry is (filename, title, description, body)."""

import math

# The section rule is the logo's argument in miniature: one stem, one branch that
# stops at a single tip, one branch that keeps splitting.
BRANCH = ('<svg class="branch" viewBox="0 0 40 22" aria-hidden="true">'
          '<path d="M0 10 H10 M10 4 V13.5 M10 4 H26 M10 13.5 H18 '
          'M18 8 V19 M18 8 H36 M18 13.5 H36 M18 19 H36"/></svg>')

# --- The chelicerate cladogram, with described-species richness ---------------
# Topology follows:
#   (Pycnogonida,((Xiphosura,Opiliones,Solifugae,Acariformes,Parasitiformes,
#   Palpigradi,Ricinulei),((Scorpiones,Pseudoscorpiones),((Amblypygi,(Uropygi,
#   Schizomida)),Araneae))));
# i.e. Scorpiones+Pseudoscorpiones are sister to Tetrapulmonata (Arachnopulmonata),
# not part of the large unresolved comb. Edit TREE to change branching order;
# edit TAXA for names, counts and hover notes. Everything else — the drawing,
# both tree sizes, the richness bars — follows automatically.
TREE = (
    "Pycnogonida",
    (
        ("Xiphosura", "Opiliones", "Solifugae", "Acariformes", "Parasitiformes",
         "Palpigradi", "Ricinulei"),
        (
            ("Scorpiones", "Pseudoscorpiones"),
            (
                ("Amblypygi", ("Uropygi", "Schizomida")),
                "Araneae",
            ),
        ),
    ),
)

# name: (common name, approximate described species, hover note)
# Counts are approximate and should be checked against current catalogues.
TAXA = {
    "Pycnogonida": ("sea spiders", 1300,
        "We helped assemble the genome that revealed a shared Hox cluster motif in arthropods with a reduced rear body."),
    "Xiphosura": ("horseshoe crabs", 4,
        "Four living species, and a lineage older than most of this tree. Their gene trees conflict with the species tree in a way that points to ancient hybridisation."),
    "Opiliones": ("harvestmen", 6700,
        "Diverse, ancient, and still moving around the tree depending on which data you use."),
    "Solifugae": ("camel spiders", 1200,
        "We published their first global phylogeny and named three new families in the process."),
    "Acariformes": ("mites", 32000,
        "One of the two great acarine radiations, and the one with the most eroded genomes we have looked at."),
    "Parasitiformes": ("ticks and mites", 12500,
        "Our first paper from Hyderabad settled how the major acarine lineages fit together."),
    "Palpigradi": ("microwhip scorpions", 130,
        "The smallest and most elusive arachnid order, rarely collected and still short of a well-sampled phylogeny."),
    "Ricinulei": ("hooded tickspiders", 100,
        "Slow-moving, armoured, and known from a fossil record older than most of their relatives' family trees."),
    "Scorpiones": ("scorpions", 2900,
        "They carry a whole-genome duplication that they share with spiders and vinegaroons — and, on this topology, are the nearest relatives of that whole group."),
    "Pseudoscorpiones": ("pseudoscorpions", 4000,
        "Thirty times more species than a vinegaroon, on a branch of much the same age, and stubbornly hard to place."),
    "Amblypygi": ("whip spiders", 260,
        "Rediscovering one relict lineage unlocked the first global phylogeny of the order."),
    "Uropygi": ("vinegaroons", 120,
        "A hundred-odd species, and exactly the same age as the spiders. We assembled the first chromosome-level genome for the order."),
    "Schizomida": ("short-tailed whip scorpions", 350,
        "The closest living relatives of the vinegaroons, and rarely collected as anything more than a bycatch."),
    "Araneae": ("spiders", 53000,
        "About 53,000 described species, and the thread that runs through everything the lab does."),
}

MAXC = max(v[1] for v in TAXA.values())
FLOOR = 2.0


def bar_frac(count):
    """Log scale with a floor, so four species and fifty thousand both read."""
    return (math.log10(count) - math.log10(FLOOR)) / (math.log10(MAXC) - math.log10(FLOOR))


def fmt(n):
    return f"{n:,}"


# --- Generic cladogram layout ---------------------------------------------
# Walks TREE once, assigns each leaf an evenly spaced y (top to bottom, in the
# order it appears in TREE) and each internal node the mean y of its children.
# x is assigned by depth on a canonical scale where tips sit at x = 330; the
# renderer below scales x (never y) to fit the full-size and compact SVGs.
_CANON_TIP_X = 330.0
_Y0, _Y1 = 26.0, 386.0
_ROOT_STUB_X = 6.0

_LEAF_ORDER = []


def _collect_leaves(node):
    if isinstance(node, str):
        _LEAF_ORDER.append(node)
    else:
        for child in node:
            _collect_leaves(child)


_collect_leaves(TREE)
_N = len(_LEAF_ORDER)
_LEAF_Y = {name: _Y0 + i * (_Y1 - _Y0) / (_N - 1) for i, name in enumerate(_LEAF_ORDER)}


def _build(node):
    if isinstance(node, str):
        return {"leaf": True, "name": node, "y": _LEAF_Y[node]}
    children = [_build(c) for c in node]
    return {"leaf": False, "children": children, "y": sum(c["y"] for c in children) / len(children)}


def _assign_depth(node, depth):
    node["depth"] = depth
    if not node["leaf"]:
        for c in node["children"]:
            _assign_depth(c, depth + 1)


_LAYOUT = _build(TREE)
_assign_depth(_LAYOUT, 1)


def _max_internal_depth(node):
    if node["leaf"]:
        return 0
    return max([node["depth"]] + [_max_internal_depth(c) for c in node["children"]])


_MAX_DEPTH = _max_internal_depth(_LAYOUT)
# Canonical x per depth: depth 1 (root) starts just past the stub; depth
# _MAX_DEPTH sits comfortably before the tips so the last leaf-stub is legible.
_X_START, _X_END = 20.0, 295.0
_X_OF_DEPTH = {
    d: _X_START + (d - 1) * (_X_END - _X_START) / max(1, _MAX_DEPTH - 1)
    for d in range(1, _MAX_DEPTH + 1)
}


def _segments(node, out):
    """Collect (x_canon, y0, y1, is_vertical, x2_canon) drawing segments."""
    if node["leaf"]:
        return
    x = _X_OF_DEPTH[node["depth"]]
    ys = [c["y"] for c in node["children"]]
    out.append(("V", x, min(ys), max(ys)))
    for c in node["children"]:
        target_x = _CANON_TIP_X if c["leaf"] else _X_OF_DEPTH[c["depth"]]
        out.append(("H", x, c["y"], target_x))
        _segments(c, out)


_SEGMENTS = [("H", _ROOT_STUB_X, _LAYOUT["y"], _X_OF_DEPTH[1])]
_segments(_LAYOUT, _SEGMENTS)


def branch_paths(tip_x):
    """Scale canonical x-coordinates (never y) to an actual tip position."""
    ratio = tip_x / _CANON_TIP_X
    paths = []
    for kind, x, a, b in _SEGMENTS:
        x = x * ratio
        if kind == "V":
            paths.append(f"M{x:.1f} {a:.1f} V{b:.1f}")
        else:
            paths.append(f"M{x:.1f} {a:.1f} H{(b * ratio):.1f}")
    return paths


def tree_svg(variant):
    """variant 'full' for wide screens, 'compact' for phones."""
    if variant == "full":
        W, tip_x, lab_x, bar_x, bar_w, hit_w = 646, 250, 262, 392, 200, 384
        show_common, show_count = True, True
    else:
        W, tip_x, lab_x, bar_x, bar_w, hit_w = 380, 106, 116, 264, 106, 266
        show_common, show_count = False, False

    p = [f'<svg class="tree-svg tree-{variant}" viewBox="0 0 {W} 412" role="img" '
         f'aria-labelledby="tt-{variant} td-{variant}">',
         f'<title id="tt-{variant}">Described species richness across the chelicerates</title>',
         f'<desc id="td-{variant}">A branching diagram of {_N} chelicerate lineages, each with a '
         f'bar showing approximate described species richness on a logarithmic scale. Horseshoe '
         f'crabs have four living species; spiders have about fifty-three thousand. Scorpions and '
         f'pseudoscorpions are drawn as the nearest relatives of spiders, whip spiders, vinegaroons '
         f'and short-tailed whip scorpions together.</desc>']

    for d in branch_paths(tip_x):
        p.append(f'<path class="branch-line" d="{d}"/>')

    for name in _LEAF_ORDER:
        common, count, note = TAXA[name]
        y = _LEAF_Y[name]
        w = max(3.0, bar_frac(count) * bar_w)
        p.append(
            f'<g class="tip-group" tabindex="0" role="button" data-name="{name}" '
            f'data-count="{fmt(count)}" data-note="{note}">'
            f'<rect class="tip-hit" x="{tip_x - 8}" y="{y - 14:.1f}" width="{hit_w}" height="28"/>'
            f'<circle class="tip-dot" cx="{tip_x}" cy="{y:.1f}" r="3.4"/>'
            f'<text class="tip-label" x="{lab_x}" y="{(y - 1 if show_common else y + 4):.1f}">{name}</text>'
            + (f'<text class="tip-common" x="{lab_x}" y="{y + 11:.1f}">{common}</text>' if show_common else "")
            + f'<rect class="tip-bar" x="{bar_x}" y="{y - 4:.1f}" width="{w:.1f}" height="8"/>'
            + (f'<text class="tip-count" x="{bar_x + w + 7:.1f}" y="{y + 3.5:.1f}">{fmt(count)}</text>'
               if show_count else "")
            + '</g>')
    p.append('</svg>')
    return "\n      ".join(p)


# --- Home ---------------------------------------------------------------------
HOME = f"""
<section class="hero">
  <div class="shell hero-grid">
    <div>
      <h1>Same ancestor, same age, wildly different outcomes.</h1>
      <p class="hero-place"><strong>BiomE Lab</strong> &middot; Biodiversity Genomics and Evolution &middot;
        Laboratory for Conservation of Endangered Species, CSIR-CCMB, Hyderabad</p>
      <p class="lede">Spiders number about 53,000 described species. Tetrapulmonates, their
        sister group which diverged at the same time, are merely in a few hundreds. We use genomes, phylogenetics, collections and fieldwork
        across the chelicerates to work out what makes the difference.</p>
      <div class="btn-row">
        <a class="btn btn-solid" href="research.html">See the research</a>
        <a class="btn" href="students.html">Work with us</a>
      </div>
    </div>
    <div class="tree-panel">
      <div class="tree">
      {tree_svg("full")}
      {tree_svg("compact")}
      </div>
      <p class="tree-note">Eleven lineages of one common ancestor. The bars are described species on
        a logarithmic scale &mdash; on a linear one, most of them would be invisible.</p>
      <p class="tree-caption">Select a lineage to see where our work touches it.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>One split, four fates</h2>
      <p>The clearest version of the problem sits inside a single well-supported clade.</p>
    </div>
    <div class="split-grid">
      <div>
        <p>Tetrapulmonata contains four living lineages, all descended from one ancestor, all
          therefore exactly the same age. One of them holds more than ninety-eight per cent of the
          species.</p>
        <p>No environmental accident explains this on its own, and neither does collecting effort.
          Something about how these genomes are built, rearranged and duplicated appears to let one
          lineage keep generating species while its sisters did not. Finding out what is the lab's
          central question.</p>
      </div>
      <div class="split-figure">
        <div class="ratio-bar" role="img"
             aria-label="Of about 53,730 described tetrapulmonate species, 98.6 per cent are spiders, 0.7 per cent Schizomida, 0.5 per cent Amblypygi and 0.2 per cent Uropygi.">
          <span class="ratio-seg ratio-rich" style="width:98.6%"></span>
          <span class="ratio-seg ratio-a" style="width:0.65%"></span>
          <span class="ratio-seg ratio-b" style="width:0.48%"></span>
          <span class="ratio-seg ratio-c" style="width:0.22%"></span>
        </div>
        <dl class="ratio-key">
          <div><dt><span class="sw sw-rich"></span>Araneae</dt><dd>spiders</dd><dd class="n">53,000</dd></div>
          <div><dt><span class="sw sw-a"></span>Schizomida</dt><dd>short-tailed whip scorpions</dd><dd class="n">350</dd></div>
          <div><dt><span class="sw sw-b"></span>Amblypygi</dt><dd>whip spiders</dd><dd class="n">260</dd></div>
          <div><dt><span class="sw sw-c"></span>Uropygi</dt><dd>vinegaroons</dd><dd class="n">120</dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="section featured-pub-section">
  <div class="shell">
    <div class="featured-pub" data-featured-pub></div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>How we go at it</h2>
      <p>Four threads, one question underneath all of them.</p>
    </div>
    <div class="grid grid-2">
      <article class="theme">
        <h3>Asymmetric diversification</h3>
        <p>We look for the genomic correlates that separate the runaway lineages from the ones that
          stood still: gene family turnover, chromosome rearrangement, whole-genome duplication and
          rates of molecular change, tested against richness rather than assumed.</p>
        <p class="taxa"><span>Acari</span><span>Solifugae</span><span>Uropygi</span><span>Araneae</span></p>
      </article>
      <article class="theme">
        <h3>Building the chelicerate tree</h3>
        <p>You cannot ask why a lineage diversified until you know where it sits. We design
          ultraconserved element probe sets, assemble chromosome-level genomes, and test whether gene
          order across whole chromosomes carries signal that sequences miss.</p>
        <p class="taxa"><span>Phylogenomics</span><span>UCEs</span><span>Macrosynteny</span></p>
      </article>
      <article class="theme">
        <h3>Biodiversity discovery</h3>
        <p>Richness counts are only as good as the taxonomy behind them, and much of South Asian
          arachnid diversity has never been collected. We run field expeditions, work through museum
          collections, and describe what turns out to be new.</p>
        <p class="taxa"><span>Western Ghats</span><span>Eastern Ghats</span><span>Arunachal Pradesh</span></p>
      </article>
      <article class="theme">
        <h3>Community science</h3>
        <p>Where a species actually lives is a question thousands of people can answer better than
          any one lab. Through SpiderIndia we work with more than 8,000 naturalists across South Asia
          whose observations become distribution data, new records and sometimes new species.</p>
        <p class="taxa"><span>SpiderIndia</span><span>iNaturalist</span><span>India Biodiversity Portal</span></p>
      </article>
    </div>
    <div class="stats">
      <div><div class="stat-n">1st</div><div class="stat-l">New genomes for Opilioacarida, Palpigradi, Ricinulei</div></div>
      <div><div class="stat-n">1st</div><div class="stat-l">Global phylogeny of Solifugae</div></div>
      <div><div class="stat-n">1st</div><div class="stat-l">Global phylogeny of Amblypygi</div></div>
      <div><div class="stat-n">2</div><div class="stat-l">New Solifugae suborders</div></div>
      <div><div class="stat-n">3</div><div class="stat-l">New Solifugae families</div></div>
      <div><div class="stat-n">8,000+</div><div class="stat-l">community observers</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Latest from the bench</h2>
      <p>The three most recent things out of the lab. <a href="publications.html">All publications</a>.</p>
    </div>
    <div class="grid grid-3" data-highlights></div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Lab news</h2>
      <p>People arriving, papers landing, places we have been. <a href="news.html">Full archive</a>.</p>
    </div>
    <ul class="timeline" style="list-style:none" data-news="6"></ul>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="grid grid-2">
      <div class="callout">
        <h3>Doctoral and postdoctoral positions</h3>
        <p>A five-year Ph.D. position at LaCONES for someone who wants to spend it on genomes,
          phylogenies and arachnids, plus support for postdoctoral fellowship applications.</p>
        <p><a class="btn btn-solid" href="join.html">Positions</a></p>
      </div>
      <div class="callout warn">
        <h3>Dissertations, internships and summer projects</h3>
        <p>BS-MS and Masters dissertations, CCMB training programmes and short internships, with a
          list of projects that are available right now.</p>
        <p><a class="btn btn-solid" href="students.html">For students</a></p>
      </div>
    </div>
  </div>
</section>
"""

# --- Research -----------------------------------------------------------------
RESEARCH = f"""
<div class="shell page-head">
  <h1>Research</h1>
  <p class="lede">We study asymmetry in arthropod evolution: why lineages of equal age end up so
    unequal in number, form and range. Chelicerates make an unusually good test case, because the
    asymmetry is extreme, the tree is still being built, and the genomes are only now arriving.</p>
</div>

<section class="section" id="asymmetry">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Asymmetric diversification</h2>
    </div>
    <div class="measure">
      <p>Acariformes and Parasitiformes together account for well over forty thousand described
        species. Their relatives the camel spiders and vinegaroons account for about twelve hundred
        and about a hundred and twenty. Age does not explain the gap. Neither does sampling effort,
        though it makes every number on this page noisier than anyone would like.</p>
      <p>We treat this as a genomic question. Our work compares gene family birth and death, the
        retention or loss of ancient linkage groups, and the signature of whole-genome duplication
        across chelicerate genomes, asking which of these track species richness and which merely
        track time. The vinegaroon genome we assembled carries a duplication older than the
        Silurian. The acarine genomes we are assembling now appear to have shed material in a
        coordinated way, which is not what you would naively expect of a lineage that went on to
        radiate.</p>
    </div>
  </div>
</section>

<section class="section" id="tree">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Building the chelicerate tree of life</h2>
    </div>
    <div class="measure">
      <p>Comparative questions need a tree, and for arachnids large parts of that tree have been
        stuck for decades. Several orders form what has been called the apulmonate polytomy: no
        matter how much sequence data is thrown at it, the branching order refuses to settle. On the
        home page that polytomy is drawn honestly, as an unresolved comb.</p>
      <p>We attack it from three sides. We design and benchmark target-capture probe sets &mdash;
        Spider2Kv1 for spiders and a broader chelicerate set &mdash; that let any lab collect
        hundreds of orthologous loci cheaply. We assemble chromosome-level genomes for lineages that
        have none. And we test whether macrosynteny, the arrangement of genes along whole
        chromosomes, offers the near-noiseless phylogenetic character it has been claimed to be. So
        far the honest answer is that it recapitulates the same conflicts as sequence data, which is
        itself worth knowing.</p>
    </div>
  </div>
</section>

<section class="section" id="discovery">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Biodiversity discovery and natural history</h2>
    </div>
    <div class="measure">
      <p>Every richness number on this page rests on somebody having collected, compared and named
        the specimens behind it. A great deal of chelicerate diversity in South Asia has never been
        collected, and much of what has been collected sits undescribed in museum drawers.</p>
      <p>Species discovery is therefore not a side activity for us. Without specimens and tissue
        there is nothing to sequence, and without names there is nothing to count. Field expeditions
        have taken the lab to the Western Ghats, the Eastern Ghats, Kerala and Arunachal Pradesh,
        alongside collections work at the Smithsonian, the California Academy of Sciences, Naturalis
        and elsewhere. This thread has produced new species of spiders and assassin bugs, new records
        for India, and three new families of Solifugae.</p>
    </div>
  </div>
</section>

<section class="section" id="community">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Community science</h2>
    </div>
    <div class="measure">
      <p>Distribution data is the one kind of biodiversity data that scales with people rather than
        equipment. SpiderIndia, which the lab coordinates, is a network of more than 8,000
        naturalists, photographers and students across the Indian subcontinent who record spiders on
        iNaturalist and the India Biodiversity Portal.</p>
      <p>Their observations have produced range extensions, first records and material for
        description, and they underpin our work on where introduced species such as the Australian
        redback have established. <a href="spiderindia.html">More about SpiderIndia</a>.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Tools and data</h2>
      <p>Everything we build is meant to be used by other labs.</p>
    </div>
    <div class="grid grid-3">
      <article class="card">
        <h3>Spider2Kv1 probe set</h3>
        <p>Ultraconserved element probes designed for spiders, now in use worldwide for resolving
          nodes across Araneae.</p>
      </article>
      <article class="card">
        <h3>Chelicerata probe set</h3>
        <p>A broader UCE set covering the arachnid orders, developed for phylogenomics beyond
          spiders.</p>
      </article>
      <article class="card">
        <h3><a href="https://github.com/kulkarni-lab/GenomeCartographer/tree/main">GenomeCartographer</a></h3>
        <p>Tools for querying and analysing molecular sequences for phylogenetic work.</p>
      </article>
      <article class="card">
        <h3>Genome assemblies</h3>
        <p>Chromosome-level assemblies produced by the lab and collaborators, including the giant
          vinegaroon, released with each paper.</p>
      </article>
    </div>
  </div>
</section>
"""

# --- People -------------------------------------------------------------------
PEOPLE = f"""
<div class="shell page-head">
  <h1>People</h1>
  <p class="lede">A small group at LaCONES, CSIR-CCMB, working across wet lab, computation and
    fieldwork, together with students and collaborators elsewhere in India and abroad.</p>
</div>

<section class="section">
  <div class="shell">
    <div class="person-lead" data-pi></div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div data-people></div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Past members and mentees</h2>
    </div>
    <ul class="alumni-list" data-alumni></ul>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="callout">
      <h3>Your name could go here</h3>
      <p>We take doctoral students through the CCMB programme, host dissertation and internship
        students through several routes, and are glad to hear from postdocs with their own ideas.</p>
      <p><a class="btn btn-solid" href="join.html">Positions</a>
         &nbsp; <a class="btn" href="students.html">For students</a></p>
    </div>
  </div>
</section>
"""

# --- Publications -------------------------------------------------------------
PUBLICATIONS = f"""
<div class="shell page-head">
  <div class="page-head-split">
    <div>
      <h1>Publications</h1>
      <p class="lede">Research papers and book/-chapters chelicerate phylogenomics, comparative genomics and systematics. </p>
    </div>
    <div class="pub-covers" data-pub-covers></div>
  </div>
</div>

<section class="section">
  <div class="shell">
    <div class="pub-controls" data-pub-controls></div>
    <p class="small muted" data-pub-count></p>
    <div data-publications></div>
    <p class="legend">Bold marks Siddharth Kulkarni; an underline marks a lab member. An asterisk
      marks corresponding authorship. Google Scholar: https://scholar.google.com/citations?user=xo9jTM0AAAAJ&hl.</p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Books and chapters</h2>
    </div>
    <div data-books></div>
  </div>
</section>
"""

# --- News ---------------------------------------------------------------------
NEWS = """
<div class="shell page-head">
  <h1>News and updates</h1>
  <p class="lede">People joining, papers landing, meetings run and places visited, newest first.</p>
</div>

<section class="section">
  <div class="shell">
    <ul class="timeline" style="list-style:none" data-news="0"></ul>
  </div>
</section>
"""

# --- SpiderIndia --------------------------------------------------------------
SPIDERINDIA = f"""
<div class="shell page-head">
  <h1>SpiderIndia</h1>
  <p class="lede">A community science initiative to map the spiders of the Indian subcontinent, run
    with and by the people who go out and find them.</p>
</div>

<section class="section">
  <div class="shell measure">
    <p>Spiders are the richest chelicerate lineage by a wide margin, and in South Asia they are also
      among the least recorded. Closing that gap is not something a lab can do on its own.</p>
    <p>SpiderIndia began in 2005 as a mailing list started by
      <a href="http://vijaybarve.net/">Vijay Barve</a>, where naturalists helped each other identify
      spiders from field photographs. Membership was around 400 by 2011, when the community moved to
      <a href="https://www.facebook.com/groups/SpiderIndia/">Facebook</a>. A group on the
      <a href="https://indiabiodiversity.org/group/spiderindia/show">India Biodiversity Portal</a>
      followed in 2012, and later an
      <a href="https://www.inaturalist.org/projects/spiderindia">iNaturalist project</a> to capture
      Indian araneae records systematically in one place. Today more than 8,000 people take part.</p>
    <p>Annual meets began in Kolkata in 2016 and have run since, moving each year to a different
      landscape. Spider Week, held each August, is a concentrated recording push: the 2020 edition
      logged over 5,500 observations from 225 participants, and 2021 passed 5,000 again.</p>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>How to take part</h2>
    </div>
    <div class="grid grid-3">
      <article class="card">
        <h3>Record what you find</h3>
        <p>Photograph spiders wherever you are and post them to the
          <a href="https://www.inaturalist.org/projects/spiderindia">SpiderIndia project on
          iNaturalist</a>. Location and date matter more than a perfect picture.</p>
      </article>
      <article class="card">
        <h3>Ask for an identification</h3>
        <p>The <a href="https://www.facebook.com/groups/SpiderIndia/">Facebook group</a> is where
          most identification happens, with experienced arachnologists answering.</p>
      </article>
      <article class="card">
        <h3>Come to a meet</h3>
        <p>Meets are held annually, in the field, and are open to anyone. Write to
          <a href="mailto:spiderindia.in@gmail.com">spiderindia.in@gmail.com</a> for the next one.</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Past meets</h2>
    </div>
    <dl class="rows">
      <div class="row"><dt>7th meet, 2025</dt><dd>Sirumalai, Tamil Nadu &mdash; spiders of the Eastern Ghats.</dd></div>
      <div class="row"><dt>6th meet, 2023</dt><dd>Near Desert National Park, Rajasthan.</dd></div>
      <div class="row"><dt>5th meet, 2021</dt><dd>Auroville, Tamil Nadu, hosted by Anubhav Agarwal.
        <a href="https://www.inaturalist.org/observations?project_id=123867">Observations</a>.</dd></div>
      <div class="row"><dt>4th meet, 2019</dt><dd>Castle Rock, Karnataka.</dd></div>
      <div class="row"><dt>3rd meet, 2018</dt><dd>Amba, northern Western Ghats.
        <a href="https://flic.kr/s/aHsmyqnzpP">Photographs by Atul Vartak</a>.</dd></div>
      <div class="row"><dt>2nd meet, 2017</dt><dd>Gibbon Wildlife Sanctuary, Assam. Reported in the
        newsletter of the British Arachnological Society.</dd></div>
      <div class="row"><dt>1st meet, 2016</dt><dd>Kolkata, West Bengal.</dd></div>
    </dl>
    <p class="small muted" style="margin-top:1rem">No meeting was held in 2020 because of the
      pandemic; Spider Week ran online instead.</p>
  </div>
</section>
"""

# --- Positions (PhD and postdoc) ----------------------------------------------
JOIN = f"""
<div class="shell page-head">
  <h1>Positions</h1>
  <p class="lede">Doctoral and postdoctoral routes into the lab. If you are looking for a
    dissertation project, a summer training place or an internship, the
    <a href="students.html">students page</a> is the one you want.</p>
</div>

<section class="section">
  <div class="shell">
    <div class="callout">
      <h2>Ph.D. position in ecology and evolution</h2>
      <p><strong>Five years, starting January 2027, at CSIR-CCMB, Hyderabad.</strong>
        Applications close <strong>31 October 2026</strong>.</p>
    </div>

    <div class="measure" style="margin-top:2rem">
      <p>A staggering megadiversity in some lineages, set against disparately microdiverse close
        relatives, poses a fundamental question: what makes one lineage so much more diverse than its
        sister? This has fascinated biologists since the early days of systematics, because the
        patterns of origin and diversification across space and time are so strikingly uneven.</p>
      <p>In our newly started lab we explore the genetic underpinnings of that asymmetry, focusing on
        Chelicerata &mdash; ticks, mites, spiders, scorpions, camel spiders and the rest &mdash;
        using genomic, computational and experimental approaches in an evolutionary framework.</p>
      <p>Recent work established the plesiomorphic configuration of gene families using the first
        chromosome-scaffolded genome for Uropygi, which shares a whole-genome duplication with
        spiders and with sea spiders. Earlier work closed several long-standing gaps in the
        chelicerate tree: the first global phylogenies for Amblypygi and Solifugae, and the most
        comprehensive phylogeny of the major spider lineages to date. We designed the Spider2Kv1 and
        Chelicerata probe sets for ultraconserved elements, now used worldwide.</p>
      <p>We are based at the Laboratory for Conservation of Endangered Species (LaCONES), a dedicated
        facility for ecological, evolutionary and conservation research at CSIR-CCMB.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Who can apply</h2>
    </div>
    <dl class="rows">
      <div class="row">
        <dt>Qualifying degree</dt>
        <dd>A two-year Master's degree in science following a three-year Bachelor's in science, with
          at least 55% in aggregate or equivalent. Or a four-year Bachelor's degree in science with
          at least 75% in aggregate or equivalent. A relaxation of 5% or equivalent applies to
          candidates from SC, ST, OBC (non-creamy layer), Differently-Abled and EWS categories.</dd>
      </div>
      <div class="row">
        <dt>Fellowship</dt>
        <dd>A valid national-level fellowship from any funding agency &mdash; CSIR, ICMR, UGC, DBT,
          INSPIRE, RGNF and others. Candidates who have qualified GATE in Ecology and Evolution will
          also be considered.</dd>
      </div>
      <div class="row">
        <dt>What helps</dt>
        <dd>Comfort with the command line, an interest in genomes or trees, and a willingness to go
          into the field. None of these are prerequisites, but say so if you have them.</dd>
      </div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>How to apply</h2>
    </div>
    <dl class="rows">
      <div class="row">
        <dt>Step one</dt>
        <dd>Apply through the <a href="https://www.ccmb.res.in/academics/#phd-sec">CCMB portal</a>
          and select the <strong>LaCONES only</strong> option. Upload your statement of purpose with
          the online application.</dd>
      </div>
      <div class="row">
        <dt>Step two</dt>
        <dd>Send one consolidated file to
          <a href="mailto:siddharth@csirccmb.org">siddharth@csirccmb.org</a> containing your cover
          letter, statement of purpose, CV with publication list, contact details for two referees,
          and optionally one sample publication.</dd>
      </div>
      <div class="row">
        <dt>Selection</dt>
        <dd>LaCONES-only candidates are exempt from the computer-based written test and are screened
          on the statement of purpose and an interview. Shortlisted candidates are interviewed online
          in December 2026, and selection is on the overall merit of the application and the interview.</dd>
      </div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Postdoctoral researchers</h2>
    </div>
    <div class="measure">
      <p>We do not always have an advertised postdoctoral opening, but we are glad to hear from
        people who want to work here. Candidates with their own fellowship &mdash; Ramanujan, N-PDF,
        DBT-RA, DST INSPIRE Faculty, or an international scheme &mdash; are especially welcome to
        write, and we will help with the application from the beginning rather than the week before
        the deadline.</p>
      <p>Write with a CV, a paragraph on what you would want to do here, and a note on which
        fellowship you have in mind or already hold.</p>
      <p><a class="btn btn-solid" href="mailto:siddharth@csirccmb.org">Write to the lab</a></p>
    </div>
  </div>
</section>
"""

# --- Students: dissertations and internships ----------------------------------
STUDENTS = f"""
<div class="shell page-head">
  <h1>Dissertations and internships</h1>
  <p class="lede">Every year a handful of students spend a few months to a year in the lab on a
    dissertation, a training programme or an internship, and several have ended up as authors on
    papers. This page sets out the routes in, what the projects look like, and how to write to us.</p>
</div>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>Routes into the lab</h2>
      <p>Pick the one that matches where you are. If none of them fit, write anyway and say so.</p>
    </div>
    <dl class="rows">
      <div class="row">
        <dt>BS-MS or M.Sc. dissertation</dt>
        <dd>A six to twelve month thesis project, usually the final year of a BS-MS or M.Sc.
          programme. This is the most common route and the one that most often leads to a
          publication. Come with your institute's paperwork and timeline.
          <span class="tagline">6&ndash;12 months &middot; year-round</span></dd>
      </div>
      <div class="row">
        <dt>CSIR-CCMB Dissertation Research Training Programme</dt>
        <dd>CCMB's own scheme for students carrying out dissertation research here, with a stipend.
          Applications go through CCMB; write to us as well, so we know to look out for your file.
          <span class="tagline">6&ndash;12 months &middot; CCMB scheme</span></dd>
      </div>
      <div class="row">
        <dt>CCMB Summer Training Programme</dt>
        <dd>A short summer project for undergraduate and Masters students, advertised by CCMB early
          in the year. Competitive, and a good way to find out whether this kind of work suits you.
          <span class="tagline">2&ndash;3 months &middot; summer</span></dd>
      </div>
      <div class="row">
        <dt>Short research internship</dt>
        <dd>A few weeks to a few months, self-arranged, usually unfunded unless you bring a
          fellowship. Best for learning one specific thing well: a bioinformatics pipeline, a library
          preparation, a morphological technique.
          <span class="tagline">4 weeks and up &middot; year-round</span></dd>
      </div>
      <div class="row">
        <dt>Visiting student from another lab</dt>
        <dd>If you are doing a Ph.D. elsewhere and need a technique, a probe set or a dataset that we
          have, a short visit is often the fastest route. Several people have done exactly this.
          <span class="tagline">by arrangement</span></dd>
      </div>
    </dl>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>What to expect</h2>
    </div>
    <div class="grid grid-2">
      <article class="card">
        <h3>A real question, not a task list</h3>
        <p>You will be told what is unknown, what we suspect the answer might be, and why it
          matters. Then you go and find out.</p>
      </article>
      <article class="card">
        <h3>You will learn to compute</h3>
        <p>Almost everything here touches the command line at some point. No prior experience is
          expected; a willingness to be bad at it for a few weeks is.</p>
      </article>
      <article class="card">
        <h3>Weekly meetings</h3>
        <p>One-to-one time each week, plus lab meeting. If something is not working we would rather
          hear about it in week two than in month four.</p>
      </article>
      <article class="card">
        <h3>Fieldwork, sometimes</h3>
        <p>Depending on the season and the project you may end up in the Eastern Ghats or the
          Northeast. It is not guaranteed, and it is not compulsory.</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      {BRANCH}
      <h2>How to write to us</h2>
      <p>One email, to <a href="mailto:siddharth@csirccmb.org">siddharth@csirccmb.org</a>. It does
        not need to be long, but it does need to be specific.</p>
    </div>
    <dl class="rows">
      <div class="row">
        <dt>Subject line</dt>
        <dd>The route you are applying for and your dates &mdash; for example, <em>BS-MS
          dissertation, Jan&ndash;Jun 2027</em>. Generic subject lines get lost.</dd>
      </div>
      <div class="row">
        <dt>What interests you</dt>
        <dd>A paragraph on which part of the lab's work you want to be near, and why. Naming one of
          our papers and saying what you would do next with it works far better than praise.</dd>
      </div>
      <div class="row">
        <dt>What you can already do</dt>
        <dd>Programming, molecular lab work, microscopy, fieldwork, statistics, illustration,
          languages. Say honestly what you have not done as well; nobody expects all of it.</dd>
      </div>
      <div class="row">
        <dt>Attachments</dt>
        <dd>A CV of one or two pages, and your transcript if your programme requires it. One PDF is
          easier than five.</dd>
      </div>
      <div class="row">
        <dt>Timing</dt>
        <dd>Write three to six months ahead. Summer places fill by February or March, and
          dissertation slots by the middle of the preceding semester.</dd>
      </div>
      <div class="row">
        <dt>If we do not reply</dt>
        <dd>Send one polite reminder after ten days. It is almost always an overloaded inbox rather
          than a decision.</dd>
      </div>
    </dl>
    <div class="btn-row">
      <a class="btn btn-solid" href="mailto:siddharth@csirccmb.org?subject=Dissertation%20or%20internship%20enquiry">Write to the lab</a>
      <a class="btn" href="research.html">Read the research first</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="callout">
      <h3>Looking for a Ph.D. or a postdoc instead?</h3>
      <p>Doctoral admission runs through the CCMB programme and has its own deadlines, and we support
        postdoctoral fellowship applications.</p>
      <p><a class="btn btn-solid" href="join.html">Positions</a></p>
    </div>
  </div>
</section>
"""

# --- Contact ------------------------------------------------------------------
CONTACT = f"""
<div class="shell page-head">
  <h1>Contact</h1>
  <p class="lede">The lab sits at LaCONES, a few kilometres from the main CCMB campus in Hyderabad.
    Visitors, collaborators and prospective students are all welcome to write.</p>
</div>

<section class="section">
  <div class="shell">
    <dl class="rows">
      <div class="row">
        <dt>Email</dt>
        <dd><a href="mailto:siddharth@csirccmb.org">siddharth@csirccmb.org</a></dd>
      </div>
      <div class="row">
        <dt>Phone</dt>
        <dd><a href="tel:+914024006427">+91 40 2400 6427</a></dd>
      </div>
      <div class="row">
        <dt>Post</dt>
        <dd>Dr Siddharth Kulkarni<br>
          Laboratory for Conservation of Endangered Species (LaCONES)<br>
          CSIR-Centre for Cellular and Molecular Biology<br>
          162 Pillar, PVNR Expressway, Attapur Ring Road<br>
          Hyderguda, Hyderabad 500 048, Telangana, India</dd>
      </div>
      <div class="row">
        <dt>Getting here</dt>
        <dd>LaCONES is on the Attapur Ring Road near the PVNR Expressway, about 40 minutes from Rajiv
          Gandhi International Airport and 20 minutes from Hyderabad Deccan railway station.
          <a href="https://maps.google.com/?q=LaCONES+CCMB+Hyderguda+Hyderabad">Open in Maps</a>.</dd>
      </div>
      <div class="row">
        <dt>Students</dt>
        <dd>For dissertations, summer training and internships, read
          <a href="students.html">the students page</a> first &mdash; it says what to put in the
          email.</dd>
      </div>
      <div class="row">
        <dt>Profiles</dt>
        <dd><a href="https://scholar.google.co.in/citations?user=xo9jTM0AAAAJ&amp;hl=en">Google Scholar</a>
          &nbsp; <a href="https://www.researchgate.net/profile/Siddharth_Kulkarni6">ResearchGate</a>
          &nbsp; <a href="https://github.com/kulkarni-lab">GitHub</a></dd>
      </div>
      <div class="row">
        <dt>SpiderIndia</dt>
        <dd><a href="https://www.inaturalist.org/projects/spiderindia">iNaturalist</a>
          &nbsp; <a href="https://www.facebook.com/groups/SpiderIndia/">Facebook group</a>
          &nbsp; <a href="https://indiabiodiversity.org/group/spiderindia/show">India Biodiversity Portal</a><br>
          <a href="mailto:siddharth@csirccmb.org">siddharth@csirccmb.org</a></dd>
      </div>
      <div class="row">
        <dt>Press</dt>
        <dd>For comment on spiders, ticks, mites or arachnid evolution generally, email the lab
          directly. We are happy to help journalists and are glad to talk to schools.</dd>
      </div>
    </dl>
  </div>
</section>
"""

NOT_FOUND = """
<div class="shell page-head">
  <h1>That page has moved or never existed</h1>
  <p class="lede">The link you followed does not lead anywhere on this site. The pages below cover
    everything that is here.</p>
</div>
<section class="section">
  <div class="shell">
    <div class="btn-row">
      <a class="btn btn-solid" href="index.html">Home</a>
      <a class="btn" href="research.html">Research</a>
      <a class="btn" href="publications.html">Publications</a>
      <a class="btn" href="people.html">People</a>
      <a class="btn" href="students.html">Students</a>
      <a class="btn" href="contact.html">Contact</a>
    </div>
  </div>
</section>
"""

D = ("BiomE Lab at CSIR-CCMB Hyderabad asks why lineages of equal age end up so unequal in species "
     "richness, using chelicerate genomics, phylogenetics and community science.")

PAGES = [
    ("index.html", "BiomE Lab &mdash; Biodiversity Genomics and Evolution, CSIR-CCMB", D, HOME),
    ("research.html", "Research &mdash; BiomE Lab",
     "Asymmetric diversification, chelicerate phylogenomics, biodiversity discovery and community science at the BiomE Lab, CSIR-CCMB.", RESEARCH),
    ("people.html", "People &mdash; BiomE Lab",
     "Members of the BiomE Lab at LaCONES, CSIR-CCMB, Hyderabad, and past mentees.", PEOPLE),
    ("publications.html", "Publications &mdash; BiomE Lab",
     "Papers, books and chapters from Siddharth Kulkarni and the BiomE Lab on chelicerate genomics, phylogenetics and taxonomy.", PUBLICATIONS),
    ("news.html", "News &mdash; BiomE Lab",
     "Updates from the BiomE Lab at CSIR-CCMB: new members, new papers, meetings and fieldwork.", NEWS),
    ("spiderindia.html", "SpiderIndia &mdash; BiomE Lab",
     "SpiderIndia is a community science initiative mapping the spiders of the Indian subcontinent with more than 8,000 participants.", SPIDERINDIA),
    ("join.html", "Positions &mdash; BiomE Lab",
     "Open Ph.D. position and postdoctoral routes into the BiomE Lab, CSIR-CCMB, Hyderabad.", JOIN),
    ("students.html", "Dissertations and internships &mdash; BiomE Lab",
     "Dissertation projects, CCMB training programmes and research internships at the BiomE Lab, CSIR-CCMB, Hyderabad, and how to apply.", STUDENTS),
    ("contact.html", "Contact &mdash; BiomE Lab",
     "How to reach the BiomE Lab at LaCONES, CSIR-CCMB, Hyderabad.", CONTACT),
    ("404.html", "Page not found &mdash; BiomE Lab", D, NOT_FOUND),
]
