
import os
from lxml import etree
import random
random.seed(100101)

root = 'CoraXML/ReN_2018-07-23'
target = 'ren'
if not os.path.isdir(target):
    os.makedirs(target)


def readlines(path):
    with open(path, 'rb') as f:
        tree = etree.fromstring(f.read()).getroottree()
        for token in tree.findall('token'):
            # there are 8 cases were tok_dipl is empty (resort to trans)
            form = token.find('dipl').attrib['utf'] or token.attrib['trans']
            anno = token.find('anno')
            pos = anno.find('pos').attrib['tag']
            lemma = anno.find('lemma').attrib['tag']
            morph = anno.find('morph').attrib['tag']
            # there are 3 cases where lemma has whitespace: "wager man"
            if len(lemma.split()) > 1:
                print("Substituting complex lemma:", lemma)
                lemma = lemma.split()[0]
            # there are 5 cases with empty lemma
            if not lemma:
                lemma = "<none>"

            yield form, lemma, pos, morph


def writelines(f, lines):
    for token, lemma, pos, morph in lines:
        f.write("{}\t{}\t{}\t{}\n".format(token, lemma, pos, morph))


files = ['Lüb._Chr._Bard..xml', 'Agneta_Willeken.xml', 'Brem._Uk._1301-1350.xml', 'Kortw._Hist._Sifrit.xml', 'Rossiliun_Frag..xml', 'Tew._Hocht._1640.xml', 'Lüb._NdStB.xml', 'Hildesh._MünzV_1300.xml', 'Reinke_de_Vos_1539.xml', 'Osn._Sühne_1288.xml', 'Münster_Veghe-Aut..xml', 'Schwer._Stb._1451-1500.xml', 'Brem._Uk._1451-1500.xml', 'Märk._Hochzeitsgedicht.xml', 'Hamb._Uk._1401-1450.xml', 'Brem._StR_1303,08.xml', 'Brs._Dud._1279a,b.xml', 'Schwer._Stb._1401-1450.xml', 'Brs._Best._Ius_O._1265.xml', 'Veer_Koeplude.xml', 'Brem._StR_1303,08_Kopie.xml', 'Cincinnius_Nieder._1539.xml', 'Mag._MünzV_1294.xml', 'Strals._Frieden.xml', 'Mandeville.xml', 'Brem._Uk._1401-1450.xml', 'Gött._LiebesBr..xml', 'Alexander_Helmst..xml', 'Kölner_Bibel_Ku_1478,79.xml', 'Brem._Ssp..xml', 'Hamb._Uk._1451-1500.xml', 'Hamb._SchiffsR.xml', 'Reval_Tot..xml', 'Bord._Marien-Kl..xml', 'Brem._Uk._1351-1400.xml', 'Kortw._Hist._Sigenot.xml', 'Rav._Urk._1292.xml', 'Stader_StR.xml', 'Brs._Ius_Otton._1227.xml', 'Lauremberg_1652.xml', 'Werl._Urk._Neheim_1294.xml', 'Griseldis.xml', 'Verl._Sohn.xml', 'Kortw._Hist._Laurin.xml', 'Lüb._Henselyn_1498.xml', 'Vespucci_Nygen_ins._1506.xml', 'Brs._Ält._DegB_Altst._I.xml', 'Buxteh._Ev..xml', 'Hamb._Uk._1301-1350.xml', 'Rost._Bürgerspr._1580.xml', 'Brs._Ält._DegB_Altst._II.xml', 'Lud._Sudh._Hs._Ms.xml', 'Seekarte_1577.xml', 'Veghe_Predigten_1492.xml', 'SSp._Berlin_Fragm._22.xml', 'Hamb._Uk._1351-1400.xml']
random.shuffle(files)
formatter = os.path.join(target, '{}.tsv').format
with open(formatter('train'), 'w+') as train, \
     open(formatter('test'), 'w+') as test, \
     open(formatter('dev'), 'w+') as dev:
    train.write('token\tlemma\tpos\tmorph\n')
    test.write('token\tlemma\tpos\tmorph\n')
    dev.write('token\tlemma\tpos\tmorph\n')
    for f in files:
        lines = list(readlines(os.path.join(root, f)))
        if len(lines) < 5000:
            writelines(train, lines)
        else:
            five = int(len(lines) * 0.05)
            ten = int(len(lines) * 0.1)
            writelines(dev, lines[:ten])
            writelines(test, lines[ten: five + (2*ten)])
            writelines(train, lines[five + (2*ten):])
