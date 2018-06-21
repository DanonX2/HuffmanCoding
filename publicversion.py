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
        self._q.sort(key=lambda x: x[1])

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
        holder = (node, int(left[1] + right[1]))
        p.put(holder)      
    return p.get() 

#get frequence
freq = {}
filename = input('please type the file name/path\n')
#filename = 'C://Users//10111//documents//GitHub//HuffmanCoding//raw'
try:
    with open(filename,'r') as raw:
        for i in raw.read():
            try:
                freq[i]+=1
            except:
                freq[i] = 1
except:
    print('unable to locate file.')
freq = sorted(freq.items(), key=operator.itemgetter(0))
#create new tree

node = createtree(freq)
def walk_tree(node, prefix="", code={}):
    n = node
    if isinstance(n[0], str):
        code[n[0]] = prefix
    else:
        walk_tree(n[0].left, prefix + "0")
        walk_tree(n[0].right, prefix + "1")
    return code
values = []
keys = []
code = walk_tree(node) 

with open('code.txt','w') as output:
    output.write(str(code))

input()




