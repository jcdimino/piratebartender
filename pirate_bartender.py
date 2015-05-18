import random
 
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}
 
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
 
stock = {
    "strong": 5,
    "salty": 5,
    "bitter": 5,
    "sweet": 5,
    "fruity": 5
}  
  
preferences = []

for flavor, question in questions.iteritems():
    print question
    if raw_input() == "y":
        preferences.append(random.choice(ingredients[flavor]))

print 'Your drink contans a: '
for preference in preferences:
    print preference + ','