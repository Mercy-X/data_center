from django.db import models


class Stock(models.Model):
    """
    Stock Model
    :author Mercy
    :date 2019-04-19
    """

    SH = 'SH'
    SZ = 'SZ'
    MARKET_CHOICES = (
        (SH, '上证交易所'),
        (SZ, '深圳交易所'),
    )

    MAIN_BOARD = 0
    SME_BOARD = 1
    SEC_BOARD = 2
    BOARD_CHOICES = (
        (MAIN_BOARD, '主板'),
        (SME_BOARD, '中小板'),
        (SEC_BOARD, '创业板'),
    )

    code = models.CharField(verbose_name='股票代码', max_length=6, primary_key=True)
    market_code = models.CharField(verbose_name='市场代码', max_length=2, choices=MARKET_CHOICES)
    name = models.CharField(verbose_name='名称', max_length=8)
    full_name = models.CharField(verbose_name='全名', max_length=64)
    en_name = models.CharField(verbose_name='英文名称', max_length=128)
    area = models.CharField(verbose_name='地区', max_length=8)
    industry = models.CharField(verbose_name='行业', max_length=8)
    board = models.IntegerField(verbose_name='板块', choices=BOARD_CHOICES)
    list_dt = models.DateField(verbose_name='上市日期')

    class Meta:
        db_table = 'stock'
        ordering = ['code']
        verbose_name = '股票'
        verbose_name_plural = '股票'

    def __str__(self):
        return '{} {} {}'.format(
            self.market_code, self.code, self.name
        )

    @property
    def ts_code(self):
        """
        Create tushare query code
        :return: str
        """
        return '{}.{}'.format(self.code, self.market_code)

    @property
    def query_code(self):
        """
        Create query code
        :return: str
        """
        return '{}{}'.format(self.market_code, self.code)

    @property
    def is_st(self):
        """
        Stock is st
        :return: boolean
        """
        if self.name.find('ST') == -1:
            return False
        else:
            return True

    @property
    def sina_url(self):
        return "http://finance.sina.com.cn/realstock/company/{}/nc.shtml".format(self.query_code.lower())

    # # trade part
    # @property
    # def position(self):
    #     amounts = 0
    #     for trade in self.trades.all():
    #         amounts += trade.amount_for_cal
    #     return amounts
    #
    # @property
    # def earn(self):
    #     money = 0.0
    #     for trade in self.trades.all():
    #         money += trade.real_money_for_cal
    #     return round(money, 2)
    #
    # @property
    # def trade_times(self):
    #     return len(self.trades.all())
    #
    # @property
    # def buy_times(self):
    #     return len(self.trades.filter(direction='B'))
    #
    # @property
    # def sale_times(self):
    #     return len(self.trades.filter(direction='S'))
