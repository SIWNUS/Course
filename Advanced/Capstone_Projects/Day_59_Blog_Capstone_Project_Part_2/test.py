import requests

blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
blog_posts = blog_response.json()

print(blog_posts[0])