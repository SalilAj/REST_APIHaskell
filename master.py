import requests

def pullRepository():

	tokenFile = open('gittoken', 'r')
	print tokenFile.read()

def main():
	pullRepository()



if __name__ == "__main__": main()