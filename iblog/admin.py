from django.contrib import admin


from .models import Category,Post,Author,User,Comment

# For config of Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'cat_id', 'title', 'description', 'url')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('pimg_tag', 'post_id', 'ptitle', 'pcategory', 'pauthor', 'pdate')
    search_fields = ('ptitle',)
    list_filter = ('pcategory',)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name', 'uname', 'email', 'password')
    search_fields = ('name',)

class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','fname', 'username', 'eid', 'passw')
    search_field=('fname','user_id')

class CommentAdmin(admin.ModelAdmin):
    list_display=('username','post','created','active')
    list_filter = ('active','created','updated')
    search_field = ('username','message')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(User)
admin.site.register(Comment)
