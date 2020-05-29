# INTRO TO OOP
Object Orientated Programming is a model that focuses around using data within objects instead of functions. This allows for more efficient and organised layout of code, and prevents data from being overused or lost within the logic of the program.
## What is OOP
Objects are collections of data that share attributes and methods that can be used ot manipulate and access certain functional requirements at certain times rather than access all the functions at all times. 
## Why
Stops the program running redundant lines of code that it is not using, and makes hte code more readable by separating the main run code from the functions that operate in the background, making it easier for users and other developers to navigate the code.
## Class
A Class is the structure used ot create an object in OOP. This would be where the methods and attributes for that specific object will be stored. For example, Class Car would be the holder for attributes such as 'color' and 'model' as well as the methods such as 'Drive()'
## Methods
Methods, like Functions, are blocks of code that are executable when called upon. However, methods only exist within Objects and classes which means that an instance of an object is required to call the methods. Whereas functions are available throughout the entire program.
## Convention
Naming convention of the class file follows the same as any other. However when writing the code to set up a Class, capitalisation is needed. ie. Class Person
## 4 Pillars
- Abstraction
        - Showing users only relevant information and hiding unimportant information that the user doesn't need to see
    
    - Encapsulation 
        - Keeps functions and methods separate from other data and segments of code. So that if something needs modifying, only the function of it needs updating. the rest of the code will be unaffected by the changes.
    
    - Inheritance
        - This is when Classes have access to the function from other Classes above them. For example, a Person class could have attributes such as name and address. A second class, for an Employee could inherit those attributes as well as have their own; such as location and job role.
        - The Parent Class would be Person; and Employee would be the Child Class.
        - Inheritance can happen between multiple classes and have multiple layers. (hierarchical and multiple inheritance)
        
    - Polymorphism
        - This is allowing a method/ function/ variable etc. to be used in more than one way/form.
            - For example; a method could take a variable and depending on its type the function will perform different actions ie. have more than one form.