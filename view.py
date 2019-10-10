from django.http import HttpResponse
from booktest.models import BookInfo # 导入图书模型类
from django.template import loader,RequestContext

def my_render(request, template_path, context_dict={}):
    '''使用模板文件'''
    # 使用模板文件
    # 1.加载模板文件, 模板对象
    temp = loader.get_template(template_path)
    # 2.定义模板上下文:给模板文件传递数据
    context = RequestContext(request, context_dict)
    # 3.模板渲染:产生标准的html内容
    res_html = temp.render(context)
    # 4.返回给浏览器
    return HttpResponse(res_html)
