Normal = {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 1 , "Grass" : 1 , "Ice" : 1 , "Fighting" : 2 , "Poison" : 1 , "Ground"  : 1 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 0 , "Dragon" : 1} 
Fire =  {"Normal" : 1, "Fire" : 0.5 , "Water" : 2 , "Electric" : 1 , "Grass" : 0.5 , "Ice" : 1 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 2 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 0.5 , "Rock" : 2 , "Ghost" : 1 , "Dragon" : 1}
Water =  {"Normal" : 1, "Fire" : 0.5 , "Water" : 0.5 , "Electric" : 2 , "Grass" : 2 , "Ice" : 0.5 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 1 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}
Electric =  {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 0.5 , "Grass" : 1 , "Ice" : 1 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 2 , "Flying" : 0.5 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}
Grass =  {"Normal" : 1, "Fire" : 2 , "Water" : 0.5 , "Electric" : 0.5 , "Grass" : 0.5 , "Ice" : 2 , "Fighting" : 1 , "Poison" : 2 , "Ground"  : 0.5 , "Flying" : 2 , "Psychic" : 1 , "Bug" : 2 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}
Ice =  {"Normal" : 1, "Fire" : 2 , "Water" : 1 , "Electric" : 1 , "Grass" : 1 , "Ice" : 0.5 , "Fighting" : 2 , "Poison" : 1 , "Ground"  : 1 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 2 , "Ghost" : 1 , "Dragon" : 1}
Fighting =  {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 1 , "Grass" : 1 , "Ice" : 1 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 1 , "Flying" : 2 , "Psychic" : 2 , "Bug" : 0.5 , "Rock" : 0.5 , "Ghost" : 1 , "Dragon" : 1}
Poison =  {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 1 , "Grass" : 0.5 , "Ice" : 1 , "Fighting" : 0.5 , "Poison" :  0.5, "Ground"  : 2 , "Flying" : 1 , "Psychic" : 2 , "Bug" : 2 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}
Ground =  {"Normal" : 1, "Fire" : 1 , "Water" : 2 , "Electric" : 0 , "Grass" : 2 , "Ice" : 2 , "Fighting" : 1 , "Poison" : 0.5 , "Ground"  : 2 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 0.5 , "Ghost" : 1 , "Dragon" : 1}
Flying =  {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 2 , "Grass" : 0.5 , "Ice" : 2 , "Fighting" : 0.5 , "Poison" : 1 , "Ground"  : 0 , "Flying" : 1, "Psychic" : 1 , "Bug" : 0.5 , "Rock" : 2 , "Ghost" : 1 , "Dragon" : 1}
Psychic =  {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 1 , "Grass" : 1 , "Ice" : 1 , "Fighting" : 0.5 , "Poison" : 1 , "Ground"  : 1 , "Flying" : 1 , "Psychic" : 0.5 , "Bug" : 2 , "Rock" : 1 , "Ghost" : 0 , "Dragon" : 1}
Bug =  {"Normal" : 1, "Fire" : 2 , "Water" : 1 , "Electric" : 1 , "Grass" : 0.5 , "Ice" : 1 , "Fighting" : 0.5 , "Poison" : 2 , "Ground"  : 2 , "Flying" : 2 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}
Rock =  {"Normal" : 0.5, "Fire" : 0.5 , "Water" : 2 , "Electric" : 1 , "Grass" : 2 , "Ice" : 1 , "Fighting" : 2 , "Poison" : 0.5 , "Ground"  : 2 , "Flying" : 0.5 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}
Ghost =  {"Normal" : 0, "Fire" : 1 , "Water" : 1 , "Electric" : 1 , "Grass" : 1 , "Ice" : 1 , "Fighting" : 0 , "Poison" : 0.5 , "Ground"  : 1 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 0.5 , "Rock" : 1 , "Ghost" : 2 , "Dragon" : 1}
Dragon =  {"Normal" : 1, "Fire" : 0.5 , "Water" : 0.5 , "Electric" : 0.5 , "Grass" : 0.5 , "Ice" : 2 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 1 , "Flying" : 1 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 2}

