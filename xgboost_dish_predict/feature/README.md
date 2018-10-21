1. feature_catogroy.py 是量化菜品内部特征的脚本，主要有菜品名称、菜品类别等，将汉字数值化，最后生成的文件为 	   catogroy_num.csv。
2. feature_day_of_week.py 是生成星期的特征脚本，最后生成的文件为 day_of_week.csv。
3. feature_date_to_str.py 是日期转换为时间字符串脚本，最后生成的文件为 feature_date_to_str.csv。
4. feature_holiday.py 是节假日特征生成脚本，最后生成的文件为 holiday_1.csv 。holiday.csv 人工手动生成家假日文件，进而通过脚本生成最终的 holiday_1.csv。
5. feature_season.py 是季节特征生成脚本，最终生成的文件为 season.csv 。（季节区分也是手动）
6. feature_weather.py 是天气特征生成脚本，最终生成的天气特征文件为 weather_ssd_2.csv （注：天气爬虫获取，不同的年份的天气爬虫获取时候的js接口不一致，最后分别获取后再合并进行天气特征生成）
7. feature_year_month_day.py 是生成年、月、日特征的脚本，生成的特征文件为 year_month_day.csv 
8. feature_merge.py 是上述特征融合生成脚本，生成的最后的文件为 data_feature.csv 