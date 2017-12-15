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
			value = self.doWork()
			print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
			print value



	def doWork(self):
		print 3
		config = Config(exclude='',ignore='venv',order=SCORE,no_assert=True,show_closures=False,min='A',max='F')
		complexity = CCHarvester('./worker1tempfolder', config)._to_dicts()
		print 4
		print complexity
		print 5
		print complexity.values()

		totalComplexity = 0
		for doc in complexity.values():
			docComplexity = 0
			for codeBlock in doc:
				docComplexity = docComplexity + codeBlock['complexity']

		totalComplexity = totalComplexity + docComplexity
		self.deletefiles()
		return total_cc / len(complexity)


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