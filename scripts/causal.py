import numpy as np
import pandas as pd
import dowhy
import matplotlib.pyplot as plt
from causalgraphicalmodels import CausalGraphicalModel
from sklearn.model_selection import train_test_split
pd.set_option('display.max_columns',35)
import sys
sys.path.append("../scripts/")
#from plot import plot_distribution
import warnings
warnings.filterwarnings('ignore')
from dowhy import CausalModel
from IPython.display import Image, display
from causalnex.structure import StructureModel
from causalnex.structure.notears import from_pandas
from causalnex.structure.notears import from_pandas_lasso
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE


class Causal: 
    def create_causal_model(df,treatment: str, outcome: str, common_causes):
        # Create a causal model from the train data.
        # model = create.....
        CausalModel(data, treatment, outcome, common_causes).view_model()
        
    def causal_effect(model):
        # estimands = causal...
        print(model.identify_effect())
        
    def causal_effect_estimation(model, estimands):
        # estimate = ...
        print(model.estimate_effect(estimands,method_name = "backdoor.propensity_score_weighting"))
        
    def random_common_cause(model, estimands, estimate):
        print(model.refute_estimate(estimands,estimate, "random_common_cause"))
        
    def data_subset_refuter(model, estimands, estimate):
        print(model.refute_estimate(estimands,estimate, "data_subset_refuter"))
        
    def placebo_treatment(model, estimands, estimate):
        print(model.refute_estimate(estimands,estimate, "placebo_treatment_refuter"))
        
        
    def vis_sm(sm):
        viz = plot_structure(sm,
        graph_attributes={"scale": "2.0", 'size': 3.0},
        all_node_attributes=NODE_STYLE.WEAK,
        all_edge_attributes=EDGE_STYLE.WEAK)
        return Image(viz.draw(format='png'))
        
        
    def lasso(x_portion):
        # s2 0r s3 etc = ....
        from_pandas_lasso(x_portion, tabu_parent_nodes=['diagnosis'],
                          w_threshold=0.3, beta=0.8).get_largest_subgraph()
        
    def jaccard_similarity(g, h):
        i = set(g).intersection(h)
        return round(len(i) / (len(g) + len(h) - len(i)),3)

