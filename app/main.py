from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config.handlers import get_exception_handlers
from app.routers.impl.camera_router import CameraRouter
from app.routers.impl.device_group_router import DeviceGroupRouter
from app.routers.impl.disk_usage_router import DiskUsageRouter
from app.routers.impl.recording_router import RecordingRouter
from app.routers.impl.reed_router import ReedRouter
from app.routers.router_wrapper import RouterWrapper

exception_handlers = get_exception_handlers()
routers: List[RouterWrapper] = [
    CameraRouter(),
    ReedRouter(),
    RecordingRouter(),
    DiskUsageRouter(),
    DeviceGroupRouter()
]

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

for exc, handler in exception_handlers:
    app.add_exception_handler(exc, handler)

for router in routers:
    app.include_router(router.get_fastapi_router())
