""" Created by Vladimir Gonchrov, 11.04.2018
    This file declares specific classes of units of the race Gondor
    message() is method which prints message when unit is created
    check_attack() is method which prints units attack """

from unithierarchy import Gondor, DamageDealer, Support


class Soldier(Gondor, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)
        self.wall_of_shield = characteristics['wall_of_shield']

    def wall_of_shield(self):
        self.speed = self.speed * 0.7
        self.defence = self.defence * 1.8
        self.wall_of_shield = True



class Archer(Gondor, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class Knight(Gondor, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class GuardianOfCitadeles(Gondor, DamageDealer):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


class Pathfinder(Gondor, Support):
    def __init__(self, **characteristics):
        super().__init__(**characteristics)


"""--------------------в проекте осадные орудия и тд и тп-----------------"""

# class SiegeGun(Gondor, Support):
#   """docstring for SiegeGun"""
#   def __init__(self, **characteristics):
#       super().__init__(**characteristics)21
