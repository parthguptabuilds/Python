staff = {
    'EMP01': {'name': 'Arun', 'dept': 'Engineering', 'monthly_salary': 8500},
    'EMP02': {'name': 'Bala', 'dept': 'HR', 'monthly_salary': 6000},
    'EMP03': {'name': 'Chitra', 'dept': 'Engineering', 'monthly_salary': 9200},
    'EMP04': {'name': 'Deepa', 'dept': 'Marketing', 'monthly_salary': 7100}
}

engineering_payroll = {data['name']: data['monthly_salary'] * 12 for eid, data in staff.items() if data['dept'] == 'Engineering'}

print("Engineering Annual Payroll:")
print(engineering_payroll)