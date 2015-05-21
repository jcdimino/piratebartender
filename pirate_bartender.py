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
    "strong": 0,
    "salty": 5,
    "bitter": 5,
    "sweet": 5,
    "fruity": 0
}

coctail_adj = ["Green", "Purple", "Hairy", "Glorious", "Spritely", "Jubilant", "Stiff"]

coctail_noun = ["Old Fashioned", "Big Boy", "Steamboat", "Sangria", "Mixey"]

customer = {
  "sarah": []
}
  
def find_name():
    new = raw_input("Whats yer name?")
    if new in customer:
        print "Wood yer like the usual mix, %s?" % (new)
        if raw_input() == "y":
            make_drink()
        else:
            make_drink()
    else:
        customer[new] = []
        make_drink()
    return new
  
def preferences():
    preference = {}
    for flavor, question in questions.iteritems():
        print question
        if raw_input() == "y":
            if stock[flavor]:
                preference[flavor] = True
            elif raw_input("We are out of that flavor do ye mind if I restock?") == "n":
                print "One second let me restock"
                stock[flavor] == 5
                preference[flavor] = True
            else:
                preference[flavor] = False
        else:
            preference[flavor] = False
    return preference

def contents(preference):
    drink_recipe = []
    for flavor, yes in preference.iteritems():
        if not yes:
            continue
            
        drink_recipe.append(random.choice(ingredients[flavor]))
        stock[flavor] -= 1
    return drink_recipe
  
def make_drink():
    pref = preferences()
    drink_recipe = contents(pref)
    print 'Your drink, the %s %s contains a: ' % (random.choice(coctail_adj), random.choice(coctail_noun))
    for ingredient in drink_recipe:
        print ingredient + ','
    
     
if __name__ == "__main__":
    find_name()
    drink = raw_input("Would ye like another?")
    for x in drink:
        if x == "y":
            make_drink()