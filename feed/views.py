
from cgitb import text
from email.mime import image
from hashlib import new
from multiprocessing import context
from django.views.generic import TemplateView,FormView,DetailView
#from requests import request
#from requests import post
from .forms import PostForm
from .models import Post
from django.contrib import messages
# Create your views here.

class HomePageView(TemplateView):
    template_name ='home.html'
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
      #  context['my_thing']="Hello world ths is dynamic"
        context['posts']=Post.objects.all().order_by('-id')
        return context 
    
class PostDetailView(DetailView):
    template_name="detail.html"
    model=Post
    
class AddPostView(FormView):
  
  template_name="new_post.html"
  form_class=PostForm
  success_url="/"
  
  
  def dispatch(self, request, *args, **kwargs):
    self.request=request
    return super().dispatch(request, *args, **kwargs)
    
  
  def form_valid(self, form):
    #print(form.cleaned_data['text'])
    #creaatea a new post
    
    new_object=Post.objects.create(
      text=form.cleaned_data['text'],
      image=form.cleaned_data['image']
    )
    messages.add_message(self.request,messages.SUCCESS,'Your Post Was Successful')
    return super().form_valid(form)
  