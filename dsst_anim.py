#%%




import os
import numpy as np
import pandas as pd
import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas import Timestamp
import itertools

from mhdpy import *
import mhdpy




import matplotlib.animation as animation
# plt.rcParams['animation.ffmpeg_path'] = r'C:\Users\aspit\ffmpeg\bin\ffmpeg.exe'


#%%

# datestr = '2020-06-23'
# datafolder = mhdpy.fp.gen_path('sharepoint','Data Share', 'MHD Lab', 'HVOF Booth',datestr)

datafolder = r'C:\Users\aspit\National Energy Technology Laboratory\MHD Lab - Documents\Team Member Files\Lee\MHDGEN\AIAA 2020 Talk\Movie plot\Figure Animations\0623_TorchOn'

dsst = mhdpy.load.loadprocesseddata(os.path.join(datafolder, 'Processed CDF'))


# %%
timewindow_on = slice(Timestamp('2020-06-23 17:07:20'),Timestamp('2020-06-23 17:07:50'))
timewindow_seed = slice(Timestamp('2020-06-23 17:57:04'),Timestamp('2020-06-23 17:57:34'))
dt = timewindow_on.stop - timewindow_on.start


das = [
    dsst['hvof']['flow_fuel_hvof'],
    # dsst['hvof']['flow_o2_hvof'],
    # dsst['hvof_input_calcs']['totalmassflow_hvof'],
    # dsst['hvof']['P_CC_hvof']
    ]

das_rs = []
for da in das:
    da = da.sel(time=timewindow_on).dropna('time','all')
    da = da.resample(time='500ms').mean(keep_attrs=True)
    das_rs.append(da)



#%% 


def dsst_anim(da, ):

    timedata = da.coords['time'].values

    fig, ax = plt.subplots()

    lines = da.plot(ax=ax)

    fig.tight_layout()

    line = lines[0]

    def init():
        line.set_ydata([np.nan]*len(timedata))
        return line,

    def animate(i):
        timesel = timedata[i]
        vals= da.where(da.coords['time']<timesel).values
        line.set_ydata(vals)
        return line,


    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(timedata))

    return ani

# output_folder = r'C:\Users\aspit\National Energy Technology Laboratory\MHD Lab - Documents\Team Member Files\Lee\Movie plot\Figure movies'
output_folder = os.getcwd()


da = das_rs[0]

fp_out = os.path.join(output_folder, da.name + "_figuremovie.html")
ani = dsst_anim(da)
fps = len(da.coords['time'].values)/dt.seconds
# FFwriter = animation.FFMpegWriter(fps = fps)
# ani.save(fp_out, writer=FFwriter)
html_text = ani.to_jshtml(fps)

#%%
with open('dsst_anim.htm', 'w') as file:
    file.write(html_text)

# %%

