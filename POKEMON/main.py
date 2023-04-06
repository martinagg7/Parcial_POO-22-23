#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from pokemon import Pokemon
  

"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""

class Pokemon():
  def __init__(self, ID, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
    self.ID = ID
    self.pokemon_name = pokemon_name
    self.weapon_type = weapon_type
    self.health_points = health_points
    self.attack_rating = attack_rating
    self.defense_rating = defense_rating



def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """
    list_pokemons = []
    with open(name_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                ID = int(row[0])
                pokemon_name = row[1]
                weapon_type = row[2]
                health_points = int(row[3])
                attack_rating = int(row[4])
                defense_rating = int(row[5])
                pokemon = Pokemon(ID, pokemon_name, weapon_type, health_points, attack_rating, defense_rating)
                list_pokemons.append(pokemon)
            except ValueError:
                print("Algo no funciona con el archivo")
    return list_pokemons

coach_1_pokemons=get_data_from_user("/Users/martinagarciagonzalez/Desktop/Parcial_POO-22-23-main/DATA/coach_1_pokemons.csv")
coach_2_pokemons=get_data_from_user("/Users/martinagarciagonzalez/Desktop/Parcial_POO-22-23-main/DATA/coach_2_pokemons.csv")

coach_1=[]
coach_2=[]

for pokemon in coach_1_pokemons:
    coach_1.append(pokemon.pokemon_name)
for pokemon in coach_2_pokemons:
    coach_2.append(pokemon.pokemon_name)

print("Estos son los pokemon de coach 1:")
print(coach_1)
print("Estos son los pokemon de coach 2:")
print(coach_2)




    
          






def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """



def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """


def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.


    # Get configuration for Game User 2.


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:


    # Choose first pokemons
 

    # Main loop.



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
