#%%

import xarray as xr
import numpy as np
import holoviews as hv
from holoviews import opts
hv.extension('matplotlib')

opts.defaults(opts.Scatter3D(color='Value', cmap='fire', edgecolor='black', s=50))


dataset3d = hv.Dataset((range(3), range(5), range(7), np.random.randn(7, 5, 3)),
                       ['x', 'y', 'z'], 'Value')
dataset3d


t = (dataset3d.to(hv.Image, ['y', 'z'], 'Value', ['x']) +
hv.HoloMap({x: hv.Scatter3D(dataset3d.select(x=x)) for x in range(3)}, kdims='x'))

hv.save(t, 'boxplot.html')
#%% 

xr_ds = xr.tutorial.open_dataset("air_temperature").load()
xr_ds

hv_ds = hv.Dataset(xr_ds)[:, :, "2013-01-01"]
print(hv_ds)

airtemp = hv_ds.to(hv.Image, kdims=["lon", "lat"], dynamic=False)
airtemp[:, 220:320, :].opts(colorbar=True, fig_size=200)

hv.save(airtemp, 'airtemp.html')