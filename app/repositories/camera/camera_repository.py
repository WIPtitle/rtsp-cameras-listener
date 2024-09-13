from abc import ABC, abstractmethod
from typing import Sequence

from app.models.camera import Camera


class CameraRepository(ABC):
    @abstractmethod
    def find_by_ip(self, ip: str) -> Camera:
        pass

    @abstractmethod
    def find_by_generic_device_id(self, device_id: int):
        pass

    @abstractmethod
    def create(self, camera: Camera) -> Camera:
        pass

    @abstractmethod
    def update(self, camera: Camera) -> Camera:
        pass

    @abstractmethod
    def delete_by_ip(self, ip: str) -> Camera:
        pass

    @abstractmethod
    def find_all(self) -> Sequence[Camera]:
        pass

    @abstractmethod
    def update_listening(self, camera: Camera, listening: bool):
        pass
