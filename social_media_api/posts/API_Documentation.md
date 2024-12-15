

# Social Media API Documentation

## Endpoints
### Posts
- **GET /posts/**: List all posts.
- **POST /posts/**: Create a new post. Requires authentication.
- **GET /posts/?search=keyword**: Search posts by title or content.

### Comments
- **GET /comments/**: List all comments.
- **POST /comments/**: Add a comment to a post. Requires authentication.

## Request Examples
### Create a Post
**POST /posts/**
```json
{
    "title": "Sample Post",
    "content": "This is a sample post content."
}
