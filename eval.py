import sys
accs={}
y=[]
y_pred=[]
for line in sys.stdin:
  if line.strip()!='':
    true,pred=line[:-1].split('\t')[-2:]
    y.append(true[2:])
    y_pred.append(pred[2:])
    pair=(true[2:],pred[2:])
    accs[pair]=accs.get(pair,0)+1
#print sorted(accs.items(),key=lambda x:-x[1])
from sklearn.metrics import classification_report,confusion_matrix
print classification_report(y,y_pred)
print confusion_matrix(y,y_pred)
