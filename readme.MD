# Django-rest-framework 快速上手

# 启动

1、进入虚拟环境

```py
source venv/bin/activate
```

2、启动项目

```py
python3 manage.py runserver
```


# 新建一个新的项目：myapi 

## 1. 新建项目
### 1.1 新建

Django 架子初始化后，新建新的模块时，应该独立出来，成为一个“新的项目”。  
下面，我们开始新建一个新的项目（模块）——myapi  

```py
$ python manage.py startapp myapi
```

命令执行成功后，项目的目录下会新增一个 `myapi` 的文件夹，说明我们新建成功了。  

### 1.2 注册

接着，我们在主项目注册 `myapi`，编辑 `rest_api/settings` 的文件：

```py
# Application definition
INSTALLED_APPS = [
    'myapi.apps.MyapiConfig',
    # ....
]
```

这样，新的项目我们就算注册好了。

### 1.3 Migrate 迁移模型到数据库

接着，我们需要告诉 Django 要把我们的新的模块迁移到数据库，Django 就会给我们生产对于的配套：

```py
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.
```

切记，在 Django 中，你新建模块（项目）都得 `python manage.py migrate` 一下,不然是无法生效的。  

## 2. 新建模型

现在，我们要使用 Django ORM 来创建我们的模型。

### 2.1 `myapi/models.py`

```py
# models.py
from django.db import models


class Company(models.Model):
    '''
        Company model
    '''
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=60)
    fields = models.CharField(max_length=60)
    official_website = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

```

上面我们的代码，新建了一个 Company 模型，并创建了五个字段：name,address,city,fields,official_website。

### 2.2 makemigrations and migrate

新建模型之后，也不要忘记了执行迁移：

```py
python manage.py makemigrations

Migrations for 'myapi':
  myapi/migrations/0001_initial.py
    - Create model Company
```

接着：

```py
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapi, sessions
Running migrations:
  Applying myapi.0001_initial... OK
```

### 2.3 添加到 Django administration

为了方面数据管理，我们还得把新模型添加到 Django 自带的后台系统里面。  
打开编辑 `myapi/admin.py`文件：

```py
from django.contrib import admin

from .models import Company

admin.site.register(Company)
```

搞定，运行试试。


# 使用 Django REST Framework

## 1. 安装 && 配置

目前为止，Django 最火的 rest 框架还是 `djangorestframework`，安装：

```py
$ pip install djangorestframework
```

接在在项目配置模块 `mysite/settings.py` 加上即可：

```py
INSTALLED_APPS = [
    # All your installed apps stay the same
    ...
    'rest_framework',
]
```

教程地址：
[Build a REST API in 30 minutes with Django REST Framework](https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c)

## 2. 应用到项目

### 2.1 序列化 model

在新建的项目下新建 `serializers.py` 文件,并编辑：

```py
from rest_framework import serializers   # 1. 导入 rest_framework
from .models import Company              # 2. 导入 model


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    '''
        3. 系列化 Company model 
    '''
    class Meta:
        model = Company
        fields = ('id','name','address','city','official_website')


```

### 2.2 页面视图

系列化后，需要在页面展示出来，这个时候就在目录的 `myapi/views.py` 编写：

```py
from rest_framework import viewsets 
from .serializers import CompanySerializer
from .models import Company

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

```

### 2.3 路由

在目录下新建 `myapi/urls.py` 文件，添加：

```py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

然后，在主项目下的 `mysite/urls.py` 新增新的模块：

```py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapi/', include('myapi.urls')),
]
```

搞定，然后 `python manage.py runserver` 启动一下，访问：`http://127.0.0.1:8000/myapi/` 即可

完成。