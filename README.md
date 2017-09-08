# blog

Step: http://localhost:8000/swagger/

Api's: 


Signup:


POST:
http://localhost:8000/api/v1/signup/
{
    "username": "test",
    "password": "welcome",
    "first_name": "ranvijay",
    "last_name": "sachan",
    "email":"r@r.com"
}



POST:
Login: 

http://localhost:8000/api/v1/login/

{
	"username" : "root",
	"password" : "Welcome"
}


Blog Posts:

http://localhost:8000/api/v1/posts/

{
    "text": "",
    "title": ""
}

GET: http://localhost:8000/api/v1/posts/
GET by Parameter : http://localhost:8000/api/v1/posts/1

PUT: http://localhost:8000/api/v1/posts/1
{
    "text": "",
    "title": ""
}


