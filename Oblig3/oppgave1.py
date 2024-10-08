student = {
    "first name" : "Ola",
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1"
}
print(student)
print("--------------------------------------------------")

print(f"Studentens fullstendige navn er {student['first name']} {student['last name']}")
print("--------------------------------------------------")

student["favourite course"] = "ITF10219 " + student["favourite course"]
print(student)
print("--------------------------------------------------")

student["age"] = 30
print(student)