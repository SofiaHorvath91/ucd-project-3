# Include hogwarts_quiz app's urls in project myproject
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hogwarts_quiz.urls')),
]
# Configure url path for statis files (static/txt+img+css)
urlpatterns += staticfiles_urlpatterns()

