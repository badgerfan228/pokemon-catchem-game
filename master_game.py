import gamebox
import pygame
import random
import math

camera = gamebox.Camera(800, 600)
main_logo = gamebox.from_image(380, 240, "Menu_Sprites/pokemon_logo.png")
trainer_sprite = gamebox.load_sprite_sheet("trainer_sprite_sheet.png", 1, 12)
camera.clear("white")
camera.draw("Press Space to begin a new game!", 40, "red", 385, 350)
b1 = gamebox.from_color(385, 450, "red", 300, 50)
camera.draw(b1)
camera.draw("Click to login to saved account", 28, "black", 385, 450)
camera.draw(main_logo)
bulbasaur_starter_sprite = gamebox.from_image(175, 300, "Pokemon_Sprites/bulbasaur.png")
bulbasaur_starter_sprite.size = [200, 145]
bulbasaur_select_box = gamebox.from_color(175, 435, "red", 200, 50)
charmander_starter_sprite = gamebox.from_image(410, 300, "Pokemon_Sprites/charmander.png")
charmander_starter_sprite.size = [275, 260]
charmander_select_box = gamebox.from_color(410, 435, "red", 200, 50)
squirtle_starter_sprite = gamebox.from_image(645, 300, "Pokemon_Sprites/squirtle.png")
squirtle_starter_sprite.size = [275, 260]
squirtle_select_box = gamebox.from_color(645, 435, "red", 200, 50)
battle_grounds = gamebox.from_image(400, 100, "Menu_Sprites/battleground.png")
battle_spaces = gamebox.from_image(400, 250, "Town_Sprites/battle_spaces.png")
fight_options = gamebox.from_image(400, 480, "Menu_Sprites/fight_screen.png")
move_options = gamebox.from_image(400, 480, "Menu_Sprites/move_options.png")
twinleaf = gamebox.from_image(400, 300, "Town_Sprites/twinleaf_town.png")
route_201 = gamebox.from_image(400, 300, "Town_Sprites/route_201.png")
twinleaf.size = [800, 600]
route_201.size = [800, 600]
battle_grounds.size = [800, 500]
battle_spaces.size = [600, 300]
fight_options.size = [600, 250]
move_options.size = [600, 250]
trainer = gamebox.from_image(400, 400, trainer_sprite[0])
trainer.size = [50, 50]
camera.display()
game_on = False
new_user = False
default_battle_screen = True
move_screen = False
bag_screen = False
pokemon_screen = False
new_game = False
filename = ""
user = ""
current_town = twinleaf
last_town = twinleaf
current_party = []
slot_1 = None
slot_2 = None
slot_3 = None
slot_4 = None
slot_5 = None
slot_6 = None
sheet_index = 0

