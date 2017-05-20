from django.contrib import admin
from database_integration.models import GroupType, Group, Member, Event

class GroupTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'createdAt')
admin.site.register(GroupType, GroupTypesAdmin)

class GroupAdmin(admin.ModelAdmin):
	list_display = ('id','group_type','name','quantityMembers','url','createdAt')
	def get_group(self, obj):
		return obj.group_type.name
admin.site.register(Group, GroupAdmin)

class MemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(Member, MemberAdmin)

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)


