# import classes here and initialise objects and run methods
# this separation will make your code more efficient and organised.

from dog_class import *
from cat_class import *

scoobz = Dog('Brown', 'Scooby', 'Great Dane', False, 8, 'BIG')
tabby = Cat('timid', 'black', 'midnight', False, 'Bengal', 2)
print(tabby.happy_birthday())
print(scoobz.happy_birthday())