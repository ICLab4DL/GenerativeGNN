from torch_geometric import data
import numpy as np

class Data(data.Data):
    def __init__(self,
                 x=None,
                 edge_index=None,
                 edge_attr=None,
                 y=None,
                 v_outs=None,
                 e_outs=None,
                 g_outs=None,
                 o_outs=None,
                 laplacians=None,
                 v_plus=None,
                 **kwargs):

        additional_fields = {
            'v_outs': v_outs,
            'e_outs': e_outs,
            'g_outs': g_outs,
            'o_outs': o_outs,
            'laplacians': laplacians,
            'v_plus': v_plus

        }
        super().__init__(x, edge_index, edge_attr, y, **additional_fields)
        self.N = self.x.shape[0]
        
    def set_additional_attr(self, attr_name, attr_value):
        setattr(self, attr_name, attr_value)
        
    def to_numpy_array(self):
        self.N = self.x.shape[0]
        m = np.ones((self.N, self.N))
        m[self.edge_index[0], self.edge_index[1]] = 1
        return m
        
        
class Batch(data.Batch):
    @staticmethod
    def from_data_list(data_list, follow_batch=[]):
        laplacians = None
        v_plus = None

        if 'laplacians' in data_list[0]:
            laplacians = [d.laplacians[:] for d in data_list]
            v_plus = [d.v_plus[:] for d in data_list]

        copy_data = []
        for d in data_list:
            copy_data.append(Data(x=d.x,
                                  y=d.y,
                                  edge_index=d.edge_index,
                                  edge_attr=d.edge_attr,
                                  v_outs=d.v_outs,
                                  g_outs=d.g_outs,
                                  e_outs=d.e_outs,
                                  o_outs=d.o_outs)
                             )

        batch = data.Batch.from_data_list(copy_data, follow_batch=follow_batch)
        batch['laplacians'] = laplacians
        batch['v_plus'] = v_plus
        # TODO: 2022.10.20, implement graph-wise features.
        return batch
