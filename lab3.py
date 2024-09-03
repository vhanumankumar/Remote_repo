# REQ - 1 : Create dictionary
emp = {'ename':['hari', 'Thomas', 'Raj', 'Laksh', 'subha'], 'age':[21, 23, 22, 35, 20], 'salary':[15000, 18000, 26000, 30000, 10000]}
print("The Employee datase is:", emp)
print("The Employee salaries are:")
print(emp['salary'])
print("The salaries are:")
for v in emp['salary']:
    print(v)
L1 = emp['salary']
print("The listed salaries:", L1)
print('The sorted salaries are:', sorted(L1))
print("The reveresed salaries:",L1[::-1])
print("The minimum salary is:", min(L1))
print("The maximum salary is:", max(L1))
print("The total salaary is:", sum(L1))