# This part of the code contains the gameboxes for the pokemon in the game
bulbasaur = gamebox.from_image(540, 200, "Pokemon_Sprites/bulbasaur.png")
bulbasaur.size = [150, 100]
bulbasaur_back = gamebox.from_image(277, 302, "Pokemon_Sprites/bulbasaur_b.png")
bulbasaur_back.size = [150, 160]
ivysaur = gamebox.from_image(565, 200, "Pokemon_Sprites/ivysaur.png")
ivysaur.size = [200, 200]
ivysaur_back = gamebox.from_image(277, 290, "Pokemon_Sprites/ivysaur_b.png")
ivysaur_back.size = [150, 160]
venusaur = gamebox.from_image(540, 175, "Pokemon_Sprites/venusaur.png")
venusaur.size = [200, 200]
venusaur_back = gamebox.from_image(277, 290, "Pokemon_Sprites/venusaur_b.png")
venusaur_back.size = [160, 170]
charmander = gamebox.from_image(539, 180, "Pokemon_Sprites/charmander.png")
charmander.size = [200, 200]
charmander_back = gamebox.from_image(277, 290, "Pokemon_Sprites/charmander_b.png")
charmander_back.size = [150, 160]
charmeleon = gamebox.from_image(540, 180, "Pokemon_Sprites/charmeleon.png")
charmeleon.size = [200, 200]
charmeleon_back = gamebox.from_image(277, 285, "Pokemon_Sprites/charmeleon_b.png")
charmeleon_back.size = [150, 160]
charizard = gamebox.from_image(533, 147, "Pokemon_Sprites/charizard.png")
charizard.size = [200, 200]
charizard_back = gamebox.from_image(277, 270, "Pokemon_Sprites/charizard_b.png")
charizard_back.size = [150, 160]
squirtle = gamebox.from_image(545, 190, "Pokemon_Sprites/squirtle.png")
squirtle.size = [200, 200]
squirtle_back = gamebox.from_image(277, 292, "Pokemon_Sprites/squirtle_b.png")
squirtle_back.size = [150, 160]
wartortle = gamebox.from_image(545, 180, "Pokemon_Sprites/wartortle.png")
wartortle.size = [200, 200]
wartortle_back = gamebox.from_image(277, 285, "Pokemon_Sprites/wartortle_b.png")
wartortle_back.size = [150, 160]
blastoise = gamebox.from_image(545, 180, "Pokemon_Sprites/blastoise.png")
blastoise.size = [200, 200]
blastoise_back = gamebox.from_image(277, 280, "Pokemon_Sprites/blastoise_b.png")
blastoise_back.size = [170, 180]
master_pokedict_wild = {1: bulbasaur, 2: ivysaur, 3: venusaur, 4: charmander, 5: charmeleon, 6: charizard, 7: squirtle,
                        8: wartortle, 9: blastoise}
master_pokedict_user = {1: bulbasaur_back, 2: ivysaur_back, 3: venusaur_back, 4: charmander_back, 5: charmeleon_back,
                        6: charizard_back, 7: squirtle_back, 8: wartortle_back, 9: blastoise_back}
master_pokedict_names = {1: "bulbasaur", 2: 'ivysaur', 3: 'venusaur', 4: 'charmander', 5: 'charmeleon', 6: 'charizard',
                         7: 'squirtle', 8: 'wartortle', 9: 'blastoise'}

master_towns_login = {0: battle_grounds, 1: twinleaf, 2: route_201}
master_towns_save = {battle_grounds: 0, twinleaf: 1, route_201: 2}
current_pokemon = 1
mouse_xpos = 300
mouse_ypos = 300
database = {}
with open('PokemonDataCsv.csv', 'r+') as f:
    next(f)
    for line in f:
        data = line.strip().split(',')
        database.update({data[0]: dict()})
        database[data[0]].update({'movelist': []})
        database[data[0]].update({'basestats': []})
        database[data[0]].update({'type': ''})
        database[data[0]].update({'dexNo': 0})
        for i in range(1, 5):
            database[data[0]]['movelist'].append(data[i])
        for i in range(5, 13):
            database[data[0]]['basestats'].append(int(data[i]))
        database[data[0]]['type'] += data[13]
        database[data[0]]['dexNo'] = int(data[14])


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.dexNo = database[name]['dexNo']
        self.level = random.randint(1, 9)
        self.ivs = [random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31),
                    random.randint(0, 31), random.randint(0, 31)]
        self.current_hp = calc_max_hp(self)
        self.moveset = database[name]['movelist']
        self.type = database[name]['type']
        self.realstats = calc_all_stats(self)
        self.max_hp = calc_max_hp(self)
        self.barLength = 100
        self.barRatio = self.max_hp / self.barLength
        self.hBar = gamebox.from_color(200, 214, "red", self.current_hp / self.barRatio, 4)
        self.hBarTrim = gamebox.from_color(200, 214, "white", self.barLength + 1, 6)

    def set_level(self, level):
        self.level = int(level)

    def set_ivs(self, hp, att, defense, spA, spD, speed):
        self.ivs = [hp, att, defense, spA, spD, speed]

    def set_current_hp(self, hp):
        self.current_hp = int(hp)

    def set_type(self, type):
        self.type = type

    def set_dexNo(self, dexNo):
        self.dexNo = int(dexNo)

    def set_stats(self, arr):
        self.realstats = arr

    def __str__(self):
        return f"{self.name}|{self.ivs[0]},{self.ivs[1]},{self.ivs[2]},{self.ivs[3]},{self.ivs[4]},{self.ivs[5]}|" \
               f"{self.type}|{self.current_hp}|{self.level}|{self.dexNo}"

    def update(self):
        self.draw_health()

    def take_damage(self, amt):
        if self.current_hp > 0:
            self.current_hp -= amt
        elif self.current_hp <= 0:
            self.current_hp = 0
        self.update()

    def gain_health(self, amt):
        if self.current_hp > 0:
            if self.current_hp + amt > self.max_hp:
                self.current_hp = self.max_hp
            else:
                self.current_hp += amt
        self.update()

    def draw_health(self):
        self.max_hp = calc_max_hp(self)
        self.barRatio = self.max_hp / self.barLength
        self.hBar = gamebox.from_color((200 - self.barLength / 2) + ((self.current_hp / self.barRatio) / 2), 214, "red", (self.current_hp / self.barRatio), 4)
        camera.draw(self.hBarTrim)
        camera.draw(self.hBar)
        # print(self.max_hp)
        # print(self.current_hp)
        # print(self.barRatio)

