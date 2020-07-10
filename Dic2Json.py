import json

dict = {'Python2': '.py2', 'C++2': '.cpp2', 'Java2': '.java2'}
data = json.load(open('dict.json'))
data.update(dict)


json.dump(data, open('recent.json', "w"))
#for first time make json
#json = json.dumps(dict)

f = open("dict.json", "w")
f.write(json)
f.close()

