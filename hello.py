# say hello


def hello(name)
  if name :
    print 'Hello',name
  else:
    print 'Hello world'


def main()
  hello(sys.argv[1])


if __name__=='__main__'
  main()
