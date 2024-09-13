from typing import List

from app.config.bindings import inject
from app.models.device_group import DeviceGroup, Device, DeviceGroupInputDto
from app.routers.router_wrapper import RouterWrapper
from app.services.device_group.device_group_service import DeviceGroupService


class DeviceGroupRouter(RouterWrapper):
    @inject
    def __init__(self, device_group_service: DeviceGroupService):
        super().__init__(prefix=f"/device-group")
        self.device_group_service = device_group_service


    def _define_routes(self):
        @self.router.post("/")
        def create_device_group(device_group_dto: DeviceGroupInputDto):
            device_group = DeviceGroup.from_dto(device_group_dto)
            return self.device_group_service.create_device_group(device_group)


        @self.router.get("/")
        def get_device_group(group_id: int):
            return self.device_group_service.get_device_group_by_id(group_id)


        @self.router.delete("/{group_id}")
        def delete_device_group(group_id: int):
            return self.device_group_service.delete_device_group(group_id)


        @self.router.put("/{group_id}")
        def update_device_group(group_id: int, group: DeviceGroup):
            return self.device_group_service.update_device_group(group_id, group)


        @self.router.post("/{group_id}/devices")
        def update_devices_in_group(group_id: int, device_ids: List[int]):
            return self.device_group_service.update_devices_in_group(group_id, device_ids)


        @self.router.get("/{group_id}/devices")
        def get_devices_in_group(group_id: int):
            return self.device_group_service.get_device_list_by_id(group_id)


        @self.router.post("/{group_id}/start-listening")
        def start_listening(group_id: int):
            return self.device_group_service.start_listening(group_id)


        @self.router.post("/{group_id}/stop-listening")
        def stop_listening(group_id: int):
            return self.device_group_service.stop_listening(group_id)