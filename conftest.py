import pytest
from python_code.calc import Calculator
# 加载yaml测试数据
import yaml

with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']['datas']
    add_ids = datas['add']['myid']
    sub_data = datas['sub']['datas']
    sub_ids = datas['sub']['myid']
    mul_data = datas['mul']['datas']
    mul_ids = datas['mul']['myid']
    div_data = datas['div']['datas']
    div_ids = datas['div']['myid']

# 使用fixture方法对计算器进行实例化
@pytest.fixture(scope='module')
def get_calc():
    print('开始计算') # 实现执行用例前打印：开始计算
    calc = Calculator()
    yield calc
    print('结束计算') # 实现执行用例后打印：结束计算

# 加载yaml文件中的测试数据
import yaml

with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)
    add_data = datas['add']['datas']
    add_ids = datas['add']['myid']
    sub_data = datas['sub']['datas']
    sub_ids = datas['sub']['myid']
    mul_data = datas['mul']['datas']
    mul_ids = datas['mul']['myid']
    div_data = datas['div']['datas']
    div_ids = datas['div']['myid']

# 对加减乘除进行数据参数化，并返回
@pytest.fixture(params=add_data, ids=add_ids)
def get_add(request): # 对加法参数化
    data = request.param
    return data

@pytest.fixture(params=sub_data, ids=sub_ids)
def get_sub(request): # 对减法进行参数化
    data = request.param
    return data

@pytest.fixture(params=mul_data, ids=mul_ids)
def get_mul(request): # 对乘法进行参数化
    data = request.param
    return data

@pytest.fixture(params=div_data, ids=div_ids)
def get_div(request): # 对减法进行参数化
    data = request.param
    return data