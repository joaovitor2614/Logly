
from fastapi import APIRouter, status
from bson.objectid import ObjectId

def update_document_object_instance(database, object_id: str, updated_object):
    
    updated_object = {k: v for k, v in updated_object.dict().items() if v is not None}
    if len(updated_object) >= 1:
        update_result = database.update_one(
            {"_id": ObjectId(id)}, {"$set": updated_object}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object with ID {id} not found")

    if (
        existing_object := database.find_one({"_id": ObjectId(id)})
    ) is not None:
        return existing_object

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object with ID {id} not found")