from src.ui.element import ElementType
import pygame

class UI:
    def __init__(self) -> None:
        self.surface_display = pygame.display.get_surface()

        self.width, self.height = self.surface_display.get_size()

        self.is_event = False

        self.elements: dict[str, ElementType] = {}

    def add(self, elem_id: str, element: ElementType) -> None:
        if not isinstance(elem_id, str):
            raise ValueError(f'{elem_id} 的 id 必须是字符串!')

        if not isinstance(element, ElementType):
            raise ValueError(f'{element} 必须是 Element 类型!')

        for key, value in self.elements.items():
            if elem_id == key:
                raise ValueError(f'{elem_id} 已经存在!')

        self.elements[elem_id] = element

    def adds(self, *elems: tuple[str, ElementType]) -> None:
        if not elems:
            raise ValueError('请至少添加一个元件!')
        for elem in elems:
            if not isinstance(elem, tuple) or len(elem) != 2:
                raise ValueError(f'elems的值必须是长度为 2 的元组!')

            elem_id, element = elem

            self.add(elem_id, element)

    def get(self, elem_id: str) -> ElementType:

        if elem_id not in self.elements:
            raise ValueError(f'元件 id {elem_id} 不存在!')
        return self.elements[elem_id]

    def gets(self, *elems: str) -> list[ElementType]:
        elem_list = []

        if not elems:
            raise ValueError('请至少有一个元件!')

        for elem_id in elems:
            elem_list.append(self.get(elem_id))

        return elem_list

    def get_all(self) -> list[ElementType]:
        elem_list = []

        if not self.elements:
            raise ValueError('没有一个元件!')

        for elem_id in self.elements.keys():
            elem_list.append(self.get(elem_id))

        return elem_list

    def all_draw(self):
        if not self.elements:
            raise ValueError('没有一个元件!')

        for element in self.elements.values():
            element.draw(self.surface_display)

    def handle_event(self, event: pygame.event.Event):
        for element in self.elements.values():
            element.handle_event(event)

    def draw(self, element_id: str | ElementType):
        if isinstance(element_id, str):
            elem = self.get(element_id)
        elif isinstance(element_id, ElementType):
            elem = element_id
        else:
            raise ValueError(f'element_id 必须是字符串或 Element 类型!')

        elem.draw(self.surface_display)

UIType = UI