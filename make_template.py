import json

with open("/home/dantheman/Desktop/everything/codes/cpp-template/cpp_template.cpp", "r") as file:
  result = {}
  result["cpp_template"] = {}
  result["cpp_template"]["prefix"] = "my_temp"
  result["cpp_template"]["description"] = "my custom cpp template"
  result["cpp_template"]["isFileTemplate"] = True
  result["cpp_template"]["body"] = []

  for line in file:
    result["cpp_template"]["body"].append(line.rstrip())


with open("/home/dantheman/.config/Code/User/snippets/cpp.json", "w") as file:
  file.write(json.dumps(result, indent=4))

print("Template successfully saved")