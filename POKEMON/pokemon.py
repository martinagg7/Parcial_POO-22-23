#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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


# Source packages.


from weapon_type import WeaponType
class Pokemon():

    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
    >>> from pokemon import Pokemon
    >>> from weapon_type import WeaponType
    >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """
    IDs=[]
        #introducimos los atributos
    def __init__(self,ID,pokemon_name,weapon_type,health_points,attack_rating,defense_rating):


        #ajustamos los valores para que se cumplan las reglas del juego
        if ID in self.IDs:
            raise ValueError("Introduzca otro Id, este ya existe")
        else:
            self.IDs.append(id)
        if health_points>100 or health_points<1:
            raise ValueError("Introduzca unos puntos de vida entre 100 y 1")
        else:
            self.__health_points=health_points
        if attack_rating>10 or attack_rating<1:
            raise ValueError("Introduzca unos puntos de ataque entre 1 y 10")
        else:
            self.__attack_rating=attack_rating
        if defense_rating>10 or defense_rating<1:
            raise ValueError("Introduzca unos puntos de defensa entre 1 y 10")
        else:
            self.__defense_rating=defense_rating
        
        #introducimos los atributos
        self.__ID=ID
        self.__pokemon_name=pokemon_name
        self.__weapon_type=weapon_type
        self.__health_points=health_points
        self.__attack_rating=attack_rating
        self.__defense_rating=defense_rating

            
    def __str__(self):#este el constructor
        return "Pokemon ID "+ str(self.__ID) +" with name "+ str(self.__pokemon_name) +" has as weapon "+ str(self.__weapon_type.name) +" and health "+ str(self.__health_points)
    def __del__(self):#este es el destructor
       print("El pokemon con ID"+ str(self.__ID) +" fue eliminado")
    #Getters
    def get_pokemon_name(self):
        return self.__pokemon_name
    def get_weapon_type(self):
        return self.__weapon_type
    def get_health_points(self):
        return self.__health_points
    def get_attack_rating(self):
        return self.__attack_rating
    def get_defense_rating(self):
        return self.__defense_rating
    
    #Comprobar si el pokemon esta vivo
    def is_alive(self):
        if self.__health_points>0:
            return True
        else:
            return False
        #Defensa de un pokemon
    def fight_defense(self, damage):
        if self.__defense_rating > damage:
            return True
        
        else:
            self.__health_points -= damage - self.__defense_rating
            return True
    #Atacar a otro pokemon
    def fight_attack(self, pokemon):      
        return pokemon.fight_defense(self.__attack_rating)

    


    




    



def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