def tick(keys):
    global game_on
    global new_game
    global new_user
    global sheet_index
    global current_town
    global mouse_xpos
    global mouse_ypos
    global current_party
    global filename
    global user
    if camera.mouseclick and game_on:
        print(slot_1)
        print(calc_max_hp(slot_1))
    if camera.mouseclick:
        mouse_xpos = camera.mouse[0]
        mouse_ypos = camera.mouse[1]
        print(mouse_xpos)
        print(mouse_ypos)
        # print(master_towns_save[current_town])
        print(user)
        print(trainer.x)
        print(trainer.y)
    if game_on is False and new_user is False:
        if camera.mouseclick and b1.contains(mouse_xpos, mouse_ypos):
            user = input("Type in your username ")
            login(user)
    if game_on:
        camera.clear("white")
        camera.draw(current_town)
        collision_check(current_town)
    if pygame.K_SPACE in keys and new_user is False and game_on is False:
        try:
            user = input("What do you want to be called? ")
            f = open(user + ".txt", "r")
            print("Username already exists!")
            f.close()
            keys.clear()
        except FileNotFoundError as e:
            f = open(user + ".txt", "w")
            f.close()
            new_user = True
    if game_on is False and new_user:
        camera.clear("white")
        camera.draw("Choose your starter Pokemon!", 50, "black", 400, 100)
        camera.draw(bulbasaur_starter_sprite)
        camera.draw(charmander_starter_sprite)
        camera.draw(squirtle_starter_sprite)
        camera.draw(bulbasaur_select_box)
        camera.draw(charmander_select_box)
        camera.draw(squirtle_select_box)
        camera.draw("Bulbasaur", 33, "black", 175, 435)
        camera.draw("Charmander", 33, "black", 410, 435)
        camera.draw("Squirtle", 33, "black", 645, 435)
        if camera.mouseclick and bulbasaur_select_box.contains(mouse_xpos, mouse_ypos):
            bulba = Pokemon('bulbasaur')
            f = open(user + ".txt", "w+")
            f.write(str(bulba))
            f.close()
            convert_saved_pokemon(user + ".txt")
            game_on = True
        elif camera.mouseclick and charmander_select_box.contains(mouse_xpos, mouse_ypos):
            charm = Pokemon('charmander')
            f = open(user + ".txt", "w")
            f.write(str(charm))
            f.close()
            convert_saved_pokemon(user + ".txt")
            game_on = True
        elif camera.mouseclick and squirtle_select_box.contains(mouse_xpos, mouse_ypos):
            squirt = Pokemon('squirtle')
            f = open(user + ".txt", "w+")
            f.write(str(squirt))
            f.close()
            convert_saved_pokemon(user + ".txt")
            game_on = True

    if game_on and pygame.K_RIGHT in keys and current_town != battle_grounds:
        trainer.image = trainer_sprite[sheet_index]
        if sheet_index == 3:
            sheet_index = 4
        elif sheet_index == 4:
            sheet_index = 5
        elif sheet_index != 3:
            sheet_index = 3
        trainer.move(4, 0)
    if game_on and pygame.K_LEFT in keys and current_town != battle_grounds:
        trainer.image = trainer_sprite[sheet_index]
        if sheet_index == 9:
            sheet_index = 10
        elif sheet_index == 10:
            sheet_index = 11
        elif sheet_index != 9:
            sheet_index = 9
        trainer.move(-4, 0)
    if game_on and pygame.K_DOWN in keys and current_town != battle_grounds:
        trainer.image = trainer_sprite[sheet_index]
        if sheet_index == 0:
            sheet_index = 1
        elif sheet_index == 1:
            sheet_index = 2
        elif sheet_index != 0:
            sheet_index = 0
        trainer.move(0, 4)
    if game_on and pygame.K_UP in keys and current_town != battle_grounds:
        trainer.image = trainer_sprite[sheet_index]
        if sheet_index == 6:
            sheet_index = 7
        elif sheet_index == 7:
            sheet_index = 8
        elif sheet_index != 6:
            sheet_index = 6
        trainer.move(0, -4)
    if game_on and pygame.K_5 in keys and current_town != battle_grounds:
        wild_encounter()
    if game_on and pygame.K_6 in keys and current_town != battle_grounds:
        save()
    if game_on and pygame.K_8 in keys and current_town != battle_grounds:
        print(slot_1.realstats)
        keys.clear()
    if game_on and pygame.K_0 in keys and current_town == battle_grounds:
        slot_1.take_damage(1)
    if game_on and pygame.K_b in keys and current_town == battle_grounds:
        slot_1.gain_health(1)
    camera.display()


