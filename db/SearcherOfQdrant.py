class SearcherOfQdrant:
    @staticmethod
    def search(query, qdrant, search_method='max_marginal_relevance_search'):
        res = []
        if search_method is 'max_marginal_relevance_search':
            found_docs = qdrant.max_marginal_relevance_search(query)
        else:
            found_docs = qdrant.similarity_search(query)
        for i in found_docs:
            res.append(i.page_content)
        return res
