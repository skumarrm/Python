import sys
import getopt

def main(argv):
    inputfile=''
    outputfile=''
    try:
        opts,args=getopt.getopt(argv,"i:o:",["input=","output="])
        print(opts)
        print(args)
    except getopt.GetoptError:
        print('HelloWorld.py -i <inputfile> -o outputfile')
        sys.exit()
    for opt,arg in opts:
        if opt == "-h":
            print('HelloWorld.py -i <inputfile> -o outputfile')
            sys.exit()
        elif opt in ("-i","--input"):
            inputfile = arg
        elif opt in ("-o","--output"):
            outputfile = arg

        print("Input file is", inputfile)
        print( "output file is", outputfile)

if __name__=="__main__":
    main(sys.argv[1:])




