dinosaur = {
    'Tyrannosaurus rex' : 'North America',
    'Velociraptor' : 'Gobi Dessert',
    'Triceratops' : 'North America',
    'Stegosaurus' : 'North America',
    'Brachiosaurus' : 'North America',
    'Spinosaurus' : 'North Africa',
    'Allosaurus' : 'North America',
}

print("Dinosaurs and where their fossils were found:", dinosaur)

print("Location of Stregosaurus:", dinosaur['Stegosaurus'])

dinosaur['Velociraptor'] = 'Mongolia'

del dinosaur['Spinosaurus']

print("Last key-value pair:", dinosaur)