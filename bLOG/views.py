from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.urls import reverse
# from hitcount.views import HitCountDetailView
from .form import CommentForm
from .models import Post, Comment
from django.shortcuts import get_object_or_404
# Create your views here.
# from .. import wblog


def home(request):
    posts = Post.objects.all()[:11]
    data = {
        'posts':posts,
    }
    # return render(request,"home.html",data)
    return render(request,"unsplash.html",data)

def post(request,url):
    post = get_object_or_404(Post, url=url)
    return render(request,'post.html',{'post':post})


# class PostDetailView(HitCountDetailView):
#     model = Post
#     template_name = "blog/post.html"
#     slug_field = "slug"
#     count_hit = True
#     form = CommentForm
#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             post = self.get_object()
#             form.instance.user = request.user
#             form.instance.post = post
#             form.save()
#             return redirect(reverse("post", kwargs={
#                 'slug': wblog.slug
#             }))
#     def get_context_data(self, **kwargs):
#         post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
#         post_comments = Comment.objects.all().filter(post=self.object.id)
#         context = super().get_context_data(**kwargs)
#         context.update({
#             'form': self.form,
#             'post_comments': post_comments,
#             'post_comments_count': post_comments_count,
#         })
#         return context