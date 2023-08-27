import typing
import strawberry


@strawberry.type
class Hero:
    id: int
    name: str
    secret_name: str
    age: int
    team_id: int


def get_heros():
    return [Hero(id=1, name="test", secret_name="test secret", age=10, team_id=1)]


@strawberry.type
class Query:
    heros: typing.List[Hero] = strawberry.field(resolver=get_heros)


schema = strawberry.Schema(query=Query)
