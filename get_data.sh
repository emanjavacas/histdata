

wget https://github.com/Jean-Baptiste-Camps/Geste/archive/9c1fd27e1f9266b2c31e3959b09efe62f96ce577.zip
unzip 9c1fd27e1f9266b2c31e3959b09efe62f96ce577.zip -d Geste
rm 9c1fd27e1f9266b2c31e3959b09efe62f96ce577.zip
mv Geste/Geste-9c1fd27e1f9266b2c31e3959b09efe62f96ce577/tsv/* ./Geste/
rm -r Geste/Geste-9c1fd27e1f9266b2c31e3959b09efe62f96ce577
python process_geste.py
mv Geste/corpus ./geste
rm -r Geste

wget https://corpora.uni-hamburg.de/hzsk/de/islandora/object/file:ren-0.7_CorAXML/datastream/ZIP/CorAXML-0.7.zip
unzip CorAXML-0.7.zip
python process_ren.py
rm -r CoraXML
rm CorAXML-0.7.zip 

wget https://www.clarin.si/repository/xmlui/handle/11356/1025/allzip
unzip allzip
unzip goo300k-vert.zip
python process_goo300k.py
rm allzip
rm -r goo300k-*

wget https://zenodo.org/record/1197357/files/LLCT1.xml
python process_llct.py
rm LLCT1.xml

mkdir historical
mv geste historical/
mv ren historical/
mv goo300k historical/
mv LLCT1 historical/

echo "Corpora should be now inside 'historical'. Enjoy!"
