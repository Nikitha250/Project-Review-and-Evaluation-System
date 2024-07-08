from dataset import Dataset
from sentence_similarity import SentenceSimilarity

data = Dataset('static/uploads/titles1.txt')
sentence_sim = SentenceSimilarity(data)

most_similar = sentence_sim.get_most_similar("How is it possible for machines to learn?")
print("\n".join(most_similar))