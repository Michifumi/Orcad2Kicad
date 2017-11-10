# About "Cmp2Csv" 


## A. Overview 
+ "Cmp2Csv.py" is a macro program that runs on PC design software Pcbnew of KiCADv4, and it converts Pcbnew component file (.cmp) to csv file.


## B. File contents 
+ "Cmp2Csv.py" ... Convert Pcbnew component file to parts information csv file conversion software (macro)


## C. Confirmation environment 
+ KiCAD Ver 4.07 on Windows 7-64 bit / Ubuntu14.04LTS-64 bit


## D. Usage 
1. Start Pcbnew and select "File" -> "Export" -> "Component file (.cmp)" to create the component file of the board you are designing now.
2. Select and execute the Python console. In case
3. In the console, execute "pwd" and copy this software "Cmp2Csv.py" to the folder that came out (normally "C:\Program Files\KiCad").
4. In the console, enter 'execfile ("Cmp2Csv.py")' and execute it. 
5. The csv file "@partlist.csv" is generated.
