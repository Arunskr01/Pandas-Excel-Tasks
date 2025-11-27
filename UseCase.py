employees = {
    "E001": {"name": "Arun", "skills": ["Python", "SQL", "Azure"]},
    "E002": {"name": "Riya", "skills": ["Python", "AWS"]},
    "E003": {"name": "Sam", "skills": ["SQL", "GCP", "PowerBI"]},
}

#set of all unique skills
unique_skills = set()
for emp_id, details in employees.items():
    unique_skills.update(details["skills"])
print("Unique Skills:", unique_skills)

#Reversed Dictionary
rev={}
for emp_id, details in employees.items():
    for skill in details["skills"]:
        if skill not in rev:
            rev[skill] = []
        rev[skill].append(details["name"])
print("Reversed Dictionary:", rev)

#Duplicate Skill Set
Duplicate = []
for i in rev.values():
    if len(i)>1:
        Duplicate.append(i)
print("Duplicate Skill Sets:", Duplicate)

#3 most common skill
skills =[]
skildict = {}
for details in employees.values():
    for skill in details["skills"]:
        skills.append(skill)
for i in skills:
    if i not in skildict:
        skildict[i]= 0
    else:
        skildict[i] += 1
skills.clear()
sortedSkills = sorted(skildict,reverse=True)
for i in range(3):
    skills.append(sortedSkills[i])
print("3 most common skills:",tuple(skills))

