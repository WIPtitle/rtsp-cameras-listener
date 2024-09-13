from typing import List

from sqlmodel import SQLModel, Field, Relationship

from app.models.enums.device_type import DeviceType


class DeviceGroupLink(SQLModel, table=True):
    device_id: int | None = Field(default=None, foreign_key="device.id", primary_key=True)
    group_id: int | None = Field(default=None, foreign_key="devicegroup.id", primary_key=True)


class DeviceGroupInputDto(SQLModel):
    name: str


class DeviceGroup(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    devices: List["Device"] | None = Relationship(back_populates="groups", link_model=DeviceGroupLink)

    @classmethod
    def from_dto(cls, dto: DeviceGroupInputDto):
        return cls(
            id=None,
            name=dto.name,
            devices=[]
        )


class Device(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    device_type: DeviceType
    groups: List["DeviceGroup"] = Relationship(back_populates="devices", link_model=DeviceGroupLink)

