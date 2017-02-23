from abc import ABCMeta, abstractmethod


class Notebooks(metaclass=ABCMeta):
	pass


class OS(metaclass=ABCMeta):
	pass


class Asus(Notebooks):

	def interact(self, notebook: Notebooks) -> None:
		print('Вы купили ноутбук {}'.format(
		notebook.__class__.__name__))


class Windows(OS):
	def interact(self, os: OS) -> None:
		print('Вы купили OS {}'.format(
		os.__class__.__name__))


class NtShop():
	@abstractmethod
	def buy_notebook(self) -> Notebooks:
		return Asus()

class OSShop():
	@abstractmethod
	def buy_os(self) -> OS:
		return Windows()


if __name__ == '__main__':
	Nt_shop = NtShop()
	Notebooks = Nt_shop.buy_notebook()
	OS_shop = OSShop()
	OS = OS_shop.buy_os()
	_choise = 0
	_choise = int(input("1 - купить ноутбук; 2 - купить OS; 3 - купить ноутбук + OS "))
	while _choise not in range(1, 4):
		print("Введите значение от 1 до 3!")
		_choise = int(input("1 - купить ноутбук; 2 - купить OS; 3 - купить ноутбук + OS: "))
	if _choise == 1:
		Notebooks.interact(Notebooks)
	elif _choise == 2:
		OS.interact(OS)
	elif _choise == 3:
		Notebooks.interact(Notebooks)
		print("И")
		OS.interact(OS)


