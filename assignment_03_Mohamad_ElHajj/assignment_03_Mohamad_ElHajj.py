def tuple_sum(tup1, tup2):
    if len(tup1) != len(tup2):
        raise ValueError("Input tuples must be of the same length.")
    result = tuple(a + b for a, b in zip(tup1, tup2))
    return result
    

    
def write_dict_to_json(dictionary, filename):
    with open(filename, 'w') as file:
        file.write("{\n")
        for key, value in dictionary.items():
            file.write(f'    "{key}": ')
            if isinstance(value, str):
                file.write(f'"{value}"')
            elif isinstance(value, bool):
                file.write('true' if value else 'false')
            elif isinstance(value, (int, float)):
                file.write(str(value))
            elif isinstance(value, list):
                file.write("[")
                for item in value:
                    if isinstance(item, str):
                        file.write(f'"{item}", ')
                    else:
                        file.write(f'{item}, ')
                file.write("]")
            elif isinstance(value, dict):
                write_dict_to_json(value, filename)
            file.write(",\n")
        file.write("}\n")




def read_json_to_dict_list(file_name):
    dict_list = []  # Initialize an empty list to store dictionaries

    with open(file_name, 'r') as file:
        json_data = file.read()  # Read the entire JSON file content as a string

    # Variables to keep track of the parsing process
    current_object = ""
    curly_brace_count = 0

    # Process each character in the JSON string
    for char in json_data:
        if char == '{':
            curly_brace_count += 1
            current_object += char
        elif char == '}':
            curly_brace_count -= 1
            current_object += char
            if curly_brace_count == 0:
                # When curly_brace_count reaches 0, it means we have a complete JSON object
                # Convert the JSON object to a Python dictionary and append to the list
                # Note: eval() is used here for simplicity, but be cautious about using it with untrusted data
                obj_dict = eval(current_object)
                dict_list.append(obj_dict)
                current_object = ""
        else:
            current_object += char

    return dict_list


def main():
  print("---------------------------------")
  print("1. Sum Tuples")
  print("2. Export JSON")
  print("3. Import JSON")
  print("4. Exit")
  c = int(input("Enter your choice: "))
  if c == 1:
    tup1 = (1, 2, 3)
    tup2 = (4, 5, 6)
    output = tuple_sum(tup1, tup2)
    print(output)  
    main()

  elif c == 2:
    # Example dictionary
    my_dict = {
      "name": "John Doe",
      "age": 30,
      "is_student": False,
      "hobbies": ["reading", "hiking", "painting"],
      "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}

    # Example usage
    write_dict_to_json(my_dict, "output.json")
    main()
  elif c == 3:
    json_file_name = "example.json"  # Replace with the actual JSON file name
    result_list = read_json_to_dict_list(json_file_name)
    print(result_list)
    main()

  elif c == 4:
    print("Thank you")
  

main()