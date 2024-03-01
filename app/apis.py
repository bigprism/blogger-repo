from django.http import JsonResponse

from .models import Post


def post_list_api(request):
    posts = Post.objects.all()
    data = []
    for post in posts:
        data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at,
        })
    return JsonResponse(data, safe=False)


def post_detail_api(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found.'}, status=404)

    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'created_at': post.created_at,
        'updated_at': post.updated_at,
    }
    return JsonResponse(data)


def post_create_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
            author=request.user,
        )
        return JsonResponse({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at,
        })
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def post_update_api(request, pk):
    if request.method == 'PUT':
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found.'}, status=404)

        data = json.loads(request.body)
        post.title = data['title']
        post.content = data['content']
        post.save()

        return JsonResponse({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at,
            'updated_at': post.updated_at,
        })
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def post_delete_api(request, pk):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found.'}, status=404)

        post.delete()
        return JsonResponse({'success': 'Post deleted.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)









