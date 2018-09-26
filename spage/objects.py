'''

The 'objects', accessed by spage.objects module allows functionality regarding
objects within the SPAGE environment.

'''

areas = []
characters = []


class Area:
    """
    Consists of various planes on which the user may exist.
    """
    def __init__(self, **kwargs):
        """
        Creates an area.
        """
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
    
    def __str__(self):
        """
        Returns the name of the area.
        """
        return self.name


class Character:
    """
    A generic character who may travel and talk on screen.
    """
    def __init__(self, **kwargs):
        """
        Creates a character.
        """
        self.id = kwargs.get('character_id')
        self.name = kwargs.get('name')
        self.area = kwargs.get('area')
    
    def __str__(self):
        """
        Returns the name of the character.
        """
        return self.name
    
    def set_details(self, img_path, **kwargs):
        """
        Takes a variety of inputs and stores them as character values. Usually
        performed immediately after initialization.
        """
        self.img_path = img_path


def find_character(character_id):
    """
    Returns the character object given the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return character
    
    raise ValueError(f"No Character defined with id: {character_id}")

def character_exists(character_id):
    """
    Returns a boolean corresponding to the character_id provided.
    """
    for character in characters:
        if character.id == character_id:
            return True
    
    return False

def create_character(character_id, **kwargs):
    """
    Adds a character to the list of characters.
    """
    if character_exists(character_id):
        raise ValueError(f"Character with id {character_id} already created.")
    
    new_character = {
        'character_id': character_id,
        'name': kwargs.get('name', character_id),
        'area': kwargs.get('area', None)
        }
    
    characters.append(Character(**new_character))

def find_area(area_id):
    """
    Returns the area object given the area_id provided.
    """
    for area in areas:
        if area.id == area_id:
            return area
    
    raise ValueError(f"No Area defined with id: {area_id}")

def area_exists(area_id):
    """
    Returns a boolean corresponding to the area_id provided.
    """
    for area in areas:
        if area.id == area_id:
            return True
    
    return False

def create_area(area_id, **kwargs):
    """
    Adds an area to the list of areas.
    """
    if area_exists(area_id):
        raise ValueError(f"Area with id {area_id} already created.")
    
    new_area = {
        'area_id': area_id,
        'name': kwargs.get('name', area_id)}
    areas.append(Area(**new_area))
