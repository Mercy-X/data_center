import time
import datetime

from django.conf import settings
from django.http import JsonResponse
from .models import Stock

import tushare as ts

from utils.ding import send_markdown

MSG_TITLE = '数据中心'  # 消息标题
AT = ['18812347890', ]  # 特殊消息需要@的列表


def update_stock_data(request):
    """
    借由tushare更新股票基础数据，ST信息等。
    :date 2019-03-30
    :version 1.0
    :param request: /stock/update_stock_data/
    :return:JsonResponse
    """

    send_markdown(MSG_TITLE, '## {} Message - Start \n#### {} 更新股票基础数据。。。'.format(
        settings.MY_NAME, datetime.datetime.now().strftime('%m-%d %H:%M:%S')))
    try:
        df = ts.get_stock_basics()
    except:
        time.sleep(1 * 60 * 30)
        try:
            df = ts.get_stock_basics()
        except:
            send_markdown(
                MSG_TITLE,
                '## {} Message - ERROR \n#### {} 更新股票基础数据失败！ {}\n 获取TS数据失败'.format(
                    settings.MY_NAME, datetime.datetime.now().strftime('%m-%d %H:%M:%S'), '@' + ' @'.join(AT)),
                at=AT)
            return JsonResponse({
                'result': False
            })
    try:
        rdf = df.reset_index()
        stocks = Stock.objects.all()
        msg = ""
        update_count = 0
        for stock in stocks:
            rows = rdf[rdf.code == stock.code]
            if len(rows) == 1:
                if stock.name != rows.name.values[0].strip().replace(' ', '').replace('Ａ', 'A'):
                    msg += '  * {} {} -> {}\n'.format(stock.code, stock.name, rows.name.values[0])
                    stock.name = rows.name.values[0]
                    stock.save()
                    update_count += 1

        report = '## {} Message - Report \n#### {} 更新股票基础数据 完成！\n {}  \n'.format(
            settings.MY_NAME,
            datetime.datetime.now().strftime('%m-%d %H:%M:%S'),
            "今日无变化。" if update_count == 0 else "更新{}条记录。".format(update_count)
        )
        send_markdown(MSG_TITLE, report + msg)
        return JsonResponse({
            'result': True,
            'update_count': update_count
        })
    except:
        send_markdown(MSG_TITLE,
                      '## {} Message - ERROR \n#### {} 更新股票基础数据失败！ {}\n 更新过程出错'.format(
                          settings.MY_NAME, datetime.datetime.now().strftime('%m-%d %H:%M:%S'), '@' + ' @'.join(AT)),
                      at=AT)
        return JsonResponse({
            'result': False,
            'update_count': 0
        })
