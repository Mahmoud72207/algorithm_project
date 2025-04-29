import pandas as pd

# قراءة البيانات
df = pd.read_csv('path_to_your_file.csv')

# التحقق من القيم المفقودة
print(df.isnull().sum())

# ملء القيم المفقودة بمتوسط العمود
df.fillna(df.mean(), inplace=True)

# حذف الصفوف المتكررة
df.drop_duplicates(inplace=True)

# حفظ البيانات بعد التنظيف
df.to_csv('cleaned_data.csv', index=False)
