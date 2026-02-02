
def insert_student_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age Cannnot be Less than Zero or Negative")
        
        else:
            print(name)
            print(age)
            print("Inserted into Database.")

    else:
        raise TypeError("Incorrect Data Type")
    

def update_student_data(name:str,age:int):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age Cannnot be Less than Zero or Negative")
        
        else:
            print(name)
            print(age)
            print("Inserted into Database.")

    else:
        raise TypeError("Incorrect Data Type")


# We have 2 fields here in above code and you can think for these 2 fields we have to write this much code...Suppose if there are 10 fields then code will be too long instead we will use Pydantic.