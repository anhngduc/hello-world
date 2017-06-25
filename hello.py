# say hello
import sys


def hello(name):
  if name :
    print 'Hello',name

  
def main():
  if len(sys.argv) >1 :
    hello(sys.argv[1])
  else:
    print 'Hello world'
    

if __name__=='__main__':
  main()
