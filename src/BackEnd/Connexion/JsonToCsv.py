
import json
import csv
class JsonToCsv(object):


  @staticmethod
  def convert(jsonfile_, csvfile_):
   with open(jsonfile_) as file0:
      file1 = json.load(file0)

      # now we will open a file for writing
      data_file = open(csvfile_, 'w')

      # create the csv writer object
      csv_writer = csv.writer(data_file)

      # Counter variable used for writing
      # headers to the CSV file
      count = 0

      for emp in file1:
       if count == 0:

        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

       # Writing data of CSV file
       csv_writer.writerow(emp.values())

       data_file.close()
