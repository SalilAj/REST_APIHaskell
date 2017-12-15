import requests
import socket


class TCPClient(object):

	host = 'localhost'

	def __init__(self, port=None):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def askForWork(self):
		sock.connect((self.host, port))
        sock.sendall('needWork')
        message = connection.recv(4064)
        sock.close()
        if message == 'NoWork':
        	self.die()
        else
        	self.doWork(message)

	def doWork(self, message):
		'''call pull commit get commits and calculate complexity'''
		'''call sendWork with results'''

	def sendWork(self, result):
		sock.connect((self.host, port))
        sock.sendall('doneWork:%s' % result)
        sock.close()

	def die(self):

	def pullCommit(self):
		print 'DONE'


def main():
		connection = TCPClient(8001)
		while True:
			connection.askForWork()
			'''if no work'''
				'''die'''
			'''else'''
				'''doWork'''
		'''sendWork'''

if __name__ == "__main__": main()