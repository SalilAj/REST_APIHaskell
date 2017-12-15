import requests
import socket
from re import match
from radon.complexity import SCORE
from radon.cli.harvest import CCHarvester
from radon.cli import Config

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
			fileTree = responce.json()['tree']

			blobURLs = []
			for blob in fileTree:
				if blob['type'] == 'blob':
					if match('.*\.py', blob['path']):
						blobURLs.append(blob['url'])

			headers = {'Accept': 'application/vnd.github.v3.raw'}

			for index, url in enumerate(blobURLs):
				responce = requests.get(url, params=payload, headers=headers)

				with open('./worker1tempfolder/{}.py'.format(index), 'w') as f:
					f.write(responce.text)
			print 1
			self.doWork()



	def doWork(self):
		print 3
		config = Config(exclude='',ignore='venv',order=SCORE,no_assert=True,show_closures=False,min='A',max='F')
		result = CCHarvester('./worker1tempfolder', config)
		print 4
		print result
		complexity = result._to_dicts()
		print 5
		print complexity


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