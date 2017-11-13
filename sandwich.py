"""
sandwich.py
A fun little script that lets you build out a sandwich/burger.
Hopefully, this pans out.
(c) Nico Lasta, 2017
"""

def main():
    """
    The main module.
    """
    print("Entering sandwich.py's main module.") # TODO comment out when testing

    # list all possible yes/no options
    yes = ['yes','y','ye','yeah','ya','yas']
    no = ['no', 'n', 'nah', 'nope', 'no thanks', 'nah, bro']

    print("Hello there! :)") # greet the user!

    # initialize variables through input
    bread = input('What kind of bread would you like? >').lower()
    bread_toast = input('Would you like that toasted? >').lower()
    if(bread_toast in yes):
    	bread = 'toasted ' + bread
    meat = input('Great! Now what kind of meat would you like on your bread? >').lower()
    cheese_opt = input('Excellent! Would you like any cheese? >').lower()
    if(cheese_opt in yes):
    	cheese = input('What kind of cheese would you like on your sandwich? >').lower()
    else:
    	cheese = "no"
    print('Great! Your', meat, 'sandwich on', bread, 'with', cheese, 'cheese will be ready shortly.')
    print("Below this line, build module's print statement should show.") # TODO comment out when testing
    # build(meat, bread, cheese) # run build module, pass above variables

def build(meat="no", bread="no", cheese="no"):
	"""
	The build module.
	This is where the sandwich/burger will get built out.
	"""
	print("Entering sandwich.py's build module.") # TODO comment out when testing

	# initialize variables
	meat_choice = meat
	bread_choice = bread
	cheese_choice = cheese

	print(meat_choice, bread_choice, cheese_choice) # TODO comment out when testing
	