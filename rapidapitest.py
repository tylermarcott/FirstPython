import requests

# this API call works, but comes up with a 404 not found, maybe the API is no longer supported.

words = '10'
paragraphs = '1'
format = 'text'

reponse = requests.get("https://alexnormand-dino-ipsum.p.rapidapi.com/?format={formats}&words={words}&paragraphs={paragraphs}",                        
    headers = {                  
        "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
        "X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"                           
    }
)

print(reponse)
