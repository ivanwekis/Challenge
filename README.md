### This script was developed by Iván Moreno Arias using Python 3
#### The purpose of this program is to be able to encrypt a csv file taking into account the following points :

- The output encrypted file is shown with 'X'. Except for the billing field, which shows the average of all customers.
- If the output file does not exist it is created, and if it does exist it will be overwritten without warning.
- Finally, some statistics are shown on the console. The average, maximum and minimum billing is shown. The average, maximum and minimum length of the names is also shown.
__ __
*CODE STRUCTURE*
#### The code is structured in modules that perform different functions. There are 5 modules in total:
1. main.py: This is the core of the script. Here we execute the different functions of the rest of the modules in order.
2. data_io.py:  The input/output module. In it, we have the functions that allow us to read the .csv files and write to the output one.
3. validations.py: In this module we check if different fields have a correct format.
4. mask.py: As its name indicates, in this module we carry out the algorithms that allow us to encrypt the file.
5. stats.py: Finally, in this module, we calculate the statistics of the customers, whether they are their name or billing.
__ __ 
*EXECUTION*
#### To execute the code we need to introduce the input and output file paths. By default, the script has predefined paths. 
```commandline
python3 main.py --input_file argv[1] --output_file argv[2]
```
#### With the examples provided in the files, an example of execution is...
```commandline
python3 main.py --input_file test_files/customers3.csv --output_files output_files/encrypted.csv
```
__ __
*TEST*
#### Five .csv files are included, only two have correct formats and has been done on purpose. The other three have incorrect formats for different reasons.
#### A file has been created to perform the tests, 'test_main.py'. To execute this file its necessary to execute by the command line the following code:
```
 pytest test_main.py
```
__ __ 
*POSIBLE ERRORS*
#### Errors may appear during execution when the csv file does not have a correct structure.
- Since it is a CSV file in this case, and the separator is ',' this could lead into problems when having a line like: `1, name, surname, email@gmail.com...` this could lead into a bad splitting and hence not being correctly processed.
- If the file does not exist, an exception will be thrown and the scrip will end. 
- If the input file does not have the header correctly, that is, it does not have a "Name", "Email" and "Billing", an exception will be thrown.
- The code checks if the email has a correct format,if the format is not correct, an exception will be thrown and the program will end
- The code also checks if the billing field is a number, if not, an exception will be thrown.
- In resume, if there are any problem, the script will end unsuccessfully.
