import requests
import json
import os
import pandas
import datetime
from pandas.io.json import json_normalize

from pyecharts.charts import Map
from pyecharts import options as opts


url = 'https://gwpre.sina.cn/interface/fymap2020_data.json'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
json_file = 'data_sina.json'
history_xlsx = 'history.xlsx'
province_by_stillnum_xlsx = 'province_by_stillnum.xlsx'
province_by_curerate_xlsx = 'province_by_curerate.xlsx'
city_xlsx = 'city.xlsx'
world_by_stillnum_xlsx = 'world_by_stillnum.xlsx'
province_name = ''
# '陕西' 的 province_ename = 'shanxis'
# province_ename = 'guangdong'
China_province_Map = 'China_province_Map.html'
province_city_Map = 'province_city_Map.html'
world_country_Map = 'world_country_Map.html'
china_total = ''
province_total = ''
world_total = ''
china_pieces = [
    {"min": 1001, "color": "#70161d"},
    {"min": 501, "max": 1000, "color": "#cb2a2f"},
    {"min": 101, "max": 500, "color": "#e55a4e"},
    {"min": 11, "max": 100, "color": "#f59e83"},
    {"min": 1, "max": 10, "color": "#fdebcf"}
]
common_province_pieces = [
    {"min": 101, "color": "#70161d"},
    {"min": 51, "max": 100, "color": "#cb2a2f"},
    {"min": 21, "max": 50, "color": "#e55a4e"},
    {"min": 11, "max": 20, "color": "#f59e83"},
    {"min": 1, "max": 10, "color": "#fdebcf"}
]
serious_province_pieces = [
    {"min": 10001, "color": "#70161d"},
    {"min": 1001, "max": 10000, "color": "#cb2a2f"},
    {"min": 501, "max": 1000, "color": "#e55a4e"},
    {"min": 11, "max": 500, "color": "#f59e83"},
    {"min": 1, "max": 10, "color": "#fdebcf"}
]

# get china_total & province_total as Map's subtitle
def get_CNtotal_PROtotal(data):
    global china_total
    china_total = "确诊:{}  仍存:{}  疑似:{}  治愈:{}  死亡:{}  更新日期:{}".format(data["data"]["gntotal"],
        int(data["data"]["gntotal"])-int(data["data"]["curetotal"])-int(data["data"]["deathtotal"]),
        data["data"]["sustotal"], data["data"]["curetotal"],data["data"]["deathtotal"], data["data"]["times"])

    province_json_data = ""
    for x in data["data"]["list"]:
        if x["name"] == province_name:
            province_json_data = x 
    if len(province_json_data) == 0:
        print('没有这个省：'+province_name+' ,请您仔细检查！！！')
    global province_total
    province_total = "确诊:{}  仍存:{}  疑似:{}  治愈:{}  死亡:{}  更新日期:{}".format(province_json_data["value"],
        int(province_json_data["value"])-int(province_json_data["cureNum"])-int(province_json_data["deathNum"]),
        province_json_data["susNum"], province_json_data["cureNum"],province_json_data["deathNum"], data["data"]["times"])

    world_value = 0
    world_susNum = 0
    world_cureNum = 0
    world_deathNum = 0
    world_stillNum = 0
    for x in data["data"]["worldlist"]:
        world_value += int(x["value"])
        world_susNum += int(x["susNum"])
        world_cureNum += int(x["cureNum"])
        world_deathNum += int(x["deathNum"])
    world_stillNum = world_value - world_cureNum - world_deathNum
    global world_total
    world_total = "确诊:{}  仍存:{}  疑似:{}  治愈:{}  死亡:{}  更新日期:{}".format(world_value,world_stillNum,
        world_susNum,world_cureNum,world_deathNum,data["data"]["times"])
    # print(china_total)
    # print(province_total)

# get data by URL
def get_URL():
    try :
        response = requests.get(url, headers)
        response_data = json.loads(response.text)
        with open(json_file, 'w', encoding='utf-8') as fi:
            json.dump(response_data, fi, indent=2, ensure_ascii=False)
            print('JSON 数据已写入 '+json_file+' 文件')
        get_CNtotal_PROtotal(response_data)
        print('通过 URL 获取数据完成')
        return response_data
    except BaseException as err:
        print('连接失败:',err)

