"""
自定义分页组件
"""
from django.utils.safestring import mark_safe


class Pagination(object):


    def __init__(self,request,queryset,page_size=10,page_param='page',plus=2):
        '''

        @param request: 请求
        @param queryset: 后端数据
        @param page_size: 每页数据量
        @param page_param: 前后端传递页码的name
        @param plus: 当前页前后的间隔页
        # 在views中输入
        page_obj = Pagination(request,queryset)
        context = {
            'queryset':page_obj.page_queryset, #分完页的数据
            'page_string':page_obj.html() #生成页码信息

        }
        return render(request,'xxxx.html',context)

        使用时候在html中加入
                <ul class="pagination">
            {{ page_string }}
            <li>
                <form method="get" style="float: left;margin-left: -1px">
                    <div class="input-group" style="width: 200px">
                        <input type="text" class="form-control" placeholder="页码" name="page">
                        <span class="input-group-btn">
                <button class="btn btn-default" type="submit">跳转</button>
            </span>
                    </div>
                </form>
            </li>
        </ul>
        '''
        page = request.GET.get(page_param,'1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        # 总页码计算
        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)  # div是余数
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 显示的起始页和最终页 由于每次只显示 当前页的前2页和后2页
        start_page = self.page - self.plus if self.page - self.plus > 0 else 1
        end_page = self.page + self.plus if self.page + self.plus <= self.total_page_count else self.total_page_count

        # 拼接成html返回前端
        page_str_list = []  # 页码
        # 首页
        page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))
        # 上一页
        pre_page = '<li><a href="?page={}">上一页</a></li>'.format(self.page - 1) if self.page > 1 else ''
        page_str_list.append(pre_page)
        # 页码
        for i in range(start_page, end_page + 1):
            if i == self.page:  # 当前页高亮
                ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        # 下一页实现
        pre_page = '<li><a href="?page={}">下一页</a></li>'.format(self.page + 1) if self.page < self.total_page_count else ''
        page_str_list.append(pre_page)
        # 尾页
        page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(self.total_page_count))
        page_string = mark_safe(''.join(page_str_list))  # 组成字符串注意要加mark_safe前端才能通过
        return page_string
