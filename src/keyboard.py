from src.item import Item


class MixinLang:
    """Класс для хранения и изменения раскладки клавиатуры."""

    def __init__(self, language: str = "EN") -> None:
        self._language = language

    @property
    def language(self) -> str:
        return self._language


class Keyboard(Item, MixinLang):
    """Класс Keyboard для объекта клавиатуры, отнаследован от 'Item'."""

    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        """Создание экземпляра класса Keyboard."""
        super().__init__(name, price, quantity)
        MixinLang.__init__(self, language)

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self._language
