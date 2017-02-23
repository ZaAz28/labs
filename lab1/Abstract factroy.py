from abc import ABCMeta, abstractmethod


class Notebooks(metaclass=ABCMeta):
	pass


class OS(metaclass=ABCMeta):

	@abstractmethod
	def interact(self, notebook: Notebooks) -> None:
		pass


class AbstractShop(metaclass=ABCMeta):

	@abstractmethod
	def buy_notebook(self) -> Notebooks:
		pass

	@abstractmethod
	def buy_os(self) -> OS:
		pass


class Asus(Notebooks):
	pass


class Samsung(Notebooks):
	pass


class Windows(OS):

	def interact(self, notebook: Notebooks) -> None:
		print('Вы купили ноутбук {} с OS Windows'.format(
			notebook.__class__.__name__))


class Linux(OS):

	def interact(self, notebook: Notebooks) -> None:
		print('Вы купили ноутбук {} с OS Linux'.format(
			notebook.__class__.__name__))


class AsusShop(AbstractShop):

	def buy_notebook(self) -> Notebooks:
		return Asus()

	def buy_os(self) -> OS:
		return Windows()


class SamsungShop(AbstractShop):

	def buy_notebook(self) -> Notebooks:
		return Samsung()

	def buy_os(self) -> OS:
		return Linux()


if __name__ == '__main__':
	Asus_shop = AsusShop()
	Samsung_shop = SamsungShop()
	print('OUTPUT:')
	Notebooks = Asus_shop.buy_notebook()
	OS = Samsung_shop.buy_os()
	OS.interact(Notebooks)
	Notebooks = Samsung_shop.buy_notebook()
	OS = Asus_shop.buy_os()
	OS.interact(Notebooks)
