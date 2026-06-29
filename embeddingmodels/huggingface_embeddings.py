from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# Step 1

# Convert documents into embeddings.

# Step 2

# Store them in a vector database.

# Step 3

# User asks question.

# Step 4

# Convert question into embedding.

# Step 5

# Find closest matching vectors.

# Step 6

# Send relevant text to LLM.
# creating embedding of a sentence using an embedding model
# An embedding in Generative AI is a way to convert text (or images/audio) into numbers so that AI models can understand meaning mathematically.
texts=[
    "my name is vj",
    "this is my first project"
]
vector=embedding.embed_documents(texts)
print(vector)