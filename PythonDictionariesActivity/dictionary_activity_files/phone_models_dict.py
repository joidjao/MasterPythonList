phone_models = {
    'iPhone 15' : 'Apple',
    'Galaxy S23' : 'Samsung',
    'Pixel 7' : 'Google',
    'Xperia 1 V' : 'Sony',
    'OnePlus 11' : 'OnePlus',
    'Mate 60 Pro' : 'Huawei',
    'Oppo Find N2 Flip' : 'Oppo',
    'Xiaomi 13 Pro' : 'Redmi',
    'Nokia G50' : 'Nokia',
    'Realme GT 2 Pro' : 'Realme',
}

print("Phone models and their manufacturers:", phone_models)

print("Manufacturer of Galaxy S23:", phone_models['Galaxy S23'])

phone_models['Xiaomi 13 Pro'] = 'Xiaomi'

del phone_models['Mate 60 Pro']

print("Last key-value pair:", phone_models)