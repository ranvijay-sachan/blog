# blog

Step: ```http://localhost:8000/swagger/```

Api's: 

UserProfile: http://localhost:8000/api/v1/users/
UserProfile Details: http://localhost:8000/api/v1/users/1


Signup:


POST:
```http://localhost:8000/api/v1/signup/
{
    "username": "test",
    "password": "welcome",
    "first_name": "ranvijay",
    "last_name": "sachan",
    "email":"r@r.com"
}```



```Login: 
POST:
http://localhost:8000/api/v1/login/

{
	"username" : "root",
	"password" : "Welcome"
}

```


Blog Posts:

```
http://localhost:8000/api/v1/posts/

{
    "text": "",
    "title": ""
}

```

Fech all GET: 

```http://localhost:8000/api/v1/posts/```



GET by Parameter : 

```http://localhost:8000/api/v1/posts/1```


PUT: 

```http://localhost:8000/api/v1/posts/1
{
    "text": "",
    "title": ""
}```



Delete by Parameter : 

```http://localhost:8000/api/v1/posts/1```



Comment POST: http://localhost:8000/api/v1/comment/
```{
    "text": "",
    "post": null
}```


GET ALL: http://localhost:8000/api/v1/comment/
GET WITH PARAMETER: http://localhost:8000/api/v1/comment/1/



PUT: http://localhost:8000/api/v1/comment/1/

```{
    "text": "",
    "post": null
}```

DELETE WITH PARAMETER: http://localhost:8000/api/v1/comment/1/


