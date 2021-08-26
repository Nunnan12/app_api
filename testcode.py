from pydantic import BaseModel
a= {123,123,123}
 
class Con(BaseModel):
	title:str
def add(param:Con):
	re = param.dict()
add("hello badguy")