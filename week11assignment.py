def enroll_student(student_db, course_db, student_id, course_code):
    #checks data base
    if student_id not in student_db or course_code not in course_db:
        raise KeyError("Record not found")

    student = student_db[student_id]
    course = course_db[course_code]

    #shows if student is already enrolled
    if course_code in student["current_courses"]:
        raise ValueError("Already enrolled")

    #looks up prereq for the course
    prereq = course["prereq"]
    if prereq is not None:
        if prereq not in student["passed_courses"]:
            raise ValueError(f"Missing Prereq: {prereq}")

    #appends course_code to the student’s current_courses
    student["current_courses"].append(course_code)
    return True

def process_enrollments(student_db, course_db, request_list):
    result = {
        "successful": [],
        "failed": []
    }

    for student_id, course_code in request_list:
        try:
            enroll_student(student_db, course_db, student_id, course_code)
            result["successful"].append(student_id)
        except (KeyError, ValueError) as e:
            print(f"Enrollment failed for {student_id} in {course_code}: {e}")
            result["failed"].append(student_id)

    return result

#input values
courses = {
    "CS101": {"prereq": None},
    "CS102": {"prereq": "CS101"}
}

students = {
    "Alice": {"passed_courses": ["CS101"], "current_courses": []},
    "Bob":   {"passed_courses": [],        "current_courses": []}
}

requests = [
    ("Alice", "CS102"),     # valid
    ("Bob", "CS102"),       # error: Missing prereq
    ("Charlie", "CS101"),   # errorStudent not found
    ("Alice", "CS102")      # allready enrolled
]

result = process_enrollments(students, courses, requests)
print(result)
