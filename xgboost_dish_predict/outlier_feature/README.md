1. outlier_detection.py 是菜品销量异常值检测文件脚本，生成的销量异常处理的值文件为 outlier_4_03.csv。
2. outlier_feature_same_week1.py 是生成前一周同星期销量的特征脚本，最后生成的文件为 outlier_same_week1.csv。
3. outlier_feature_same_week2.py 是生成前2周同星期销量均值的特征脚本，最后生成的文件为 outlier_same_week2.csv。
4. outlier_feature_same_week3.py 是生成前3周同星期销量均值的特征脚本，最后生成的文件为 outlier_same_week3.csv。
5. outlier_feature_same_week4.py 是生成前4周同星期销量均值的特征脚本，最后生成的文件为 outlier_same_week4.csv。
6. outlier_same_week1_sales_percent.py 是生成前1周同星期销量占所在周销量总和占比的特征脚本，最后生成的文件为 outlier_same_week1_sales_percent.csv。
7. outlier_feature_same_week_line_regression.py 是生成2,3,4,5,6线性回归值特征的脚本，生成的特征文件为 outlier_feature_same_week_line_regression.csv.csv ，注：feature_same_week_line_regression.csv是合并成2,3,4,5,6特征的文件。
8. outlier_merge.py 是上述特征和之前外部特征融合生成脚本，生成的最后的文件为 data_feature_12.csv。
9. feature_get_dummies_week_month_weather_holiday_season.py 是 one-hot 星期、月份、天气类型、节假日、季节字段特征。
	最后的文件为 data_feature_12.csv。