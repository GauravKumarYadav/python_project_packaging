from fastapi import FastAPI, HTTPException
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
def read_hive(output_limit: int = 10):
    '''
    Reads data from hive using subprocess
    :return:
    the output of the hive query
    '''
    try:

        output = subprocess.check_output(
            f"hive -e 'select * from test.fastapi_table LIMIT {output_limit}'", shell=True)
        output_str = output.decode('utf-8')
        output_list = []
        for line in output_str.splitlines():
            age, name, email = line.split('\t')
            output_list.append({
                'age': age,
                'name': name,
                'email': email
            })

        print(output_list)
        return {"message": "", "data": output_list, "status": 200, "size": len(output_list)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/post_into_hive")
def insert_into(payload: CustomModel):
    try:
        data1 = payload.name
        data2 = payload.age
        data3 = payload.email

        print(payload)
        try:
            subprocess.check_output(
                "hive -e 'insert into test.fastapi_table values (\"{}\", {}, \"{}\")'".format(data1, data2, data3), shell=True)
        except subprocess.CalledProcessError as e:
            raise HTTPException(
                status_code=500, detail="Data not inserted in Hive")

        output = subprocess.check_output(
            f"hive -e 'select * from test.fastapi_table where name=\"{data1}\" and age={data2} and email=\"{data3}\"'", shell=True)

        output_str = output.decode('utf-8')

        for line in output_str.splitlines():
            age, name, email = line.split('\t')
            if age == data2 and name == data1 and email == data3:
                return {"message": "Data written to Hive successfully"}

        raise HTTPException(
            status_code=500, detail="Data not inserted in Hive")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
