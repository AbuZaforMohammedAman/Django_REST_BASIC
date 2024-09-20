https://www.django-rest-framework.org/#installation 

1) Creating a media folder.
2) Creating a status app.
3) pip install pillow.
4) pip freeze > requirements.txt
5) python manage.py makemigrations
6) python manage.py migrate
7) python manage.py createsuperuser
Username: aman
Pass: 123
Email: aman@gmail.com
8) Creating serializers.py file in status
 model = Status
fields = ['id', 'text', 'created_at', 'user']

9) python manage.py shell
from status.models import Status
from status.serializers import StatusSerializer
all_status = Status.objects.all()
serializer = StatusSerializer(all_status,many=True)
print(serializer.data)
[{'id': 1, 'text': 'This is a simple status', 'created_at': '2024-09-12T08:31:28.056354Z', 'user': 1}]

https://www.django-rest-framework.org/api-guide/serializers/#modelserializer

10) python manage.py startapp api

11) List, Create API view part: 1
12) List, Create API View (Part 2)
13) List, Create API View (Part 3)
from rest_framework import generics 

Using generics from Uploading Json text in the sarver
14) Detail, Delete, Update API View using genericAPIView
It is used very little in Rest_API

15) Importance of Test.

16) https://www.django-rest-framework.org/api-guide/testing/

17) Testing CRUD requests (Part 1)

18) Testing CRUD requests (Part 2)

19) Mixins (Part 1) and (Part 2)

mixins is used for using less number of codes like delete, update and post.

20) CRUD with 2 Endpoints

This will need more less code then mixin

21) Handling File Uploads Part 2

import parsers

parser_classes = [parsers.FormParser, parsers.MultiPartParser]
parser_classes = [parsers.FormParser, parsers.MultiPartParser]

this is for uploading images and update images and also using django cleanup