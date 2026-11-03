
""" NetPulse Devices API's"""

from typing import Optional

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, Field

app = FastAPI(
    title="Devices API",
    version="1.0.0",
    description="CRUD API's for Netpulse Project",
)

# Pydantic Models

class DeviceBase(BaseModel):
    name: str = Field(min_length=1)
    status: str = Field(min_length=2)


class DeviceCreate(DeviceBase):
    pass


class DeviceUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    status: Optional[str] = Field(default=None, min_length=2)


class Device(DeviceBase):
    id: int


devices: dict[int, Device] = {
    1: Device(id=1, name="Router", status="UP"),
    2: Device(id=2, name="Switch", status="DOWN"),
}

# Implement the Home Page

@app.get("/")
def home():
    return {"message":"Net Pulse Server Started"}

# Implement the /devices endpoint

@app.get("/devices")
def  list_devices():
    return list(devices.values())

