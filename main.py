from Player import Player, Warrior, Mage

def __main__():
    player1 = Player("Sara", level=3, health=90)
    print(player1.checkStatus())


    warrior1 = Warrior("Leon", level=5, health=100, rage=10)
    print(warrior1.checkStatus())

    mage1 = Mage("Eldin", level=4, health=80, mana=120)
    print(mage1.checkStatus())

    print(warrior1.attackPlayer(mage1, damage=20, rage_gain=15))
    print(mage1.checkStatus())

    print(mage1.castSpell(warrior1, spell_damage=35, spell_mana_cost=30))
    print(warrior1.checkStatus())

    print(warrior1.powerSmach(mage1))
    print(mage1.checkStatus())



if __name__ == "__main__":
    __main__()