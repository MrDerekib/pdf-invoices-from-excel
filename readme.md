# :uk: What is this project?
### This is an app that creates PDF invoices out of Excel files.


Libraries and packages used in this project:
- FPDF2
- Pandas
- pathlib
- glob

-----------------------

The target of this project is generate an invoice pdf of each Excel file given in a folder (invoices/).


We use the name of the file to extract from it the invoice number and date of the invoice.
![input file example](screenshots/input_files.png "File input example")

We parse the excel files one by one to generate a table with the table of items with prices and quantities and do the 
total sum.

Inside an excel file:
![input file example](screenshots/input.png "File input example")

In the output folder (PDFs/) we generate pdf file for each excel file like bellow:

![input file example](screenshots/output.png "Generated output pdf")


# :es: Qué hace este proyecto?
## A partir de unos archivos excel, generamos facturas en PDF

Paquetes y librerías usados en este proyecto:
- FPDF2
- Pandas
- glob
- pathlib

-----------------------

El objetivo del proyecto es generar archivos PDF a partir de archivos excel ubicados en la carpeta (invoices/).


Usaremos el nombre de cada uno de los archivos para extraer el número de factura y la fecha de esta.
![input file example](screenshots/input_files.png "File input example")

Recorreremos cada una de las celdas de cada archivo excel para extraer la información a insertar en la factura.

Cada archivo de entrada sigue esta estructura:
![input file example](screenshots/input.png "File input example")

El la carpeta de salida (PDFs/) obtendremos archivos resultantes como este, conservando el mismo nombre que el archivo de origen:

![input file example](screenshots/output.png "Generated output pdf")
