from typing import Dict, Generic, List, TypeVar
from uuid import UUID


CreateTDTO = TypeVar("CreateTDTO")
ReadTDTO = TypeVar("ReadTDTO")
UpdateTDTO = TypeVar("UpdateTDTO")


class BaseRepositoryInterface(Generic[CreateTDTO, ReadTDTO, UpdateTDTO]):
    async def create(self, dto: CreateTDTO) -> None:
        raise NotImplementedError("Optional method not implemented")

    async def find_by_id(self, id: UUID) -> ReadTDTO:
        raise NotImplementedError("Optional method not implemented")

    async def list(self, filter_query: Dict) -> List[ReadTDTO]:
        raise NotImplementedError("Optional method not implemented")

    async def update(self, id: UUID, dto: UpdateTDTO) -> None:
        raise NotImplementedError("Optional method not implemented")
