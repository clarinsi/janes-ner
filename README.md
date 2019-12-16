# janes-ner
NER system for Slovene, Croatian and Serbian. The system itself is a slight modification of the CRF-based [reldi-tagger](https://github.com/clarinsi/reldi-tagger) with Brown clusters information added. It differentiates between person, person derivative, location, organization and miscelaneous.

The Slovene model was trained on [ssj500k](http://hdl.handle.net/11356/1210), the Croatian on [hr500k](http://hdl.handle.net/11356/1183), while the Serbian model was trained on [SETimes.SR](http://hdl.handle.net/11356/1200).

```
$ python2.7 tagger.py sl < example_sl.txt
Slovenija	Npfsn	B-loc
je	Va-r3s-n	O
zelo	Rgp	O
# kot Hrvaška #	Z Rgp Npfsn Z	O O B-loc O
lepa	Agpfsn	O
.	Z	O

$ python2.7 tagger.py hr < example_hr.txt
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

## Necessary preprocessing

To produce data that is tokenised and part-of-speech-tagged (prerequisite for named entity recognition), you should apply the following tools to running text:

- [reldi-tokeniser](https://github.com/clarinsi/reldi-tokeniser) for tokenization
- [reldi-tagger](https://github.com/clarinsi/reldi-tagger) for morphosyntactic tags

One exemplary run of these processes in a pipeline is this:

```
$ echo 'U Piranu pada kiša.' | python2.7 reldi-tokeniser/tokeniser.py hr | python2.7 reldi-tagger/tagger.py hr | python2.7 janes-ner/tagger.py -i 2 -m 3 hr
1.1.1.1-1	U	Sl	O
1.1.2.3-8	Piranu	Npmsl	B-loc
1.1.3.10-13	pada	Vmr3s	O
1.1.4.15-18	kiša	Ncfsn	O
1.1.5.19-19	.	Z	O
```

## Evaluation

The tagger was evaluated inside the [babushka-bench](https://github.com/clarinsi/babushka-bench) benchmarking platform.

On Slovene the overall macro-F1 of 0.673 and accuracy of 0.984 were obtained, with the following per-class results:

```
             precision    recall  f1-score   support

                  0.99      1.00      1.00     16984
  deriv-per       0.50      0.35      0.41        17
        loc       0.84      0.77      0.80       230
       misc       0.35      0.22      0.27        79
        org       0.72      0.63      0.67       200
        per       0.90      0.88      0.89       422

avg / total       0.98      0.98      0.98     17932
```

On Croatian the overall macro-F1 of 0.752 and accuracy of 0.978 were obtained, with the following per-class results:

```
             precision    recall  f1-score   support

                  0.99      1.00      0.99     47763
  deriv-per       0.57      0.57      0.57        23
        loc       0.86      0.84      0.85       840
       misc       0.55      0.45      0.49       517
        org       0.76      0.69      0.72      1183
        per       0.86      0.92      0.89      1038

avg / total       0.98      0.98      0.98     51364
```

On Serbian the overall macro-F1 of 0.781 and accuracy of 0.975 were obtained, with the following per-class results:

```
             precision    recall  f1-score   support

                  0.99      1.00      1.00     16984
  deriv-per       0.50      0.35      0.41        17
        loc       0.84      0.77      0.80       230
       misc       0.35      0.22      0.27        79
        org       0.72      0.63      0.67       200
        per       0.90      0.88      0.89       422

avg / total       0.98      0.98      0.98     17932
```

### Slovene-only evaluation

The tagger was previously evaluated on different flavours of Slovene held-out data: standard data, non-standard data and mixture of standard and non-standard data.

The evaluation results on the standard data are the following:

```
             precision    recall  f1-score   support

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
             precision    recall  f1-score   support

          o       0.99      1.00      1.00      1740
  deriv-per       0.00      0.00      0.00         1
        loc       0.79      0.92      0.85        12
       misc       0.75      0.21      0.33        14
        org       0.50      0.33      0.40         6
        per       0.98      1.00      0.99        82

avg / total       0.99      0.99      0.99      1855
```

The evaluation results on the mixture of standard and non-standard data are these:

```
             precision    recall  f1-score   support

          o       0.99      1.00      0.99     40418
  deriv-per       0.44      0.52      0.48        29
        loc       0.85      0.75      0.80       606
       misc       0.41      0.24      0.30       343
        org       0.69      0.48      0.56       509
        per       0.88      0.96      0.92       983

avg / total       0.98      0.98      0.98     42888
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
