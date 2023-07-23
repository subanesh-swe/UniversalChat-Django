#from django.contrib import admin
#from .models import Room

#admin.site.register(Room)

from django.contrib import admin
from .models import Profile, Room


def getMissingFields(allFieldset, includedFieldset):
    if 'id' in allFieldset:
        # because id cannot be used, thae are generated by objects
        allFieldset.remove('id')
    fields = []
    for item in includedFieldset:
        #print("Item:", item)
        fields += item[1]['fields']
    return [field for field in allFieldset if field not in fields]


def getCustomFieldsets():
    customFieldsets = [
        (None, {
            'fields': ('roomId', 'roomName', 'roomPassword',),
        }),
        ('App data', {
            'fields': ('roomProfiles',),
        }),
        ('Important dates', {
            'fields': ('createdAt', 'updatedAt',),
        }),
    ]
    
    allFieldsets =  [field.name for field in Room._meta.fields]
    
    toIncludeFieldsets = getMissingFields(allFieldsets, customFieldsets)

    if toIncludeFieldsets :
        customFieldsets.insert(2, ('Additional data', {
            'fields': tuple(toIncludeFieldsets),
            'description': 'Fieldsets not defined yet. This view is because admin set undefined fields to be here with view (classes: collapse)',
            'classes': ('collapse',),
        }) )

    #print("*****************",allFieldsets)
    #print("-----------------",toIncludeFieldsets)
    #print(">>>>>>>>>>>>>>>>>",customFieldsets)
    #print("\n\n")

    return tuple(customFieldsets)
    

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'isAdmin')
    list_filter = ('user', 'isAdmin')

admin.site.register(Profile, ProfileAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('roomId', 'roomName', 'createdAt', 'updatedAt')

    list_filter = ('createdAt', 'updatedAt')

    readonly_fields = ('roomId',)
    ## use if roomId is set as editable = False
    
    fieldsets = getCustomFieldsets()
    

admin.site.register(Room, RoomAdmin)




    ## using tuple
    ##customFieldsets = (
    ##    (None, {
    ##        'fields': ('roomId', 'roomName', 'roomPassword',),
    ##    }),
    ##    ('App data', {
    ##        'fields': ('roomProfiles',),
    ##    }),
    ##    ('Important dates', {
    ##        'fields': ('createdAt', 'updatedAt',),
    ##    }),
    ##)
    
    ##allFieldsets =  [field.name for field in Room._meta.fields]
    
    ##toIncludeFieldsets = getMissingFields(allFieldsets, customFieldsets)

    ##if len(toIncludeFieldsets) > 0:
    ##    customFieldsets += (('Additional data', {
    ##        'fields': tuple(toIncludeFieldsets , ),
    ##        'description': 'Fieldsets not defined yet. This view is because admin set undefined fields to be here with view (classes: collapse)',
    ##        'classes': ('collapse',),
    ##    }),)

    ##print("*****************",allFieldsets)
    ##print("-----------------",toIncludeFieldsets)
    ##print(">>>>>>>>>>>>>>>>>",customFieldsets)
    ##print("\n\n")
    ##return customFieldsets

    #    return "\n".join([f"{participant['username']} ({participant['userid']})" for participant in obj.Profiles.values()])

    #get_participants.short_description = 'participants'
