# StackedOffsetPlugin
[Veusz](https://veusz.github.io/) plugin to add an increasing offset to selected datasets

# How it works
This plugin adds stacked offsets to selected datasets. The offset increases for each dataset in the list (e.g., offset, 2×offset, 3×offset, ...).

# How to install
1. Download [the plugin file](https://github.com/korintje/StackedOffsetPlugin/archive/refs/tags/v1.0.zip)
2. Extract the compressed folder
3. Move the `stacked_offset.py` in the unzipped folder to somewhere preferable (e.g. C:\Program Files (x86)\Veusz\plugins)
4. Start Veusz
5. `Edit` -> `Preferences` -> `Data` -> `Add`, and choose the saved `stacked_offset.py`
6. Restart Veusz

# How to use
In veusz
1. `Data` -> `Operations` -> `Add` -> `Stacked offset`
2. Select datasets to be added offset.
3. Set the unit offset value
4. Set the suffix of the newly created datasets
5. Apply

If you want to change the offset value after the operation, right click on a newly created dataset and select `Edit`.
The operation dialog will apear again. 

# Requirements
- [Veusz](https://veusz.github.io/)

# License
GNU General Public License v3.0 or later  

See [LICNESE](https://github.com/korintje/StackedOffsetPlugin/blob/main/LICENSE) for the full text.
