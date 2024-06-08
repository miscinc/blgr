import pytumblr

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    'your_consumer_key',
    'your_consumer_secret',
    'your_oauth_token',
    'your_oauth_secret'
)

# Function to get the most popular blog posts
def get_most_popular_blog_posts(blog_name, limit=10):
    posts = client.posts(blog_name, limit=limit, filter='text')
    sorted_posts = sorted(posts['posts'], key=lambda x: x.get('note_count', 0), reverse=True)
    return sorted_posts

def get_filtered_popular_blog_posts(blog_name, min_note_count=100, limit=10):
    posts = client.posts(blog_name, limit=limit, filter='text')
    filtered_posts = [post for post in posts['posts'] if post.get('note_count', 0) >= min_note_count]
    sorted_posts = sorted(filtered_posts, key=lambda x: x.get('note_count', 0), reverse=True)
    return sorted_posts

# Example usage
blog_name = 'example-blog.tumblr.com'
popular_posts = get_filtered_popular_blog_posts(blog_name, min_note_count=200)

for i, post in enumerate(popular_posts, start=1):
    print(f"Post {i}:")
    print(f"Title: {post.get('title', 'No Title')}")
    print(f"Note Count: {post.get('note_count', 0)}")
    print(f"URL: {post.get('post_url')}")
    print()