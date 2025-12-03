"""
gradebook.py
Simple GradeBook Analyzer CLI
Name: Vansh Negi
Course: B.Tech CSE AI & ML - 1st Year
Section: A
Enrollment Number: 2501730158
Subject: Programming for Problem Solving using Python
# I made this for Lab Assignment 2
"""

import csv  # for reading csv files (simple excel like files)

# ---------------------------------------------
# reading from csv file
# ---------------------------------------------
def read_csv_file(fname):
    students = {}
    try:
        with open(fname, newline='', encoding='utf-8') as f:
            r = csv.reader(f)
            for row in r:
                if len(row) >= 2:
                    name = row[0].strip()
                    mk = row[1].strip()
                    try:
                        mk = int(float(mk))  
                        students[name] = mk
                    except:
                        print("Skipping invalid marks for:", name)
                else:
                    # if row too small, just skip
                    pass
    except:
        print("Error in reading file or file not found.")
    return students


# ---------------------------------------------
# taking input manually
# ---------------------------------------------
def take_input():
    print("Enter student details (leave name empty to finish):")
    data = {}
    while True:
        nm = input("Name: ").strip()
        if nm == "":
            break
        mrk = input("Marks: ").strip()
        try:
            mrk = int(float(mrk))
            data[nm] = mrk
        except:
            print("Enter proper number for marks!")
    return data


# ---------------------------------------------
# average 
# ---------------------------------------------
def avg(marks):
    if len(marks) == 0:
        return 0
    total = 0
    for m in marks:
        total += m
    return round(total / len(marks), 2)


# ---------------------------------------------
# median 
# ---------------------------------------------
def med(marks):
    if len(marks) == 0:
        return 0
    s = sorted(marks)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2


# ---------------------------------------------
# highest scoring student
# ---------------------------------------------
def highest(stu):
    if not stu:
        return ("", 0)
    max_name = ""
    max_mark = -999
    for n, m in stu.items():
        if m > max_mark:
            max_mark = m
            max_name = n
    return max_name, max_mark


# ---------------------------------------------
# lowest scoring student
# ---------------------------------------------
def lowest(stu):
    if not stu:
        return ("", 0)
    min_name = ""
    min_mark = 9999
    for n, m in stu.items():
        if m < min_mark:
            min_mark = m
            min_name = n
    return min_name, min_mark


# ---------------------------------------------
# Grades
# ---------------------------------------------
def get_grade(m):
    if m >= 90:
        return "A"
    elif m >= 80:
        return "B"
    elif m >= 70:
        return "C"
    elif m >= 60:
        return "D"
    else:
        return "F"


def grading_all(stu):
    g = {}
    cnt = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for n, m in stu.items():
        gr = get_grade(m)
        g[n] = gr
        cnt[gr] += 1
    return g, cnt


# ---------------------------------------------
# pass fail logic
# ---------------------------------------------
def pass_fail(stu, pass_mark=40):
    passed = []
    failed = []
    for n, m in stu.items():
        if m >= pass_mark:
            passed.append(n)
        else:
            failed.append(n)
    return passed, failed


# ---------------------------------------------
# printing table
# ---------------------------------------------
def show_table(stu, grd):
    print("\nName                 Marks   Grade")
    print("--------------------------------------")
    for n, m in stu.items():
        print(f"{n:<20} {m:<6} {grd[n]}")
    print("--------------------------------------")


# ---------------------------------------------
# saving output csv
# ---------------------------------------------
def save_csv(fname, stu, grd):
    try:
        with open(fname, "w", newline='', encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Name", "Marks", "Grade"])
            for n, m in stu.items():
                w.writerow([n, m, grd[n]])
        print("Saved to", fname)
    except:
        print("Error saving file :(")


# ---------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------
def main():
    print("Simple GradeBook Program")
    print("Done by: Vansh Negi\n")

    while True:
        print("\n1. Enter data manually")
        print("2. Load from CSV file")
        print("3. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            students = take_input()
        elif ch == "2":
            fname = input("Enter CSV filename: ")
            students = read_csv_file(fname)
        elif ch == "3":
            print("Exiting program... bye!")
            return
        else:
            print("Invalid choice!")
            continue

        if not students:
            print("No students found! Try again.")
            continue

        marks = list(students.values())
        print("\n--- RESULTS ---")
        print("Total students:", len(students))
        print("Average:", avg(marks))
        print("Median:", med(marks))

        hi_n, hi_m = highest(students)
        lo_n, lo_m = lowest(students)
        print("Highest:", hi_n, "->", hi_m)
        print("Lowest: ", lo_n, "->", lo_m)

        grades, counts = grading_all(students)
        print("\nGrade counts:", counts)

        p, f = pass_fail(students)
        print("Passed:", p)
        print("Failed:", f)

        show_table(students, grades)

        sav = input("Save output to CSV? (y/n): ").lower()
        if sav == "y":
            out = input("Output filename (results.csv): ").strip()
            if out == "":
                out = "results.csv"
            save_csv(out, students, grades)

        again = input("Do you want to analyse another file? (y/n): ").lower()
        if again != "y":
            print("Okay, done. Bye!")
            break


if __name__ == "__main__":
    main()

