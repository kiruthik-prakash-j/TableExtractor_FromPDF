import camelot as cm
import sys

from camelot.core import TableList


def get_pdf_location():
    """
    Gets the pdf path/url from the System Argument
    Returns the path/url
    """
    if len(sys.argv) >= 1:
        return sys.argv[1]
    else:
        sys.exit("Type the pdf path or URL")


def get_pdf(pdf_location):
    """
    Gets the pdf location
    Loads the pdf into a TableList
    returns the pdf TableList
    """
    print("Reading the PDF File")
    input_pdf: TableList = cm.read_pdf(pdf_location, flavor='stream')
    return input_pdf


def get_dataframe(input_pdf):
    """
    Gets the TableList as an argument
    Scrapes the required data
    Returns the dataframe of required data (literacy rate)
    """
    print("Getting the Table")
    df = input_pdf[1].df.loc[19:22, 1:3]
    print("Resetting the Index and Table Headings")
    df = df.reset_index(drop=True)
    df.columns = ["KPI", "2001", "2011"]
    print("Converting the values to Float datatype")
    df.loc[:, ["2001", "2011"]] = df.loc[:, ["2001", "2011"]].astype(float)
    return df


def save_csv(df):
    """
    Gets the Dataframe as an argument
    Saves the dataframe as a CSV File
    """
    print("Saving to CSV File")
    csv_filename = "packt_output.csv"
    df.to_csv(csv_filename)
    print("Saved " + csv_filename)


def save_excel(df):
    """
    Gets the Dataframe as an argument
    Saves the dataframe as a Excel file
    """
    print("Saving to Excel File")
    excel_filename = "packt_output_excel.xlsx"
    df.to_excel(excel_filename)
    print("Saved " + excel_filename)


def main():
    pdf_location = get_pdf_location()
    input_pdf = get_pdf(pdf_location)
    df = get_dataframe(input_pdf)
    save_csv(df)
    save_excel(df)


if __name__ == "__main__":
    main()