class Pokemon() : 
    def __init__(self, name, level, ptype, type_matchup, current_hp, KO) : 
        self.name = name
        self.level = level
        self.ptype = ptype
        self.type_match = type_matchup
        self.max_hp = int(level * 10)
        self.current_hp = int(current_hp)
        self.KO = KO
    
    def __repr__(self) : 
        return "The Pokemon is = \n Name : {Name}\n Level : {level}\n Type : {type}\n Current Health : {current_hp}/{max_hp} ".format(Name = self.name, level = self.level, type = self.ptype, current_hp = self.current_hp, max_hp = self.max_hp)
    
    def attack(self, enemy) : 
        if type(enemy) != Pokemon : 
            return print("That's no pokemon!")
        else : 
            try :  
                type_damage = enemy.type_match[self.ptype]
            except KeyError : 
                print("Type Unown")
                enemy.lose_hp(5)
            print(type_damage)
            print(self.level)
            damage = self.level*type_damage
            if type_damage == 0.5 : 
                print("The attack wasn't very effective.")
            if type_damage == 1 : 
                print("The attack was effective.")
            if type_damage == 2 : 
                print("The attack was super effective!.")
            if type_damage == 0 : 
                return ("This attack does not effect this type")
            enemy.lose_hp(damage)

    def lose_hp(self, damage) : 
        self.current_hp = self.current_hp - damage
        if self.current_hp <= 0 : 
            self.ko()
        else : 
            return print("{Pokemon} has taken {damage} from that attack!\nCurrent Health : {CurrentHP}/{MaxHp}".format(Pokemon = self.name, damage = damage, CurrentHP = self.current_hp, MaxHp = self.max_hp))

    def heal(self) : 
        heal = self.level * 5
        if self.current_hp + heal >= self.max_hp : 
            self.current_hp = self.max_hp
            return print("The Pokemon is full health now!")
        if self.current_hp <= 0 : 
            self.revive()
            self.current_hp = self.current_hp + heal
        if self.current_hp >= 0 : 
            self.current_hp = self.current_hp + heal
            return print("{Pokemon} has healed {heal} from that!\nCurrent Health : {CurrentHP}/{MaxHp}".format(Pokemon = self.name, heal = heal, CurrentHP = self.current_hp, MaxHp = self.max_hp))

    def ko(self) : 
        self.KO = True
        return print("{} has been knocked out! Take them to the nearest PokeCenter!".format(self.name))
    
    def revive(self) : 
        self.KO = False
        return print("{} has been revived!".format(self.name))

class Trainer() : 
    def __init__(self, name, pokemons, potions, current_poke) : 
        self.name = name
        self.pokemon = pokemons
        self.potions = potions
        self.current_poke = pokemons[current_poke]

    def use_potion(self) :
        print(self.potions) 
        if self.potions <= 0 : 
            return print("You have no potions left!")
        else : 
            if self.current_poke.current_hp >= self.current_poke.max_hp : 
                return print("The Pokemon is already full health!")
            else : 
                self.potions = self.potions - 1
                self.current_poke.heal()

    def use_attack(self, enemy) : 
        if self.current_poke.current_hp <= 0 : 
            print("This PokeMon cannot attack, it's Knocked Out")
            self.current_poke.KO = False
            self.switch_pokemon()
        else : 
            self.current_poke.attack(enemy.current_poke)

    def switch_pokemon(self) : 
        print("what Pokemon would you like to switch to? 0 to {}".format(len(self.pokemon)))
        print(self.pokemon)
        pokemon = int(input())
        if self.pokemon[pokemon].current_hp <= 0 :
            self.pokemon[pokemon].KO = True
            return print("You cannot switch to this Pokemon, they are knocked out!")
        print("You have switched from {old} to {new} as your active PokeMon".format(old = self.current_poke, new = self.pokemon[pokemon]))
        self.current_poke = self.pokemon[pokemon]

pikachu = Pokemon("Picka", 10, "Electric", Electric, 70, False)
charmander = Pokemon("Chari", 15, "Fire", Fire, 0, True)
bulbasaur = Pokemon("Bulbi", 10, "Grass", Grass, 70, False)
squirtle = Pokemon("Squirti", 12, "Water", Water, 75, False)
pidgy = Pokemon("Pidgin", 8, "Flying", Flying, 30, False)
ratata = Pokemon("Ratty", 9, "Normal", Normal, 45, False)

caterpie = Pokemon("Caterpie", 7, "Bug", Bug, 23, False)
weedle = Pokemon("Weedle", 10, "Bug", Bug, 20, False)
nidorino = Pokemon("Nido", 10, "Normal", Normal, 13, False)

ash = Trainer("Ash", [pikachu, charmander, bulbasaur, squirtle, pidgy, ratata], 5, 1)
gary = Trainer("Gary", [caterpie, weedle, nidorino], 2, 1)

#ash.use_attack(gary)
#ash.switch_pokemon()
gary.use_potion()
gary.use_potion()
gary.use_potion()
gary.use_attack(ash)