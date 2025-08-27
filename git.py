def modify_file_content(content: str) ->str:
    """
    Modify the file content before writing to the new file.
    You can customize this function as needed.
    For now, it just converts the text to uppercase.
    """
    return content.upper()

def main():
    try:
        
        # Ask user for input file name
        input_filename = input("Enter the name of the file to read:")
        
        # Try to open and read the file 
        with open(input_filename,"r") as infile:
            content = infile.read()
            
        # Modify the cotent
        modified_content = modify_file_content(content)
        
        # Ask user for output file name
        output_filename = input("Enter the name of the new file to write: ")
        
        # Write modified content to new file
        with open(output_filename,"w") as outfile:
            outfile.write(modified_content)
            
        print(f"Modified content successfully written to'{output_filename}'.")
        
    except FileNotFoundError:
        print("Error: The file you specified does not exist.") 
    except PermissionError:
        print("Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
