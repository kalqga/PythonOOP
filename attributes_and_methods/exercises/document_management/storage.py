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
        for cat in self.categories:
            if cat.id == category_id:
                cat.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for top in self.topics:
            if top.id == topic_id:
                top.topic = new_topic
                top.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        for doc in self.documents:
            if doc.id == document_id:
                doc.file_name = new_file_name

    def delete_category(self, category_id):
        for cat in self.categories:
            if cat.id == category_id:
                self.categories.remove(cat)

    def delete_topic(self, topic_id):
        for top in self.topics:
            if top.id == topic_id:
                self.topics.remove(top)

    def delete_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                self.documents.remove(doc)


    def get_document(self, document_id):
        for doc in self.documents:
            if doc.id == document_id:
                return doc
