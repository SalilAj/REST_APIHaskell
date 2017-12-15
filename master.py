import requests
import Queue
import socket
from flask import Flask
from flask_restful import Resource, Api, request
from time import time

from flask import Flask
app = Flask(__name__)
api = Api(app)

jobQueue = Queue.Queue()
totalWork = 0
workCompleted = 0
totalComplexityValue = 0
accessToken = None

class Server(Resource):

	def get(self):
		global accessToken
		repoTreeListURL = 'https://api.github.com/repos/xysun/pychat/git/trees/{}'
		work=jobQueue.get()
		if work:
			return {'work': work, 'tree': repoTreeListURL, 'token':accessToken}
		else:
			return '', 100

	def doneWork(self):
		value = request.form['complexityValue']
		totalComplexityValue = totalComplexityValue + value
		workCompleted = workCompleted + 1
		if workCompleted == totalWork:
			calculateMeanComplexity()

	def calculateMeanComplexity(self):
		averageComplexityValue = totalComplexityValue / totalWork
		print averageComplexityValue
		closeServer()

api.add_resource(Server, '/')

def closeServer():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
		func()


def pullRepository():
	global jobQueue
	global totalWork
	global accessToken
	tokenFile = open('gittoken', 'r')
	accessToken =  tokenFile.read()
	payload = {'access_token': accessToken}
	resp = requests.get('https://api.github.com/repos/xysun/pychat/commits', params=payload)
	for i in resp.json():
		print i
		print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
		jobQueue.put(i['sha'])
	totalWork = jobQueue.qsize()


if __name__ == "__main__":
	pullRepository()
	startTime = time()
	app.run(host='localhost', port=8001)
	endTime = time()
	TotalRunningTime = endTime - startTime