from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.memo_service import MemoService


router = APIRouter(prefix="/memos", tags=["memos"])
templates = Jinja2Templates(directory="app/templates")
service = MemoService()


def not_found(request: Request, memo_id: int):
    return templates.TemplateResponse(
        request=request,
        name="not_found.html",
        context={"memo_id": memo_id},
        status_code=404,
    )


@router.get("", response_class=HTMLResponse)
def memo_list(request: Request, db: Session = Depends(get_db)):
    memos = service.list_memos(db)
    return templates.TemplateResponse(
        request=request,
        name="memos/list.html",
        context={"memos": memos},
    )


@router.get("/new", response_class=HTMLResponse)
def memo_create_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="memos/form.html",
        context={"page_title": "새 메모 작성", "memo": None, "error": None, "action": "/memos"},
    )


@router.post("")
def memo_create(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        memo = service.create_memo(db, title=title, content=content)
    except ValueError as exc:
        return templates.TemplateResponse(
            request=request,
            name="memos/form.html",
            context={
                "page_title": "새 메모 작성",
                "memo": {"title": title, "content": content},
                "error": str(exc),
                "action": "/memos",
            },
            status_code=400,
        )
    return RedirectResponse(url=f"/memos/{memo.id}", status_code=303)


@router.get("/{memo_id}", response_class=HTMLResponse)
def memo_detail(request: Request, memo_id: int, db: Session = Depends(get_db)):
    memo = service.get_memo(db, memo_id)
    if memo is None:
        return not_found(request, memo_id)
    return templates.TemplateResponse(
        request=request,
        name="memos/detail.html",
        context={"memo": memo},
    )


@router.get("/{memo_id}/edit", response_class=HTMLResponse)
def memo_edit_form(request: Request, memo_id: int, db: Session = Depends(get_db)):
    memo = service.get_memo(db, memo_id)
    if memo is None:
        return not_found(request, memo_id)
    return templates.TemplateResponse(
        request=request,
        name="memos/form.html",
        context={
            "page_title": "메모 수정",
            "memo": memo,
            "error": None,
            "action": f"/memos/{memo_id}/edit",
        },
    )


@router.post("/{memo_id}/edit")
def memo_update(
    request: Request,
    memo_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        memo = service.update_memo(db, memo_id, title=title, content=content)
    except ValueError as exc:
        return templates.TemplateResponse(
            request=request,
            name="memos/form.html",
            context={
                "page_title": "메모 수정",
                "memo": {"id": memo_id, "title": title, "content": content},
                "error": str(exc),
                "action": f"/memos/{memo_id}/edit",
            },
            status_code=400,
        )
    if memo is None:
        return not_found(request, memo_id)
    return RedirectResponse(url=f"/memos/{memo.id}", status_code=303)


@router.post("/{memo_id}/delete")
def memo_delete(request: Request, memo_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_memo(db, memo_id)
    if not deleted:
        return not_found(request, memo_id)
    return RedirectResponse(url="/memos", status_code=303)
