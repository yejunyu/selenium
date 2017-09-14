1. celery中起子进程会报错
    ```
    AssertionError: daemonic processes are not allowed to have children
    ```
    > 解决办法
    
    ```python
    process = multiprocessing.current_process()
    # 进程启动前设为非守护进程启动
    process.daemon = False
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # 启动后再设为true
    process.daemon = True
    pool.apply_async(browser.browser_click, args=(url, count, md5))
    pool.close()
    pool.join()
    ```
    
2. futuer 模块
    ```python
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
    # 设置池的大小 (线程和进程只需要换thread或者process)
    pool = ProcessPoolExecutor(max_workers=20)
    futures = []
    for i in range(int(count)):
        futures.append(pool.submit(browser_click1,url))
        time.sleep(1)
    # 线程等待
    print(wait(futures, timeout=60))
    ```

3. 不管是ThreadPoolExecutor, ProcessPoolExecutor或者multiprocessing使用selenium都会偶尔出现元素找不到的问题,后台统计数也误差很大
    ~~selenium只能作为测试框架,或者爬虫爬取反扒严格的网站,并不能作为并发爬虫使用~~
    ** 更正 **
    > 网络问题导致找不到元素,并不是selenium库的问题

4. Django 的save()会更新所有字段,所以做更新数据的时候加上要更新的字段比如:

    ```m
    q.save(update_fields=['finish_count'])
    ```

5. get字符串截取
```
    url=http://42.62.65.11/s?z=ap&c=55
    url = request.GET.get('url')
    取得url = http://42.62.65.11/s?z=ap
    从&截开了
```

6. 代理&服务器卡死

    1. 无忧代理 普通高级代理 7月7号晚9点到早9点
    2. 站大爷     短效优质代理 7月8号12点
    3. 不加代理                          7月8号19点到20点
    4. 不加代理去掉模拟手机  7月8号20点到22点     chrome进程数918个
    
        2017-07-08 22:07:32 browser [line:45]: b    
        2017-07-08 22:07:33 browser [line:43]: a
        
    5. 不加代理去掉模拟手机换成mutil库      7月8号23点
    6. mutil库 无忧代理不加模拟手机             7月9号10点,16点
    7.thread 不加代理                                         7月12号,15点23点
    8.mutil

7. You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set.
    > action="/CPM" 应该改成"/CPM/",最后一个/不能少
    
    > 补充  
         路由加上名字name="XXX",然后action="{% url "name" %}" 

8. CSRF验证失败. 请求被中断.
    > 跨域请求

    解决办法: 

    1. setting中django.middleware.csrf.CsrfViewMiddleware 确认存在
    2. html中的form添加模板标签{% csrf_token %}
    ```html
    <form action="." method="post">{% csrf_token %}
    ```


9. (models.E014) ordering' must be a tuple or list (even if you want to order by only one field).
    ordering = (args,)  (和线程传参一样,即使一个元素也得通过元祖传参)

10. model中default=datetime.now时now不能加括号,加了默认时间都会是model创建的时间

11. django自带ADMIN,创建新用户时,密码存储是明文,且明文无法登录
    > 安装xadmin

12. django1.11不支持xadmin后台系统,换成1.10

13. xadmin不支持python3
    1. 安装django-formtools,httplib2
    2. 安装django-reversion, future
    3. git 源码安装xadmin,然后导入项目
    4. 注册 app

14. xadmin 重载 BaseSetting
```python
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)
```
<font color=red>xadmin.sites.AlreadyRegistered: The model UserWidget is already registered</font> 
> users中的adminx中from xadmin 改成    
import xadmin    
from xadmin import views 

15.  xadmin中外键添加搜索功能
```python
list_filter = ['course','name','create_at']
```
![更改前](https://coding.net/u/scrapyy/p/photos/git/raw/master/1.png)
```python
# 双下划线添加要搜索的字段
list_filter = ['course__name','name','create_at']
```
![更改后](https://coding.net/u/scrapyy/p/photos/git/raw/master/2.png)

16. 菜单折叠且显示中文
```python
# 折叠菜单
class GlobalSettings(object):
    site_title = "后台管理系统"
    site_footer = "yy's company"
    menu_style = "accordion"

# 菜单改为中文
# apps里添加verbose_name
# -*- coding: utf-8 -*-
class OperationConfig(AppConfig):
    name = 'operation'
    verbose_name = u"用户操作"
# init里引用config
default_app_config = "operation.apps.OperationConfig"
``` 

17. 登录函数不能取名login,django有一个内置的函数叫login(坑)

18. <font color=red>AttributeError: 'Manager' object has no attribute 'get_by_natural_key'</font>  
     ```python
    from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
     ```
     更正: 不要继承Base,太多东西要重写
      ```python
    from django.contrib.auth.models import AbstractUser,
     ```

19. <font color=red>RuntimeError: Model class browser.models.ClickTask doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.</font>  
    把 INSTALLED_APPS 中 apps.browser 改成 browser (不明白为什么,但是这么改就好了)


20. 表格中的按钮,点击会自动提交表单.
    把name="button" 改成name="submit"

21. form中有table,如何获取table中的值

22. supervisor中自动重启程序要置为false,要不然celery会启动很多个(原因不知道)

23. MEDIA_ROOT = os.path.join(BASE_DIR,'upload').replace('//','/'),MEDIA_ROOT不能和static一样是个列表,会报错,'list' has no attribute 'startwith'




