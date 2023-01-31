from typing import (
    TypeVar,
)


_KT = TypeVar("_KT")
_VT = TypeVar("_VT")


class DictAsCache(dict):

    def __init__(self, mapping=(), size=0, **kwargs):
        self.size = size
        self.key_keeper_list = list()  #
        super().__init__(mapping, **kwargs)

    # def clear(self) -> None:
    #     pass
    #
    # def copy(self) -> Dict[_KT, _VT]:
    #     pass
    #
    # def popitem(self) -> Tuple[_KT, _VT]:
    #     pass
    #
    # def setdefault(self, __key: _KT, __default: _VT = ...) -> _VT:
    #     pass
    #
    # def update(self, __m: Mapping[_KT, _VT], **kwargs: _VT) -> None:
    #     pass
    #
    # def keys(self) -> KeysView[_KT]:
    #     pass
    #
    # def values(self) -> ValuesView[_VT]:
    #     pass
    #
    # def items(self) -> ItemsView[_KT, _VT]:
    #     pass
    #
    # def fromkeys(cls, __iterable: Iterable[_T], __value: None = ...) -> dict[_T, Optional[Any]]:
    #     pass
    #
    # def __len__(self) -> int:
    #     pass

    # def __getitem__(self, k: _KT) -> _VT:
    #     return super().__getitem__(k=k)

    # def __delitem__(self, v: _KT) -> None:
    #     return super().__delitem__(v=v)

    def __setitem__(self, k: _KT, v: _VT) -> None:

        if self.size == 0:
            return super().__setitem__(k, v)

        if self.__contains__(k):
            super().__setitem__(k, v)
            self.key_keeper_list.append(self.key_keeper_list.pop(self.key_keeper_list.index(k)))
        else:
            super().__setitem__(k, v)
            self.key_keeper_list.append(k)

        if self.__len__() > self.size:
            del self[self.key_keeper_list.pop(0)]

        return

