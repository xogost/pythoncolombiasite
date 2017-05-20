from django.db import models

class GroupType(models.Model):	
	class Meta:
		db_table = 'dbi01web_group_types'

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	createdAt =models.DateTimeField(null=False)
	updatedAt =models.DateTimeField(null=True)

class Group(models.Model):	
	class Meta:
		db_table = 'dbi02web_groups'

	id = models.AutoField(primary_key=True)
	group_type = models.ForeignKey('GroupType')
	name = models.CharField(max_length=255)
	quantityMembers = models.IntegerField()
	url = models.CharField(max_length=255)
	createdAt = models.DateTimeField(null=False)

class Member(models.Model):	
	class Meta:
		db_table = 'dbi03web_members'

	id = models.AutoField(primary_key=True)
	group = models.ForeignKey('Group')
	firstName = models.CharField(max_length=255)
	lastName = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=30)
	url = models.CharField(max_length=255)
	skills = models.TextField()
	createdAt =models.DateTimeField(null=False)
	updatedAt =models.DateTimeField(null=True)

class Event(models.Model):	
	class Meta:
		db_table = 'dbi04web_events'

	id = models.AutoField(primary_key=True)
	group = models.ForeignKey('Group')
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	date = models.DateTimeField()
	openHour = models.TimeField()
	closeHour = models.TimeField()
	description = models.TextField()
	country = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	tickets = models.CharField(max_length=100)
	createdAt =models.DateTimeField(null=False)
	updatedAt =models.DateTimeField(null=True)


