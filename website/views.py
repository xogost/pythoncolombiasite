from django.http import JsonResponse
from django.shortcuts import render
import requests

base_url = "https://api.meetup.com/"

def index(request):
	return render(request, "index.html")

def groups(request):
	"""
	Get python groups from meetup.com
	"""
	locaitons = ['bogota', 'medellin', 'pasto', 'cali', 'barranquilla', 'bucaramanga', 'cartagena', 'popayan', 'pereira']
	groups = list()
	for item in locaitons:
		url = "%s/find/groups?filter=all&text=python&country=CO&location=%s&sign=true&key=a6443747e92a6b4e347c6d6c7c4b4f" % (base_url, item)
		response = requests.get(url)
		groups.append(response.json())

	context = {
		"response_data" : groups
	}
	return render(request, "groups.html", context)

def members(request, group_id):
	"""
	Get members of python groups from meetup.com
	"""
	url = "%s/2/members?group_id=%s&sign=true&key=a6443747e92a6b4e347c6d6c7c4b4f" % (base_url, group_id)
	response = requests.get(url)
	context = {
		"response_data" : response.json()
	}
	return render(request, "members.html", context)

def events(request):
	"""
	Get python events from meetup.com
	"""
	url = "%s/find/events?text=python&radius=global&sign=true&key=a6443747e92a6b4e347c6d6c7c4b4f" % (base_url)
	response = requests.get(url)
	context = {
		"response_data" : response.json()
	}
	return render(request, "events.html", context)