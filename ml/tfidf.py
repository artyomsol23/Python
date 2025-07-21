from math import log10

def calculate_tfidf(target_word: str, docs: list):
  if not docs:
        return 0.0
    
    term_count = docs[0].count(target_word)
    tf = term_count / len(docs[0]) if docs[0] else 0.0
    
    doc_count = sum(1 for doc in docs if target_word in doc)
    idf = log10(len(docs) / doc_count) if doc_count > 0 else 0.0
    
    tf_idf = tf * idf
    
    return round(tf_idf, 1)
