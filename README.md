
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
@inproceedings{manjavacas-etal-2019-improving,
    title = "Improving Lemmatization of Non-Standard Languages with Joint Learning",
    author = "Manjavacas, Enrique  and
      K{\'a}d{\'a}r, {\'A}kos  and
      Kestemont, Mike",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N19-1153",
    doi = "10.18653/v1/N19-1153",
    pages = "1493--1503",
    abstract = "Lemmatization of standard languages is concerned with (i) abstracting over morphological differences and (ii) resolving token-lemma ambiguities of inflected words in order to map them to a dictionary headword. In the present paper we aim to improve lemmatization performance on a set of non-standard historical languages in which the difficulty is increased by an additional aspect (iii): spelling variation due to lacking orthographic standards. We approach lemmatization as a string-transduction task with an Encoder-Decoder architecture which we enrich with sentence information using a hierarchical sentence encoder. We show significant improvements over the state-of-the-art by fine-tuning the sentence encodings to jointly optimize a bidirectional language model loss. Crucially, our architecture does not require POS or morphological annotations, which are not always available for historical corpora. Additionally, we also test the proposed model on a set of typologically diverse standard languages showing results on par or better than a model without fine-tuned sentence representations and previous state-of-the-art systems. Finally, to encourage future work on processing of non-standard varieties, we release the dataset of non-standard languages underlying the present study, which is based on openly accessible sources.",
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

