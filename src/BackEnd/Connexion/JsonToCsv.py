import csv
import io
import json
import logging
import sys

import pandas as pd

logger = logging.getLogger(__name__)
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


def to_string(s):
 try:
     return str(s)

 except :
     #Change the encoding type if needed
     return s.encode('utf-8')


class JsonToCsv:
   def __init__(self):
    self.reduced_item = None
    self.key = None

   def encode(self, param):
     pass


   def reduce_item(self, key, value):


     #Reduction Condition 1
     if type(value) is list:

         i_=0
         for sub_item in value:
             self.reduce_item(key + '_' + to_string(i_), sub_item)
             i_= i_ + 1

     #Reduction Condition 2
     elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            self.reduce_item(key + '_' + to_string(sub_key), value[sub_key])
     #Base Condition
     else:
            self.reduced_item[to_string(key)] = to_string(value)

   def convert(self,json_filename=None, csv_filename=None)->None:
     if len(sys.argv) != 4:
        print ("\nUsage: python json_to_csv.py <node> <json_in_file_path> <csv_out_file_path>\n")
        logger.info("\"Usage: python "+json_filename +"<node> <json_in_file_path> <"+csv_filename+">")

     else:
        #Reading arguments
        node = sys.argv[1]
        json_file_path = sys.argv[2]
        csv_file_path = sys.argv[3]

        with io.open(json_file_path, 'r', encoding='utf-8-sig') as fp:
            json_value = fp.read()
            raw_data = json.loads(json_value)

        try:
            data_to_be_processed = raw_data[node]


        except:
            data_to_be_processed = raw_data

        processed_data = []
        header = []
        for item in data_to_be_processed:
            reduced_item_ = {}
            self.reduce_item(node, item)

            header += reduced_item_.keys()

            processed_data.append(reduced_item_)

        header = list(set(header))
        header.sort()

        with open(csv_file_path, 'w+') as f:
            writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for row in processed_data:
                writer.writerow(row)

        print ("Just completed writing csv file with %d columns" % len(header))
        logger.info("Writing csv file with %d columns" % len(header))
        # Read the JSON file as python dictionary







