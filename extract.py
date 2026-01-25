import requests

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"function":"TIME_SERIES_DAILY","symbol":"MSFT","outputsize":"compact","datatype":"json"}

headers = {
	"x-rapidapi-key": "37afda3a09msh0d5ca0efc1c83c9p104ffcjsn466a18e525c6",
	"x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())