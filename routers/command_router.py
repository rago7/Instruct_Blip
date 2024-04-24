# routers/command_router.py
from fastapi import APIRouter
from utils.multion_api import execute_command

router = APIRouter()

@router.post("/execute-command/")
async def execute_browser_command(command: str):
    result = execute_command(command)
    return {"result": result}
