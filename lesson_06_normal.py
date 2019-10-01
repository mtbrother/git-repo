# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class person():
	"""создание класса участника"""
	def __init__(self, name, damage, armor):
		self.name = name
		self.damage = damage
		self.armor = armor
	def description_players(self):
		desc = str('Игрок: ' + self.name +' защита: ' + self.armor + ' удар: ' + self.damage)
		return desc.title()

class Player(person):
	"""создание класса игрок"""
	def __init__(self, name, damage, armor, health):
		super().__init__(name, damage, armor)
		self.__health = 100
	def player_health(self):
		'''здоровье игрока с учетом брони'''
		self.health1 = (int(self.__health) + int(self.armor))
		return self.health1
	def description_players(self):
		desc = str('Игрок: ' + self.name +' защита: ' + self.armor + ' удар: '
		 + self.damage + ' здоровье: ' + str(self.__health))
		return desc.title()
	def player_attack(self):
		return self.damage


class Enemy(person):
	"""создание класса враг"""
	def __init__(self, name, damage, armor, health):
		super().__init__(name, damage, armor)
		self.__health = 100
	def enemy_health(self):
		'''здоровье врага с учетом брони'''
		health2 = (self.__health + int(self.armor))
		return health2
	def description_players(self):
		desc = str('Игрок: ' + self.name +' защита: ' + self.armor + ' удар: '
		 + self.damage + ' здоровье: ' + str(self.__health))
		return desc.title()
	def enemy_attack(self):
		return self.damage

class Game():
	"""docstring for Game"""
	def attack1(self):
		return ('Player атакует')
	def attack2(self):
		return ('Enemy атакует')



match = Game()
player1 = Player('Avalon', '30', '25', '100')
player2 = Enemy('Ninja', '34', '22', '100')
print(player1.description_players())
print(player2.description_players())
print(match.attack1(), (int(player2.enemy_health()) - int(player1.player_attack())))
print(match.attack2(), 'у игрока осталось ', (int(player1.player_health()) - int(player2.enemy_attack())))
