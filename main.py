import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv("Dataset/Sample_dataset.csv")

def clean_data(df):

    df = df.drop_duplicates().copy()

    df["Sales"] = df["Sales"].fillna(df["Sales"].mean())

    df["Product"] = df["Product"].fillna("Unknown")

    df["PaymentMethod"] = df["PaymentMethod"].fillna(df["PaymentMethod"].mode()[0])

    df["OrderStatus"] = df["OrderStatus"].fillna(df["OrderStatus"].mode()[0])


    
    df["Category"] = df["Category"].str.strip().str.title()

    df["PaymentMethod"] = df["PaymentMethod"].str.strip().str.title()

    df["OrderStatus"] = df["OrderStatus"].str.strip().str.title()


    columns = ["Product", "Category", "Region", "PaymentMethod", "OrderStatus"]

    for col in columns:
        print(f"\n{col}:")
        print(df[col].unique())


    df.to_csv("Reports/Cleaned_data.csv", index=False)

    print(df.head())
    
    return df

def generate_reports(df):

    summary = df.describe()
    print(summary)

    pd.options.display.float_format = '{:,.0f}'.format

    product_sales = df.groupby('Product')['Sales'].sum()    # Product wise sales

    region_sales = df.groupby('Region')['Sales'].sum()     # Region wise sales

    summary.to_csv('Reports/Summary_report.csv')

    product_sales.to_csv('Reports/Product_sales_report.csv')

    region_sales.to_csv('Reports/Region_sales_report.csv')

def generate_charts(df):

    product_sales = df.groupby('Product')['Sales'].sum()    # Product wise sales

    region_sales = df.groupby('Region')['Sales'].sum()     # Region wise sales

    product_sales.plot(kind="bar")
    plt.title("Product Sales")
    plt.tight_layout()
    plt.savefig("Images/Product_sales.png")
    plt.close()

    region_sales.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.savefig("Images/Region_sales.png")
    plt.close()
        
    df["Sales"].plot(kind="hist", bins=10)
    plt.title("Sales Distribution")
    plt.savefig("Images/Sales_distribution.png")
    plt.close()  

def main():
    df = load_data()
    df = clean_data(df)
    generate_reports(df)
    generate_charts(df)

    print("Automation Completed Successfully")

if __name__ == "__main__":
    main()