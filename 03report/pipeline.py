import pandas as pd
import pprint
import matplotlib
import matplotlib.pyplot as plt
import pylab

#plot setting
plt.style.use('ggplot')
pylab.rcParams['figure.figsize'] = (20, 8)

def find_max(df,n):
    lis = ['Date','Time','Cost','DayName']
    for i in lis:
        print(df.sort_values('Usage')[-1*n:][lis][i].value_counts())
# def count_max(df,n):
# df.sort_values('Usage')[-1*10:].Date.value_counts()
# find_max(df,15)

def cal_cost(df):
    cost_dic = {}
    cost_dic["sum"] = [round(df.Cost.sum())]
    cost_dic["weekday"] = list(round(df.groupby('Weekday').sum().Cost))
    cost_dic["week"] = list(round(df.groupby('Week').sum().Cost))
    cost_dic["hour"] = list(round(df.groupby('Time').sum().Cost))
    return(cost_dic)

def reveal_cost(cost_dic):
    for key in cost_dic:
        print()
        for i in range(len(cost_dic[key])):
            print("{} {}: {}".format(key,i, cost_dic[key][i]))
        
# reveal_cost(cal_cost(df))

# cost_rate：一度電大概多少錢
def generate_cost_columns(df, Rate):
    df['Cost'] = df.Usage * Rate
    print('Column "Cost" had been generated!')
    return df


# plot_weekday(df)
# plot_hour(df)

def make_df(Path, Place, Rate):
    df = pd.read_csv(Path)
    # print(df.Building.unique())
    df = df[df.Building == Place] #選定地方
    df.Week.unique() #確認日期
    print(df.head())
    return df

def usage_pct(df):
    mean_Sat = df[df.Weekday == 6].Usage.mean()
    mean_3am = df[df.Time == '03:00'].Usage.mean()
    return mean_Sat, mean_3am
# usage_pct(df)

def week_usage_pct(df):
    total = df.groupby('Week').sum().Usage.sum()
    for i in df.Week.unique():
        week = df[df.Week == i].Usage.sum()
        pct = round(week/total, 3) * 100
        print("Week {}: {} %".format(i,pct))
# week_usage_pct(df)

def analysis(Path, Place, Rate):
    df = make_df(Path, Place, Rate)
    df = generate_cost_columns(df,Rate)
    print(find_max(df,10))
    print(reveal_cost(cal_cost(df)))
    # print(plot_weekday(df))
    # print(plot_hour(df))
    print(usage_pct(df))
    print(week_usage_pct(df))