from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.dynamodb import DynamoDBVectorStore


def test_class():
    names_of_base_classes = [b.__name__ for b in DynamoDBVectorStore.__mro__]
    assert VectorStore.__name__ in names_of_base_classes
