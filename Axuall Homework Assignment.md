## Wiki-searcher

The goal of this project is to create a small web-application that offers a somewhat different way to search for information on wikipedia. We'd love for you to use Python, but we are okay with you choosing a language you are most comfortable with as well. 


We present the following scenario: 

* There is a web server running that resolves to http://*.wiki-search.com
* Depending on the subdomain used, the web service will return the results of the appropriate search on wikipedia. 
* There are notably two types of results that can be supplied - Sometimes wikipedia will direct you to a single result ( exact match ), in other cases it will return a page that indexes possible results.

* For eg: a query to http://dogs.wiki-search.com should return a response of 
```
{ 
    "links": [
        "https://en.wikipedia.org/wiki/Dog"
    ]
}
```

* For eg: a query to http://ordinary.wiki-search.com should return a response of 
```
{ 
    "links": [
        "https://en.wikipedia.org/wiki/Ordinary_(EP)",
        "https://en.wikipedia.org/wiki/Ordinary_(Every_Little_Thing_album)",
        ....
    ]
}
```

Since you don't actually possess the wildcard domain, you can test your app by using a cURL like utility while modifying the Host header to simulate each use case. 

