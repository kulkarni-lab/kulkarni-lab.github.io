/* ============================================================================
   PUBLICATIONS
   ----------------------------------------------------------------------------
   To add a paper, copy the top entry, change the fields, and put it at the top.

     n        running number shown nowhere, but keeps the list ordered
     year     number, or the expected year for submitted work
     status   "" for published, or "submitted" / "in press" / "preprint"
     authors  <b>…</b> = Siddharth,  <u>…</u> = lab member
     title    plain text; use <i>…</i> for genus/species names
     venue    journal or publisher
     detail   volume / pages
     tags     any of: genomics, phylogenomics, taxonomy, spiders, acari,
              solifugae, amblypygi, community, other  (used by the filters)
     url      link to the paper. Leave "" if there is none yet.

   To feature a paper on the HOME PAGE with an image and a blurb, add three
   fields to its entry: featured: true, blurb: "one or two sentences on what
   it found and why it matters", figure: "filename.jpg" (a file placed in
   assets/img/publications/ — leave figure: "" if you don't have one yet, and
   the home page will show the blurb full-width instead of a broken image).
   Only one paper should carry featured: true; move it when a new one should
   take the spot.
   ========================================================================== */

window.PUBLICATIONS = [
  {
    n: 43, year: 2026, status: "submitted",
    authors: "<u>Arjun Cherukutty</u>, <u>Pratik Khopkar</u>, <u>Shreya Salunkhe</u>, <u>Dibyo Mazumder</u>, <b>Siddharth Kulkarni</b>*",
    title: "Ancestral genomic stasis and coordinated genome erosion underlie asymmetric acarine diversification",
    venue: "Cladistics", detail: "", tags: ["genomics", "acari"], url: ""
  },
  {
    n: 42, year: 2026, status: "preprint",
    authors: "Erika Garcia, <b>Siddharth Kulkarni</b>, Matthew Graham, Carlos Santibanez-Lopez, Prashant Sharma",
    title: "Comparative genomics of the unusual arachnid order Solifugae spotlight the molecular and genetic basis for adaptations to arid habitats",
    venue: "bioRxiv", detail: "", tags: ["genomics", "solifugae"], url: "https://www.biorxiv.org/content/10.64898/2026.06.25.734573v1.abstract"
  },
  {
    n: 41, year: 2026, status: "submitted",
    authors: "<b>Siddharth Kulkarni</b>, Benjamin Klementz, Jesus Ballesteros, Kaitlyn Abshire, Tauana J. Cunha, … , Prashant Sharma",
    title: "No silver bullet: patterns of macrosynteny recapitulate systemic conflicts in the higher-level relationships of the arachnids",
    venue: "Molecular Biology and Evolution", detail: "", tags: ["genomics", "phylogenomics"], url: "https://www.biorxiv.org/content/10.64898/2026.06.22.733561v1.abstract"
  },
  {
    n: 40, year: 2026, status: "submitted",
    authors: "Erika L. Garcia , Zeana Ganem , <b>Siddharth Kulkarni</b>, Ilil Perl , Prashant P. Sharma, Efrat Gavish-Regev",
    title: "Genomic insights unveil taxonomic incongruities and evolutionary origins of solifuges across the southern Levant",
    venue: "Molecular Phylogenetics and Evolution", detail: "", tags: ["genomics", "phylogenomics"], url: "https://www.sciencedirect.com/science/article/pii/S1055790326000242"
  },
  {
    n: 39, year: 2026, status: "",
    authors: "<u>Jyoti Bhoi</u>, <u>Rushikesh Mule</u>, <u>Nishaad Savale</u>, Prashant Sharma, <b>Siddharth Kulkarni</b>*",
    title: "Ancient gene linkages and ultraconserved elements disentangle Acari interrelationships",
    venue: "iScience", detail: "29(2): 114616", tags: ["genomics", "phylogenomics", "acari"],
    url: "https://www.cell.com/iscience/fulltext/S2589-0042(25)02877-9",
    featured: true,
    blurb: "Relationships among ticks and mites have resisted resolution for decades. By combining ancient gene linkages that survive across whole chromosomes with hundreds of ultraconserved elements, we recovered a stable backbone for the group \u2014 the lab's first published result.",
    figure: ""
  },
  {
    n: 38, year: 2025, status: "",
    authors: "Benjamin Klementz, <b>Siddharth Kulkarni</b>, Kaitlyn Abshire, Prashant Sharma",
    title: "Exploring genome architecture as a source of phylogenetic characters for resolving the apulmonate arachnid polytomy",
    venue: "Molecular Phylogenetics and Evolution", detail: "210: 108380 · shared first authorship",
    tags: ["genomics", "phylogenomics"], url: "https://www.sciencedirect.com/science/article/pii/S1055790325000971"
  },
  {
    n: 37, year: 2025, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Benjamin Klementz, Prashant Sharma",
    title: "A chromosome-level genome of the giant vinegaroon <i>Mastigoproctus giganteus</i> exhibits the signature of pre-Silurian whole genome duplication",
    venue: "Journal of Heredity", detail: "116(3): 279–292", tags: ["genomics"],
    url: "https://academic.oup.com/jhered/advance-article/doi/10.1093/jhered/esae074/7925303"
  },
  {
    n: 36, year: 2025, status: "",
    authors: "Nikolaos Papadopoulos, <b>Siddharth Kulkarni</b>, Christian Baranyi, Bastian Fromm, Emily Setton, Prashant Sharma, Andreas Wanninger, Georg Brenneis",
    title: "The genome of a sea spider corroborates a shared Hox cluster motif in arthropods with reduced posterior tagma",
    venue: "BMC Biology", detail: "23: 196", tags: ["genomics"], url: ""
  },
  {
    n: 35, year: 2024, status: "",
    authors: "Hannah Wood, <b>Siddharth Kulkarni</b>, Martín Ramírez, Nikolaj Scharff",
    title: "Phylogeny and biogeography support ancient vicariance and subsequent dispersal out-of-Africa in Palpimanidae spiders (Araneae)",
    venue: "Zoological Journal of the Linnean Society", detail: "202(2): zlae129",
    tags: ["phylogenomics", "spiders"], url: ""
  },
  {
    n: 34, year: 2024, status: "",
    authors: "Gustavo Silva de Miranda, <b>Siddharth Kulkarni</b>*, Jéssica Tagliatela, Caitlin M. Baker, Alessandro P. L. Giupponi, Facundo M. Labarque, Efrat Gavish-Regev, Michael G. Rix, Leonardo S. Carvalho, Lívia Maria Fusari, Hannah M. Wood, Prashant P. Sharma",
    title: "The rediscovery of a relict unlocks the first global phylogeny of whip spiders (Amblypygi)",
    venue: "Systematic Biology", detail: "73(3): 495–505 · shared first authorship",
    tags: ["phylogenomics", "amblypygi", "taxonomy"], url: ""
  },
  {
    n: 33, year: 2024, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Takeshi Yamasaki, Luong Thi Hong Phung, Nanguei Karuaera, Savel R. Daniels, Efrat Gavish-Regev, Prashant P. Sharma",
    title: "Phylogenomic data reveal three new families of poorly studied Solifugae (camel spiders)",
    venue: "Molecular Phylogenetics and Evolution", detail: "191: 107989",
    tags: ["phylogenomics", "solifugae", "taxonomy"], url: ""
  },
  {
    n: 32, year: 2023, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Hugh Steiner, Erika Garcia, Hernán Iuri, Ryan Jones, Jesus Ballesteros, Guilherme Gainett, Matthew R. Graham, Danilo Harms, Robin Lyle, Andrés A. Ojanguren-Affilastro, Carlos E. Santibañez-López, Gustavo Silva de Miranda, Paula E. Cushing, Efrat Gavish-Regev, Prashant P. Sharma",
    title: "Neglected no longer: phylogenomic resolution of higher-level relationships in Solifugae",
    venue: "iScience", detail: "26(9): 107684", tags: ["phylogenomics", "solifugae"], url: ""
  },
  {
    n: 31, year: 2023, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Hannah Wood, Gustavo Hormiga",
    title: "Advances in the reconstruction of the Spider Tree of Life: a roadmap for spider systematics and comparative studies",
    venue: "Cladistics", detail: "39: 479–532", tags: ["phylogenomics", "spiders"], url: ""
  },
  {
    n: 30, year: 2023, status: "",
    authors: "Gustavo Hormiga, <b>Siddharth Kulkarni</b>, Miquel Arnedo, Dimitar Dimitrov, Gonzalo Giribet, Robert J. Kallal, Nikolaj Scharff",
    title: "Genitalic morphology and phylogenomic placement of the Australian spider <i>Paraplectanoides crassipes</i> Keyserling, 1886 (Araneae, Araneidae) with a discussion on the classification of the family Araneidae",
    venue: "Invertebrate Systematics", detail: "37(12): 797–818", tags: ["phylogenomics", "spiders", "taxonomy"], url: ""
  },
  {
    n: 29, year: 2023, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Hannah Wood, Gustavo Hormiga",
    title: "Phylogenomics illuminates the evolution of orb webs, respiratory systems and the biogeographic history of the world's smallest orb-weaving spiders (Araneae, Araneoidea, Symphytognathoids)",
    venue: "Molecular Phylogenetics and Evolution", detail: "186: 107855", tags: ["phylogenomics", "spiders"], url: ""
  },
  {
    n: 28, year: 2023, status: "",
    authors: "Maitry Jani, John T. D. Caleb, Vena Kapoor, <b>Siddharth Kulkarni</b>, Divya Uma",
    title: "Aliens in the society: foreign arthropods and small vertebrates associated with the social spider <i>Stegodyphus sarasinorum</i> Karsch, 1892 (Araneae: Eresidae)",
    venue: "The Journal of Arachnology", detail: "51(1): 57–62", tags: ["spiders", "other"], url: ""
  },
  {
    n: 27, year: 2023, status: "",
    authors: "Jacob A. Gorneau, <b>Siddharth Kulkarni</b>, Franklyn Cala-Riquelme, Lauren A. Esposito",
    title: "Biodiversity catalogs reveal taxonomic effort and geographic bias: a case study",
    venue: "BioScience", detail: "73(2): 112–123", tags: ["taxonomy", "community"], url: ""
  },
  {
    n: 26, year: 2022, status: "",
    authors: "Jacob A. Gorneau, William I. Ausich, Sandro Bertolino, Holly Bik, Marymegan Daly, Sebsebe Demissew, David A. Donoso, Ryan Folk, Alina Freire-Fierro, Shahina A. Ghazanfar, Olwen M. Grace, Ai-Qun Hu, <b>Siddharth Kulkarni</b>, Isaac H. Lichter-Marck, Lúcia G. Lohmann, Jagoba Malumbres-Olarte, A. Muthama Muasya, Abel Pérez-González, Yashica Singh, Carolina M. Siniscalchi, Chelsea D. Specht, Alycia L. Stigall, David C. Tank, Leilani A. Walker, David F. Wright, Alireza Zamani, Lauren A. Esposito",
    title: "Framing the future for taxonomic monography: improving recognition, support, and access",
    venue: "Bulletin of the Society of Systematic Biologists", detail: "1(1): 8328", tags: ["taxonomy", "community"], url: ""
  },
  {
    n: 25, year: 2021, status: "",
    authors: "Gustavo Hormiga, <b>Siddharth Kulkarni</b>, Thiago da Silva Moreira, Dimitar Dimitrov",
    title: "Molecular phylogeny of pimoid spiders and the limits of Linyphiidae, with a reassessment of male palpal homologies (Araneae, Pimoidae)",
    venue: "Zootaxa", detail: "5026(1): 71–101", tags: ["phylogenomics", "spiders", "taxonomy"], url: ""
  },
  {
    n: 24, year: 2021, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Gustavo Hormiga",
    title: "Hooroo mates! Phylogenomic data suggest that the closest relatives of the iconic Tasmanian cave spider <i>Hickmania troglodytes</i> are in Australia and New Zealand, not in South America",
    venue: "Invertebrate Systematics", detail: "35: 850–856", tags: ["phylogenomics", "spiders"], url: ""
  },
  {
    n: 23, year: 2021, status: "",
    authors: "Robert Kallal, <b>Siddharth Kulkarni</b>, Dimitar Dimitrov, Ligia Benavides, Miquel Arnedo, Gonzalo Giribet, Gustavo Hormiga",
    title: "Converging on the orb: denser taxon sampling elucidates spider phylogeny and new analytical methods support repeated evolution of the orb web",
    venue: "Cladistics", detail: "37(3): 298–316", tags: ["phylogenomics", "spiders"], url: ""
  },
  {
    n: 22, year: 2021, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Robert Kallal, Hannah Wood, Dimitar Dimitrov, Gonzalo Giribet, Gustavo Hormiga",
    title: "Interrogating genomic-scale data to resolve recalcitrant nodes in the Spider Tree of Life",
    venue: "Molecular Biology and Evolution", detail: "38(3): 891–903", tags: ["phylogenomics", "spiders"], url: ""
  },
  {
    n: 21, year: 2020, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Hannah Wood, Michael Lloyd, Gustavo Hormiga",
    title: "Spider-specific probe set for ultraconserved elements offers new perspectives on the evolutionary history of spiders (Arachnida, Araneae)",
    venue: "Molecular Ecology Resources", detail: "20: 185–203", tags: ["phylogenomics", "spiders", "genomics"], url: ""
  },
  {
    n: 20, year: 2018, status: "",
    authors: "Christopher John Thorpe, Todd Lewis, Matthew Fisher, Claudia Wierzbicki, <b>Siddharth Kulkarni</b>, Lewis Davies, David Pryce, Aparna Watve, Mairi Knight",
    title: "Climate structuring of <i>Batrachochytrium dendrobatidis</i> infection in the threatened amphibians of the northern Western Ghats, India",
    venue: "Royal Society Open Science", detail: "5(6): 180211", tags: ["other"], url: ""
  },
  {
    n: 19, year: 2018, status: "",
    authors: "Christopher John Thorpe, Todd Lewis, <b>Siddharth Kulkarni</b>, Aparna Watve, David Pryce, Lewis Davies, Nikhil Gaitonde, David Bilton, Mairi Knight",
    title: "Micro-habitat distribution drives patch quality for sub-tropical rocky plateau amphibians in the northern Western Ghats, India",
    venue: "PLOS ONE", detail: "13(3): e0194810", tags: ["other"], url: ""
  },
  {
    n: 18, year: 2018, status: "",
    authors: "Hemant Ghate, <b>Siddharth Kulkarni</b>, Suresh Benjamin",
    title: "Giant assassin in the cave: a new species of the genus <i>Myiophanes</i> from Sri Lanka (Hemiptera: Heteroptera: Reduviidae: Emesinae)",
    venue: "Zootaxa", detail: "4524(2): 237–244", tags: ["taxonomy", "other"], url: ""
  },
  {
    n: 17, year: 2017, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Atul Vartak, Vishwas Deshpande, <u>Dheeraj Halali</u>",
    title: "The spiny theridiid genus <i>Meotipa</i> Simon, 1895 in India, with description of a strange new species with translucent abdomen and a phylogenetic analysis about the genus placement (Araneae, Theridiidae)",
    venue: "Zootaxa", detail: "4291(3): 504–520", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 16, year: 2017, status: "",
    authors: "Hemant Ghate, <b>Siddharth Kulkarni</b>, Vijay Anand Ismavel",
    title: "Illustrated redescriptions of two large coreid bugs from Assam including the first Indian record of <i>Schroederia feana</i> (Distant, 1902) (Coreidae, Coreinae, Mictini)",
    venue: "Entomon", detail: "42(2): 165–172", tags: ["taxonomy", "other"], url: ""
  },
  {
    n: 15, year: 2016, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Hemant Ghate",
    title: "A new cavernicolous assassin bug of the genus <i>Bagauda</i> Bergroth (Reduviidae, Emesinae) from Western Ghats, India",
    venue: "Zootaxa", detail: "4127(2): 365–375", tags: ["taxonomy", "other"], url: ""
  },
  {
    n: 14, year: 2016, status: "",
    authors: "David Pryce, C. John Thorpe, <b>Siddharth Kulkarni</b>, Todd Lewis",
    title: "<i>Amphiesma stolatum</i> (striped keelback): habitat and reproduction",
    venue: "The Herpetological Bulletin", detail: "136: 37–38", tags: ["other"], url: ""
  },
  {
    n: 13, year: 2016, status: "",
    authors: "Peter Jäger, <b>Siddharth Kulkarni</b>",
    title: "An unexpected new species of the genus <i>Pseudopoda</i> (Araneae, Sparassidae, Heteropodinae) from the Western Ghats in India",
    venue: "ZooKeys", detail: "577: 55–62", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 12, year: 2016, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Hemant Ghate",
    title: "First record of the thread-legged assassin bug <i>Myiophanes greeni</i> Distant, 1903 (Heteroptera: Reduviidae: Emesinae) from India",
    venue: "Biodiversity Data Journal", detail: "4: e7949", tags: ["taxonomy", "other"], url: ""
  },
  {
    n: 11, year: 2016, status: "",
    authors: "Sameer Padhye, <b>Siddharth Kulkarni</b>*",
    title: "Regulated animal dissections in Indian academia as a measure to control invasive species",
    venue: "Current Science", detail: "110(2): 129–130", tags: ["other", "community"], url: ""
  },
  {
    n: 10, year: 2015, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Rahul Khot",
    title: "<i>Neosataria</i>, replacement name for <i>Sataria</i> Annandale, 1920 (Mollusca: Gastropoda: Bithyniidae), preoccupied by <i>Sataria</i> Roewer, 1915 (Arachnida: Opiliones: Sclerosomatidae)",
    venue: "Zootaxa", detail: "3974(4): 599–600", tags: ["taxonomy", "other"], url: ""
  },
  {
    n: 9, year: 2015, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Swara Yadav",
    title: "Bridging the distributional gap of <i>Tylorida striata</i> (Thorell, 1877) and new synonymy (Araneae: Tetragnathidae)",
    venue: "Biodiversity Data Journal", detail: "3: e4878", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 8, year: 2015, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Todd Lewis",
    title: "Description of male <i>Tylorida sataraensis</i> Kulkarni, 2014 (Araneae, Tetragnathidae) with notes on habits and conservation status",
    venue: "Biodiversity Data Journal", detail: "3: e4451", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 7, year: 2015, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, S. Joseph",
    title: "First record of genus <i>Siler</i> Simon, 1889 (Araneae: Salticidae) from India",
    venue: "Journal of Threatened Taxa", detail: "7(10): 7701–7703", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 6, year: 2015, status: "",
    authors: "<b>Siddharth Kulkarni</b>*",
    title: "Comments on \u201cA new species of genus <i>Thomisus</i> Walckenaer, 1805 (Araneae: Thomisidae) from Telangana, India and a detailed description of <i>Thomisus projectus</i> Tikader, 1960\u201d by Pravalikha & Srinivasulu, 2015",
    venue: "Journal of Threatened Taxa", detail: "7(9): 7605–7606", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 5, year: 2015, status: "",
    authors: "Mihir Kulkarni, Sameer Padhye, Avinash Vanjare, Shriraj Jakhalekar, Yugandhar Shinde, Shruti Paripatyadar, Sayali Sheth, <b>Siddharth Kulkarni</b>, Samadhan Phuge, Kalyani Bhakare, Aboli Kulkarni, Kalpana Pai, Hemant Ghate",
    title: "Documenting the fauna of a small temporary pond from Pune, Maharashtra, India",
    venue: "Journal of Threatened Taxa", detail: "7(6): 7196–7210", tags: ["other"], url: ""
  },
  {
    n: 4, year: 2014, status: "",
    authors: "<b>Siddharth Kulkarni</b>*",
    title: "A new species of the genus <i>Tylorida</i> Simon, 1894 (Araneae: Tetragnathidae) from a rocky outcrop in the northern Western Ghats, India",
    venue: "Journal of Threatened Taxa", detail: "6(3): 5558–5561", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 3, year: 2013, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Helen Smith",
    title: "First record of <i>Poltys columnaris</i> Thorell, 1890 (Araneae: Araneidae) from Western Ghats, India",
    venue: "Journal of Threatened Taxa", detail: "5(10): 4524", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 2, year: 2012, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Vishwas Deshpande",
    title: "New record of the spider <i>Arachnura angura</i> from Maharashtra with additional morphological description (Araneae: Araneidae)",
    venue: "Records of the Zoological Survey of India", detail: "112(2): 113–115", tags: ["taxonomy", "spiders"], url: ""
  },
  {
    n: 1, year: 2012, status: "",
    authors: "<b>Siddharth Kulkarni</b>*, Vishwas Deshpande",
    title: "A new species of the genus <i>Oxyopes</i> Latreille (Araneae: Oxyopidae) from the Sahyadri ranges of the Western Ghats",
    venue: "Records of the Zoological Survey of India", detail: "112(2): 35–37", tags: ["taxonomy", "spiders"], url: ""
  }
];

