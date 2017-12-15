import requests
import Queue
import socket


jobQueue = Queue.Queue()
total_work = 0
workCompleted = 0

class TCPServer(object):

	host = 'localhost'

	def __init__(self, port=None):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host,port))

	def listen(self):
		global total_work
		global workCompleted
		self.sock.listen(5)
		while True:
			connection, address = self.sock.accept()
			print("connected")
			message = connection.recv(4064)
			print message
			print total_work
			print workCompleted
			if message == 'needWork':
				'''pop work from queue and send to worker'''
			elif message == 'doneWork':
				'''add result to total complexity'''
				'''increment work completed'''
				if workCompleted == total_work:
					calculateMeanComplexity()

	def calculateMeanComplexity(self):
		print 'DONE'


def main():
	try:
		pullRepository()
		server = TCPServer(8001)
		server.listen()
	except socket.error, errorMsg:
		print "Failed to create a socket" + str(errorMsg)
	pullRepository()

def pullRepository():
	global jobQueue
	global total_work
	tokenFile = open('gittoken', 'r')
	token =  tokenFile.read()
	payload = {'access_token': token}
	resp = requests.get('https://api.github.com/repos/avast-tl/retdec/commits', params=payload)
	for i in resp.json():
		jobQueue.put(i['sha'])
	total_work = jobQueue.qsize()


if __name__ == "__main__": main()