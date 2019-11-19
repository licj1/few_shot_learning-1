'''
Constants for few_shot
'''
import os

CWD = os.path.dirname(os.path.realpath(__file__))
CHECKPOINTS_DIR = os.path.join(CWD, 'model_checkpoints')
DATA_DIR = os.path.join(os.path.basename(CWD), 'datasets')
