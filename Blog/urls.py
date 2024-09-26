from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.homePage,name="homePage"),
    path('createBlog/',views.createBlog,name="createBlog"),
    path('<int:blog_id>/deleteBlog/',views.deleteBlog,name="deleteBlog"),
    path('<int:blog_id>/editBlog/',views.editBlog,name="editBlog"),
    path('<int:blog_id>/confirmDeleteBlog/',views.confirmDeleteBlog,name="confirmDeleteBlog"),
    path('<int:blog_id>/blogDetail/',views.blogDetail,name="blogDetail"),
    path('login/',views.loginPage,name="loginPage"),
    path('logout/',views.logoutPage,name="logoutPage"),
    path('register/',views.registerPage,name="registerPage"),
]