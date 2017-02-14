#!/usr/bin/python
#-*-coding:utf8-*-

import sys
import re
import codecs
import cPickle as pickle
import pycrfsuite

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

def conll_iter(stream):
  sent=[]
  for line in stream:
    if line.strip()=='':
      yield sent
      sent=[]
    else:
      sent.append(line.decode('utf8').strip().split('\t'))

def packed_shape(token,index):
  packed=''
  for char in token:
    if char.isupper():
      packed+='u'
    elif char.islower():
      packed+='l'
    elif char.isdigit():
      packed+='d'
    else:
      packed+='x'
  if index==0:
    packed+='_START'
  return re.sub(r'(.)\1{2,}',r'\1\1',packed)

def islcase(token):
  return token.lower()==token

def isnum(token):
  import re
  return re.search(r'\d',token)!=None

def transnum(token):
  import re
  return re.sub(r'\d','D',token)

def wpos(sent,index):
  if index>=0 and index<len(sent):
    return transnum(sent[index].lower())

def wsuf(token,length):
  if token==None:
    return
  if len(token)>length:
    token=transnum(token.lower())
    return token[-length:]

def escape_colon(text):
  return text.replace('\\','\\\\').replace(':','\\:')

def extract_features(tokens,tags,brown):
  features=[]
  for index,(token,tag) in enumerate(zip(tokens,tags)):
    tfeat=[]
    tfeat.append('w[0]='+wpos(tokens,index))
    tfeat.append('packed_shape='+packed_shape(token,index))
    for i in range(3): #w[-1] w[1]
      if wpos(tokens,index-i-1)!=None:
        tfeat.append('w['+str(-i-1)+']='+wpos(tokens,index-i-1))
      if wpos(tokens,index+i+1)!=None:
        tfeat.append('w['+str(i+1)+']='+wpos(tokens,index+i+1))
    for i in range(4): #w[0] suffix
      if wsuf(token,i+1)!=None:
        tfeat.append('s['+str(i+1)+']='+wsuf(token,i+1))
    tfeat.append('POS='+tag[:2])
    tfeat.append('MSD='+tag)
    if wpos(tokens,index) in brown:
      path=brown[wpos(tokens,index)]
      for end in range(2,len(path)+1,2):
        tfeat.append('brown['+str(end)+']='+path[:end])
    if index==0:
      tfeat.append('__BOS__')
    elif index+1==len(tokens):
      tfeat.append('__EOS__')
    features.append(tfeat)
  return features

if __name__=='__main__':
  lang=sys.argv[1]
  trainer=pycrfsuite.Trainer(algorithm='pa',verbose=True)
  trainer.set_params({'max_iterations':10})
  brown=dict([(e[1].decode('utf8'),e[0]) for e in [e.split('\t') for e in open(lang+'.brown')]])
  for sent in conll_iter(open(lang+'.conll')):
    tokens=[e[0] for e in sent]
    tags=[e[1] for e in sent]
    try:
      labels=[e[2] for e in sent]
    except:
      print tokens
    feats=extract_features(tokens,tags,brown)
    #print tokens,labels,feats
    trainer.append(feats,labels)
  trainer.train(lang+'.ner.model')
