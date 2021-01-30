from .category import Category
from .topic import Topic
from .document import Document


class Storage:
    def __init__(self):
        self.categories: list = []
        self.topics: list = []
        self.documents: list = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self._find_category_by_id(category_id)
        category.name = new_name

    def delete_category(self, category_id: int):
        category = self._find_category_by_id(category_id)
        self.categories.remove(category)

    def _find_category_by_id(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self._find_topic_by_id(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def delete_topic(self, topic_id: int):
        topic = self._find_topic_by_id(topic_id)
        self.topics.remove(topic)

    def _find_topic_by_id(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.file_name = new_file_name

    def delete_document(self, document_id: int):
        document = self.get_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([document.__repr__() for document in self.documents])
