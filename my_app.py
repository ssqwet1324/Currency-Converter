import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from converter import *
from fastapi.staticfiles import StaticFiles

class Volute(BaseModel):
    from_currency: str
    to_currency: str
    amount: int

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def show_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
  
@app.get('/convert')
async def convert_volute(amount: str, from_currency: str, to_currency: str):
    try:
        amount = float(amount)  # Преобразуем введенное значение в число
    except ValueError:
        return {"from_currency": from_currency, "to_currency": to_currency, "amount": "Error! Enter the number"}
    result = convert_currency(from_currency, to_currency, amount)
    return {"from_currency": from_currency, "to_currency": to_currency, "amount": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)