def collision_check(town_name):
    global current_town
    global current_pokemon
    global master_pokedict_wild
    global default_battle_screen
    global move_screen
    global bag_screen
    global pokemon_screen
    global mouse_ypos
    global mouse_xpos
    global slot_1
    global slot_2
    global slot_3
    global slot_4
    global slot_5
    global slot_6
    if town_name == twinleaf:
        camera.draw(trainer)
        if trainer.x < 151:  # Left side of trees
            trainer.x = 153
        if trainer.x > 648:  # Right side of trees
            trainer.x = 646
        if trainer.y > 513:  # Southern border
            trainer.y = 510
        if trainer.y < 75 and trainer.x < 304:
            trainer.x = 306
        rightFence = gamebox.from_color(700, 35, "white", 300, 75)
        rightFence.left = 520
        rightFence.bottom = 60
        if rightFence.touches(trainer):
            trainer.move_to_stop_overlapping(rightFence)
        if 250 < trainer.y < 280:
            if 390 < trainer.x < 430:
                if trainer.y >= 260:
                    trainer.y = 284
                if trainer.y < 260:
                    trainer.y = 240
        if 176 < trainer.x < 346:
            if 73 < trainer.y < 228:
                if trainer.y > 100 and 185 < trainer.x < 338:
                    trainer.y = 232
                elif trainer.y < 100 and 185 < trainer.x < 338:
                    trainer.y = 70
                elif trainer.x < 250:
                    trainer.x = 170
                elif trainer.x > 250:
                    trainer.x = 350
        if 216 < trainer.x < 333:
            if 300 < trainer.y < 430:
                if trainer.y > 350 and 226 < trainer.x < 314:
                    trainer.y = 434
                elif trainer.y < 350 and 226 < trainer.x < 314:
                    trainer.y = 293
                elif trainer.x < 250:
                    trainer.x = 212
                elif trainer.x > 250:
                    trainer.x = 337
        if trainer.y < 0 and 292 < trainer.x < 507:
            current_town = route_201
            trainer.y = 600
            trainer.x = 400
    if town_name == route_201:
        camera.draw(trainer)
        if trainer.y > 601 and 292 < trainer.x < 507:
            current_town = twinleaf
            trainer.y = 0
            trainer.x = 400
    if town_name == battle_grounds:
        camera.draw(battle_spaces)
        camera.draw(master_pokedict_wild[current_pokemon.dexNo])
        camera.draw(master_pokedict_user[slot_1.dexNo])
        slot_1.update()
        if default_battle_screen:
            camera.draw(fight_options)
        elif move_screen:
            camera.draw(move_options)
        camera.draw("A wild " + current_pokemon.name + " appeared!", 25, "black", 200, 40)
        if camera.mouseclick and default_battle_screen:
            if 150 <= mouse_xpos <= 650 and 375 <= mouse_ypos <= 500:
                default_battle_screen = False
                move_screen = True
            elif 316 <= mouse_xpos <= 483 and 541 <= mouse_ypos <= 600:
                current_town = last_town
            # This will be where I add the switches to other battle screens
        if camera.mouseclick and move_screen:
            if 128 <= mouse_xpos <= 671 and 553 <= mouse_ypos <= 600:
                default_battle_screen = True
                move_screen = False
                pygame.time.wait(130)

    camera.display()


