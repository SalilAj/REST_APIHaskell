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

class Server(Resource):

	def giveWork(self):
		work=jobQueue.get()
		if work:
			return {'work': work}
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
	tokenFile = open('gittoken', 'r')
	token =  tokenFile.read()
	payload = {'access_token': token}
	resp = requests.get('https://api.github.com/repos/avast-tl/retdec/commits', params=payload)
	for i in resp.json():
		print i
		print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
		jobQueue.put(i['sha'])
	totalWork = jobQueue.qsize()


if __name__ == "__main__":
	pullRepository()
	startTime = time()
	app.run(host='127.0.0.0', port=8001)
	endTime = time()
	TotalRunningTime = endTime - startTime

