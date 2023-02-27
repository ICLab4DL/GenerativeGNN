#    CHEMICAL:
#         NCI1
#         DD
#         ENZYMES
#         PROTEINS
#    SOCIAL[_1 | _DEGREE]:
#         IMDB-BINARY
#         IMDB-MULTI
#         REDDIT-BINARY
#         REDDIT-MULTI-5K
#         COLLAB

gpu=02_diff
dt=0226
tag=load_degree_shuf

dat='all'
dat='NCI1'
dat='ENZYMES'
dat='DD'
dat="CSL"
dat='COLLAB'
dat='REDDIT-BINARY'
dat="PROTEINS"
dat='MUTAG'
dat='IMDB-BINARY'

nohup python3 -u Launch_Experiments.py --config-file gnn_comparison/config_GIN_lzd_imdb.yml \
--dataset-name ${dat} --result-folder results/result_GIN_${dt}_${tag} --debug > logs/${gpu}_${dt}_${tag}_nohup.log 2>&1 &