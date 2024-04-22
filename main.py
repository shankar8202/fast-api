from fastapi import FastAPI
from fastapi.params import Body
# BaseModel for validat field
from pydantic import BaseModel
# Optional this is for making field optional
from typing import Optional
# this for genrate random id number
from random import randrange
app = FastAPI()

# this is for field validation 
class MyValidationForCreateEntry (BaseModel):
    name :str
    lname:str
    age:int
    gf:str
    #profession  is optional thats how you make it optional
    profession:str = True 
    # it compleatly optinal "bhejogy to jaygi verna bhad me jay"
    futuregoals:Optional[str] = None



def checkingEntry(individualId):
    for userId in MyvariableForOpration:
     if userId["id"]== individualId:
        return userId



MyvariableForOpration= [{"name":"shankar","lname":"sahu","age":35,"id":1},
                        {"name":"ravi","lname":"patel","age":40,"id":2},
                        {"name":"satish","lname":"vd","age":45,"id":3}
                        ]


@app.get("/")
async def root():
    return {"message": "Hello World"}   
# --------------------------------------------------------
@app.get("/post")
async def handlePost():
    return{"data":MyvariableForOpration}
# -------------------------normal post api -------------------------
# @app.post("/entries")
# # this syntax need to run for get request dict  means dictionary
# async def addEntries(req: dict= Body(...)): 
#     print(req)       
#     # return {"message":req}
#     # this is like down below temlate string 
#     return {"message":f"name : {req["name"]} lname : {req["lname"]}"}



# --------------------------api with validation-----------------------------------
@app.post("/entries")
# this syntax need to run for get request dict  means dictionary
async def addEntries(req: MyValidationForCreateEntry): 
    my_dict =req.model_dump()
    # randrange this is create for random id 
    my_dict["id"] = randrange(0,1000000)
    MyvariableForOpration.append(my_dict)      
    # return {"message":req}
    # this is like down below temlate string 
    # print(req.model_dump)
    return {"data":req}
# ------------------------getting any single entry---------------------------------
@app.get("/getIndividual/{id}")
def getIndividual(id):
    # checking = checkingEntry(id)
    # becoz above one id data type is string 
    checking = checkingEntry(int(id))
    print(checking)

    return{"message":checking}

