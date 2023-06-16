from db.SearcherOfQdrant import SearcherOfQdrant
from db.UploaderOfQdrant import UploaderOfQdrant

uploder = UploaderOfQdrant()
qdrant = uploder.Upload()
query = "劳动合同无效"
found_docs = SearcherOfQdrant.search(query, qdrant)
print(found_docs)



