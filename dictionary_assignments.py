"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student_info = {
    'student_name': 'Upendra Bahinipati',
    'age': 24,
    'roll_no': 21,
    'class': 'MCA',
    'section': 'D',
    'percentage': 78.9,
    'college_name': 'Trident Academy of Technology'
}
print(student_info.get('percentage'))

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
student_infos = {
    'student_1': {'student_name': "Upendra Bahinipati", 'age': 24, 'roll_no': 21, 'class': 'MCA', 'section': 'D',
                  'percentage': 78.9, 'university_name': 'Trident Academy of Technology'},
    'student_2': {'student_name': "Kisan Swain", 'age': 23, 'roll_no': 28, 'class': 'MCA', 'section': 'D',
                  'percentage': 93.2, 'university_name': 'Trident Academy of Technology'},
    'student_3': {'student_name': "Rashmi Mohapatra", 'age': 24, 'roll_no': 20, 'class': 'MCA', 'section': 'C',
                  'percentage': 88.8, 'university_name': 'Trident Academy of Technology'}
}

print(student_infos['student_3']['class'])

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""

employees_data = {
    'employee_1': {'employee_name': 'Upendra Bahinipati', 'Salary': 300000, 'Designation': 'Automation Tester'},
    'employee_2': {'employee_name': 'Rohan Chetri', 'Salary': 1200000, 'Designation': 'Automation Tester'},
    'employee_3': {'employee_name': 'Sudarsan Parida', 'Salary': 800000, 'Designation': 'Junior AI/ML Engineer'},
    'employee_4': {'employee_name': 'Rasesh Ku. Pradhan', 'Salary': 1500000, 'Designation': 'Full Stack Developer'}
}

print(employees_data['employee_3']['Designation'])