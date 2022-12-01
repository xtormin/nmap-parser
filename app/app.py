from utils import cli
import app.modules.nmap_parser as nmap


def run():
    args = cli.get()

    filename = args.nmapxmlfile

    df_nmap_info = nmap.parser(filename)

    if args.csvfile:
        filename_csv = filename + '.csv'
        try:
            df_nmap_info.to_csv(filename_csv,
                                sep=';',
                                encoding='utf-8',
                                header=None,
                                index=False)
            print(f"|+| File created in {filename_csv}")
        except Exception as e:
            print("|-| CSV file not created")
            print(e)

    if args.xsltfile:
        filename_xlsx = filename + '.xlsx'
        try:
            df_nmap_info.style.to_excel(filename_xlsx)
            print(f"|+| File created in {filename_xlsx}")
        except Exception as e:
            print("|-| XLSX file not created")
            print(e)
