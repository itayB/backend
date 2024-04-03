from typing import Literal
from typing_extensions import TypedDict
from fastapi import APIRouter, status

STATUS = Literal["success", "error", "partial", "unknown"]


class ReturnHealthcheckStruct(TypedDict):
    status: STATUS


router = APIRouter(
    prefix="/v1/health-check",
    tags=["Health Check"],
)


@router.get(
    "/liveness",
    summary="Perform a Liveness Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=ReturnHealthcheckStruct,
)
async def liveness() -> ReturnHealthcheckStruct:
    return {"status": "success"}
