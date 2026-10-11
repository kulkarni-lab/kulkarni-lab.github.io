/* ============================================================================
   PEOPLE
   ----------------------------------------------------------------------------
   photo   filename inside assets/img/people/ — e.g. "pratik-khopkar.jpg"
           Leave "" and the card shows the person's initials instead.
   links   [{label, url}] — Scholar, ORCID, iNaturalist, personal site, etc.
   ========================================================================== */

window.PI = {
  name: "Siddharth Kulkarni",
  role: "Principal Investigator",
  titles: [
    "ANRF Ramanujan Faculty Fellow, CSIR-Centre for Cellular and Molecular Biology",
    "Assistant Professor, Academy of Scientific and Innovative Research (AcSIR)"
  ],
  photo: "siddharth-kulkarni.jpg",
  bio: [
   "I am fascinated by origins of biodiversity and by what keeps it going despite multiple mass extinction events. My work asks why some branches of the tree of life are staggeringly diverse while their close relatives are not, using chelicerates including spiders, ticks, mites, scorpions, whip spiders, camel spiders as a study system.",
   "Before starting the lab I completed a Ph.D. with Gustavo Hormiga at George Washington University on the spider tree of life and the miniature orb-weavers, and a postdoc with Prashant Sharma at the University of Wisconsin-Madison working on arachnid phylogenomics and genome architecture.",
   "Outside the lab I coordinate SpiderIndia, a community science network of more than 9,000 people across South Asia who photograph and document spiders. Much of what we know about where Indian spiders actually live comes from them. Their contributions have led to the popular A field guide to the Spider Genera of India"
  ],
  links: [
    { label: "Google Scholar", url: "https://scholar.google.co.in/citations?user=xo9jTM0AAAAJ&hl=en" },
    { label: "ResearchGate", url: "https://www.researchgate.net/profile/Siddharth_Kulkarni6" },
    { label: "GitHub", url: "https://github.com/kulkarni-lab" }
  ]
};

window.GROUPS = [
  {
    id: "research-group",
    title: "Research group",
    blurb: "Doctoral students, project staff and research assistants based at LaCONES, CSIR-CCMB.",
    people: [
      {
        name: "Sahil Rana", role: "Doctoral student", since: "2026", photo: "SahilRana.jpeg",
        note: "Exploring origins and genomic architectures of parasitism ", links: []
      },
      {
        name: "Shripad Manthen", role: "Spider taxonomist", since: "2026", photo: "smanthen.jpeg",
        note: "The lab's in-house expert on spider identification and morphology.", links: []
      },
      {
        name: "Nithin K. A.", role: "Project Associate I", since: "2026", photo: "nithinka.jpeg",
        note: "Genomics and computational work on chelicerate diversification.", links: []
      },
      {
        name: "Pratik Khopkar", role: "Project Associate I", since: "2025", photo: "pratikkhopkar.jpg.jpeg",
        note: "Molecular laboratory work, library preparation and sequencing.", links: []
      },
      {
        name: "Arjun Cherukutty", role: "Technical Assistant", since: "2025", photo: "arjunck.jpg.jpeg",
        note: "Comparative genomics of Acari; genome erosion and gene family evolution.", links: []
      }
    ]
  },
  {
    id: "students",
    title: "Students and visiting researchers",
    blurb: "Masters, dissertation and internship students working with the lab, including co-supervised students at IISER Thiruvananthapuram.",
    people: [
      {
        name: "Aakashkumar Pathak", role: "Ph.D. student, co-supervised", since: "2024", photo: "AakashT.jpg",
        note: "IISER Thiruvananthapuram.", links: []
      },
      {
        name: "Shreya Salunkhe", role: "Dissertation research trainee", AY: "2025-2026", photo: "ShreyaS.jpg",
        note: "CSIR-CCMB Dissertation Research Training Programme; from IISER Thiruvananthapuram.", links: []
      },
      {
        name: "Neha Tambe", role: "Research intern", Summer: "2026", photo: "NehaT.jpg",
        note: "D. Y. Patil University, Pune.", links: []
      },
   ]
  }
];

/* Past members and mentees. Shown as a simple list rather than cards. */
window.ALUMNI = [
  { name: "Rohan Gaurkar", detail: "Research internship, Dr. B. S. Konkan Krishi Vidyapeeth, Dapoli, Maharashtra, India \u2014 Systematics of stingless bees" },
  { name: "Meghana Balija", detail: "Summer Training Programme 2025, Sri Padmavati Mahila Visvavidyalayam, Tirupati \u2014 the first student in the new lab" },
  { name: "Sweta Acharjya", detail: "IISER Thiruvananthapuram, Varsha 2024 \u2014 Machine learning" },
  { name: "Nishaad Savale", detail: "IISER Thiruvananthapuram, Varsha 2024 \u2014 UCE phylogenomics" },
  { name: "Jyoti Bhoi", detail: "IISER Thiruvananthapuram, Varsha 2024 \u2014 UCE phylogenomics" },
  { name: "Rushikesh Mule", detail: "IISER Thiruvananthapuram, Varsha 2024 \u2014 UCE phylogenomics" },
  { name: "Brooke Pellegrini", detail: "George Washington University, 2019 \u2014 spider curation and identification" },
  { name: "Hugh Steiner", detail: "University of Wisconsin-Madison, 2022\u20132023 \u2014 UCE library preparation and analysis" },
  { name: "Brooke Pellegrini", detail: "George Washington University, 2019 \u2014 spider curation and identification" },
];
