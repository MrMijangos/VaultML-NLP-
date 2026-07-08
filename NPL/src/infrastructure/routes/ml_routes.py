from fastapi import APIRouter, Depends, HTTPException

from src.domain.dtos.recommend_request_dto import RecommendRequestDTO
from src.domain.dtos.recommend_response_dto import RecommendResponseDTO
from src.domain.dtos.segment_request_dto import SegmentRequestDTO
from src.domain.dtos.segment_response_dto import SegmentResponseDTO
from src.infrastructure.controllers.recommend_controller import RecommendController
from src.infrastructure.controllers.segment_controller import SegmentController
from src.infrastructure.dependencies import get_recommend_controller, get_segment_controller

router = APIRouter(prefix="/ml", tags=["Machine Learning"])


@router.post("/segment", response_model=SegmentResponseDTO)
def segment(
    request: SegmentRequestDTO,
    controller: SegmentController = Depends(get_segment_controller),
) -> SegmentResponseDTO:
    try:
        return controller.handle(request)
    except (FileNotFoundError, ValueError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/recommend", response_model=RecommendResponseDTO)
def recommend(
    request: RecommendRequestDTO,
    controller: RecommendController = Depends(get_recommend_controller),
) -> RecommendResponseDTO:
    try:
        return controller.handle(request)
    except (FileNotFoundError, ValueError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
