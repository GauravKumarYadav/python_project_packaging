from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()


class CustomModel(BaseModel):
    name: str
    age: int
    email: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/get_from_hive")
def read_hive():
    '''
    Reads data from hive using subprocess
    :return:
    the output of the hive query
    '''
    output = subprocess.call(
        "hive -e 'select * from test.fastapi_table'", shell=True)
    print(output)
    return {"message": "Data read from Hive successfully", "data": output}


@app.post("/post_into_hive")
def insert_into(payload: CustomModel):
    data1 = payload.name
    data2 = payload.age
    data3 = payload.email

    print(payload)
#    subprocess.call("hive -e 'insert into test.fastapi_table values (\"{}\", {}, \"{}\")'".format(data1, data2, data3),shell=True)
    return {"message": "Data written to Hive successfully"}
