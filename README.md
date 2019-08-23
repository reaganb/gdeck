# Machine Problem: Cards

### Requirements:

1. A Python class that will represent a deck of cards named "Deck"

    It should have a class attribute "cards" which contains a list of Card objects upon initialization

2. The Card class represents a card. It has 2 instance variables: suit and rank
    
    The Card class should display the value of its suit and rank when using the print function on it
3. An instance of class Deck should return a random card when the function choice is used on it (Do: from random import choice to be able to use choice)

    Hint: choice takes in a sequence as parameter. To know more: https://pynative.com/python-random-choice/ and https://docs.python.org/3/library/random.html#random.choice

4. An instance of class Deck should return a card/list of cards when slicing is used (To know more about slicing: https://www.oreilly.com/learning/how-do-i-use-the-slice-notation-in-python)

5. Commit your code in GitHub in a repository named gdeck

6. Submit the link to the project here

### Prerequisites
1. Windows/Linux OS
2. Python 3

## The Deck and Card Class

The python file cards.py consist of two classes that represents a deck of cards. These classes can be individually instantiated to another object but one of them is dependent to another, which is the Deck class.

### Card class

1. Class attributes

    **SUIT_SET** - A set for the valid card suits

    **RANK_SET** - A set for the valid card ranks
2. Instance attributes

    **suit** - the suit for the instance
    
    **rank** - the rank for the instance
3. Special methods

    ```__init__``` - The constructor method. Everything in here will be executed once the class was instantiated for another object.
    
    ```__str__``` - The string representation method. This will be called once the object was passed to a print() function.
    
    ```__repr__``` - The object representation method. This will be called when the repr() function was used on it.
    
### Deck class

1. Class attributes

    **cards** - A list containing all the valid Card objects for the deck

2. Special methods

    ```__init__``` - The constructor method. Everything in here will be executed once the class was instantiated for another object.
    
    ```__getitem__``` - This method will make the object iterable. The object can be indexed to get a particular item from the list of cards.
    
    ```__len__``` - The object can passed to the len() method to query for the total number of cards.
    
3. Static methods

    ```shuffle``` - Called at the constructor method. It will shuffle the cards class attribute.

### Run the script:
```
$ python cards.py

A of HEARTS

Shuffling cards.... done!

Number of cards from the deck:  52
10th card:  J of SPADES
1st to 10th card:  [3 of HEARTS, 10 of CLUBS, 8 of SPADES, 2 of HEARTS, 2 of DIAMONDS, 4 of CLUBS, 10 of DIAMONDS, 4 of HEARTS, K of HEARTS, J of SPADES]
1st to 10th with 2 step card:  [3 of HEARTS, 8 of SPADES, 2 of DIAMONDS, 10 of DIAMONDS, K of HEARTS]
Last to First card:  [7 of SPADES, Q of CLUBS, 10 of SPADES, 3 of CLUBS, 7 of HEARTS, 9 of HEARTS, Q of SPADES, A of DIAMONDS, 7 of CLUBS, 9 of DIAMONDS, 6 of DIAMONDS, J of HEARTS, Q of
 HEARTS, 5 of DIAMONDS, J of DIAMONDS, K of SPADES, 10 of HEARTS, 4 of SPADES, 2 of CLUBS, 4 of DIAMONDS, 6 of CLUBS, 5 of HEARTS, A of HEARTS, J of CLUBS, 8 of HEARTS, 8 of CLUBS, A of
SPADES, 9 of CLUBS, 8 of DIAMONDS, K of CLUBS, Q of DIAMONDS, K of DIAMONDS, 5 of SPADES, 9 of SPADES, 2 of SPADES, 5 of CLUBS, 6 of SPADES, 3 of DIAMONDS, A of CLUBS, 7 of DIAMONDS, 6 o
f HEARTS, 3 of SPADES, J of SPADES, K of HEARTS, 4 of HEARTS, 10 of DIAMONDS, 4 of CLUBS, 2 of DIAMONDS, 2 of HEARTS, 8 of SPADES, 10 of CLUBS, 3 of HEARTS]
Randomly pick a card:  6 of SPADES

Shuffling cards.... done!

9th card:  Q of DIAMONDS
1st to 10th card:  [9 of CLUBS, J of CLUBS, 5 of DIAMONDS, 6 of HEARTS, 3 of HEARTS, 3 of SPADES, 6 of SPADES, 9 of DIAMONDS, 10 of CLUBS, Q of DIAMONDS]
1st to 10th, 2 step card:  [9 of CLUBS, 5 of DIAMONDS, 3 of HEARTS, 6 of SPADES, 10 of CLUBS]
Last to First card:  [A of DIAMONDS, 10 of HEARTS, 5 of HEARTS, 7 of DIAMONDS, 7 of CLUBS, 2 of CLUBS, J of DIAMONDS, 9 of SPADES, K of HEARTS, 7 of HEARTS, 4 of SPADES, A of CLUBS, 6 of
 CLUBS, K of DIAMONDS, 2 of SPADES, A of HEARTS, Q of SPADES, 8 of DIAMONDS, 4 of CLUBS,
 8 of SPADES, Q of CLUBS, 7 of SPADES, 5 of CLUBS, 10 of SPADES, 8 of HEARTS, 9 of HEART
S, K of CLUBS, J of SPADES, 6 of DIAMONDS, J of HEARTS, 2 of HEARTS, 3 of CLUBS, 2 of DI
AMONDS, K of SPADES, Q of HEARTS, 4 of DIAMONDS, 4 of HEARTS, 8 of CLUBS, 10 of DIAMONDS
, A of SPADES, 5 of SPADES, 3 of DIAMONDS, Q of DIAMONDS, 10 of CLUBS, 9 of DIAMONDS, 6
of SPADES, 3 of SPADES, 3 of HEARTS, 6 of HEARTS, 5 of DIAMONDS, J of CLUBS, 9 of CLUBS]

Randomly pick a card:  7 of SPADES

```
Note: due to to the static method shuffle(), the output will be different every execution.