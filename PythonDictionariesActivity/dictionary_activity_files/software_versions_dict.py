software_versions = {
    'Microsoft Windows' : 'Windows 11 (22H2)',
    'Adobe Photoshop' : 'Photoshop 2024 (24.0)',
    'Google Chrome' : 'Chrome 118.0.5993.90',
    'Mozilla Firefox' : 'Firefox 118.0',
    'Microsoft Office' : 'Office 2021',
    'Zoom' : 'Zoom 5.15.8',
}

print("Software programs and their latest versions:", software_versions)

print("Version of Mozilla Firefox:", software_versions['Mozilla Firefox'])

software_versions['Adobe Photoshop'] = 'Photoshop 2024 (25.0)'

del software_versions['Microsoft Office']

print("Last key-value pair:", software_versions)