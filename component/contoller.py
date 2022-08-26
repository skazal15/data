
from core.analis import all_data,m
from odm import data
from component.appflask import root_dir
import matplotlib.pyplot as plt
import matplotlib

def dashboard():
    key2=[]
    datepred = []
    lastusage = []
    persen = []
    predict = []
    mer = []
    for it in range(0,len(data.instances)):
        prediction_date = all_data[it][1]
        datepred.append(prediction_date)
        lastusage.append(round(all_data[it][13],2))
        predict.append(round(all_data[it][8],2))
        if data.measure[all_data[it][7]] != '%':
            persen.append(round(all_data[it][13] / 1000,0))
        if data.measure[all_data[it][7]] == '%':
            persen.append(round(all_data[it][13]))
        mer.append(data.measure[all_data[it][7]])
    duedate = datepred[0]
    for it in range(len(data.instances)):
        if all_data[it][1] == duedate:
            key2 = all_data[it][0]
            prediction_date1=all_data[it][1]
            d = all_data[it][2]
            series1 = all_data[it][3]
            color = all_data[it][4]
            predictiondat1 = all_data[it][5]
            mse = all_data[it][6]
            instance = all_data[it][7]
            predict1 = round(all_data[it][8],2)
            d1 = all_data[it][9]
            predictdat1 = all_data[it][10]
            predictmax = round(max(all_data[it][10]),0)
            predictmin = round(min(predictdat1),0)
    return(datepred,lastusage,key2,d,series1,color,predictiondat1,mse,instance,predict,d1,predictdat1,predictmax,predictmin,persen,prediction_date1,predict1,mer)


def fore():
    i = data.instances[1]
    mer = data.measure[i]
    for it in range(len(data.instances)):
        if i == all_data[it][7]:
            key2 = all_data[it][0]
            prediction_date = all_data[it][1]
            d = all_data[it][2]
            series1 = all_data[it][3]
            color = all_data[it][4]
            predictiondat1 = all_data[it][5]
            mse = all_data[it][6]
            instance = all_data[it][7]
            predict = round(all_data[it][8],2)
            d1 = all_data[it][9]
            predictdat1 = all_data[it][10]
    print(len(predictdat1))
    print(len(d1))
    return(mer,key2,prediction_date,d,series1,color,predictiondat1,mse,instance,predict,d1,predictdat1)

def bot_data():
    for i in range(len(m)):
        if all_data[i][7].lower() == 'emas1':
            per=round(all_data[i][8],2)
        if per >= 70:
            mon=all_data[i][7]
            dat=all_data[i][1]
            df=all_data[i][11]
            mon=str(mon)
            dat=str(dat)
            per=str(per)
            matplotlib.use('Agg')
            plt.ioff()
            plt.style.use("dark_background")
            for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
                plt.rcParams[param] = '0.9'  # very light grey
            for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
                plt.rcParams[param] = '#212946'  # bluish dark grey
            colors = [
                '#08F7FE',  # teal/cyan
                '#FE53BB',  # pink
                '#F5D300',  # yellow
                '#00ff41',  # matrix green
                ]
            fig, ax = plt.subplots()
            df.plot(marker='o', color=colors, ax=ax)
            # Redraw the data with low alpha and slighty increased linewidth:
            n_shades = 10
            diff_linewidth = 1.05
            alpha_value = 0.3 / n_shades
            for n in range(1, n_shades+1):
                df.plot(marker='o',
                        linewidth=2+(diff_linewidth*n),
                        alpha=alpha_value,
                        legend=False,
                        ax=ax,
                        color=colors)
            # Color the areas below the lines:
            for column, color in zip(df, colors):
                ax.fill_between(x=df.index,
                                y1=df.values,
                                color=color,
                                alpha=0.1)
            ax.grid(color='#2A3459')
            ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
            ax.set_ylim(0)
            plt.title('prediction')
            plt.ylabel('%')
            plt.savefig(root_dir+'\warning.png')
            img = open(root_dir+'\warning.png', 'rb')
            return(mon,per,dat,img)