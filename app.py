from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # الحصول على البيانات المدخلة من النموذج
        gender = int(request.form["gender"])
        business = int(request.form["business"])
        design = int(request.form["design"])
        engineering = int(request.form["engineering"])
        software = int(request.form["software"])
        ai = int(request.form["ai"])
        english = int(request.form["english"])
        gpa = int(request.form["gpa"])
        projects = int(request.form["projects"])

        # حساب المسار المهني بناءً على المدخلات (مثال بسيط)
        if ai == 1 and software == 1:
            career = "AI Specialist"
        elif engineering == 1 and design == 1:
            career = "Engineer with Design Expertise"
        elif business == 1 and projects == 2:
            career = "Business Leader"
        elif english == 2 and gpa == 4:
            career = "Global Corporate Role"
        else:
            career = "General Professional Role"
        
        return render_template("form.html", career=career)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
