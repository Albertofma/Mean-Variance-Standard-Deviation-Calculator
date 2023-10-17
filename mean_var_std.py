import numpy as np

def calculate(list):
  if len(list)<9:
      raise ValueError("List must contain nine numbers.")
  df=np.array(list)
  df=np.reshape(df,(3,3))
  df=df.astype(float)

  #First we make sure the list is 9 numbers so that the reshape command works, then we convert that list to a numpy array and reshape to a 3x3 array
  
  meanx=df.mean(axis=0).tolist()
  meany=df.mean(axis=1).tolist()
  meanflat=df.mean(axis=None).tolist()
#The mean of the array by x axis, then y axis and then of all the individual values
  
  varx=df.var(axis=0).tolist()
  vary=df.var(axis=1).tolist()
  varflat=df.var(axis=None).tolist()
#The variance of the array by x axis, then y axis and then of all the individual values
  
  stdx=df.std(axis=0).tolist()
  stdy=df.std(axis=1).tolist()
  stdflat=df.std(axis=None).tolist()
#The standard deviation of the array by x axis, then y axis and then of all the individual values
  
  maxx=df.max(axis=0).tolist()
  maxy=df.max(axis=1).tolist()
  maxflat=df.max(axis=None).tolist()
#The maximum value of the array by x axis, then y axis and then of all the individual values

  minx=df.min(axis=0).tolist()
  miny=df.min(axis=1).tolist()
  minflat=df.min(axis=None).tolist()
#The minimum value of the array by x axis, then y axis and then of all the individual values

  sumx=df.sum(axis=0).tolist()
  sumy=df.sum(axis=1).tolist()
  sumflat=df.sum(axis=None).tolist()
#The sum of the value of the array by x axis, then y axis and then of all the individual values
  
  calculations={'mean': [meanx, meany, meanflat]
               ,'variance': [varx, vary, varflat]
               ,'standard deviation': [stdx, stdy, stdflat]
               ,'max': [maxx, maxy, maxflat]
               ,'min': [minx, miny, minflat]
               ,'sum': [sumx, sumy, sumflat]}


  return calculations
