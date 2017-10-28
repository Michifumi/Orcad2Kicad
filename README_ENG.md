#About "Orcad2Kicad" 



##A. Overview 

+ "Orcad2Kicad.py" is a macro program that runs on the PCB design software Pcbnew of KiCADv4, inputs the OrCAD netlist file, and outputs Pcbnew netlist.


## B. File contents 

1. "Orcad2Kicad.py" ... From OrCAD to KiCAD netlist conversion software (macro)
2. "calay.net" ... sample Calay netlist
3. "partlist.csv" ... sample part information file


## C. Confirmation environment 

+ KiCAD Ver 4.07 on Windows 7-64 bit / Ubuntu14.04LTS-64 bit


## D. Usage 

1. In OrCAD, select the net list format "Calay" and create a net list with the file name "calay.net".
2. Copy this file to KiCAD's board design folder to be edited.
3. Start Pcbnew, in case, select and execute Python console.
4. In the console, execute "pwd" and copy this software "Orcad2Kicad.py" to the folder that is outputed (normally "C: \ Program Files \ KiCad").
5. In the console, enter "execfile (" Orcad2Kicad.py ")" and execute it.
6. A Pcbnew netlist "kicad.net" file is generated. In the created file, the component pads are automatically assigned pin headers with the maximum pin count of each component.
7. Import that netlist. After that, if you change the parts pad, you can design the board.
8. Since the methods up to 7 above are changed for each part, it is troublesome if there are many parts. So, if you can prepare part number and part pad information in csv file, you can use it to create a netlist for KiCAD.
    + Create the part number and component pad information csv file name "partlist.csv" with the attached sample referring to the board design folder you are currently editing.
    + In this state, if you execute "execfile (" Orcad2Kicad.py ")" in the console as in the above 5, the program will automatically detect "partlist.csv" and use this file A netlist is generated.
