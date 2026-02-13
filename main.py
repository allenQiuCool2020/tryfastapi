import random
# data = {
#     "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
#     "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
#     "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
# }


# def check_valid_id(id: str):
#     if not id.startswith(("isbn-", "imdb-")):
#         raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
#     return id


# @app.get("/items/")
# async def read_items(
#     id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
# ):
#     if id is None:
#         id, item = random.choice(list(data.items()))
#         print(data)
#     elif id is not None:
#         if id in data:
#             item = data.get(id)
#         else:
#             item = f" Your id: {id} does not in the data list"
#     return {"id": id, "name": item}


from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results