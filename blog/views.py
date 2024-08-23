from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import BlogPost
from django.views.generic import DetailView
from blog.like_task import create_task

def BlogPostLike(request, pk):
    print(f"post_id: {pk}, user_id: {request.user.id}")  # Debugging line
    create_task.delay(pk,request.user.id)
    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data
