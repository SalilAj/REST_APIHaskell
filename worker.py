import requests
import socket

token = ''
class WorkerClient:

	host = 'localhost'
	port = '8001'

	def askForWork(self):
		workFile = requests.get('http://localhost:8001/').json()
		if workFile is None:
			die()
		else:
			print workFile
			sha = workFile['work']
			treeURL = workFile['tree']
			token = workFile['token']
			print sha
			print treeURL.format(sha)
			print token

			payload = {'access_token': token}

			responce = requests.get(treeURL.format(sha), params=payload)
			print responce.status_code
			print str(responce.headers)

	def doWork(self, message):
		self.pullCommit(message)
		'''call pull commit get commits and calculate complexity'''
		'''call sendWork with results'''

	def sendWork(self, result):
		sock.connect((self.host, port))
		sock.sendall('doneWork:%s' % result)
		sock.close()

	def die(self):
		return False


	def pullCommit(shaMessage):

		payload = {
		'recursive': 'true',
		'access_token': self.token
		}

		resp = requests.get('https://api.github.com/repos/avast-tl/retdec/commits/%s.patch' % shaMessage, params=payload)
		print resp
		if resp.status_code == 301:
			redirect_url = resp.headers['location'].split('?')[0]
			payload = {'access_token': self.token}
			resp = requests.get(redirect_url, params=payload)
		return resp.json()['tree']


def main():

	tokenFile = open('gittoken', 'r')
	token =  tokenFile.read()
	client = WorkerClient()
	print 1
	client.askForWork()
	'''die'''
	'''else'''
	'''doWork'''
	'''sendWork'''

if __name__ == "__main__": main()