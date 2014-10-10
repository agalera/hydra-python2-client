#Example use:

#import class
from hydra import hydra

#cachetime optional
hy = hydra("https://best-domain.bla/app/hydra", cachetime=60)

#return list
hy.get_list()

#return update list
hy.get_list(force=True)