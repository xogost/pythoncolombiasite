from django.http import JsonResponse
from django.shortcuts import render
import requests

base_url = "https://api.meetup.com/"

def index(request):
	return render(request, "index.html")

def groups(request):
	url = "%s/find/groups?filter=all&text=python&country=57&sign=true&key=a6443747e92a6b4e347c6d6c7c4b4f" % (base_url)
	response = requests.get(url)
	context = {
		"response_data" : response.json()
	}
	return render(request, "groups.html", context)

def members(request, group_id):
	url = "%s/2/members?group_id=%s&sign=true&key=a6443747e92a6b4e347c6d6c7c4b4f" % (base_url, group_id)
	response = requests.get(url)
	context = {
		"response_data" : response.json()
	}
	return render(request, "members.html", context)

def events(request):
	url = "%s/find/events?text=python&sign=true&key=a6443747e92a6b4e347c6d6c7c4b4f" % (base_url)
	response = requests.get(url)
	context = {
		"response_data" : response.json()
	}
	return render(request, "events.html", context)