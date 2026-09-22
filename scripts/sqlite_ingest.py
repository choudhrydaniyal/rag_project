from ingest import load_faq_data
from sqlitesearch import TextSearchIndex

documents = load_faq_data()
print(f"Loaded {len(documents)} documents.")

index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)

for doc in documents:
    index.add(doc)

index.close()
print("Done. Index saved to faq.db")
