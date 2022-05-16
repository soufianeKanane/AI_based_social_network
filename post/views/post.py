from django.http import JsonResponse
from post.models import Post
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getAllPosts(request):
    if request.method == 'GET':
        try:
            posts = Post.nodes.all()
            print(posts)
            response = []
            for post in posts :
                obj = {
                "id" : post.id,
                "body" :post.body,
                "caption":post.caption ,
                "categories":post.categories,
                "type" :post.type,
                "isHidden" :post.isHidden,
                "isPopolar" :post.isPopolar ,
                }
                response.append(obj)
            return JsonResponse(response, safe=False)
        except:
            response = {"error": "Error occurred "}
            return JsonResponse(response, safe=False)
@csrf_exempt
def postDetails(request):
    if request.method == 'GET':
        # get one person by name
        id = request.GET.get('id', ' ')
        try:
            post = Post.nodes.get(id=id)
            response = {
                "id" : post.id,
                "body" :post.body,
                "caption":post.caption ,
                "categories":post.categories,
                "type" :post.type,
                "isHidden" :post.isHidden,
                "isPopolar" :post.isPopolar ,
            }
            return JsonResponse(response, safe=False)
        except :
            response = {"error":"Error occurred person not found"}
            return JsonResponse(response, safe=False)

    if request.method == 'POST':
        # create one post
        json_data = json.loads(request.body)
        body=json_data['body']
        caption=json_data['caption']
        categories=json_data['categories']
        type=json_data['type']
        isHidden=bool(json_data['isHidden'])
        isPopolar=bool(json_data['isPopolar'])
        try:
            post = Post(type=type,body=body,caption=caption,categories=categories,isHidden=isHidden,isPopolar=isPopolar)
            post.save()
            response = {
                "id": post.id,
            }
            return JsonResponse(response)
        except :
            response = {"error":"Error occurred post not created"}
            return JsonResponse(response, safe=False)

    if request.method == 'PUT':
        # update one post
        json_data = json.loads(request.body)
        id=json_data['id']
        body=json_data['body']
        caption=json_data['caption']
        categories=json_data['categories']
        type=json_data['type']
        isHidden=bool(json_data['isHidden'])
        isPopolar=bool(json_data['isPopolar'])
        try:
            post = Post.nodes.get(id=id)
            post.type = type
            post.body = body
            post.caption = caption
            post.categories = categories
            post.isHidden = isHidden
            post.isPopolar = isPopolar
            post.save()
            response = {
                "id": post.id,
                "body": post.body,
                "caption": post.caption,
                "categories": post.categories,
                "type": post.type,
                "isHidden": post.isHidden,
                "isPopolar": post.isPopolar,
            }
            return JsonResponse(response, safe=False)
        except:
            response = {"error":"Error occurred - post not modified"}
            return JsonResponse(response, safe=False)

    if request.method == 'DELETE':
        # delete one post
        json_data = json.loads(request.body)
        id = json_data['id']
        try:
            post = Post.nodes.get(id=id)
            post.delete()
            response = {"success": "Post deleted"
                        }
            return JsonResponse(response, safe=False)
        except:
            response = {"error":"Error occurred - post not deleted"}
            return JsonResponse(response, safe=False)
