#!/usr/bin/python
#-*-coding:utf8-*-

import warnings
warnings.filterwarnings("ignore")

import sys
import os
reldir=os.path.dirname(os.path.abspath(__file__))

from train_tagger import extract_features
from subprocess import Popen, PIPE
import cPickle as pickle
from StringIO import StringIO
import pycrfsuite

def tag_sent(tokens,tags):
  #print extract_features(tokens,tags,brown)
  return tagger.tag(extract_features(tokens,tags,brown))

def read_and_write(istream,index,msdindex,ostream):
  entry_list=[]
  sents=[]
  for line in istream:
    if line.strip()=='':
      tokens=[]
      tags=[]
      for token,tag in [(e[index],e[msdindex]) for e in entry_list]:
        if ' ' in token:
          if len(token)>1:
            tokens.extend(token.split(' '))
            tags.extend(tag.split(' '))
        else:
          tokens.append(token)
          tags.append(tag)
      tag_counter=0
      ner=tag_sent(tokens,tags)
      ner_proper=[]
      for token in [e[index] for e in entry_list]:
        if ' ' in token:
          if len(token)==1:
            ner_proper.append(' ')
          else:
            ner_proper.append(' '.join(ner[tag_counter:tag_counter+token.count(' ')+1]))
            tag_counter+=token.count(' ')+1
        else:
          ner_proper.append(ner[tag_counter])
          tag_counter+=1
      ostream.write(u''.join(['\t'.join(entry)+'\t'+tag+'\n' for entry,tag in zip(entry_list,ner_proper)])+'\n')
      entry_list=[]
    else:
      entry_list.append(line[:-1].decode('utf8').split('\t'))

if __name__=='__main__':
  import argparse
  parser=argparse.ArgumentParser(description='NER tagger for Slovene (Croatian and Serbian to follow)')
  parser.add_argument('lang',help='language of the text',choices=['sl','sl.true','sl.lower'])
  parser.add_argument('-i','--index',help='index of the column containing surface forms',type=int,default=1)
  parser.add_argument('-m','--msdindex',help='index of the column containing MSDs',type=int,default=2)
  args=parser.parse_args()
  tagger=pycrfsuite.Tagger()
  tagger.open(os.path.join(reldir,args.lang+'.ner.model'))
  brown=dict([(e[1].decode('utf8'),e[0]) for e in [e.split('\t') for e in open(os.path.join(reldir,args.lang+'.brown'))]])
  read_and_write(sys.stdin,args.index-1,args.msdindex-1,sys.stdout)