/* Books and book chapters, newest first. */
window.BOOKS = [
  {
    year: "in press",
    authors: "<b>Siddharth Kulkarni</b>, Dimitar Dimitrov, Gustavo Hormiga",
    title: "Two chapters: \u201cThe rise of spider taxonomy and systematics in Southeast Asia and the global South\u201d and \u201cShaking the tree: understanding spider diversity and relationships in a broader context\u201d",
    venue: "In: Dimitrov D. & Hormiga G. (eds), <i>Spider Systematics and Taxonomy</i>. Elsevier",
    url: ""
  },
  {
    year: "in preparation",
    authors: "Prashant Sharma, <b>Siddharth Kulkarni</b>, Efrat Gavish-Regev, Erika Garcia, Jason Dunlop",
    title: "Chapter: Systematics and biogeography of Solifugae",
    venue: "In: Cushing P., Vrech D. & Sharma P. (eds), <i>Biology and Natural History of Camel Spiders (Arachnida, Solifugae)</i>. Springer",
    url: ""
  },
  {
    year: 2020,
    authors: "Ayan Mondal, Debomay Chanda, Atul Vartak, <b>Siddharth Kulkarni</b>",
    title: "A Field Guide to the Spider Genera of India",
    venue: "Kolkata, India. 400 pp.",
    url: ""
  }
];
