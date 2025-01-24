print("Hello Worlds!, I love testing!")

# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

diceOptions = list(range(1, 7))
#combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))
################The order of operations is screwed(the starter code and in class work don't really match)
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
print("Available weapons area: ".join(weapons))

def getCombatStrength(prompt):
    while True:
        value = int(input(prompt))
        if 1<= value <= 6:
            return value
        else:
            print("Invalid input. Please enter a number between 1-6")

combatStrength = getCombatStrength("Enter the player combat Strength [1-6]: ")
mCombatStrength = getCombatStrength("Enter the monster combat Strength [1-6]: ")

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll -1]#dice roll does not follow index rules
    monsterWeapon = weapons[monsterRoll -1]

    heroTotal = combatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    if heroTotal > monsterTotal:
        print("Player wins!")
    elif heroTotal < monsterTotal:
        print("Monster wins!")
    else:
        print("Draw!")


#######Starter code below!
if (combatStrength < 1 or combatStrength > 6):
    print("Input must be an integer between 1-6")
else:
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
    if (mCombatStrength < 1 or mCombatStrength > 6):
        print("Input must be an integer between 1-6")
    else:
        weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

        input("Roll the dice for your health points (Press enter)")
        healthPoints = random.choice(diceOptions)
        print("You rolled " + str(healthPoints) + " health points")

        input("Roll the dice for the monster's health points (Press enter)")
        mHealthPoints = random.choice(diceOptions)
        print("You rolled " + str(mHealthPoints) + " health points for the monster")

        input("Roll the dice to see if you find a healing potion (Press enter)")
        healingPotion = random.choice([0, 1])
        print("Have you found a healing potion?: " + str(bool(healingPotion)))

        # Roll the dice (1-6) to choose which weapon you must use. Save the roll in a variable called weaponRoll.
        weaponRoll = random.choice([0, 1])

        # Add your weaponRoll to the hero's combat strength
        combatStrength += weaponRoll

        # Use this variable as an index into the weapons array and print out the name of the hero's weapon.
        print("The name of the hero's weapon is: " + weapons[weaponRoll])

        # if weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
        if (weaponRoll <= 2):
            print("You rolled a weak weapon, friend")
        # But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
        elif (weaponRoll <= 4):
            print("Your weapon is meh")
        # Else, print out "Nice weapon, friend! "
        else:
            print("Nice weapon, friend! ")

        # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
        if (weapons[weaponRoll] != "Fist"):
            print("Thank goodness you didn't roll the Fist...")

        input("Analyze the roll (Press enter)")
        # Equality operators
        print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

        # Relational operators
        print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

        # and keyword
        print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

        # not keyword
        print("--- Phew, you have a healing potion: " + str(
            not (  # monster will NOT kill hero in one blow
                    healthPoints < mCombatStrength  # monster will kill hero in one blow
            )
            and
            healingPotion == 1  # hero has a healing potion
        ))

        # or keyword
        print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

        # in keyword
        print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

        # --- Expanded if statement
        if healthPoints >= 5:
            print("--- Your health is ok")
        elif healingPotion == 1:
            healingPotion = 0
            healthPoints = 6
            print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
        else:
            print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

        # --- Nested if statement
        print("You meet the monster. FIGHT!!")
        input("You strike first (Press enter)")

        print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
        if combatStrength >= mHealthPoints:
            mHealthPoints = 0
            print("You've killed the monster")
        else:
            mHealthPoints -= combatStrength

            print("You've reduced the monster's health to: " + str(mHealthPoints))

            print("The monster strikes!!!")
            print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
            if mCombatStrength >= healthPoints:
                healthPoints = 0
                print("You're dead")
            else:
                healthPoints -= mCombatStrength
                print("The monster has reduced your health to: " + str(healthPoints))
