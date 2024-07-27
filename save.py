import csv
import pandas as pd

def save_products_to_files(products, excel_filename, text_filename):
    # Save to Excel file
    df = pd.DataFrame(products)
    df.to_excel(excel_filename, index=False)
    
    # Save to text file
    with open(text_filename, 'w', newline='', encoding='utf-8') as text_file:
        writer = csv.writer(text_file, delimiter='\t')
        writer.writerow(['productTitle', 'productUrl', 'finalPrice', 'sales'])  # Write header
        for prod in products:
            writer.writerow([prod['productTitle'], prod['productUrl'], prod['finalPrice'], prod['sales']])

# Пример использования функции
products = [
    {'productTitle': 'Product 1', 'productUrl': 'http://example.com/1', 'finalPrice': 10.99, 'sales': 100},
    {'productTitle': 'Product 2', 'productUrl': 'http://example.com/2', 'finalPrice': 20.99, 'sales': 150}
]

save_products_to_files(products, 'products.xlsx', 'products.txt')
