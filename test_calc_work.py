# 定义测试类
import allure
import pytest
@allure.feature('测试计算器')
class TestCalc:
    @allure.story('测试加法')
    @pytest.mark.run(order=1)   #设置用例执行顺序，为第一个执行
    def test_add(self, get_calc, get_add):
        # 调用add方法
        with allure.step('计算两个数的加和'):
            result = get_calc.add(get_add[0],get_add[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言，如果结果相等，则测试用例通过，结果不相等，测试不通过
        assert result == get_add[2]

    @allure.story('测试除法')
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div):
        # 调用div方法
        with allure.step('计算两个数的除商'):
            result = get_calc.div(get_div[0], get_div[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言，如果结果相等，则测试用例通过，结果不相等，测试不通过
        assert result == get_div[2]

    @allure.story('测试减法')
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub):
        # 调用sub方法
        with allure.step('计算两个数的之差'):
            result = get_calc.sub(get_sub[0], get_sub[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言，如果结果相等，则测试用例通过，结果不相等，测试不通过
        assert result == get_sub[2]

    @allure.story('测试乘法')
    @pytest.mark.run(order=3)  #设置运行顺序为第三个执行
    def test_mul(self, get_calc, get_mul):
        # 调用mul方法
        with allure.step('计算两个数的之积'):
            result = get_calc.mul(get_mul[0], get_mul[1])
        # 判断如果结果为浮点数，保留两位小数
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果后，设置断言，如果结果相等，则测试用例通过，结果不相等，测试不通过
        assert result == get_mul[2]