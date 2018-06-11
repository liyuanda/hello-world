#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 12:51:00 2018

@author: Yuanda
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from p4_database_setup import Categories, Base, Item, User
engine = create_engine('sqlite:///newdata.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture=("https://pbs.twimg.com/profile_images/2671170543/"
                      "18debd694829ed78203a5a36dd364160_400x400.png")
             )
session.add(User1)
session.commit()

# Items in Categories 1:
categories1 = Categories(user_id=1, name="Asian")
session.add(categories1)
session.commit()

Item1 = Item(user_id=1, name="Lo Mein",
             description="Stir fry noodles with veggies",
             categories=categories1)
session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Rice Bowl",
             description="Stir fry rice with meats",
             categories=categories1)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Sushi Roll",
             description="Raw fish in a rice roll",
             categories=categories1)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Thai Tea",
             description="Tea with ice and milk",
             categories=categories1)
session.add(Item4)
session.commit()


# Items in Categories 2:
categories2 = Categories(user_id=1, name="American")
session.add(categories2)
session.commit()

Item1 = Item(user_id=1, name="Burger", description="Beef between buns",
             categories=categories2)
session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="French Fries",
             description="Fried potato sticks",
             categories=categories2)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Hot Dog",
             description="Weiner between weiner bun",
             categories=categories2)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Cola",
             description="Brown colored caffeinated drink",
             categories=categories2)
session.add(Item4)
session.commit()


# Items in Categories 3:
categories3 = Categories(user_id=1, name="Italian")
session.add(categories3)
session.commit()

Item1 = Item(user_id=1, name="Pasta", description="Noodles in tomato sauce",
             categories=categories3)
session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Breadstick", description="Greased up bread",
             categories=categories3)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Ravioli",
             description="Cheesed stuffed dumplings",
             categories=categories3)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Wine", description="Grape alcohol",
             categories=categories3)
session.add(Item4)
session.commit()

# Items in Categories 4:
categories4 = Categories(user_id=1, name="Indian")
session.add(categories4)
session.commit()

Item1 = Item(user_id=1, name="Chicken Curry",
             description="Chicken in curry sauce",
             categories=categories4)
session.add(Item1)
session.commit()

Item2 = Item(user_id=1, name="Beef Curry", description="Beef in curry sauce",
             categories=categories4)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Naan", description="Indian bread",
             categories=categories4)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Curry", description="Plain curry sauce",
             categories=categories4)
session.add(Item4)
session.commit()

print("added all data items!")
