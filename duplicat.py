
student_data = {

"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},

"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},

"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"}, # duplicate of id1

"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen = []

for key, value in student_data.items():
    if value not in seen:
        seen.append(value)
        result[key] = value

for key, value in result.items():
    print(f"{key}: {value}")
