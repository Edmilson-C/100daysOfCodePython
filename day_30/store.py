import json

def update_file(data, file_name):
      = read_file(file_name)
    loaded_data.update(data)
    write_file(loaded_data, file_name)

def read_file(file_name):
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("File Not Found")
        file = open(file_name, 'w')
        json.dump({}, file, indent=2)
        return {}
        # raise FileNotFoundError("Ficheiro nao existente")
    else:
        current_data = json.load(file)
        return current_data
    finally:
        file.close()

def write_file(data, file_name):
    try:
        file = open(file_name, 'w')
    except Exception as error:
        print("An error as occurred", error)
    else:
        json.dump(data, file, indent=2)
        print("File generated successfully")
    finally:
        file.close()
