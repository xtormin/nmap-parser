# nmap-parser
Nmap parser to csv and xlsx files.

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

If you have the file in 'nmap/10.10.1.0-24/' (e.g.: nmap/192.168.1.0-24/tcp.xml), run the following command to parse all the .xml files you have in the folder.

```
for xmlfile in $(ls nmap/*/*.xml); do python3 nmap-parser.py -x $xmlfile -C -X; done
```

The csv and/or xlsx will be saved in the same location as the original.

### Output

You will get the following columns with scanner information:

```
Hostname;IP;State;Port;Protocol;State Port; Service Name; Product; Version; Extrainfo
xtormin.local;10.10.1.9;up;445;tcp;open;microsoft-ds;Windows Server 2016 Standard 14393 microsoft-ds;;
xtormin.local;10.10.1.9;up;1433;tcp;open;ms-sql-s;Microsoft SQL Server 2017;"14.00.1000.00; RTM";
xtormin.local;10.10.1.9;up;3389;tcp;open;ms-wbt-server;Microsoft Terminal Services;;
```