import json
def load_data(filename):
    with open(filename,'r') as f:
        return json.load(f)
def finding_pages_you_might_like(data,user_id):
    liked_pages={}
    for user in data['users']:
        liked_pages[user['id']]=set(user['liked_pages'])
    if user_id not in liked_pages:
        return []
    user_liked_pages=liked_pages[user_id]
    suggestions={}
    for other_user,pages in liked_pages.items():
        if other_user!=user_id:
            shared_pages=user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                suggestions[page]=suggestions.get(page,0)+len(shared_pages)

    sorted_pages=sorted(suggestions.items(),key=lambda x:x[1],reverse=True)
    return sorted_pages
data =load_data("massive_data.json")
suggestion=finding_pages_you_might_like(data,3)
print(suggestion)
