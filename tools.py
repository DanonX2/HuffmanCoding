def totalbit(filename):
    with open(filename,'rb') as raw:
        data = raw.read()
        p = ''
        for letter in data:
            p += format(letter,'b')
        l = len(p)
    return l


def main():
    with open('C://Users//10111//documents//GitHub//HuffmanCoding//raw','rb') as raw:
        data = raw.read()
        p = ''
        for letter in data:
            p += format(letter,'b')
        l = len(p)
        print(p)
def main2():
    with open('C://Users//10111//documents//GitHub//HuffmanCoding//compressed.txt','rb') as compressed:
        c = compressed.read()
        c.decode('utf-8')
        print(c)

if __name__ == '__main__':
    main2()
    