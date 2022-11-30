
import pandas as pd
import xml.etree.ElementTree as ET


def parser(nmapxmlfile):
    tree = ET.parse(nmapxmlfile)
    root = tree.getroot()

    output = []
    
    for host in root.findall('host'):
        addr = host.find('address').get('addr')
        state = host.find('status').get('state')
        ports = host.find('ports')
        host_name = None
        
        if host.find('hostnames') is not None:
            for hostname in host.find('hostnames'):
                hostname_type = hostname.get('type')
                if hostname_type == 'user':
                    host_name = hostname.get('name')
        
        if state == 'up':
            for port in ports:
                portid = port.get('portid')
                protocol = None
                if port.get('protocol') is not None:
                    protocol = port.get('protocol')

                if port.find('state') is not None:
                    state_port = port.find('state').get('state')

                if port.find('service') is not None:
                    service_name = port.find('service').get('name')
                    product = port.find('service').get('product')
                    version = port.find('service').get('version')
                    extrainfo = port.find('service').get('extrainfo')

                    output.append([host_name, addr, state, portid, protocol, state_port, service_name, product, version, extrainfo])

        df = pd.DataFrame(output, columns= ['Hostname', 'IP', 'State', 'Port', 'Protocol', 'State Port', 'Service Name', 'Product', 'Version', 'Extrainfo'])

    return df