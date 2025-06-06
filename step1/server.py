import random

import fastapi

app = fastapi.FastAPI()


@app.get("/proverka")
def index():
    value = random.randint(0,100)
    print(value)
    if value > 50:
        response = "gay"
    else:
        response  = "povezlo syka"
    return {"you": response}


# Запуск сервака
# fastapi dev server.py
