from fastapi import FastAPI

app = FastAPI()

notes = []

@app.get("/")
def home():
    return {"message": "Welcome to Notes App"}

@app.post("/add_note")
def add_note(note: str):
    notes.append(note)
    return {"message": "Note added successfully", "notes": notes}

@app.get("/all_notes")
def all_notes():
    return {"notes": notes}

@app.delete("/delete_note")
def delete_note(index: int):
    if index < len(notes):
        removed = notes.pop(index)
        return {"message": "Note deleted", "removed": removed}
    return {"error": "Note not found"}