def wild_encounter():
    global current_town
    global current_pokemon
    global master_pokedict_wild
    global master_pokedict_names
    global last_town
    last_town = current_town
    current_town = battle_grounds
    current_pokemon = Pokemon(master_pokedict_names[random.randint(1, 9)])
    print(current_pokemon)


def calc_max_hp(pokemon):
    max_hp = math.floor((2 * database[master_pokedict_names[pokemon.dexNo]]['basestats'][1] + pokemon.ivs[0] + 21)
                        * pokemon.level / float(100)) + pokemon.level + 10
    return max_hp


def calc_all_stats(pokemon):
    stat_arr = [calc_max_hp(pokemon)]
    for i in range(2, 7):
        stat = math.floor((math.floor((2 * database[master_pokedict_names[pokemon.dexNo]]['basestats'][i] +
                                       pokemon.ivs[i - 1] + 21) * pokemon.level / float(100)) + 5))
        stat_arr.append(stat)
    return stat_arr


def login(username):
    global game_on
    global filename
    global current_party
    global current_town
    filename = username + ".txt"
    try:
        with open(filename, 'r+') as f:
            try:
                convert_saved_pokemon(filename)
                f.readline()
                current_town = master_towns_login[int(f.readline())]
            except ValueError as e:
                pass
            f.close()
            game_on = True
    except FileNotFoundError as e:
        print("Username not recognized!")


def save():
    global user
    f = open(user + ".txt", "w")
    f.write(str(slot_1) + "-" + str(slot_2) + "-" + str(slot_3) + "-" + str(slot_4) + "-" + str(slot_5) + "-" + str(
        slot_6) + "\n")
    f.write(str(master_towns_save[current_town]))
    f.close()


def convert_saved_pokemon(filename):
    global current_party
    global slot_1
    global slot_2
    global slot_3
    global slot_4
    global slot_5
    global slot_6
    counter = 1
    current_party.clear()
    # In save file, the Pokemon data is formatted as: pokemon|6 diff ivs|type|currentHP|level|dexNumber
    with open(filename, 'r+') as file:
        file_party = file.readline().strip().split('-')
        while 'None' in file_party:
            file_party.remove('None')
        for pokemon in file_party:
            pokemon_data = pokemon.strip().split('|')
            ivs = [int(x) for x in pokemon_data[1].split(',')]
            p = Pokemon(pokemon_data[0])
            p.set_current_hp(pokemon_data[3])
            p.set_ivs(ivs[0], ivs[1], ivs[2], ivs[3], ivs[4], ivs[5])
            p.set_level(pokemon_data[4])
            p.set_type(pokemon_data[2])
            p.set_dexNo(pokemon_data[5])
            p.set_stats(calc_all_stats(p))
            current_party.append(p)
            if counter == 1:
                slot_1 = p
            elif counter == 2:
                slot_2 = p
            elif counter == 3:
                slot_3 = p
            elif counter == 4:
                slot_4 = p
            elif counter == 5:
                slot_5 = p
            else:
                slot_6 = p
            counter += 1


ticks_per_second = 20
gamebox.timer_loop(ticks_per_second, tick)
