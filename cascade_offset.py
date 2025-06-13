# -*- coding: utf-8 -*-

import veusz.plugins as plugins
import numpy as np

class AddCascadingOffsetPlugin(plugins.DatasetPlugin):
    """
    Veusz DataSetPlugin to add a cascading offset to multiple datasets.
    """

    menu = ('Add', 'Add Cascading Offset')
    name = 'AddCascadingOffset'
    description_short = 'Add an increasing offset to selected datasets'
    description_full = 'This plugin adds a cascading offset to a list of selected datasets. The offset increases for each dataset in the list (e.g., offset, 2*offset, 3*offset, ...).'

    def __init__(self):
        """
        Define input fields
        """
        self.fields = [
            plugins.FieldDatasetMulti('datasets_in', 'Input datasets'),
            plugins.FieldFloat('offset', 'Offset value per dataset', default=1.0),
            plugins.FieldText('output_suffix', 'Output suffix', default='_offset'),
        ]
        self.output_datasets = []

    def getDatasets(self, fields):
        """
        Get datasets
        """
        self.output_datasets = []
        input_names = fields['datasets_in']
        if not input_names:
            raise plugins.DatasetPluginException('Please select at least one input dataset.')

        output_suffix = fields['output_suffix']
        for name in input_names:
            output_name = f"{name}{output_suffix}"
            if output_name == name:
                raise plugins.DatasetPluginException(
                    f'Output name "{output_name}" is the same as the input. Please use a different suffix.'
                )
            ds_out = plugins.Dataset1D(output_name)
            self.output_datasets.append(ds_out)

        return self.output_datasets

    def updateDatasets(self, fields, helper):
        """
        Main logic
        """
        input_names = fields['datasets_in']
        offset_base = fields['offset']

        for idx, in_name in enumerate(input_names):
            ds_in = helper.getDataset(in_name)
            current_offset = (idx + 1) * offset_base
            new_data = ds_in.data + current_offset
            ds_out = self.output_datasets[idx]
            ds_out.update(data=new_data,
                          serr=ds_in.serr, perr=ds_in.perr, nerr=ds_in.nerr)

plugins.datasetpluginregistry.append(AddCascadingOffsetPlugin)
