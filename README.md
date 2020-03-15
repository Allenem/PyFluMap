# Python 爬取"新型冠状病毒"数据

本程序必须文件： 
- `main.py`, 
- `country_ename.json`

直接运行 `main.py` 文件即可

```bash
python main.py
```

世界地图：https://allenem.github.io/PyFluMap/world_country_Map.html

全国地图：https://allenem.github.io/PyFluMap/China_province_Map.html

湖北地图：https://allenem.github.io/PyFluMap/湖北_province_city_Map.html

广东地图：https://allenem.github.io/PyFluMap/广东_province_city_Map.html

甘肃地图：https://allenem.github.io/PyFluMap/甘肃_province_city_Map.html

---

## 更新日期:截至2月19日17时31分

<details>
<summary>OUTPUT1 甘肃</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：甘肃
JSON 数据已写入 data_sina.json 文件
通过 URL 获取数据完成
写入 history.xlsx 文件完成
写入 province.xlsx 文件完成
写入 甘肃_city.xlsx 文件完成
{'湖北': 50524, '广东': 726, '河南': 678, '浙江': 590, '安徽': 579, '江西': 571, '湖南': 449, '黑龙江': 341, '四川': 325, '江苏': 322, '山东': 316, '重庆': 296, '北京': 244, '福建': 188, '河北': 161, '广西': 156, '上
海': 145, '陕西': 142, '云南': 112, '天津': 77, '海南': 75, '贵州': 75, '山西': 69, '内蒙古': 66, '辽宁': 65, '香港': 56, '新疆': 55, '吉林': 52, '宁夏': 29, '甘肃': 27, '台湾': 20, '澳门': 5, '青海': 2, '西藏': 0}
确诊:74279  疑似:5248  治愈:14387  死亡:2006  更新日期:截至2月19日17时31分
绘制 中国地区 疫情地图完成
{'兰州市': 12, '平凉市': 6, '甘南藏族自治州': 4, '白银市': 3, '天水市': 1, '定西市': 1, '庆阳市': 1, '陇南市': 0, '临夏回族自治州': 0, '张掖市': 0, '金昌市': 0}
确诊:91  疑似:0  治愈:62  死亡:2  更新日期:截至2月19日17时31分
绘制 甘肃地区 疫情地图完成
```
</details>

<details>
<summary>OUTPUT2 湖北</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：湖北
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province.xlsx 文件完成
写入 湖北_city.xlsx 文件完成
{'湖北': 50524, '广东': 726, '河南': 678, '浙江': 590, '安徽': 579, '江西': 571, '湖南': 449, '黑龙江': 341, '四川': 325, '江苏': 322, '山东': 316, '重庆': 296, '北京': 244, '福建': 188, '河北': 161, '广西': 156, '上海': 145, '陕西': 142, '云南': 112, '天津': 77, '海南': 75, '贵州': 75, '山西': 69, '内蒙古
': 66, '辽宁': 65, '香港': 56, '新疆': 55, '吉林': 52, '宁夏': 29, '甘肃': 27, '台湾': 20, '澳门': 5, '青海': 2, '西藏': 0}
确诊:74279  疑似:5248  治愈:14387  死亡:2006  更新日期:截至2月19日17时31分
绘制 中国地区 疫情地图完成
{'武汉市': 37945, '孝感市': 2690, '黄冈市': 1700, '荆州市': 1094, '鄂州市': 1005, '随州市': 1000, '襄阳市': 913, '荆门市': 687, '宜昌市': 674, '黄石市': 674, '咸宁市': 597, '十堰市': 472, '天门市': 402, '仙桃市': 394, '恩施土家族苗族自治州': 150, '潜江市': 139, '神农架林区': 0}
确诊:61682  疑似:0  治愈:9237  死亡:1921  更新日期:截至2月19日17时31分
绘制 湖北地区 疫情地图完成
```
</details>

---

## 更新日期:截至2月22日22时00分

<details>
<summary>OUTPUT3 甘肃</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：甘肃
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 甘肃_city.xlsx 文件完成
{'青海': 0, '西藏': 0, '甘肃': 13, '湖南': 317, '上海': 105, '宁夏': 23, '河北': 100, '河南': 422, '江苏': 230, '海南': 60, '贵州': 54, '云南': 65, '陕西': 95, '安徽': 386, '澳门': 4, '山西': 53, '浙江': 485, '
江西': 378, '吉林': 38, '福建': 130, '重庆': 250, '辽宁': 54, '广东': 606, '天津': 67, '四川': 273, '北京': 217, '黑龙江': 263, '广西': 143, '山东': 444, '新疆': 49, '内蒙古': 52, '湖北': 47514, '香港': 57, '台
湾': 23}
确诊:76396  仍存:52970  疑似:5365  治愈:21078  死亡:2348  更新日期:截至2月22日22时00分
绘制 中国地区 疫情地图完成
{'兰州市': 5, '平凉市': 3, '甘南藏族自治州': 2, '定西市': 1, '白银市': 1, '庆阳市': 1, '天水市': 0, '陇南市': 0, '临夏回族自治州': 0, '张掖市': 0, '金昌市': 0}
确诊:91  仍存:13  疑似:0  治愈:76  死亡:2  更新日期:截至2月22日22时00分
绘制 甘肃地区 疫情地图完成
```
</details>

<details>
<summary>OUTPUT4 湖北</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：湖北
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 湖北_city.xlsx 文件完成
{'青海': 0, '西藏': 0, '甘肃': 13, '湖南': 317, '上海': 105, '宁夏': 23, '河北': 100, '河南': 422, '江苏': 230, '海南': 60, '贵州': 54, '云南': 65, '陕西': 95, '安徽': 386, '澳门': 4, '山西': 53, '浙江': 485, '
江西': 378, '吉林': 38, '福建': 130, '重庆': 250, '辽宁': 54, '广东': 606, '天津': 67, '四川': 273, '北京': 217, '黑龙江': 263, '广西': 143, '山东': 444, '新疆': 49, '内蒙古': 52, '湖北': 47514, '香港': 57, '台
湾': 23}
确诊:76396  仍存:52970  疑似:5365  治愈:21078  死亡:2348  更新日期:截至2月22日22时00分
绘制 中国地区 疫情地图完成
{'武汉市': 36594, '孝感市': 2414, '黄冈市': 1396, '鄂州市': 950, '荆州市': 914, '随州市': 824, '襄阳市': 745, '宜昌市': 612, '荆门市': 581, '黄石市': 536, '咸宁市': 462, '十堰市': 418, '仙桃市': 321, '天门市': 283, '': 218, '恩施土家族苗族自治州': 131, '潜江市': 114, '神农架林区': 1}
确诊:63454  仍存:47514  疑似:0  治愈:13690  死亡:2250  更新日期:截至2月22日22时00分
绘制 湖北地区 疫情地图完成
```
</details>

---

## 更新日期:截至2月29日20时30分

<details>
<summary>OUTPUT5 默认广东</summary>

```bash
>python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：
JSON 数据已写入 data_sina.json 文件
通过 URL 获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 广东_city.xlsx 文件完成
{'青海': 0, '西藏': 0, '宁夏': 4, '河南': 81, '云南': 15, '甘肃': 7, '河北': 31, '安徽': 116, '海南': 16, '江西': 123, '上海': 47, '山西': 20, '陕西': 37, '浙江': 188, '湖南': 170, '江苏': 108, '福建': 53, '新疆': 11, '吉林': 17, '天津': 24, '澳门': 2, '辽宁': 25, '贵州': 32, '重庆': 148, '广东': 366, '广西': 74, '北京': 132, '内蒙 古': 26, '四川': 184, '黑龙江': 166, '山东': 332, '湖北': 34596, '香港': 62, '台湾': 29}
确诊:79394  仍存:37242  疑似:1418  治愈:39314  死亡:2838  更新日期:截至2月29日20时30分
绘制 中国地区 疫情地图完成
{'深圳市': 115, '广州市': 97, '东莞市': 42, '佛山市': 37, '珠海市': 26, '江门市': 10, '中山市': 8, '湛江市': 5, '茂名市': 5, '肇庆市': 5, '梅州市': 4, '惠州市': 4, '汕头市': 3, '阳江市': 3, '揭阳市': 2, '韶关市': 1, '清远市': 0, '汕尾市': 0, '潮州市': 0, '河源市': 0}
确诊:1349  仍存:366  疑似:0  治愈:976  死亡:7  更新日期:截至2月29日20时30分
绘制 广东地区 疫情地图完成
写入 world_by_stillnum.xlsx 文件完成
{'China': 37242, 'South Korea': 3105, 'Italy': 930, 'Japan': 892, 'Iran': 427, 'United States': 62, 'Germany': 52, 'Kuwait': 45, 'France': 43, 'Singapore': 40, 'Spain': 39, 'Bahrain': 38, 'Australia': 20, 'United Arab Emirates': 16, 'Switzerland': 15, 'Thailand': 14, 'Sweden': 12, 'Canada': 12, 'Britain': 12, 'Malaysia': 10, 'Israel': 8, 'Iraq': 8, 'Norway': 7, 'Croatia': 5, 'Austria': 5, 'Oman': 5, 'Afghanistan': 4, 'Greece': 4, 'Lebanon': 3, 'Denmark': 3, 'Romania': 3, 'Mexico': 3, 'Georgia': 2, 'Finland': 2, 'Holand': 2, 'Pakistan': 2, 'North Macedonia': 1, 'Estonia': 1, 'Nigeria': 1, 'Lithuania': 1, 'New Zealand': 1, 'Belarus': 1, 'San Marino': 1, 'Sri Lanka': 1, 'Algeria': 1, 'Nepal': 1, 'Qatar': 1, 'Philippines': 1, 'Iceland': 1, 'Azerbaijan': 1, 'Brazil': 1, 'Monaco': 1, 'Egypt': 0, 'Cambodia': 0, 'Belgium': 0, 'Russia': 0, 'India': 0, 'Vietnam': 0}
确诊:85770  仍存:43108  疑似:1435  治愈:39729  死亡:2933  更新日期:截至2月29日20时30分
绘制 全世界地区 疫情地图完成
```
</details>

<details>
<summary>OUTPUT6 甘肃</summary>

```bash
>python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：甘肃
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 甘肃_city.xlsx 文件完成
{'青海': 0, '西藏': 0, '宁夏': 4, '河南': 81, '云南': 15, '甘肃': 7, '河北': 31, '安徽': 116, '海南': 16, '江西': 123, '上海': 47, '山西': 20, '陕西': 37, '浙江': 188, '湖南': 170, '江苏': 108, '福建': 53, '新疆': 11, '吉林': 17, '天津': 24, '澳门': 2, '辽宁': 25, '贵州': 32, '重庆': 148, '广东': 366, '广西': 74, '北京': 132, '内蒙 古': 26, '四川': 184, '黑龙江': 166, '山东': 332, '湖北': 34596, '香港': 62, '台湾': 29}
确诊:79394  仍存:37242  疑似:1418  治愈:39314  死亡:2838  更新日期:截至2月29日20时30分
绘制 中国地区 疫情地图完成
{'平凉市': 3, '兰州市': 2, '定西市': 1, '庆阳市': 1, '天水市': 0, '甘南藏族自治州': 0, '白银市': 0, '陇南市': 0, '临夏回族自治州': 0, '张掖市': 0, '金昌市': 0}
确诊:91  仍存:7  疑似:0  治愈:82  死亡:2  更新日期:截至2月29日20时30分
绘制 甘肃地区 疫情地图完成
写入 world_by_stillnum.xlsx 文件完成
{'China': 37242, 'South Korea': 3105, 'Italy': 930, 'Japan': 892, 'Iran': 427, 'United States': 62, 'Germany': 52, 'Kuwait': 45, 'France': 43, 'Singapore': 40, 'Spain': 39, 'Bahrain': 38, 'Australia': 20, 'United Arab Emirates': 16, 'Switzerland': 15, 'Thailand': 14, 'Sweden': 12, 'Canada': 12, 'Britain': 12, 'Malaysia': 10, 'Israel': 8, 'Iraq': 8, 'Norway': 7, 'Croatia': 5, 'Austria': 5, 'Oman': 5, 'Afghanistan': 4, 'Greece': 4, 'Lebanon': 3, 'Denmark': 3, 'Romania': 3, 'Mexico': 3, 'Georgia': 2, 'Finland': 2, 'Holand': 2, 'Pakistan': 2, 'North Macedonia': 1, 'Estonia': 1, 'Nigeria': 1, 'Lithuania': 1, 'New Zealand': 1, 'Belarus': 1, 'San Marino': 1, 'Sri Lanka': 1, 'Algeria': 1, 'Nepal': 1, 'Qatar': 1, 'Philippines': 1, 'Iceland': 1, 'Azerbaijan': 1, 'Brazil': 1, 'Monaco': 1, 'Egypt': 0, 'Cambodia': 0, 'Belgium': 0, 'Russia': 0, 'India': 0, 'Vietnam': 0}
确诊:85770  仍存:43108  疑似:1435  治愈:39729  死亡:2933  更新日期:截至2月29日20时30分
绘制 全世界地区 疫情地图完成
```
</details>

<details>
<summary>OUTPUT7 湖北</summary>

```bash
>python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：湖北
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 湖北_city.xlsx 文件完成
{'青海': 0, '西藏': 0, '宁夏': 4, '河南': 81, '云南': 15, '甘肃': 7, '河北': 31, '安徽': 116, '海南': 16, '江西': 123, '上海': 47, '山西': 20, '陕西': 37, '浙江': 188, '湖南': 170, '江苏': 108, '福建': 53, '新疆': 11, '吉林': 17, '天津': 24, '澳门': 2, '辽宁': 25, '贵州': 32, '重庆': 148, '广东': 366, '广西': 74, '北京': 132, '内蒙 古': 26, '四川': 184, '黑龙江': 166, '山东': 332, '湖北': 34596, '香港': 62, '台湾': 29}
确诊:79394  仍存:37242  疑似:1418  治愈:39314  死亡:2838  更新日期:截至2月29日20时30分
绘制 中国地区 疫情地图完成
{'武汉市': 28731, '孝感市': 1356, '黄冈市': 670, '鄂州市': 599, '荆州市': 568, '随州市': 470, '宜昌市': 437, '襄阳市': 340, '荆门市': 324, '黄石市': 291, '十堰市': 243, '咸宁市': 148, '仙桃市': 148, '天门市': 121, '潜江市': 82, '恩施土家族苗族自治州': 67, '神农架林区': 1}
确诊:66337  仍存:34596  疑似:0  治愈:29014  死亡:2727  更新日期:截至2月29日20时30分
绘制 湖北地区 疫情地图完成
写入 world_by_stillnum.xlsx 文件完成
{'China': 37242, 'South Korea': 3105, 'Italy': 930, 'Japan': 892, 'Iran': 427, 'United States': 62, 'Germany': 52, 'Kuwait': 45, 'France': 43, 'Singapore': 40, 'Spain': 39, 'Bahrain': 38, 'Australia': 20, 'United Arab Emirates': 16, 'Switzerland': 15, 'Thailand': 14, 'Sweden': 12, 'Canada': 12, 'Britain': 12, 'Malaysia': 10, 'Israel': 8, 'Iraq': 8, 'Norway': 7, 'Croatia': 5, 'Austria': 5, 'Oman': 5, 'Afghanistan': 4, 'Greece': 4, 'Lebanon': 3, 'Denmark': 3, 'Romania': 3, 'Mexico': 3, 'Georgia': 2, 'Finland': 2, 'Holand': 2, 'Pakistan': 2, 'North Macedonia': 1, 'Estonia': 1, 'Nigeria': 1, 'Lithuania': 1, 'New Zealand': 1, 'Belarus': 1, 'San Marino': 1, 'Sri Lanka': 1, 'Algeria': 1, 'Nepal': 1, 'Qatar': 1, 'Philippines': 1, 'Iceland': 1, 'Azerbaijan': 1, 'Brazil': 1, 'Monaco': 1, 'Egypt': 0, 'Cambodia': 0, 'Belgium': 0, 'Russia': 0, 'India': 0, 'Vietnam': 0}
确诊:85770  仍存:43108  疑似:1435  治愈:39729  死亡:2933  更新日期:截至2月29日20时30分
绘制 全世界地区 疫情地图完成
```
</details>

---

## 更新日期:截至3月15日13时30分

<details open>
<summary>OUTPUT8 默认广东</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：
JSON 数据已写入 data_sina.json 文件
通过 URL 获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 广东_city.xlsx 文件完成
{'山西': 0, '江苏': 0, '西藏': 0, '青海': 0, '澳门': 0, '江西': 0, '福建': 0, '湖南': 0, '安徽': 0, '重庆': 0, '云南': 0, '浙江': 19, '河南': 1, '贵州': 1, '吉林': 1, '山东': 12, '河北': 2, '宁夏': 2, '天津': 1, '广西': 7, '新疆': 0, '广东': 46, '四川': 21, '海南': 2, '陕西': 11, '内蒙古': 3, '黑龙江': 16, '上海': 26, '辽宁': 10, '湖北': 10431, '北京': 81, '甘肃': 39, '香港': 56, '台湾': 32}
确诊:81048  仍存:10820  疑似:113  治愈:67024  死亡:3204  更新日期:截至3月15日13时30分
绘制 中国地区 疫情地图完成
{'深圳市': 19, '广州市': 16, '佛山市': 4, '中山市': 4, '东莞市': 2, '汕头市': 1, '阳江市': 0, '潮州市': 0, '汕尾市': 0, '揭阳市': 0, '韶关市': 0, '清远市': 0, '肇庆市': 0, '茂名市': 0, '梅州市': 0, '湛
江市': 0, '江门市': 0, '惠州市': 0, '珠海市': 0, '河源市': 0}
确诊:1357  仍存:46  疑似:1  治愈:1303  死亡:8  更新日期:截至3月15日13时30分
绘制 广东地区 疫情地图完成
写入 world_by_stillnum.xlsx 文件完成
{'Italy': 17750, 'China': 10820, 'Iran': 7779, 'Korea': 7253, 'Spain': 5627, 'Germany': 4530, 'France': 4373, 'United States': 2754, 'Switzerland': 1175, 'Britain': 1101, 'Norway': 1043, 'Sweden': 959,
'Holand': 947, 'Denmark': 827, 'Belgium': 684, 'Austria': 652, 'Japan': 630, '': 509, 'Qatar': 334, 'Canada': 245, 'Greece': 225, 'Finland': 223, 'Australia': 209, 'Malaysia': 203, 'Israel': 194, 'Czech': 189, 'Slovenia': 181, 'Iceland': 156, 'Bahrain': 151, 'Brazil': 151, 'Ireland': 127, 'Singapore': 115, 'Portugal': 112, 'Estonia': 109, 'Saudi Arabia': 103, 'Poland': 101, 'Philippines': 101, 'Romania': 95, 'Kuwait': 95, 'Indonesia': 94, 'Lebanon': 89, 'Egypt': 87, 'India': 81, 'Iraq': 75, 'San Marino': 66, 'United Arab Emirates': 62, 'Chile': 61, 'Russia': 51, 'Luxemburg': 50, 'Serbia': 46, 'Thailand': 46, 'Slovakia': 44, 'Argentina': 42, 'Panama': 42, 'Mexico': 40, 'Brunei Darussalam': 40, 'Vietnam': 37, 'Albania': 37, 'Croatia': 37, 'South Africa': 37, 'Palestine': 35, 'Bulgaria': 34, 'Georgia': 30, 'Hungary': 29, 'Pakistan': 29, 'Peru': 28, 'Latvia': 26, 'Belarus': 24, 'Algeria': 24, 'Ecuador': 22, 'Colombia': 22, 'Cyprus': 21, 'Bosnia': 21, 'Senegal': 20, 'Armenia': 20, 'Oman': 18, 'Malta': 18, 'Tunis': 16, 'Morocco': 14, 'Costa Rica': 13, 'North Macedonia': 13, 'Moldova': 12, 'Azerbaijan': 12, 'Venezuela': 10, 'Bolivia': 10, 'Maldives': 10, 'Afghanistan': 10, 'Sri Lanka': 10, 'Lithuania': 8, 'New Zealand': 8, 'Kazakhstan': 6, 'Cambodia': 6, 'Uruguay': 6, 'Turkey': 6, 'Paraguay': 6, 'Dominican': 5, 'Cuba': 4, 'Ukraine': 3, 'Puerto Rico': 3, 'Monaco': 3, 'Cameroon': 3, 'Bengal': 3, 'Nigeria': 2, 'Democratic Republic of Congo': 2, 'Ghana': 2, 'Honduras': 2, 'Seychelles': 2, 'Burkina Faso': 2, 'Guinea': 1, 'Antiguaand Barbuda': 1, 'Republic of Congo': 1, 'Suriname': 1, 'Mauritania': 1,
'Equatorial Guinea': 1, 'Guatemala': 1, 'Swaziland': 1, 'Rwanda': 1, 'Namibia': 1, 'Andorra': 1, 'Ethiopia': 1, 'Kenya': 1, 'Trinidadand Tobago': 1, 'Gabon': 1, 'Jamaica': 1, 'Mongolia': 1, 'Principality of Liechtenstein': 1, 'Togo': 1, 'Coted Ivoire': 1, 'Vatican': 1, 'Bhutan': 1, 'Nepal': 1, 'Jordan': 1, 'Central African Republic': 1, 'Sudan': 0, 'Guyana': 0}
确诊:156067  仍存:74654  疑似:308  治愈:75584  死亡:5829  更新日期:截至3月15日13时30分
绘制 全世界地区 疫情地图完成
```
</details>

<details open>
<summary>OUTPUT9 甘肃</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：甘肃
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 甘肃_city.xlsx 文件完成
{'山西': 0, '江苏': 0, '西藏': 0, '青海': 0, '澳门': 0, '江西': 0, '福建': 0, '湖南': 0, '安徽': 0, '重庆': 0, '云南': 0, '浙江': 19, '河南': 1, '贵州': 1, '吉林': 1, '山东': 12, '河北': 2, '宁夏': 2, '天津': 1, '广西': 7, '新疆': 0, '广东': 46, '四川': 21, '海南': 2, '陕西': 11, '内蒙古': 3, '黑龙江': 16, '上海': 26, '辽宁': 10, '湖北': 10431, '北京': 81, '甘肃': 39, '香港': 56, '台湾': 32}
确诊:81048  仍存:10820  疑似:113  治愈:67024  死亡:3204  更新日期:截至3月15日13时30分
绘制 中国地区 疫情地图完成
{'': 39, '兰州市': 0, '天水市': 0, '定西市': 0, '平凉市': 0, '甘南藏族自治州': 0, '白银市': 0, '陇南市': 0, '庆阳市': 0, '临夏回族自治州': 0, '张掖市': 0, '金昌市': 0}
确诊:132  仍存:39  疑似:0  治愈:91  死亡:2  更新日期:截至3月15日13时30分
绘制 甘肃地区 疫情地图完成
写入 world_by_stillnum.xlsx 文件完成
{'Italy': 17750, 'China': 10820, 'Iran': 7779, 'Korea': 7253, 'Spain': 5627, 'Germany': 4530, 'France': 4373, 'United States': 2754, 'Switzerland': 1175, 'Britain': 1101, 'Norway': 1043, 'Sweden': 959,
'Holand': 947, 'Denmark': 827, 'Belgium': 684, 'Austria': 652, 'Japan': 630, '': 509, 'Qatar': 334, 'Canada': 245, 'Greece': 225, 'Finland': 223, 'Australia': 209, 'Malaysia': 203, 'Israel': 194, 'Czech': 189, 'Slovenia': 181, 'Iceland': 156, 'Bahrain': 151, 'Brazil': 151, 'Ireland': 127, 'Singapore': 115, 'Portugal': 112, 'Estonia': 109, 'Saudi Arabia': 103, 'Poland': 101, 'Philippines': 101, 'Romania': 95, 'Kuwait': 95, 'Indonesia': 94, 'Lebanon': 89, 'Egypt': 87, 'India': 81, 'Iraq': 75, 'San Marino': 66, 'United Arab Emirates': 62, 'Chile': 61, 'Russia': 51, 'Luxemburg': 50, 'Serbia': 46, 'Thailand': 46, 'Slovakia': 44, 'Argentina': 42, 'Panama': 42, 'Mexico': 40, 'Brunei Darussalam': 40, 'Vietnam': 37, 'Albania': 37, 'Croatia': 37, 'South Africa': 37, 'Palestine': 35, 'Bulgaria': 34, 'Georgia': 30, 'Hungary': 29, 'Pakistan': 29, 'Peru': 28, 'Latvia': 26, 'Belarus': 24, 'Algeria': 24, 'Ecuador': 22, 'Colombia': 22, 'Cyprus': 21, 'Bosnia': 21, 'Senegal': 20, 'Armenia': 20, 'Oman': 18, 'Malta': 18, 'Tunis': 16, 'Morocco': 14, 'Costa Rica': 13, 'North Macedonia': 13, 'Moldova': 12, 'Azerbaijan': 12, 'Venezuela': 10, 'Bolivia': 10, 'Maldives': 10, 'Afghanistan': 10, 'Sri Lanka': 10, 'Lithuania': 8, 'New Zealand': 8, 'Kazakhstan': 6, 'Cambodia': 6, 'Uruguay': 6, 'Turkey': 6, 'Paraguay': 6, 'Dominican': 5, 'Cuba': 4, 'Ukraine': 3, 'Puerto Rico': 3, 'Monaco': 3, 'Cameroon': 3, 'Bengal': 3, 'Nigeria': 2, 'Dem. Rep. Congo': 2, 'Ghana': 2, 'Honduras': 2, 'Seychelles': 2, 'Burkina Faso': 2, 'Guinea': 1, 'Antiguaand Barbuda': 1, 'Rep. Congo': 1, 'Suriname': 1, 'Mauritania': 1, 'Equatorial Guinea': 1, 'Guatemala': 1, 'Swaziland': 1, 'Rwanda': 1, 'Namibia': 1, 'Andorra': 1, 'Ethiopia': 1, 'Kenya': 1, 'Trinidadand Tobago': 1, 'Gabon': 1, 'Jamaica': 1, 'Mongolia': 1, 'Principality of Liechtenstein': 1, 'Togo': 1, 'Coted Ivoire': 1, 'Vatican': 1, 'Bhutan': 1, 'Nepal': 1, 'Jordan': 1, 'Central African Republic': 1, 'Sudan': 0, 'Guyana': 0}
确诊:156067  仍存:74654  疑似:308  治愈:75584  死亡:5829  更新日期:截至3月15日13时30分
绘制 全世界地区 疫情地图完成
```
</details>

<details open>
<summary>OUTPUT10 湖北</summary>

```bash
> python main.py
本程序将会爬取最新的新浪新型冠状病毒疫情数据。输出：
爬取的JSON数据，
疫情历史数据Excel表格，
全国各个省份疫情Excel表格，
指定省份各个城市疫情Excel表格，
全国疫情地图HTML文件，
指定省份疫情地图HTML文件。

请输入指定省份汉字（不包含‘市’‘省’字）：湖北
通过本地 JSON 文件获取数据完成
写入 history.xlsx 文件完成
写入 province_by_stillnum.xlsx 文件完成
写入 province_by_curerate.xlsx 文件完成
写入 湖北_city.xlsx 文件完成
{'山西': 0, '江苏': 0, '西藏': 0, '青海': 0, '澳门': 0, '江西': 0, '福建': 0, '湖南': 0, '安徽': 0, '重庆': 0, '云南': 0, '浙江': 19, '河南': 1, '贵州': 1, '吉林': 1, '山东': 12, '河北': 2, '宁夏': 2, '天津': 1, '广西': 7, '新疆': 0, '广东': 46, '四川': 21, '海南': 2, '陕西': 11, '内蒙古': 3, '黑龙江': 16, '上海': 26, '辽宁': 10, '湖北': 10431, '北京': 81, '甘肃': 39, '香港': 56, '台湾': 32}
确诊:81048  仍存:10820  疑似:113  治愈:67024  死亡:3204  更新日期:截至3月15日13时30分
绘制 中国地区 疫情地图完成
{'武汉市': 9911, '孝感市': 139, '鄂州市': 65, '随州市': 49, '荆州市': 47, '黄冈市': 44, '十堰市': 34, '宜昌市': 31, '黄石市': 29, '仙桃市': 27, '荆门市': 25, '襄阳市': 12, '潜江市': 7, '恩施土家族苗族自
治州': 4, '天门市': 4, '咸宁市': 3, '神农架林区': 0}
确诊:67794  仍存:10431  疑似:0  治愈:54278  死亡:3085  更新日期:截至3月15日13时30分
绘制 湖北地区 疫情地图完成
写入 world_by_stillnum.xlsx 文件完成
{'Italy': 17750, 'China': 10820, 'Iran': 7779, 'Korea': 7253, 'Spain': 5627, 'Germany': 4530, 'France': 4373, 'United States': 2754, 'Switzerland': 1175, 'Britain': 1101, 'Norway': 1043, 'Sweden': 959,
'Holand': 947, 'Denmark': 827, 'Belgium': 684, 'Austria': 652, 'Japan': 630, '': 509, 'Qatar': 334, 'Canada': 245, 'Greece': 225, 'Finland': 223, 'Australia': 209, 'Malaysia': 203, 'Israel': 194, 'Czech': 189, 'Slovenia': 181, 'Iceland': 156, 'Bahrain': 151, 'Brazil': 151, 'Ireland': 127, 'Singapore': 115, 'Portugal': 112, 'Estonia': 109, 'Saudi Arabia': 103, 'Poland': 101, 'Philippines': 101, 'Romania': 95, 'Kuwait': 95, 'Indonesia': 94, 'Lebanon': 89, 'Egypt': 87, 'India': 81, 'Iraq': 75, 'San Marino': 66, 'United Arab Emirates': 62, 'Chile': 61, 'Russia': 51, 'Luxemburg': 50, 'Serbia': 46, 'Thailand': 46, 'Slovakia': 44, 'Argentina': 42, 'Panama': 42, 'Mexico': 40, 'Brunei Darussalam': 40, 'Vietnam': 37, 'Albania': 37, 'Croatia': 37, 'South Africa': 37, 'Palestine': 35, 'Bulgaria': 34, 'Georgia': 30, 'Hungary': 29, 'Pakistan': 29, 'Peru': 28, 'Latvia': 26, 'Belarus': 24, 'Algeria': 24, 'Ecuador': 22, 'Colombia': 22, 'Cyprus': 21, 'Bosnia': 21, 'Senegal': 20, 'Armenia': 20, 'Oman': 18, 'Malta': 18, 'Tunis': 16, 'Morocco': 14, 'Costa Rica': 13, 'North Macedonia': 13, 'Moldova': 12, 'Azerbaijan': 12, 'Venezuela': 10, 'Bolivia': 10, 'Maldives': 10, 'Afghanistan': 10, 'Sri Lanka': 10, 'Lithuania': 8, 'New Zealand': 8, 'Kazakhstan': 6, 'Cambodia': 6, 'Uruguay': 6, 'Turkey': 6, 'Paraguay': 6, 'Dominican': 5, 'Cuba': 4, 'Ukraine': 3, 'Puerto Rico': 3, 'Monaco': 3, 'Cameroon': 3, 'Bengal': 3, 'Nigeria': 2, 'Dem. Rep. Congo': 2, 'Ghana': 2, 'Honduras': 2, 'Seychelles': 2, 'Burkina Faso': 2, 'Guinea': 1, 'Antiguaand Barbuda': 1, 'Rep. Congo': 1, 'Suriname': 1, 'Mauritania': 1, 'Equatorial Guinea': 1, 'Guatemala': 1, 'Swaziland': 1, 'Rwanda': 1, 'Namibia': 1, 'Andorra': 1, 'Ethiopia': 1, 'Kenya': 1, 'Trinidadand Tobago': 1, 'Gabon': 1, 'Jamaica': 1, 'Mongolia': 1, 'Principality of Liechtenstein': 1, 'Togo': 1, 'Coted Ivoire': 1, 'Vatican': 1, 'Bhutan': 1, 'Nepal': 1, 'Jordan': 1, 'Central African Republic': 1, 'Sudan': 0, 'Guyana': 0}
确诊:156067  仍存:74654  疑似:308  治愈:75584  死亡:5829  更新日期:截至3月15日13时30分
绘制 全世界地区 疫情地图完成
```
</details>