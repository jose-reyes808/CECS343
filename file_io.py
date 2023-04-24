import json  

# Function to save data into text file
def save_data(filename, data):  
    with open(filename, 'w') as file:  # Open the specified file in write mode 
        json.dump(data, file)  # Serialize the data to JSON format and write it to the file

# Function that takes a filename and loads the data from txt file
def load_data(filename): 
    try:  # Start a try block to handle exceptions
        with open(filename, 'r') as file:  # Open the specified file in read mode 
            data = json.load(file)  # Deserialize the JSON data from the file and store it in the 'data' variable
    except FileNotFoundError:  # If a FileNotFoundError occurs during the try block
        data = []  # Set the data variable to an empty list as a default value
    return data  # Return the data variable
