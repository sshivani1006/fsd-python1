from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from iblog.models import Post, Category, Author, User, Comment
from .forms import CommentForm

# Create your views here.
def home(request):
    # Load all the post from db (10)
    posts = Post.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    data = {'posts': posts, 'cats': cats}
    return render(request, "iblog/home.html", data)


def login(request):
    return render(request, "iblog/login.html")


def login_data(request):
    uname = request.POST['uname']
    password = request.POST['password']
    logindata = Author.objects.filter(uname=uname, password=password).count()
    if logindata > 0:
        request.session['username'] = uname
        usession = request.session['username']
        param = {"session": usession}

        record = Post.objects.all()
        param = {"data": record}
    else:
        param = {"msg": "username and password does not match..."}
    return render(request, "iblog/manage_post.html", param)


def action(request):
    post_id = request.GET.get("data")
    Post.objects.filter(post_id=post_id).delete()
    param = {"msg": "Record deleted successfully...", }
    return render(request, "iblog/manage_post.html", param)


def edit(request):
    post_id = request.GET.get("data1")
    record = Post.objects.get(post_id=post_id)
    allrec = Category.objects.all()
    auth = Author.objects.all()
    param = {"data2": record, 'allrec': allrec, 'auth': auth}
    return render(request, "iblog/edit_post.html", param)

def info_update(request):
    if request.method == "POST":
        p_id = request.POST.get("post_id")
        p_title = request.POST.get("ptitle")

        p_category = request.POST.get("pcategory")
        category = Category.objects.get(title=p_category)

        p_content = request.POST.get("pcontent")
        p_date = request.POST.get("pdate")
        p_url = request.POST.get("purl")
        if len(request.FILES) != 0:
            p_img = request.FILES['post_img']

        p_author = request.POST.get("pauthor")
        author = Author.objects.get(id=p_author)

        record = Post.objects.get(post_id=p_id)
        record.ptitle = p_title

        record.pcategory = category

        record.pcontent = p_content
        record.pdate = p_date
        record.purl = p_url
        record.post_img = p_img

        record.pauthor = author

        record.save()
        record2 = Post.objects.all()

        record7 = Post.objects.all()

        param = {"msg1": "Record Updated Successfully...", "data3": record2, 'data': record7}
        return render(request, "iblog/manage_post.html", param)


def register(request):
    return render(request, "iblog/register.html")


def reg(request):
    name = request.GET.get("name")
    u_name = request.GET.get("uname")
    eid = request.GET.get("email")
    pw = request.GET.get("password")

    data = Author(name=name, uname=u_name, email=eid, password=pw)
    data.save()
    para = {"msg": "Registration Successful"}

    return render(request, "iblog/register.html", para)


def detail(request, purl):
    record = Post.objects.get(purl=purl)
    cats = Category.objects.all()

    comments = Comment.objects.filter(post=record)

    # print(post)
    data = {'record': record, 'cats': cats, 'comments': comments, 'user': request.user}
    return render(request, "iblog/detail.html", data)


def postComment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        user = request.user
        comment = request.POST.get("message")
        post = Post.objects.get(post_id=post_id)

        comment = Comment(message=comment, username=user, post=post)
        comment.save()
        para = {"msg": "comment posted successfully"}
        return render(request, "iblog/detail.html", para)


def category(request, url):
    pcategory = Category.objects.get(url=url)
    posts = Post.objects.filter(pcategory=pcategory)
    data1 = {'pcategory': pcategory, 'posts': posts}
    return render(request, "iblog/category.html", data1)


def user_login(request):
    return render(request, "iblog/user_login.html")


def user_log(request):
    username = request.POST['username']
    passw = request.POST['passw']
    userlog = User.objects.filter(username=username, passw=passw).count()
    if userlog > 0:
        request.session['uname'] = username
        usession = request.session['uname']
        param = {"session": usession}

        # record = Post.objects.all()
        # param = {"data": record}
    else:
        param = {"msg": "username and password does not match..."}
    redirect_url=reverse('home',)
    return redirect(f'{redirect_url}?{param}')


def user_register(request):
    return render(request, "iblog/user_register.html")


def user_reg(request):
    fname = request.GET.get("fname")
    username = request.GET.get("username")
    email_id = request.GET.get("email_id")
    passw = request.GET.get("passw")

    data = User(fname=fname, username=username, email_id=email_id, passw=passw)
    data.save()
    para = {"msg": "Registration Successful"}

    return render(request, "iblog/user_register.html", para)
