from uuid import uuid4

import pytest
from unittest.mock import MagicMock

from src.core.domain.shared.interfaces.repository import BaseRepositoryInterface


class CreateDTO:
    pass


class ReadDTO:
    pass


class UpdateDTO:
    pass


@pytest.fixture
def mock_base_repository():
    return MagicMock(spec=BaseRepositoryInterface[CreateDTO, ReadDTO, UpdateDTO])


@pytest.mark.asyncio
async def test_create(mock_base_repository):
    dto = CreateDTO()

    await mock_base_repository.create(dto)

    mock_base_repository.create.assert_called_once_with(dto)


@pytest.mark.asyncio
async def test_find_by_id_existing(mock_base_repository):
    expected_read_dto = ReadDTO()
    mock_base_repository.find_by_id.return_value = expected_read_dto

    result = await mock_base_repository.find_by_id(uuid4())

    assert result == expected_read_dto
    mock_base_repository.find_by_id.assert_called_once()


@pytest.mark.asyncio
async def test_list(mock_base_repository):
    expected_list = [ReadDTO(), ReadDTO()]
    mock_base_repository.list.return_value = expected_list

    filter_query = {"some_filter": "value"}
    result = await mock_base_repository.list(filter_query)

    assert result == expected_list
    mock_base_repository.list.assert_called_once_with(filter_query)


@pytest.mark.asyncio
async def test_update(mock_base_repository):
    dto = UpdateDTO()
    uuid = uuid4()

    await mock_base_repository.update(uuid, dto)

    mock_base_repository.update.assert_called_once_with(uuid, dto)
