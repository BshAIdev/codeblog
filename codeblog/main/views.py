from django.shortcuts import render,redirect
from . import models
from django.utils import timezone

def index(request):
    return render(request, 'main/index.html')

def blog(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = models.Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다 
    return render(request, 'main/blog.html', {'postlist':postlist})

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    post = models.Post.objects.get(pk=pk)
    models.Post.objects.get(pk=pk).View()
    if request.method == 'POST':
        if "comment" in request.POST:
            new_article=models.Comment.objects.create(
                post = post,
                text = request.POST["comment"]
            )
            models.Post.objects.get(pk=pk).Com()
        else:
            models.Post.objects.get(pk=pk).Like()
        return redirect('/board/view/'+str(pk))
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        new_article=models.Post.objects.create(
            postTitle=request.POST['postname'],
            postText=request.POST['contents'],
            postCode_language=request.POST['language'],
            postCode=request.POST['codes'],
            pub_date=timezone.datetime.now()
        )
        return redirect('/board/')
    return render(request, 'main/new_post.html')