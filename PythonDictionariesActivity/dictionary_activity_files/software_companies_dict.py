software_companies = {
    'Microsoft' : 'Washington',
    'Adobe' : 'California',
    'Oracle' : 'Texas',
    'SAP' : 'Germany',
    'Salesforce' : 'San Francisco',
    'IBM' : 'New York',
    'Intuit' : 'California',
    'Atlassian' : 'San Francisco',
    'Zoom V.C' : 'California',
    'ServiceNow' : 'California',
}

print("Software Companies and their Headquarters:", software_companies)

print("Headquarters of the 3rd Company:", software_companies['Oracle'])

software_companies['Atlassian'] = 'Australia'

del  software_companies['Zoom V.C']

print("Last key-value pair:", software_companies)