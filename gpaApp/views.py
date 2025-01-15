from django.shortcuts import render

# Grade to weight mapping
GRADE_WEIGHTS = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.0,
    "F": 0.0,
}

def gpa_calculator(request):
    rows = 10  
    gpa = None  
    input_data = {}

    if request.method == "POST":
        total_points = 0
        total_credit_hours = 0

        for i in range(rows):
            credit_hours = int(request.POST.get(f"credit_hours_{i}", 0))
            grade = request.POST.get(f"grade_{i}", "F")

            input_data[f"credit_hours_{i}"] = credit_hours
            input_data[f"grade_{i}"] = grade


            total_points += GRADE_WEIGHTS.get(grade, 0) * credit_hours
            total_credit_hours += credit_hours


        gpa = round(total_points / total_credit_hours, 2) if total_credit_hours > 0 else 0

    return render(request, "app/app.html", {
        "rows": range(rows),
        "gpa": gpa if gpa is not None else 0,
        "input_data": input_data  
    })
