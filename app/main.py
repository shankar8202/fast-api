from fastapi import FastAPI, HTTPException,status
from fastapi.params import Body
# BaseModel for validat field
from pydantic import BaseModel
from typing import Union
# Optional this is for making field optional
from typing import Optional
# this for genrate random id number
from random import randrange
app = FastAPI()

# this is for field validation 
# uvicorn app.main:app --reload
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
    return None


MyvariableForOpration= [{"name":"shankar","lname":"sahu","age":35,"id":1},
                        {"name":"ravi","lname":"patel","age":40,"id":2},
                        {"name":"satish","lname":"vd","age":45,"id":3}
                        ]


def gettingIndex(id):
    # here below enumerate is a inbuilt method which is giving index and element togather so it easy to find index
    for index,element in enumerate(MyvariableForOpration):
        print(index,element)
        if element["id"] == id:
            return index

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
@app.post("/entries",status_code=status.HTTP_201_CREATED)
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
# ----------------------this is same as down below always make sure if you give same pathname like dynamic but first one is same so kai bar vo dynamic vala leleta hai or fir vha aap int pass krrhy ho or yha string to matter hojayga-------------------------
@app.get("/getIndividual/newone")
def getnewOne():
    makingCalculation = MyvariableForOpration[len(MyvariableForOpration)-1]
    return {"data":makingCalculation}


# ------------------------getting any single entry---------------------------------
@app.get("/getIndividual/{id}",status_code=status.HTTP_302_FOUND)
# we need to pass int because "id" is comming as a string
def getIndividual(id:int):
    # checking = checkingEntry(id)
    # becoz above one id data type is string 
    individual_data = checkingEntry(id)
    if individual_data is None:
    #   HTTPException it take two parameter for status code and details
      raise HTTPException(status_code=404, detail="ID not found")
    return {"data": individual_data}

    

# ------------------delete any post-------------------------
@app.delete("/deletePost/{post_id}")
# below status code is not going message when any quiry delelted it happen so far according to me in status 204
# @app.delete("/deletePost/{post_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    index =gettingIndex(post_id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id not found bro")
    print(index,"getting inddd")
    MyvariableForOpration.pop(index)
    return {"message":f"post with id {post_id} delete sucessfully"}
#  ------------------------------update any single entry-----------------------------  
@app.put("/post/{id}")
def UpdatePost(id:int,dataFromFrontend :MyValidationForCreateEntry):
    index =gettingIndex(id)
    if index == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Id not found bro for update")
#    model_dump() is used to make valid jason formate write now it is in different formate
    post_dict =   dataFromFrontend.model_dump()
    # print(type(post_dict),"yooo")
    # print(type(dataFromFrontend),"dataFromFrontend")
    post_dict["id"] = id
    MyvariableForOpration[index] = post_dict
    return {
        "message" : "sucessfully update"
    }
    
