import requests
r = requests.get("https://api.github.com/users/Anujram07")



with open("Anujram07.txt","w") as f:
    f.write(r.text)