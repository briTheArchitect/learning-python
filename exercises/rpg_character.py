"""
Practice exercise inspired by freeCodeCamp prompts.
Focus: input validation, functions, and formatted output.
"""

full_dot = '●'      # Represents one point in a stat
empty_dot = '○'     # Represents an unused slot in a stat

def create_character(character_name, strength, intelligence, charisma):
    # --- NAME VALIDATION ---
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if len(character_name) > 10:
        return 'The character name is too long'
    if " " in character_name:
        return 'The character name should not contain spaces'

    # --- STAT VALIDATION ---
    stats = (strength, intelligence, charisma)
    if any(not isinstance(stat, int) for stat in stats):
        return 'All stats should be integers'
    if any(stat < 1 for stat in stats):
        return 'All stats should be no less than 1'
    if any(stat > 4 for stat in stats):
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'

    # --- BUILD STAT DISPLAY ---
    strength_line = 'STR ' + (full_dot * strength) + (empty_dot * (10 - strength))
    intelligence_line = 'INT ' + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    charisma_line = 'CHA ' + (full_dot * charisma) + (empty_dot * (10 - charisma))

    result = (
        character_name + '\n' +
        strength_line + '\n' +
        intelligence_line + '\n' +
        charisma_line
    )
    return result


print(create_character('ren', 4, 2, 1))
