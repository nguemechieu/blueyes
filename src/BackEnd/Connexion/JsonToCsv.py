import csv
import json
import logging

import pandas as pd


def read_json(filename_: str) -> dict:
    try:
        with open(filename_, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename_} file encountered an error")
    return data

def check_data_type(data_type):
    if data_type == str :
        print("Data type  is  String" )
        return "String"
    if isinstance(data_type, object) :
        print("Data type is  object" )
        return "Object"
    if isinstance(data_type, list) :

       print("Data type is  list")
       return "List"
    if isinstance(data_type, dict)  :
        print("Data type  is dict")

        return "dict"


    if isinstance(data_type, int)  :
        print("Data type  is Integer")
        return "Integer"

    if isinstance(data_type, float)  :
        print("Data type is Float")
        return "Float"
    else:
     print("Data type  is Unknown")

     return      'Unknown'

def normalize_json(data) -> dict:
    new_data = dict()
    data1=""
    if data is not None :

      print("Normalizing JSON data from {}"  , data)
      if check_data_type(data) =='List':

        for key, value in  data.items():

            print(key + ": " + value)
            if not isinstance(value, dict):
             new_data[key] = value
             print("Normal key: {}, value: {}".format(key, value))
            else:

                for k, v in value.items():
                 new_data[key + "_" + k] = v
                 print("Normal key2 : {}, value: {}".format(v, new_data[key]))

      if check_data_type(data) =='Object':


          for key in  data:

              print(str(key) + ": " +str( data))

              new_data=[ key]
              print("Normal key: {}, value: {}".format(key,data))


    else: print("Warning Data is NULL")
    return new_data


def generate_csv_data(data) -> str:

    # Defining CSV columns in a list to maintain
    # the order
    global i, da, d, columns, rows, csv_data
    for k in data:
     csv_columns = k

     # Generate the first row of CSV
     csv_data = ",".join(csv_columns) + "\n"
     # Generate the single record present


     for col  in csv_columns:
         for i in k :
            print(  i, k[i] )
            columns = list(k[i])
            print("Normal key -->01: {}, value: {}".format(col,columns))

            csv_data = ",".join(columns) + "\n"
            return csv_data


def create_dataframe(data_: list) -> pd.DataFrame:

       # Declare an empty dataframe to append records
       dataframe = pd.DataFrame()

        # Looping through each record
       for d_ in data_:

        # Normalize the column levels
        record = pd.json_normalize(d_)

        # Append it to the dataframe
        dataframe = dataframe.append(record, ignore_index=True)

        return dataframe
def write_to_file(data: str, filepath: str) -> int:

    try:
        with open(filepath, "w") as f:
         return   f.write(data)
    except:
        raise Exception(f"Saving data to {filepath} encountered an error")


def json_to_csv(json_file_name:str=None, csv_file_name:str=None):
    # Read the JSON file as python dictionary

    global filename, fields, data_print, mydict
    json_data = read_json(filename_=json_file_name)

    # Normalize the nested python dict

    print("Normalize the nested python dict ".format(json_data))

    new_data = normalize_json(data=json_data)

    print("Checking data type...")

    if type(new_data) == dict or type(new_data) == list:
      print("Mode array  ON...")
      for key in new_data:
        count = 0
        for k_value in key:
            print("Attribute key name  " + str(k_value))


            print("Checking type  " + str( type(key.get(k_value))))
            print("Checking key " + str(key))
            print("Writing fields")
            fields =[ str(k_value)]
            print("Field Name "+ str( fields))
            print("Field value(s) "+ str( fields))
            print("Writing column values "+ str( key.get(k_value)))
            row = [ str(k_value)]
            column = [  key.get(k_value)]
            count += 1
            print("Setting rows and column data rows["+str(count)+"]"+"X["+str(count+1 ) +"]"+  "\n" +str(row)+"  "+str(column) + str())
            logging.info("Setting rows and column data rows["+str(count)+"]"+"X["+str(count+1 ) +"]"+  "\n" +str(row)+"  "+str(column) + str())

            print("Writing column values "+ str(column) )

            [data_print ]= k_value.__str__() + ':'+  key.get(k_value).__str__()

            if k_value == key:
               print("Writing column2 values "+ str(column))
               mydict  = str('{'+data_print+'}')
               print("Writing values "+ str(mydict))

            filename = "data3.csv"
            # writing to csv file
            with open(filename, 'w') as csvfile:

             #creating a csv dict writer object
             writer = csv.DictWriter(csvfile, fieldnames = fields)

             # writing headers (field names)
             writer.writeheader()

             # writing data rows
             writer.writerows(str(mydict))






    else :

        print("Mode array OFF...")
        for key in new_data:
         for value in key:
            print("Checking value  " + str(value))
            print("Checking type  " + str( type(value)))
            print("Checking key " + str(key))
            print("Writing fields")
            fields =[ str(value)]
            print("Field 1 "+ str( fields))
            print("Writing column values "+ str( fields))


            if  check_data_type(key) =="List" or check_data_type(key)==[]:
                print("Sub rows found ...")
                print("Checking sub rows values " + str(value))

                for field  in value:

                    print("Checking value " + str(field))

                    [dat]= field


                    print("Checking type " + str(type(value)))

                    for val in key[value]:
                        print("Checking val " + str(val))
                        g=[val]
                        print()




            else:
                print("No sub rows values found")






                for field in value:

                 print("Checking value " + str(field))

                 dat= field
                 print("Checking type " + str(type(dat)))

                 print("dat " +dat)