# get data from local JSON or URL
def get_data():
    if os.path.exists(json_file):
        now = datetime.datetime.now()
        update_time = datetime.datetime.fromtimestamp(os.path.getmtime(json_file))
        delta_update_time = now - update_time
        # update once an hour
        delta = datetime.timedelta(seconds=3600)
        # print(now,update_time,delta_update_time,delta)
        if (delta_update_time < delta):
            fi = open(json_file,'r',encoding='utf-8')
            json_data = json.load(fi)
            get_CNtotal_PROtotal(json_data)
            print('通过本地 JSON 文件获取数据完成')
            return json_data
        else:
            return get_URL()
    else:
        return get_URL()

# calculate still ill number & insert into specified column of dataframe 
def insert_stillNum(data,insert_place):
    data['conNum'] = data['conNum'].astype(int)
    data['deathNum'] = data['deathNum'].astype(int)
    data['cureNum'] = data['cureNum'].astype(int)
    data['stillNum'] = data['conNum'] - data['deathNum'] - data['cureNum']
    cols = list(data)
    cols.insert(insert_place,cols.pop(cols.index('stillNum')))
    data = data.loc[:,cols]
    return data

# calculate still ill number & insert into specified column of dataframe 
def insert_stillNum2(data,insert_place):
    data['value'] = data['value'].astype(int)
    data['deathNum'] = data['deathNum'].astype(int)
    data['cureNum'] = data['cureNum'].astype(int)
    data['stillNum'] = data['value'] - data['deathNum'] - data['cureNum']
    cols = list(data)
    cols.insert(insert_place,cols.pop(cols.index('stillNum')))
    data = data.loc[:,cols]
    return data

# calculate cured rate & insert into specified column of dataframe 
def insert_cureRate(data,insert_place):
    data['conNum'] = data['conNum'].astype(int)
    data['cureNum'] = data['cureNum'].astype(int)
    data['cureRate'] = data['cureNum'] / data['conNum']
    cols = list(data)
    cols.insert(insert_place,cols.pop(cols.index('cureRate')))
    data = data.loc[:,cols]
    return data

# insert country ename 
def insert_ename(data,insert_place):
    data['name'] = data['name']
    # print(type(data['name']))
    ename = []
    fi = open('country_ename.json','r',encoding='utf-8')
    json_data = json.load(fi)
    for x in data['name']:
        if x != '钻石公主号' and x != '':
            ename.append(json_data[x])
        else:
            ename.append('')
    data['ename'] = pandas.Series(ename)
    # print(type(data['ename']))
    cols = list(data)
    cols.insert(insert_place,cols.pop(cols.index('ename')))
    data = data.loc[:,cols]
    return data

# draw map function
# lists: including mapName & sillNum 
# out_path: output HTML path 
# title: as page_title, map_title 
# area_total: as subtitle, including total data 
# maptype: country or province 
# area_pieces: user-defined segmentation
def draw_Map(lists,out_path,title,area_total,maptype,area_pieces):
    name = list(lists.keys())
    values = list(lists.values())
    if maptype == 'world':
        click_title = '国家'
    elif maptype=='china':
        click_title = '省份'
    else :
        click_title = '城市'
    
        
    # 链式调用
    echarts_map = (
        Map(init_opts=opts.InitOpts(width="1200px", height="700px", page_title="新型冠状病毒疫情地图_"+title))

        # 在地图中插入数据，使用中国地图，隐藏标记
        .add("仍存", [list(z) for z in zip(name, values)], maptype, is_map_symbol_show=True)

        # 设置坐标属性，True则全国显示省份名，全省显示城市名，全球显示国家名
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False)
        )

        # 设置全局属性
        .set_global_opts(
            # 分段型数据，自定义分段
            visualmap_opts = opts.VisualMapOpts(is_piecewise = True, pieces = area_pieces),
            # 标题
            title_opts = opts.TitleOpts(title = title+"_新型冠状病毒疫情地图", subtitle = area_total, pos_left = "center", pos_top = "10px"),
            # 不显示图例{a}
            legend_opts=opts.LegendOpts(is_show = False),
            # 点击显示具体数据提示框
            tooltip_opts=opts.TooltipOpts(trigger_on="click", formatter=click_title+':{b}<br/>{a}:{c}')
        )
    )
    
    print(area_total)
    echarts_map.render(path=out_path)
    print('绘制 '+title+' 疫情地图完成')


