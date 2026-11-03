# with open("knowledge.txt", "r") as file:
#     text = file.read()

# print("data loaded from knowledge.txt")

# chunk_size = 100

# chunks = []

# for i in range(0,len(text),chunk_size):
#     chunk = text[i:i + chunk_size]
#     chunks.append(chunk)



# print("no.of chunks",len(chunks))


# for i ,chunk in enumerate(chunks):
#     print(f"chunk {i+1} ")
#     print(chunk)

from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("knowledge.txt", "r", encoding="utf-8") as file:
    text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)