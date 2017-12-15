import requests
import socket

token = ''
class WorkerClient(tokenValue):

	host = 'localhost'
	port = '8001'

	def askForWork():
		workFile = requests.get('http://127.0.0.0:8001/').json()

	def doWork(message):
		self.pullCommit(message)
		'''call pull commit get commits and calculate complexity'''
		'''call sendWork with results'''

	def sendWork(result):
		sock.connect((self.host, port))
        sock.sendall('doneWork:%s' % result)
        sock.close()

	def die(self):

	def pullCommit(shaMessage):


def main():

	tokenFile = open('gittoken', 'r')
	token =  tokenFile.read()
	client = WorkerClient(token)
	while True:
		client.askForWork()
			'''die'''
		'''else'''
			'''doWork'''
		'''sendWork'''

if __name__ == "__main__": main()