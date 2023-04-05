import pandas as pd

# Загружаем CSV файл
csv_file = pd.read_csv("example.csv")

# Конвертируем в Excel
excel_file = pd.ExcelWriter("example.xlsx")
csv_file.to_excel(excel_file, index=False)
excel_file.save()

# Выводим результаты
print("CSV file converted to Excel!")
