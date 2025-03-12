# Base Character class

import random

class Character:
    def __init__(self, name, mana, health, attack_power):
        self.name = name
        self.mana = mana
        self.health = health
        self.attack_power = attack_power
        self.max_health = health # Store the original health for maximum limit
    
    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}.")

    # Heal method that doesn't exceed max health
    def heal(self, heal_amount):
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health 
        print(f"{self.name} increased to {heal_amount}. Current health: {self.health}.")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, mana=30, health=140, attack_power=25)
        
    def raise_shield(self):
        self.health += 30
        print(f"{self.name} Raised their shield to gain temporary hitpoints. Current health: {self.health}.")
        
    # Power attack method
    def power_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage 
        print(f"{self.name} uses Power Attack on {opponent.name} for {damage} damage!")
        
    def charge_attack(self, opponent):
        damage = self.attack_power * 4
        opponent.health -= damage
        print(f"{self.name} used the charge attack and causes {damage} damage to {opponent.name}!")
    
    def use_shield(self):
        print(f"{self.name} shields the opponents attacks and escapes unscathed! Health is {self.health}.")
        
    def use_special_ability(self, opponent):
        choice = input("Please choose a number for the ability you would like: 1= Power Attack, 2= Charge Attack, 3= Use Shield.")    
        if choice == "1":
            self.charge_attack(opponent)
        elif choice == "2":
            self.use_shield()
        else:
            print("Invalid choice.")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name, mana):
        super().__init__(name, mana, health=100, attack_power=35)  # Boost attack power

    # Cast spell method here
    def cast_spell(self, opponent):
        if self.mana >= 30:
            spell_damage = self.attack_power * 3
            self.mana -= 30
            opponent.health -= spell_damage
            print(f"{self.name} cast a spell on {opponent.name} for {spell_damage}!")
        else:
            print (f"{self.name} does not have enough mana to cast a spell.")
            
    def lightening_attack(self, opponent):
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} used the lightening attack and causes {damage} damage to {opponent.name}!")
    
    def mana_shield(self):
        print(f"{self.name} used the Mana Shield and escapes! Health is {self.health}.")
        
    def use_special_ability(self, opponent):
        choice = input("Please choose a number for the ability you would like: 1= Casts Spell, 2= Lightening Attack, 3= Mana Shield.")    
        if choice == "1":
            self.cast_spell(opponent)
        elif choice == "2":
            self.lightening_attack(opponent)
        elif choice == "3":
            self.mana_shield()
        else:
            print("Invalid choice.")      
    

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, mana=50, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # added
        
    # Archer's special ability: 
    def shoot_explosive_arrows(self, opponent):
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} used an explosive arrow to cause {damage} damage to {opponent.name}!")
        
    def rapid_fire_arrow_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} used the rapid fire arrows on {opponent.name} causing {damage} damage!")
        
    def evades_attack(self):
        print(f"{self.name} evades the opponents attacks and escapes unscathed! Health is {self.health}.")
        
    def use_special_ability(self, opponent):
        choice = input("Please choose a number for the ability you would like: 1= Explosive Arrow, 2= Rapid Fire Arrow, 3= Evade Attack.")    
        if choice == "1":
            self.shoot_explosive_arrows(opponent)
        elif choice == "2":
            self.rapid_fire_arrow_attack(opponent)
        elif choice == "3":
            self.evades_attack()
        else:
            print("Invalid choice.")
            
class Paladin(Character):
    def __init__(self, name, mana):
        super().__init__(name, mana, health=120, attack_power=35)  # added
        
    def divine_blast(self, opponent):
        damage = random.randint (50, 100)
        opponent.health -= damage
        print(f"{self.name} used Divine Blast and caused {damage} damage to {opponent.name}!")
          
    def holy_fireball(self, opponent):
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} used the Holy Fireball on {opponent.name} causing {damage} damage!")
       
    def holy_shield(self, opponent):
        defense_boost = random.randint(10, 30)
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} shields the attack, deals {damage} damage to {opponent.name} and gains {defense_boost} defense boost!")
        
    def use_special_ability(self, opponent):
        choice = input("Please choose a number for the ability you would like: 1= Divine Blast, 2= Holy Fireball, 3= Holy Shield.")    
        if choice == "1":
            self.divine_blast(opponent)
        elif choice == "2":
            self.holy_fireball(opponent)
        elif choice == "3":
            self.holy_shield()
        else:
            print("Invalid choice.")
            
# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name, mana=30)
    elif class_choice == '3':
        return Archer(name)
        # Added Archer class here
    elif class_choice == '4':
        return Paladin(name, mana=30)
        # Added Paladin class here
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        # player.options()
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.use_special_ability(wizard)
        elif choice == '3':
            heal_amount = int(input("Enter the amount to heal: "))
            player.heal(heal_amount)
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue
        
        
        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()