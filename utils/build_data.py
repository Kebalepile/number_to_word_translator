import json

def read_file(file_path):
    """Reads the content of a single file given its file path."""
    try:
        # Open JSON file in read mode
        with open(file_path, "r") as file:
            content = json.load(file)
        return content
    
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"An error occurred while reading {file_path}: {e}"
    
def data_set(file_paths):
    """prepare data to be used on number to word mdoel"""
    
    dataset = {
        "number": [],
        "word": []
    }
    
    for file_path in file_paths:
        
       arr =  read_file(file_path)
       bool = determine_list_type(arr)
       
       if bool:
           dataset["number"].extend(arr)
       else:
           dataset["word"].extend(arr)
        
    
    return dataset


def determine_list_type(lst):
    str_count = 0
    int_count = 0

    for item in lst:
        if isinstance(item, str):
            str_count += 1
        elif isinstance(item, int):
            int_count += 1

    if str_count > 0 and int_count == 0:
        # "List contains only strings."
        return  False
    elif int_count > 0 and str_count == 0:
        # "List contains only integers."
        return True