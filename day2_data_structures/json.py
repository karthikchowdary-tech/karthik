#Json handling in python
# import json module
import json

#convert python object to json
import json

student = {
    "name": "Karthik",
    "age": 20,
    "course": "Python"
}
json_data = json.dumps(student)

print(json_data)
print(type(json_data))

#convert json to python object
import json

json_data = '{"name":"Karthik","age":20}'

python_data = json.loads(json_data)

print(python_data)
print(type(python_data))

#write json data to file
import json

student = {
    "name": "Karthik",
    "age": 20,
    "city": "Vijayawada"
}

with open("student.json", "w") as file:
    json.dump(student, file)

    #Read json data from file
    import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)