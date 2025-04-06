from django.shortcuts import render
from django.http import JsonResponse
def chart_list(request):
    ''' 数据统计'''
    return render(request,'chart_list.html')

def chart_bar(request):
    ''' 柱状图数据传输'''
    legend = ['总数量','本周数量']

    data_list = [
                    {
                        "name": '总数量',
                        "type": 'bar',
                        "data": [50, 210, 306, 150, 105, 220]
                    },
                    {
                        "name": '本周数量',
                        "type": 'bar',
                        "data": [5, 20, 36, 10, 10, 20]
                    },
                ]
    data = ['计算机科学学院', '机械学院', '外国语学院', '人文与新媒体学院', '经济管理学院', '教体学院']

    result = {
        'status':True,
        'data':{
            'legend':legend,
            'series_list':data_list,
            'x_axis':data
        }
    }
    return JsonResponse(result)

def chart_pie(request):
    ''' 构造饼图数据'''

    result = {
        'status': True,
        'data':[
            {'value': 648, 'name': '计算机科学学院'},
            {'value': 755, 'name': '外国语学院'},
            {'value': 680, 'name': '机械学院'},
            {'value': 484, 'name': '人文与新媒体学院'},
            {'value': 500, 'name': '经济管理学院'}
        ]
    }
    return JsonResponse(result)

def chart_line(request):
    legend = ['计算机科学学院', '外国语学院', '人文与新媒体学院', '机械学院', '经济管理学院']
    series_list = [
                    {
                        'name': '计算机科学学院',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [120, 132, 101, 134, 90, 230, 210]
                    },
                    {
                        'name': '外国语学院',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [220, 182, 191, 234, 290, 330, 310]
                    },
                    {
                        'name': '人文与新媒体学院',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [150, 232, 201, 154, 190, 330, 410]
                    },
                    {
                        'name': '机械学院',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [320, 332, 301, 334, 390, 330, 320]
                    },
                    {
                        'name': '经济管理学院',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [820, 932, 901, 934, 1290, 1330, 1320]
                    }
                ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月', '7月']
    result = {
        'status':True,
        'data':{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis
        }
    }
    return JsonResponse(result)