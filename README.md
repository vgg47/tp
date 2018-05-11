# tp

ПОСЛЕДНИЕ ИЗМЕНЕНИЯ СМОТРИ В ФАЙЛЕ historyversions.txt

Юниты различаются по двум категориям: фракция и тип.
Существует две фракции: Гондор(люди) и Изенгард(орки).
Существует два типа: наносящие урон и юниты поддержки.
Так как необходимо создавать армии(большое количество объеков), то используется паттерн Factory method, 
где каждого юнита определенного класса создает своя Concrete Factory(оформлены в виде методов). Для удобства поддержки
методы создания юнитов разных рас разнесены в разные классы.



class Army - базовый класс армии. Содержит в себе определенную фабрику для генерации юнитов и метод для найма юнитов в армию
class GondorArmy, наследуется от Army. Армия расы Gondor. Содержит изначально пустые листы для всех типов воиск этой расы.
class IzengardArmy, наследуется от Army. Армия расы Izengard. Содержит изначально пустые листы для всех типов воиск этой расы.

class UnitFactory - базовый класс фабрик
class GondorUnitFactory - наследуется от UnitFactory, содержит в себе метод create_unit(_type), который создает юнита типа _type вызывая соответствующий метод, если _type принадлежит расе Гондор.
сlass IzengardUnitFactory - наследуется от UnitFactory, содержит в себе метод create_unit(_type), который создает юнита типа _type вызывая соответствующий метод, если _type принадлежит расе Изенгард.

class Unit - базовый класс юнитов. Содержит в себе поля - характеристики юнитов, метод message(), который печатает сообщение при
создании юнита и метод get_attack(), который возвращает атаку персонажа.

class Gondor - наследуется от Unit, все его наследники - классы юнитов расы Гондор
class Izengard - наследуется от Unit, все его наследники - классы юнитов расы Изенгард
class DamageDealer - наследуется от Unit, все его наследники - классы юнитов, которые наносят урон
class Support - наследуется от Unit,  все его наследники - классы юнитов, которые оказывают поддержку

class Soldier - класс юнита Солдат(дд, гондор)
class Archer - класс юнита Лучник(дд, гондор)
class Knight - класс юнита Рыцарь(дд, гондор)
class GuardianOfCitadeles - класс юнита  Страж Цитадели(дд, гондор)
class Pathfinder - класс юнита Следопыт(сапорт, гондор)

сlass OrcWorker - класс юнита Орк-работник(дд, изенгард)
class UrukHai - класс юнита Урук-Хай(дд, изенгард)
class UrukShooter - класс юнита Урук-стрелок(дд, изенгард)
class Berserk -  класс юнита Берсерк(дд, изенгард)
class Horseman -  класс юнита Всадник на варге(дд, изенгард)
class Shaman - класс юнита Шаман(сапорт, изенгард)

Метод  choice_side(_race) позволяет игроку выбрать сторону. Метод возвращает фабрику, которая создает только персонажей расы _race или кидает исключение в случае некорректно введеной расы
Метод create_army(_race, _factory) в зависимости от расы _race  создает возвращает армию с зашитой в ней фабрикой _factory данной расы или кидает исключение в случае некорректно введеной расы


 
