from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.memo_service import MemoService, ValidationError

router = APIRouter(prefix="/memos", tags=["memos"])
templates = Jinja2Templates(directory="app/templates")
service = MemoService()


@router.get("/", response_class=HTMLResponse)
def list_memos(request: Request, db: Session = Depends(get_db)):
    memos = service.list_memos(db)
    return templates.TemplateResponse(
        request=request,
        name="memos/list.html",
        context={"memos": memos},
    )


@router.get("/new", response_class=HTMLResponse)
def new_memo_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="memos/form.html",
        context={
            "page_title": "메모 등록",
            "action": "/memos",
            "memo": None,
            "error": None,
        },
    )


@router.post("")
def create_memo(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        memo = service.create_memo(db, title=title, content=content)
    except ValidationError as exc:
        return templates.TemplateResponse(
            request=request,
            name="memos/form.html",
            context={
                "page_title": "메모 등록",
                "action": "/memos",
                "memo": {"title": title, "content": content},
                "error": str(exc),
            },
            status_code=400,
        )

    return RedirectResponse(url=f"/memos/{memo.id}", status_code=303)


@router.get("/{memo_id}", response_class=HTMLResponse)
def detail_memo(memo_id: int, request: Request, db: Session = Depends(get_db)):
    memo = service.get_memo(db, memo_id)
    if memo is None:
        return templates.TemplateResponse(
            request=request,
            name="not_found.html",
            context={"message": "해당 메모를 찾을 수 없습니다."},
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="memos/detail.html",
        context={"memo": memo},
    )


@router.get("/{memo_id}/edit", response_class=HTMLResponse)
def edit_memo_form(memo_id: int, request: Request, db: Session = Depends(get_db)):
    memo = service.get_memo(db, memo_id)
    if memo is None:
        return templates.TemplateResponse(
            request=request,
            name="not_found.html",
            context={"message": "해당 메모를 찾을 수 없습니다."},
            status_code=404,
        )

    return templates.TemplateResponse(
        request=request,
        name="memos/form.html",
        context={
            "page_title": "메모 수정",
            "action": f"/memos/{memo.id}/edit",
            "memo": memo,
            "error": None,
        },
    )


@router.post("/{memo_id}/edit")
def update_memo(
    memo_id: int,
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    memo = service.get_memo(db, memo_id)
    if memo is None:
        return templates.TemplateResponse(
            request=request,
            name="not_found.html",
            context={"message": "해당 메모를 찾을 수 없습니다."},
            status_code=404,
        )

    try:
        service.update_memo(db, memo, title=title, content=content)
    except ValidationError as exc:
        return templates.TemplateResponse(
            request=request,
            name="memos/form.html",
            context={
                "page_title": "메모 수정",
                "action": f"/memos/{memo_id}/edit",
                "memo": {"id": memo_id, "title": title, "content": content},
                "error": str(exc),
            },
            status_code=400,
        )

    return RedirectResponse(url=f"/memos/{memo_id}", status_code=303)


@router.post("/{memo_id}/delete")
def delete_memo(memo_id: int, request: Request, db: Session = Depends(get_db)):
    memo = service.get_memo(db, memo_id)
    if memo is None:
        return templates.TemplateResponse(
            request=request,
            name="not_found.html",
            context={"message": "해당 메모를 찾을 수 없습니다."},
            status_code=404,
        )

    service.delete_memo(db, memo)
    return RedirectResponse(url="/memos/", status_code=303)
