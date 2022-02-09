import uvicorn
from fastapi import Body, FastAPI
from models.database import database
from models.weather import weather_table

app = FastAPI()

@app.on_event("startup")
async def startup():
    # когда приложение запускается устанавливаем соединение с БД
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    # когда приложение останавливается разрываем соединение с БД
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-weather")
async def read_item():
    test = weather_table.select()
    return await database.fetch_all(test)

@app.post("/weather_set/")
async def fill_db(cities=Body(...)):
    for city, years in cities.items():
        for year, months in years.items():
            for month, temperature in months.items():
                query = weather_table.insert().values(
                    city=city,
                    year=int(year),
                    month=month,
                    temperature=temperature
                )
                await database.execute(query)
                print(query)
    return 'ok'

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)