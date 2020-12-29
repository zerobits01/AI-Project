from django.urls import re_path

from ai_solutions import consumer

websocket_urlpatterns = [
    re_path(r'ws/solve/(?P<method>\w+)/$', consumer.SolverConsumer.as_asgi()),
]