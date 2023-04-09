#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from pokemon import Pokemon
from weapon_type import WeaponType
from enum import Enum
import random
  

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
#son las mismas clases que en  pokemon.py y weapon_type.py
class Weapon_type(Enum):
  KICK= 4
  PUNCH= 2
  ELBOW= 6
  HEADBUTT= 10
class Pokemon():
  def __init__(self, ID, pokemon_name, weapon_type, health_points, attack_rating, defense_rating):
    self.ID = ID
    self.pokemon_name = pokemon_name
    self.weapon_type = weapon_type
    self.health_points = health_points
    self.attack_rating = attack_rating
    self.defense_rating = defense_rating
      #Comprobar si el pokemon esta vivo 
  def is_alive(self):
        if self.health_points>0:
            return True
        else:
            return False
        #Defensa de un pokemon
  def fight_defense(self, damage):
      if self.defense_rating > damage:
          return True
        
      else:
          self.health_points -= damage - self.defense_rating
          return True
    #Atacar a otro pokemon
  def fight_attack(self, pokemon):      
        return pokemon.fight_defense(self.attack_rating)
  

#Funcion para obtener los datos de cada usuario
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
    with open(name_file, newline='') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            ID, pokemon_name, weapon_type, health_points, attack_rating, defense_rating = row
            weapon_type = weapon_type.upper()
            if weapon_type == "KICK":
                weapon_type = Weapon_type.KICK
            elif weapon_type == "PUNCH":
                weapon_type = Weapon_type.PUNCH
            elif weapon_type == "ELBOW":
                weapon_type = Weapon_type.ELBOW
            elif weapon_type == "HEADBUTT":
                weapon_type = Weapon_type.HEADBUTT
            else:
                weapon_type = None
            if weapon_type is not None:
                pokemon = Pokemon(int(ID), pokemon_name, weapon_type, int(health_points), int(attack_rating), int(defense_rating))
                list_pokemons.append(pokemon)
    return list_pokemons

coach_1_pokemons=get_data_from_user("/Users/martinagarciagonzalez/Desktop/Parcial_POO-22-23-main/DATA/coach_1_pokemons.csv")
coach_2_pokemons=get_data_from_user("/Users/martinagarciagonzalez/Desktop/Parcial_POO-22-23-main/DATA/coach_2_pokemons.csv")
coach_1_list = []
# Lista de Pokemons del primer entrenador
coach_1_list = []
for pokemon in coach_1_pokemons:
    coach_1_list.append(f"{pokemon.pokemon_name} = Pokemon({pokemon.ID}, '{pokemon.pokemon_name}', Weapon_type.{pokemon.weapon_type.name}, {pokemon.health_points}, {pokemon.attack_rating}, {pokemon.defense_rating})")

# Lista de Pokemons del segundo entrenador
coach_2_list = []
for pokemon in coach_2_pokemons:
    coach_2_list.append(f"{pokemon.pokemon_name} = Pokemon({pokemon.ID}, '{pokemon.pokemon_name}', Weapon_type.{pokemon.weapon_type.name}, {pokemon.health_points}, {pokemon.attack_rating}, {pokemon.defense_rating})")






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
    coach_to_ask=int("Seleccione el entrenador del que quiere saber sus pokemons ,1 o 2")
    alive_pokemons = []
    for pokemon in list_of_pokemons:
        if pokemon.coach == coach_to_ask and pokemon.health_points > 0:
            alive_pokemons.append(pokemon)

    # Print the list of the alive Pokemons
    print("The following Pokemons are still alive:")
    for pokemon in alive_pokemons:
        print(pokemon.name)

    return alive_pokemons



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
    for pokemon in list_of_pokemons:
      if pokemon.health_points > 0:
        return False




    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.


    # Get configuration for Game User 2.


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")




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

    class Coach:
        def __init__(self, name, pokemons):
            self.name = name
            self.pokemons = pokemons
            self.defeated_pokemons = []

        def is_undefeated(self):
            for pokemon in self.pokemons:
                if pokemon not in self.defeated_pokemons:
                    return True
            return False
    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")
    # Define la función battle
    def battle(pokemon1, coach1, pokemon2, coach2):
        print(f"{pokemon1.pokemon_name} vs {pokemon2.pokemon_name}")
        while pokemon1.is_alive() and pokemon2.is_alive():
            pokemon2.fight_defense(pokemon1.fight_attack(pokemon2))
            if pokemon2.is_alive():
                pokemon1.fight_defense(pokemon2.fight_attack(pokemon1))
        if not pokemon1.is_alive():
            print(f"{pokemon2.pokemon_name} gana!")
            coach1.defeated_pokemons.append(pokemon1)
        else:
            print(f"{pokemon1.pokemon_name} gana!")
            coach2.defeated_pokemons.append(pokemon2)

    #Vamos a super que game_user_1 es el coach 1 y game_user_2 es el coach 2  
    coach_1_pokemons = get_data_from_user("/Users/martinagarciagonzalez/Desktop/Parcial_POO-22-23-main/DATA/coach_1_pokemons.csv")
    coach_2_pokemons = get_data_from_user("/Users/martinagarciagonzalez/Desktop/Parcial_POO-22-23-main/DATA/coach_2_pokemons.csv")

  

    # Creamos los entrenadores
    coach_1 = Coach("Coach 1", coach_1_pokemons)
    coach_2 = Coach("Coach 2", coach_2_pokemons)

    # Creamos las listas de los pokemons de cada entrenador
    print("Game User 1 Pokemons:")
    for pokemon_str in coach_1_list:
        print(pokemon_str)
    print("Game User 2 Pokemons:")
    for pokemon_str in coach_2_list:
        print(pokemon_str)
        
    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")
    # Enfrentamiento de los Pokémon de cada entrenador
    while coach_1_pokemons and coach_2_pokemons:
        pokemon_coach_1 = random.choice(coach_1_pokemons)
        pokemon_coach_2 = random.choice(coach_2_pokemons)
        battle(pokemon_coach_1, coach_1, pokemon_coach_2, coach_2)
        if not coach_1_pokemons:
            print("Game User 2 ha ganado!")
            print("Statitics User 2:")
            print(pokemon.pokemon_name + " tiene " + str(pokemon.health_points) + " puntos de vida aun.")
        else:
            print("Game User 1 ha ganado!")
            print("Statitics User 1:")
            print(pokemon.pokemon_name + " tiene " + str(pokemon.health_points) + " puntos de vida aun.")






# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF









        

    

  







