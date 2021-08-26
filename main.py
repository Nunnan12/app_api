from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class model_con(BaseModel):
    angle: int
    control: str
data_json = [
{
	"angle" : 90,
	"control" : "mid"
	
}

]
@app.get("/data")
async def get_data():
	return data_json
@app.put("/data")
async def create_data(control: model_con):
    resal = control
    data_json[0].update(resal)
    return resal
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)	
