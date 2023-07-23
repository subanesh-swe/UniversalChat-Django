
"""
ASGI config for UniversalChat_Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UniversalChat_Django.settings')
django_asgi_app = get_asgi_application()


# its important to make all other imports below this comment
import socketio
from socketHandler.socketConfig import sio


application = socketio.ASGIApp(sio, django_asgi_app)



###import os

###from django.core.asgi import get_asgi_application
###from channels.routing import ProtocolTypeRouter, URLRouter
###from channels.auth import AuthMiddlewareStack
###from socketHandler import routing

###os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UniversalChat_Django.settings')

###application = ProtocolTypeRouter({
###    'http': get_asgi_application(),
###    'websocket': AuthMiddlewareStack(
###        URLRouter(
###            routing.socketio_urlpatterns
###        )
###    )
###})






















#import os
#from django.core.asgi import get_asgi_application
#from channels.routing import ProtocolTypeRouter, URLRouter
#from channels.auth import AuthMiddlewareStack
#from django.urls import path

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UniversalChat_Django.settings')

##from socketHandler.socketConfig import app
##application = ProtocolTypeRouter({
##    "http": get_asgi_application(),
##    "WebSocket": AuthMiddlewareStack(
##        URLRouter(
##            [
##                path(r'socket.io/', app),
##            ]
##        )
##    ),
##})

#import socketio
#from socketHandler.socketConfig import sio
#application = socketio.ASGIApp(sio, get_asgi_application());



#import os
#from django.core.asgi import get_asgi_application
#from channels.routing import ProtocolTypeRouter, URLRouter
#from channels.auth import AuthMiddlewareStack
#from django.urls import path
##from socketHandler.socketConfig import app

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

##application = ProtocolTypeRouter({
##    "http": get_asgi_application(),
##    "socket.io": AuthMiddlewareStack(
##        URLRouter(
##            [
##                path(r'socket.io/', app),
##            ]
##        )
##    ),
##})

#import socketio
#from socketHandler.socketConfig import sio
#application = socketio.ASGIApp(sio, get_asgi_application());
