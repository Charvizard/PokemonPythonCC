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
    def attack(self, attacker) : 
        if type(attacker) != Pokemon : 
            return print("That's no pokemon!")
        else : 
            try :  
                type_damage = self.type_match[attacker.ptype]
            except KeyError : 
                print("Type Unown")
                self.lose_hp(5)
            damage = attacker.level*type_damage
            if type_damage == 0.5 : 
                print("The attack wasn't very effective.")
            if type_damage == 1 : 
                print("The attack was effective.")
            if type_damage == 2 : 
                print("The attack was super effective!.")
            self.lose_hp(damage)

    def lose_hp(self, damage) : 
        self.current_hp = self.current_hp - damage
        if self.current_hp <= 0 : 
            self.ko()
        else : 
            return print("{Pokemon} has taken {damage} from that attack!\nCurrent Health : {CurrentHP}/{MaxHp}".format(Pokemon = self.name, damage = damage, CurrentHP = self.current_hp, MaxHp = self.max_hp))

    def heal(self, heal) : 
        if self.current_hp >= self.max_hp : 
            return print("The Pokemon is already full health!")
        elif self.current_hp <= 0 : 
            revive()
            self.current_hp = self.current_hp + heal
        elif self.current_hp >= 0 : 
            self.current_hp = self.current_hp + heal
            return print("{Pokemon} has healed {heal} from that!\nCurrent Health : {CurrentHP}/{MaxHp}".format(Pokemon = self.name, heal = heal, CurrentHP = self.current_hp, MaxHp = self.max_hp))
        

    def ko(self) : 
        self.KO = True
        return print("{} has been knocked out! Take them to the nearest PokeCenter!".format(self.name))
    
    def revive(self) : 
        self.KO = False
        return print("{} has been revived!".format(self.name))


pikachu = Pokemon("Picka", 10, "Electric", {"Normal" : 1, "Fire" : 1 , "Water" : 1 , "Electric" : 0.5 , "Grass" : 1 , "Ice" : 1 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 2 , "Flying" : 0.5 , "Psychic" : 1 , "Bug" : 1 , "Rock" : 1 , "Ghost" : 1 , "Dragon" : 1}, 5, False)
charmander = Pokemon("Chari", 15, "Fire", {"Normal" : 1, "Fire" : 1 , "Water" : 2 , "Electric" : 1 , "Grass" : 0.5 , "Ice" : 1 , "Fighting" : 1 , "Poison" : 1 , "Ground"  : 2 , "Flying" : 0.5 , "Psychic" : 1 , "Bug" : 0.5 , "Rock" : 2 , "Ghost" : 1 , "Dragon" : 1}, 5, False)

pikachu.attack(charmander)
print(pikachu)