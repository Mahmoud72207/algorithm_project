import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# تحميل البيانات (تأكد إن اسم الملف ومكانه صح)
data = pd.read_csv("D:/Projects/algorithm_project/modified_sample_dataset.csv.xls")

# حذف عمود الترقيم لأنه غير مفيد
data = data.drop(columns=['name id'])

# حذف التكرارات وملء القيم الفارغة بالقيم الأكثر تكرارًا
data = data.drop_duplicates()
data = data.fillna(data.mode().iloc[0])

# تحويل كل القيم إلى رقمية
data = data.apply(pd.to_numeric, errors='coerce')

# تحديد المدخلات (X) والمخرجات (y)
X = data.drop('career path', axis=1)
y = data['career path']

# تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تدريب النموذج باستخدام Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# التقييم على بيانات الاختبار
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# التحقق المتقاطع (Cross Validation)
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"Cross-validation Scores: {cv_scores}")
print(f"Mean CV Score: {cv_scores.mean():.2f}")

# دالة لإدخال بيانات المستخدم
def get_user_input():
    user_data = {
        'gender': int(input("Gender (0=Female, 1=Male): ")),
        'besiness and leadership': int(input("Business and Leadership (0=No, 1=Yes): ")),
        'design and excel': int(input("Design and Excel (0=No, 1=Yes): ")),
        'engineering and math': int(input("Engineering and Math (0=No, 1=Yes): ")),
        'software and c++': int(input("Software and C++ (0=No, 1=Yes): ")),
        'Ai and python': int(input("AI and Python (0=No, 1=Yes): ")),
        'english level': int(input("English Level (0=Low, 1=Middle, 2=High): ")),
        'GPA': int(input("GPA (1-4): ")),
        'level projects participanted': int(input("Project Participation Level (0=Low, 1=Middle, 2=High): "))
    }
    return pd.DataFrame([user_data])

# التنبؤ بالمسار المهني بناءً على إدخال المستخدم
career_labels = {
    1: "Engineer",
    2: "Software Engineer",
    3: "AI Researcher",
    4: "Business Analyst",
    5: "Graphic Designer"
}

user_input = get_user_input()
prediction = model.predict(user_input)
print(f"The recommended career path is: {career_labels.get(prediction[0], 'Unknown')}")
