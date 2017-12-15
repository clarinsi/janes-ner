# janes-ner
NER system for South Slavic languages

```
$ python tagger.py sl < example_sl.txt
Slovenija	Npfsn	B-loc
je	Va-r3s-n	O
zelo	Rgp	O
# kot Hrvaška #	Z Rgp Npfsn Z	O O B-loc O
lepa	Agpfsn	O
.	Z	O

$ python tagger.py hr < example_hr.txt
Dodali	Vmp-pm	O
smo	Var1p	O
i	Qo	O
preostale	Agpmpay	O
jezike	Ncmpa	O
.	Z	O

Marko	Npmsn	B-per
i	Cc	O
Ana	Npfsn	B-per
rade	Vmr3p	O
u	Sl	O
Microsoftu	Npmsl	B-org
u	Sl	O
Jajcu	Ncnsl	B-loc
.	Z	O

```