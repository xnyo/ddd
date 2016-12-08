from gevent import monkey; monkey.patch_all()
import bottle
import json
import requests
import argparse

class invalidJson(Exception):
		pass

@bottle.post("/")
def route():
		responseStatus = 200
		responseData = {}
		try:
				hookURLs = [settings["default_hook"]]
				data = bottle.request.body.read().decode("utf-8")
				print("Incoming data: {}".format(data))
				data = json.loads(data)
				if data is None:
						raise invalidJson()
				if data["channel"] in settings["alternative_hooks"]:
						hookURLs.append(settings["alternative_hooks"][data["channel"]]["hook"])
				print("Sending to: {}".format(hookURLs))
				for i in hookURLs:
						response = requests.post(i, json.dumps(data))
						responseData = response.content
		except invalidJson:
				responseStatus = 400
				responseData["message"] = "Invalid json structure."
		except:
				responseStatus = 500
				responseData["message"] = "Unknown exception."
		finally:
				print("Outgoing data: {}".format(responseData))
				if type(responseData) == dict:
						responseData = json.dumps(responseData)
				bottle.response.status = responseStatus
				return responseData

with open("settings.json", "r") as f:
		settings = json.loads(f.read())

parser = argparse.ArgumentParser(description="Track Datadog updates through Discord")
parser.add_argument("-p", "--port", dest="port", help="Webserver port", default=44132, type=int)
args = parser.parse_args()
	
bottle.run(host="0.0.0.0", port=args.port, server="gevent")
