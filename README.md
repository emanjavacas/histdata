
# Data splits for Historical Corpora
----------------------------------

DISCLAIMER: This repository only provides code to download and split the corpora to replicate the experiments conducted in the paper "Improving Lemmatization of Non-Standard Languages with Joint Learning" to be presented at NAACL19-HLT.

## Installation

Make sure to have `python`. And then:

1. Install dependencies
`pip install -r requirements.txt`

2. Get the data
`bash get_data.sh`

The scripts should create a directory `historical`, with all the corpora splits inside.

## Credits

If you found this resource useful, please cite the following paper:

```
@InProceedings{
	author = "Manjavacas, Enrique
	and K{\'a}d{\'a}r, {\'A}kos
	and Kestemont, Mike",
	title = "Improving Lemmatization of Non-Standard Languages with Joint Learning",
	booktitle = "Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
	year = 	"\noop{2019}in press",
	publisher = 	"Association for Computational Linguistics"
}
```

Please note that if you use any of the corpora listed here, you should also cite the corresponding resource listed below.

# Sources
---------

## ReN 0.6

Link: https://corpora.uni-hamburg.de/hzsk/de/islandora/object/file:ren-0.6_CorAXML/datastream/ZIP/CorAXML-0.6.zip

Reference:
```
@article{barteld2017referenzkorpus, title = {{Das Referenzkorpus Mittelniederdeutsch/Niederrheinisch (1200--1650)--Korpusdesign, Korpuserstellung und Korpusnutzung}}, year = {2017}, journal = {Mitteilungen des Deutschen Germanistenverbandes}, author = {Barteld, Fabian and Dreessen, Katharina and Ihden, Sarah and Schr{\"{o}}der, Ingrid}, number = {3}, pages = {226--241}, volume = {64}, publisher = {V{\&}R unipress GmbH G{\"{o}}ttingen} }
```

## Geste

Link: https://github.com/Jean-Baptiste-Camps/Geste/archive/9c1fd27e1f9266b2c31e3959b09efe62f96ce577.zip

Reference:
```
@misc{geste,
  author = {Camps, Jean-Baptiste},
  title = {Geste: un corpus de chansons de geste},
  year = {2016},
  note = {avec la collab. d'Elena Albarran, Alice Cochet \& Lucence Ing},
  url = {http://github.com/Jean-Baptiste-Camps/Geste},
}
```

## goo300k

Link: https://www.clarin.si/repository/xmlui/handle/11356/1025/allzip

Reference:
```
@misc{11356/1025,
 title = {Reference corpus of historical Slovene goo300k 1.2},
 author = {Erjavec, Toma{\v z}},
 url = {http://hdl.handle.net/11356/1025},
 note = {Slovenian language resource repository {CLARIN}.{SI}},
 copyright = {Creative Commons - Attribution 4.0 International ({CC} {BY} 4.0)},
 year = {2015} 
}
```

## LLCT1 (v1)

Link: https://zenodo.org/record/1197357/files/LLCT1.xml

Reference:
```
@inproceedings{korkiakangas2013abbreviations,
  title={Abbreviations, fragmentary words, formulaic language: treebanking mediaeval charter material},
  place={Sofia, Bulgaria},
  author={Korkiakangas, Timo and Lassila, Matti},
  editor={Mambrini, F. and Passarotti, M. and  Sporleder, C.},
  booktitle={Proceedings of The Third Workshop on Annotation of Corpora for Research in the Humanities},
  pages = {61--72},
  year={2013}
}
```

