demo_dict = {
    "bug": "error", 
    "function": "code piece"
}

demo_dict["loop"] = "Repeating action"

demo_dict["bug"] = "code error"

print(demo_dict["bug"])

for value in demo_dict:
    print(value)
    print(demo_dict[value])

nest_demo_dict = {
    "France": ["Paris", "Lille"], 
    "Germany":"Berlin"
}

print(nest_demo_dict["France"][1])

nested_list = ["a", "b", ["c", "d"]]

print(nested_list[2][1])

nest_demo_dict["dict"] = demo_dict

print(nest_demo_dict)

print(nest_demo_dict["dict"]["loop"])

