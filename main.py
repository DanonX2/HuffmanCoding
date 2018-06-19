#initallize
import operator
def ix(self, dic, n):
   try:
       return list(dic)[n]
   except IndexError:
       print('not enough keys') 
class Queue(object):
    
    def __init__(self):
        self._q = []

    def put(self, x):
        self._q.append(x)
        self._q.sort(key=lambda x: x[0])
        self._q.reverse()

    def get(self):
        x = self._q[0]
        del self._q[0]
        return x

    def qsize(self):
        return len(self._q)
   
class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
def createtree(frequencies):
    p = Queue()
    for value in frequencies:    
        p.put(value)            
    while p.qsize() > 1:        
        left, right = p.get(), p.get()
        node = HuffmanNode(left, right)
        p.put((left[0]+right[0], node))      
    return p.get() 

#get frequence
freq = {}
with open('C://Users//10111//documents//GitHub//HuffmanCoding//raw.txt','r') as raw:
    for i in raw.read():
        try:
            freq[i]+=1
        except:
            freq[i] = 1
freq = sorted(freq.items(), key=operator.itemgetter(0))
#create new tree

node = createtree(freq)
def walk_tree(node, prefix="", code={}):
    n = node
    if isinstance(n, str):
        code[n] = prefix
    else:
        try:
            walk_tree(n.left, prefix + "0")
            walk_tree(n.right, prefix + "1")
        except:
            code[n[0]] = prefix
    return code
values = []
keys = []
code = walk_tree(node) 
for key in code:
    values += code[key]
    keys += key
values.reverse()
for i in range(0,len(keys)):
    code[i] = values[i]

for i in sorted(freq, reverse=False):
    print(i[0], i[1], code[i[0]]) 