if __name__ == '__main__':

    print('本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：\n爬取的JSON数据，\n疫情历史数据Excel表格，\n全国各个省份疫情Excel表格，\n指定省份各个城市疫情Excel表格，\n全国疫情地图HTML文件，\n指定省份疫情地图HTML文件。\n')
    temp = input('请输入指定省份汉字（不包含‘市’‘省’字）：')
    province_name = temp if temp!= '' else '广东'
    # <class 'dict'>
    test_dic = get_data()

    # 1.History to Excel
    # <class 'list'>
    history_list = test_dic['data']['historylist']
    # <class 'pandas.core.frame.DataFrame'>
    history_data = pandas.json_normalize(history_list)
    # rename columns & insert stillNum column
    history_data.rename(columns={'cn_conNum':'conNum','cn_deathNum':'deathNum','cn_cureNum':'cureNum'},inplace=True)
    history_data = insert_stillNum(history_data,1)
    # 'ascending=False' means descending order, exactlly ascending order based date
    history_data.sort_index(ascending=False, inplace=True)
    # reset index, 'drop=True' means abandoning index before
    history_data.reset_index(drop=True, inplace=True)
    history_data.to_excel(history_xlsx)
    print('写入 '+history_xlsx+' 文件完成')

    # 2.Provinces to Excel
    province_list = test_dic['data']['list']
    province_data = pandas.json_normalize(province_list)
    # delete column 'city' because this column data is very large
    province_data.drop(columns=['city'],inplace=True)
    province_data.rename(columns={'value':'conNum'},inplace=True)
    province_data = insert_stillNum(province_data,2)
    # na_position='first' means sorting NaN in first , 'last'  means in last
    province_data.sort_values(by=['stillNum'],ascending=False,inplace=True,na_position='first')
    province_data.reset_index(drop=True, inplace=True)
    province_data.to_excel(province_by_stillnum_xlsx)
    print('写入 '+province_by_stillnum_xlsx+' 文件完成')   
    # sort by cure rate excel, insert into behind of last column
    province_data = insert_cureRate(province_data,province_data.shape[1])
    province_data.sort_values(by=['cureRate'],ascending=False,inplace=True,na_position='first')
    province_data.reset_index(drop=True, inplace=True)
    province_data.to_excel(province_by_curerate_xlsx)
    print('写入 '+province_by_curerate_xlsx+' 文件完成')   

    # 3.Province's Cities to Excel
    province_list = test_dic['data']['list']
    for item in province_list:
        if item['name'] == province_name:
            city_list = item['city']
            city_data = pandas.json_normalize(city_list)
    city_data = insert_stillNum(city_data,1)
    city_data.sort_values(by=['stillNum'],ascending=False,inplace=True,na_position='first')
    city_data.reset_index(drop=True, inplace=True)
    city_data.to_excel(province_name+'_'+city_xlsx)
    print('写入 '+province_name+'_'+city_xlsx+' 文件完成') 

    # 4.Get provinces dictionary & draw provinces map in China map
    province_distribution = dict(zip(province_data.name,province_data.stillNum))
    print(province_distribution)
    draw_Map(province_distribution,China_province_Map,"中国地区",china_total,'china',china_pieces)

    # 5.Get cities dictionary & draw cities map in province map
    city_distribution = dict(zip(city_data.mapName,city_data.stillNum))
    print(city_distribution)
    province_pieces = common_province_pieces if province_name != '湖北' else serious_province_pieces
    draw_Map(city_distribution,province_name+'_'+province_city_Map,province_name+"地区",province_total,province_name,province_pieces)

    # 6.Countries to Excel
    world_list = test_dic['data']['worldlist']
    world_data = pandas.json_normalize(world_list)
    # delete column 'citycode' because this column data is unnecessary
    world_data.drop(columns=['citycode'],inplace=True)
    # world_data.rename(columns={'value':'conNum'},inplace=True)
    # world_data = insert_stillNum(world_data,1)
    world_data = insert_stillNum2(world_data,1)
    world_data = insert_ename(world_data,1)
    # na_position='first' means sorting NaN in first , 'last'  means in last
    world_data.sort_values(by=['stillNum'],ascending=False,inplace=True,na_position='first')
    world_data.reset_index(drop=True, inplace=True)
    world_data.to_excel(world_by_stillnum_xlsx)
    print('写入 '+world_by_stillnum_xlsx+' 文件完成')  

    # 7.Get Countries dictionary & draw Countries map in World map
    country_distribution = dict(zip(world_data.ename,world_data.stillNum))
    print(country_distribution)
    draw_Map(country_distribution,world_country_Map,"全世界地区",world_total,'world',serious_province_pieces)

# (1)json.dumps()  Python数据类型列表进行json格式的编码（字典 → 字符串）
# (2)json.loads()  json格式数据转换为字典（字符串 → 字典）
# (3)json.dump()   将Python数据写入json文件
# (4)json.load()   将json文件读取为Python数据

# pip install pyecharts
# pip install echarts-countries-pypkg 
# pip install echarts-china-provinces-pypkg 
# pip install echarts-china-cities-pypkg 
# pip install pyecharts_snapshot