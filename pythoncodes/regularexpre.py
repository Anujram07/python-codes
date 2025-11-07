import re
text = " Hey i am anuj i am a web developer "

#search for a pattern

# match = re.search("web",text)
# print(match)
# if match:
#     print("match  found")
#     print("start index:",match.start())
#     print("end index:",match.end())


# match = re.findall("web" , text, re.IGNORECASE)
# print("matches", match)

new_text = re.sub("web","app",text)
print("New text : " , new_text)