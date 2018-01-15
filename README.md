# Koordinaadid
Topcon GT-3000 elektrontahhüomeetri koordinaatfaili parandusprogramm

Antud programmi eesmärgiks on lisada Topcon GT-3000 (kasutatakse geodeetilistel töödel) poolt väljastatavale koordinaatide tekstfailile Eesti koordinaatsüsteemile vastavad puuduvad koordinaadiosad arvuti abiga. Puuduvad osad tuleb sisestada pärast esimest ja teist koma igas reas. Seni on seda tehtud käsitsi, mis on sadade ja tuhandete ridade pikkuste failide puhul mõistagi ajakulukas ja veaohtlik. Programm võimaldab avada lähtefail, täpsustada X- ja Y-koordinaatide ette käivad väärtused ning luua uus tekstfail sisestatud väärtustega. Uus fail luuakse programmi asukohta. Näiteks kui programm asub töölaual, siis uus fail luuakse sinna.

Programmi töö:
Programmiga samas kaustas on kaasa pandud kaks testfaili. Kõige lihtsam on tegutseda töölaual või mõnes muus tuttavas ja kiirelt leitavas kaustas, kuna programm alustab sisendfaili avamist C: kettalt, mitte programmi enda asukohast.
On defineeritud 2 funktsiooni. ava_fail lubab avada tekstfaili nin loeb seejärel faili sisu mällu, luues järjendi failis olevatest ridadest. lisa_vaartused võtab kasutaja poolt sisestatud väärtused ja sisestab need vajalikkesse kohtadesse, luues uue faili. Kui sellise nimega fail on juba olemas, kirjutatakse see üle. Seejärel võib programmi sulgeda.
