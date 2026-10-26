task_completion=92
manager_approval=True

task_completion_req= task_completion>=90
skills = ["Python", "SQL"]
skills_check = "SQL" in skills

skills_copy = skills
same_skill = skills_copy is skills

print(f"Task Completion Requirement Met: {task_completion_req}")
print(f"Manager Approval: {manager_approval}")
print(f"SQL Skill Present: {skills_check}")
print(f"Same Skills List: {same_skill}")