# nmap-parser
Nmap parser to csv and xlsx files.

## Advantages?
Filtering the info to later perform automated tests against a list of IPs according to their protocol / service / version 🧐

An example:

![Filter example of SSH services](utils/images/filter_example.png)

## Install

```
python3 -m pip install -r setup/requirements.txt
```

### Virtual environment

```
sudo apt install python3-venv
```

To create a python virtual environment:

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r setup/requirements.txt
```

## Execution

### Example

Execute nmap:

```
nmap -T4 -Pn -open --script=default,version,vuln -A -p- -oA nmap/tcp-full-scripts 10.10.1.9
```

Using the tcp-full-scripts.xml file created, execute this tool:

```
# Create CSV file with the output
python3 nmap-parser.py -x nmap/tcp-full-scripts.xml -C

# Create XLSX file with the output
python3 nmap-parser.py -x nmap/tcp-full-scripts.xml -X

# Create CSV and XLSX file with the output
python3 nmap-parser.py -x nmap/tcp-full-scripts.xml -C -X       
```

If you have the file in '10.10.1.9/nmap/' (e.g.: 10.10.1.9/nmap/tcp-full-scripts.xml), run the following command to parse all the .xml files you have in the folder.

```
for xmlfile in $(ls */nmap/*.xml); do python3 nmap-parser.py -x $xmlfile -C -X; done
```

![Parser recursive](utils/images/parser_recursive.png)

The csv and/or xlsx will be saved in the same location as the original.

If you want to save all csv's in the same file, you can do the following:

```
echo "Hostname;IP;State;Port;Protocol;State Port; Service Name; Product; Version; Extrainfo" > /tmp/all-csv-to-one-file.csv
cat */nmap/*.csv >> /tmp/all-csv-to-one-file.csv
```

To convert the information from CSV to XLSX and delete duplicates, you can use this script:

```
python3 scripts/csvtoxlsx.py -c /tmp/all-csv-to-one-file.csv
```

### Output

You will get the following columns with scanner information:

```
Hostname;IP;State;Port;Protocol;State Port; Service Name; Product; Version; Extrainfo
xtormin.local;10.10.1.9;up;445;tcp;open;microsoft-ds;Windows Server 2016 Standard 14393 microsoft-ds;;
xtormin.local;10.10.1.9;up;1433;tcp;open;ms-sql-s;Microsoft SQL Server 2017;"14.00.1000.00; RTM";
xtormin.local;10.10.1.9;up;3389;tcp;open;ms-wbt-server;Microsoft Terminal Services;;
```