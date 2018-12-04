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

## Evaluation

The tagger was evaluated on different flavours of Slovene held-out data: standard data and non-standard data.

The evaluation results on the standard data are the following:

```
          o       0.99      1.00      0.99     36938
  deriv-per       0.44      0.56      0.49        27
        loc       0.85      0.74      0.79       582
       misc       0.39      0.24      0.30       315
        org       0.69      0.48      0.57       497
        per       0.87      0.95      0.91       819

avg / total       0.98      0.98      0.98     39178
```

The evaluation results on the non-standard data are these:

```
          o       0.99      1.00      1.00      1740
  deriv-per       0.00      0.00      0.00         1
        loc       0.79      0.92      0.85        12
       misc       0.75      0.21      0.33        14
        org       0.50      0.33      0.40         6
        per       0.98      1.00      0.99        82

avg / total       0.99      0.99      0.99      1855
```

## Citing the tagger

If you use the tagger, please cite the following paper:

```
@Article{Fišer2018,
author="Fi{\v{s}}er, Darja and Ljube{\v{s}}i{\'{c}}, Nikola and Erjavec, Toma{\v{z}}",
title="The Janes project: language resources and tools for Slovene user generated content",
journal="Language Resources and Evaluation",
year="2018",
issn="1574-0218",
doi="10.1007/s10579-018-9425-z",
url="https://doi.org/10.1007/s10579-018-9425-z"
}
```
