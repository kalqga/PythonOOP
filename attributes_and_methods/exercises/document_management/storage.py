class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += f"{document.__repr__()}\n"
        return result

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        current_category = [c for c in self.categories if category_id == c.id]
        current_category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = [t for t in self.topics if topic_id == t.id]
        current_topic.topic = new_topic
        current_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        current_document = [d for d in self.documents if document_id == d.id]
        current_document.file_name = new_file_name

    def delete_category(self, category_id):
        current_category = [c for c in self.categories if c.id == category_id]
        self.categories.remove(current_category)

    def delete_topic(self, topic_id):
        current_topic = [t for t in self.topics if t.id == topic_id]
        self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_document = [d for d in self.documents if d.id == document_id]
        self.documents.remove(current_document)

    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc
