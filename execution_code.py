#Prompt user to enter file name
file_name = input("Please enter file name: ")
#Checking if file exists and handling exceptions
try:
    with open(file_name, "r") as content:
      data = content.read()
      modified_data = data.upper()
      print(data, "\n")
      #writes modified  data on new file named output.txt
      with open("output.txt", "w") as file: 
         file.write(modified_data)
         print("modifiend data written successfully:\n",modified_data,"\n")
except FileNotFoundError:
       print("File not found.")  
finally:
      print("Thank, for using our program ")
           

