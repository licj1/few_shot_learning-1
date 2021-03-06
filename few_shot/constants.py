'''
Constants for few_shot
'''
import os

CWD = os.path.dirname(os.path.realpath(__file__))
CHECKPOINTS_DIR = os.path.join(os.path.dirname(CWD), 'model_checkpoints')
DATA_DIR = os.path.join(os.path.dirname(CWD), 'datasets')

OMNIGLOT_SHAPE = (32, 32, 3)

CAR_SHAPE = (139, 139, 3)
CAR_BATCH_SIZE = 32

ANOMALY_SHAPE = (32, 32, 3)
ANOMALY_BATCH_SIZE = 32
