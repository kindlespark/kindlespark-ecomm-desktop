from fastapi import FastAPI
from desktop import Desktop


app=FastAPI()
desktop_list=[]

@app.get("/")
def desktop_shop():
    print(f"inside desktop_shop")
    return {"message": "Welcome to the Desktop Shop"}

@app.post("/new-desktop")
def add_new_desktop(desktop:Desktop):
    desktop_list.append(desktop.dict())
    return desktop_list

@app.get("/desktops")
def get_all_desktops():
    return desktop_list

@app.delete("/desktop/{id}")
def delete_desktop_by_id(id: int):
    for desktop in desktop_list:
        if desktop['id'] == id:
            desktop_id = desktop_list.index(desktop)
            desktop_list.pop(desktop_id)
            return desktop_list
    
    return {"message": "desktop not found"}

