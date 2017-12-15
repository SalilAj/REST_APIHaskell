import requests
import Queue

jobQueue = Queue.Queue()
def pullRepository():

	tokenFile = open('gittoken', 'r')
	token =  tokenFile.read()
	payload = {'access_token': token}
	resp = requests.get('https://api.github.com/repos/avast-tl/retdec/commits', params=payload)
	for i in resp.json():
		print i['sha']
		jobQueue.put(i['sha'])
		print jobQueue.qsize()

def main():
	pullRepository()


if __name__ == "__main__": main()