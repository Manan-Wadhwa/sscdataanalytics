from collections import defaultdict
import heapq


category_scores = defaultdict(lambda: {'sum': 0, 'count': 0})

category_counts = defaultdict(int)

for entry in data:
    category = entry[1]  
    score = entry[2]    
    if category and score: 
        category_scores[category]['sum'] += int(score)
        category_scores[category]['count'] += 1
        category_counts[category] += 1
average_scores = {}
for category, score_data in category_scores.items():
    if score_data['count'] > 0:
        average_scores[category] = score_data['sum'] / score_data['count']
top_5_categories = heapq.nlargest(5, category_counts, key=category_counts.get)
print("Average scores for each category:")
for category, average_score in average_scores.items():
    print(f"   {category}: {average_score:.2f}")
print("\nTop 5 most popular categories:")
for category in top_5_categories:
    print(f"   {category}: {category_counts[category]}")