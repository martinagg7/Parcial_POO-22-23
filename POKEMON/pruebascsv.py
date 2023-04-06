import csv
def get_data_from_user(name_file_1, name_file_2):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file_1 : str
          Name of the CSV file for coach 1.
      name_file_2 : str
          Name of the CSV file for coach 2.

    Returns
    -------
      list_pokemons_1 : list
          List of Pokemons obtained from CSV for coach 1.
      list_pokemons_2 : list
          List of Pokemons obtained from CSV for coach 2.

    Example
    -------
      >>> list_pokemons_1, list_pokemons_2 = get_data_from_user("coach_1_pokemons.csv", "coach_2_pokemons.csv")
    """
    list_pokemons_1 = []
    list_pokemons_2 = []


    # Read CSV file for coach 1
    try:
        with open(name_file_1, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Convert values to the appropriate types
                id_pokemon = int(row[0])
                name_pokemon = row[1]
                weapon_type = row[2]
                health_points = int(row[3])
                attack_rating = int(row[4])
                defense_rating = int(row[5])

                # Create Pokemon objects and append to list
                pokemon = Pokemon(id_pokemon, name_pokemon, weapon_type, health_points, attack_rating, defense_rating)
                list_pokemons_1.append(pokemon)
    except FileNotFoundError:
        print(f"Could not find file {name_file_1}.")
        return None

    # Read CSV file for coach 2
    try:
        with open(name_file_2, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Convert values to the appropriate types
                id_pokemon = int(row[0])
                name_pokemon = row[1]
                weapon_type = row[2]
                health_points = int(row[3])
                attack_rating = int(row[4])
                defense_rating = int(row[5])

                # Create Pokemon

