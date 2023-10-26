from lib.space import Space
from lib.base_repository_class import BaseModelManager


class SpaceRepository(BaseModelManager):

    """Space model repository"""

    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = Space
        self._table_name = "spaces"

    def create(self, new_space):
        query = (
            "INSERT INTO spaces"
            "(name, description, size, location, price, user_id)"
            "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"
        )

        rows = self._connection.execute(
            query,
            [
                new_space.name,
                new_space.description,
                new_space.size,
                new_space.location,
                new_space.price,
                new_space.user_id,
            ],
        )
        new_space.id = rows[0].get("id")
        return new_space
    
    def update(self, updated_space):
        query = 'UPDATE spaces SET name = %s, description = %s, size = %s, location = %s, price = %s WHERE id = %s;'
        rows = self._connection.execute(
            query, 
            [
                updated_space.name, 
                updated_space.description, 
                updated_space.size, 
                updated_space.location, 
                updated_space.price, 
                updated_space.id
            ]
        )


    
