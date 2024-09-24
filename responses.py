import random
import os
from ip import get_ip_info

def get_source_code() -> str:
    # Obtient le chemin du fichier source du script en cours d'exécution
    file_path = os.path.abspath("bot.py")
    
    # Lit le contenu du fichier
    with open(file_path, 'r') as file:
        source_code = file.read()
    
    return source_code

def get_response(message: str) -> str:
    p_message = message.lower()
    
    saloperies = [
        "Bougre d'extrait de cornichon !",
        "Espèce de bachi-bouzouk !",
        "salope",
        "saloperie de merde",
        "Mille milliards de mille sabords !",
        "fils de babouin des neige",
        "Moule à gaufres !",
        "Sapajou !",
        "Iconoclaste !",
        "Va-nu-pieds !",
        "Ectoplasme !",
        "Mille millions de mille milliards de mille sabords",
        "Crétin des Alpes"
    ]

    if p_message == '!help':
        return '`Bienvenue dans la section aide : les commandes son\n- !help\n- !miaou\n- !roll\n- !ip\n- !source\n- !music\n et surement d autres prochainement`'
    
    if p_message == '!miaou':
        return 'purrrrrrrrrrrrrrrr!'
    
    if p_message == '!roll':
        return str(random.randint(1, 6))
    
    if p_message == '!ip':
        get_ip_info()
    
    if p_message == '!source':
        return get_source_code()
    
    if p_message == '!music':
        return 'https://www.youtube.com/watch?v=cQKGUgOfD8U'

    return random.choice(saloperies)