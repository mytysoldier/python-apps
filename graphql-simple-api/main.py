import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from db.db import create_heros, initialize_db


@strawberry.type
class User:
    id: int
    name: str
    address: str
    phone_number: str
    sex: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(
            id=1, name="name", address="address", phone_number="phone_number", sex="sex"
        )


initialize_db()

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)


@app.get("/heros")
def heros():
    create_heros()
    return "sample data created"
