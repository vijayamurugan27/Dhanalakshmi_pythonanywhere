"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from appname import views

from appname.views import StudentReg, Studentlist ,Studentdetail , StudentUpdate, StudentDelete 

app_name='appname'

urlpatterns = [
    path('home', views.home, name = "home"),
    path('product', views.product, name = "product"),
    path('service', views.service, name = "service"),
    path('contact', views.contact, name = "contact"),
    path('aboutus', views.aboutus, name = "aboutus"),
    

   path('studentreg', StudentReg.as_view(), name = 'studentreg'),
   path('<pk>/studentdetail', Studentdetail.as_view(), name = 'studentdetail'),
   path('',Studentlist.as_view(), name = 'studentlist'),
   path('<pk>/studentupdate',StudentUpdate.as_view(),name = 'studentupdate'),
   path('<pk>/studentdelete', StudentDelete.as_view(), name = 'studentdelete'),


### for get ad post
    path('dhana',views.dhana, name = 'dhana'),
    path('get1', views.get1, name = 'get1'),
    path('post1', views.post1, name = 'post1'),

###  for Fnuction based view.
    path('form', views.form,name  = 'form'), ##student registration
    path('students', views.students, name = "students"), #studentlist
    path('detail/<int:id>', views.detail, name = 'detail'), # student Detail
    path('update/<int:id>', views.update, name = 'update'), # Stuudent update
    path('delete/<int:id>', views.delete, name = 'delete'), #Student Update




### for user registratio, sign-in sign-out
    path('index', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),


# for E-commerce
 path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),


]
