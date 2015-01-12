#
#  Copyright (c) 2009-2015, Jack Poulson
#  All rights reserved.
#
#  This file is part of Elemental and is under the BSD 2-Clause License, 
#  which can be found in the LICENSE file in the root directory, or at 
#  http://opensource.org/licenses/BSD-2-Clause
#
from El.core import *

from ctypes import CFUNCTYPE

# Linear program
# ==============

(LP_ADMM,LP_IPF,LP_IPF_SELFDUAL,LP_MEHROTRA,LP_MEHROTRA_SELFDUAL)=(0,1,2,3,4)

lib.ElLPIPFLineSearchCtrlDefault_s.argtypes = \
lib.ElLPIPFLineSearchCtrlDefault_d.argtypes = [c_void_p]
lib.ElLPIPFLineSearchCtrlDefault_s.restype = \
lib.ElLPIPFLineSearchCtrlDefault_d.restype = c_uint
class LPIPFLineSearchCtrl_s(ctypes.Structure):
  _fields_ = [("gamma",sType),("beta",sType),("psi",sType),
              ("stepRatio",sType),("progress",bType)]
  def __init__(self):
    lib.ElLPIPFLineSearchCtrlDefault_s(pointer(self))
class LPIPFLineSearchCtrl_d(ctypes.Structure):
  _fields_ = [("gamma",dType),("beta",dType),("psi",dType),
              ("stepRatio",dType),("progress",bType)]
  def __init__(self):
    lib.ElLPIPFLineSearchCtrlDefault_d(pointer(self))

# Direct conic form
# -----------------
lib.ElLPDirectADMMCtrlDefault_s.argtypes = \
lib.ElLPDirectADMMCtrlDefault_d.argtypes = [c_void_p]
lib.ElLPDirectADMMCtrlDefault_s.restype = \
lib.ElLPDirectADMMCtrlDefault_d.restype = c_uint
class LPDirectADMMCtrl_s(ctypes.Structure):
  _fields_ = [("rho",sType),("alpha",sType),
              ("maxIter",iType),
              ("absTol",sType),("relTol",sType),
              ("inv",bType),("progress",bType)]
  def __init__(self):
    lib.ElLPDirectADMMCtrlDefault_s(pointer(self))
class LPDirectADMMCtrl_d(ctypes.Structure):
  _fields_ = [("rho",dType),("alpha",dType),
              ("maxIter",iType),
              ("absTol",dType),("relTol",dType),
              ("inv",bType),("progress",bType)]
  def __init__(self):
    lib.ElLPDirectADMMCtrlDefault_d(pointer(self))

(LP_DIRECT_FULL_KKT,LP_DIRECT_AUGMENTED_KKT,LP_DIRECT_NORMAL_KKT) = (0,1,2)

lib.ElLPDirectIPFCtrlDefault_s.argtypes = \
lib.ElLPDirectIPFCtrlDefault_d.argtypes = [c_void_p,bType]
lib.ElLPDirectIPFCtrlDefault_s.restype = \
lib.ElLPDirectIPFCtrlDefault_d.restype = c_uint
class LPDirectIPFCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("centering",sType),
              ("system",c_uint),("lineSearchCtrl",LPIPFLineSearchCtrl_s),
              ("progress",bType)]
  def __init__(self,isSparse=True):
    lib.ElLPDirectIPFCtrlDefault_s(pointer(self),isSparse)
class LPDirectIPFCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("centering",dType),
              ("system",c_uint),("lineSearchCtrl",LPIPFLineSearchCtrl_d),
              ("progress",bType)]
  def __init__(self,isSparse=True):
    lib.ElLPDirectIPFCtrlDefault_d(pointer(self),isSparse)

lib.ElLPDirectMehrotraCtrlDefault_s.argtypes = \
lib.ElLPDirectMehrotraCtrlDefault_d.argtypes = [c_void_p,bType]
lib.ElLPDirectMehrotraCtrlDefault_s.restype = \
lib.ElLPDirectMehrotraCtrlDefault_d.restype = c_uint
class LPDirectMehrotraCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("maxStepRatio",sType),
              ("system",c_uint),("progress",bType)]
  def __init__(self,isSparse=True):
    lib.ElLPDirectMehrotraCtrlDefault_s(pointer(self),isSparse)
class LPDirectMehrotraCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("maxStepRatio",dType),
              ("system",c_uint),("progress",bType)]
  def __init__(self,isSparse=True):
    lib.ElLPDirectMehrotraCtrlDefault_d(pointer(self),isSparse)

lib.ElLPDirectCtrlDefault_s.argtypes = \
lib.ElLPDirectCtrlDefault_d.argtypes = [c_void_p,bType]
lib.ElLPDirectCtrlDefault_s.restype = \
lib.ElLPDirectCtrlDefault_d.restype = c_uint
class LPDirectCtrl_s(ctypes.Structure):
  _fields_ = [("approach",c_uint),("admmCtrl",LPDirectADMMCtrl_s),
              ("ipfCtrl",LPDirectIPFCtrl_s),
              ("mehrotraCtrl",LPDirectMehrotraCtrl_s)]
  def __init__(self,isSparse=True):
    lib.ElLPDirectCtrlDefault_s(pointer(self),isSparse)
class LPDirectCtrl_d(ctypes.Structure):
  _fields_ = [("approach",c_uint),("admmCtrl",LPDirectADMMCtrl_d),
              ("ipfCtrl",LPDirectIPFCtrl_d),
              ("mehrotraCtrl",LPDirectMehrotraCtrl_d)]
  def __init__(self,isSparse=True):
    lib.ElLPDirectCtrlDefault_d(pointer(self),isSparse)

lib.ElLPDirect_s.argtypes = \
lib.ElLPDirect_d.argtypes = \
lib.ElLPDirectDist_s.argtypes = \
lib.ElLPDirectDist_d.argtypes = \
lib.ElLPDirectSparse_s.argtypes = \
lib.ElLPDirectSparse_d.argtypes = \
lib.ElLPDirectDistSparse_s.argtypes = \
lib.ElLPDirectDistSparse_d.argtypes = \
  [c_void_p,
   c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p]
lib.ElLPDirect_s.restype = \
lib.ElLPDirect_d.restype = \
lib.ElLPDirectDist_s.restype = \
lib.ElLPDirectDist_d.restype = \
lib.ElLPDirectSparse_s.restype = \
lib.ElLPDirectSparse_d.restype = \
lib.ElLPDirectDistSparse_s.restype = \
lib.ElLPDirectDistSparse_d.restype = \
  c_uint

lib.ElLPDirectX_s.argtypes = \
lib.ElLPDirectXSparse_s.argtypes = \
lib.ElLPDirectXDist_s.argtypes = \
lib.ElLPDirectXDistSparse_s.argtypes = \
  [c_void_p,
   c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   LPDirectCtrl_s]
lib.ElLPDirectX_d.argtypes = \
lib.ElLPDirectXSparse_d.argtypes = \
lib.ElLPDirectXDist_d.argtypes = \
lib.ElLPDirectXDistSparse_d.argtypes = \
  [c_void_p,
   c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   LPDirectCtrl_d]
lib.ElLPDirectX_s.restype = \
lib.ElLPDirectX_d.restype = \
lib.ElLPDirectXSparse_s.restype = \
lib.ElLPDirectXSparse_d.restype = \
lib.ElLPDirectXDist_s.restype = \
lib.ElLPDirectXDist_d.restype = \
lib.ElLPDirectXDistSparse_s.restype = \
lib.ElLPDirectXDistSparse_d.restype = \
  c_uint

def LPDirect(A,b,c,x,y,z,ctrl=None):
  if A.tag != b.tag or b.tag != c.tag or c.tag != x.tag or \
     x.tag != y.tag or y.tag != z.tag:
    raise Exception('Datatypes of {A,b,c,x,y,z} must match')
  if type(b) is not type(c) or type(b) is not type(x) or \
     type(b) is not type(y) or type(b) is not type(z):
    raise Exception('{b,c,x,y,z} must be of the same type')
  args = [A.obj,b.obj,c.obj,x.obj,y.obj,z.obj]
  argsCtrl = [A.obj,b.obj,c.obj,x.obj,y.obj,z.obj,ctrl]
  if type(A) is Matrix:
    if type(b) is not Matrix: raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPDirect_s(*args)
      else:            lib.ElLPDirectX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPDirect_d(*args)
      else:            lib.ElLPDirectX_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix: raise Exception('b must be a DistMatrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPDirectDist_s(*args)
      else:            lib.ElLPDirectXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPDirectDist_d(*args)
      else:            lib.ElLPDirectXDist_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix: raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPDirectSparse_s(*args)
      else:            lib.ElLPDirectXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPDirectSparse_d(*args)
      else:            lib.ElLPDirectXSparse_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec: raise Exception('b must be a DistMultiVec')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPDirectDistSparse_s(*args)
      else:            lib.ElLPDirectXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPDirectDistSparse_d(*args)
      else:            lib.ElLPDirectXDistSparse_d(*argsCtrl)
    else: DataExcept()
  else: TypeExcept()

# Affine conic form
# -----------------
lib.ElLPAffineIPFCtrlDefault_s.argtypes = \
lib.ElLPAffineIPFCtrlDefault_d.argtypes = [c_void_p]
lib.ElLPAffineIPFCtrlDefault_s.restype = \
lib.ElLPAffineIPFCtrlDefault_d.restype = c_uint
class LPAffineIPFCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("centering",sType),
              ("lineSearchCtrl",LPIPFLineSearchCtrl_s),
              ("progress",bType)]
  def __init__(self):
    lib.ElLPAffineIPFCtrlDefault_s(pointer(self))
class LPAffineIPFCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("centering",dType),
              ("lineSearchCtrl",LPIPFLineSearchCtrl_d),
              ("progress",bType)]
  def __init__(self):
    lib.ElLPAffineIPFCtrlDefault_d(pointer(self))

lib.ElLPAffineMehrotraCtrlDefault_s.argtypes = \
lib.ElLPAffineMehrotraCtrlDefault_d.argtypes = [c_void_p]
lib.ElLPAffineMehrotraCtrlDefault_s.restype = \
lib.ElLPAffineMehrotraCtrlDefault_d.restype = c_uint
class LPAffineMehrotraCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("maxStepRatio",sType),
              ("progress",bType)]
  def __init__(self):
    lib.ElLPAffineMehrotraCtrlDefault_s(pointer(self))
class LPAffineMehrotraCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("maxStepRatio",dType),
              ("progress",bType)]
  def __init__(self):
    lib.ElLPAffineMehrotraCtrlDefault_d(pointer(self))

lib.ElLPAffineCtrlDefault_s.argtypes = \
lib.ElLPAffineCtrlDefault_d.argtypes = [c_void_p]
lib.ElLPAffineCtrlDefault_s.restype = \
lib.ElLPAffineCtrlDefault_d.restype = c_uint
class LPAffineCtrl_s(ctypes.Structure):
  _fields_ = [("approach",c_uint),
              ("ipfCtrl",LPAffineIPFCtrl_s),
              ("mehrotraCtrl",LPAffineMehrotraCtrl_s)]
  def __init__(self):
    lib.ElLPAffineCtrlDefault_s(pointer(self))
class LPAffineCtrl_d(ctypes.Structure):
  _fields_ = [("approach",c_uint),
              ("ipfCtrl",LPAffineIPFCtrl_d),
              ("mehrotraCtrl",LPAffineMehrotraCtrl_d)]
  def __init__(self):
    lib.ElLPAffineCtrlDefault_d(pointer(self))

lib.ElLPAffine_s.argtypes = \
lib.ElLPAffine_d.argtypes = \
lib.ElLPAffineDist_s.argtypes = \
lib.ElLPAffineDist_d.argtypes = \
lib.ElLPAffineSparse_s.argtypes = \
lib.ElLPAffineSparse_d.argtypes = \
lib.ElLPAffineDistSparse_s.argtypes = \
lib.ElLPAffineDistSparse_d.argtypes = \
  [c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElLPAffine_s.restype = \
lib.ElLPAffine_d.restype = \
lib.ElLPAffineDist_s.restype = \
lib.ElLPAffineDist_d.restype = \
lib.ElLPAffineSparse_s.restype = \
lib.ElLPAffineSparse_d.restype = \
lib.ElLPAffineDistSparse_s.restype = \
lib.ElLPAffineDistSparse_d.restype = \
  c_uint

lib.ElLPAffineX_s.argtypes = \
lib.ElLPAffineXDist_s.argtypes = \
lib.ElLPAffineXSparse_s.argtypes = \
lib.ElLPAffineXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,c_void_p,
   LPAffineCtrl_s]
lib.ElLPAffineX_d.argtypes = \
lib.ElLPAffineXDist_d.argtypes = \
lib.ElLPAffineXSparse_d.argtypes = \
lib.ElLPAffineXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,c_void_p,
   LPAffineCtrl_d]
lib.ElLPAffineX_s.restype = \
lib.ElLPAffineX_d.restype = \
lib.ElLPAffineXDist_s.restype = \
lib.ElLPAffineXDist_d.restype = \
lib.ElLPAffineXSparse_s.restype = \
lib.ElLPAffineXSparse_d.restype = \
lib.ElLPAffineXDistSparse_s.restype = \
lib.ElLPAffineXDistSparse_d.restype = \
  c_uint

def LPAffine(A,G,b,c,h,x,y,z,s,ctrl=None):
  if type(A) is not type(G):
    raise Exception('A and G must be of the same type')
  if type(b) is not type(c) or type(b) is not type(c) or \
     type(b) is not type(h) or type(b) is not type(x) or \
     type(b) is not type(y) or type(b) is not type(z) or \
     type(b) is not type(s):
    raise Exception('{b,c,h,x,y,z,s} must be of the same type')
  args = [A.obj,G.obj,b.obj,c.obj,h.obj,x.obj,y.obj,z.obj,s.obj]
  argsCtrl = [A.obj,G.obj,b.obj,c.obj,h.obj,x.obj,y.obj,z.obj,s.obj,ctrl]
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPAffine_s(*args)
      else:            lib.ElLPAffineX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPAffine_d(*args)
      else:            lib.ElLPAffineX_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPAffineDist_s(*args)
      else:            lib.ElLPAffineXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPAffineDist_d(*args)
      else:            lib.ElLPAffineXDist_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPAffineSparse_s(*args)
      else:            lib.ElLPAffineXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPAffineSparse_d(*args)
      else:            lib.ElLPAffineXSparse_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLPAffineDistSparse_s(*args)
      else:            lib.ElLPAffineXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLPAffineDistSparse_d(*args)
      else:            lib.ElLPAffineXDistSparse_d(*argsCtrl)
    else: DataExcept()
  else: TypeExcept()

# Basis pursuit
# =============
lib.ElBP_s.argtypes = \
lib.ElBP_d.argtypes = \
lib.ElBPDist_s.argtypes = \
lib.ElBPDist_d.argtypes = \
lib.ElBPSparse_s.argtypes = \
lib.ElBPSparse_d.argtypes = \
lib.ElBPDistSparse_s.argtypes = \
lib.ElBPDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p]
lib.ElBP_s.restype = \
lib.ElBP_d.restype = \
lib.ElBPDist_s.restype = \
lib.ElBPDist_d.restype = \
lib.ElBPSparse_s.restype = \
lib.ElBPSparse_d.restype = \
lib.ElBPDistSparse_s.restype = \
lib.ElBPDistSparse_d.restype = \
  c_uint

lib.ElBPX_s.argtypes = \
lib.ElBPXDist_s.argtypes = \
lib.ElBPXSparse_s.argtypes = \
lib.ElBPXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   LPDirectCtrl_s]
lib.ElBPX_d.argtypes = \
lib.ElBPXDist_d.argtypes = \
lib.ElBPXSparse_d.argtypes = \
lib.ElBPXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   LPDirectCtrl_d]
lib.ElBPX_s.restype = \
lib.ElBPX_d.restype = \
lib.ElBPXDist_s.restype = \
lib.ElBPXDist_d.restype = \
lib.ElBPXSparse_s.restype = \
lib.ElBPXSparse_d.restype = \
lib.ElBPXDistSparse_s.restype = \
lib.ElBPXDistSparse_d.restype = \
  c_uint

def BP(A,b,ctrl=None):
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBP_s(*args)
      else:            lib.ElBPX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBP_d(*args)
      else:            lib.ElBPX_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPDist_s(*args)
      else:            lib.ElBPXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPDist_d(*args)
      else:            lib.ElBPXDist_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPSparse_s(*args)
      else:            lib.ElBPXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPSparse_d(*args)
      else:            lib.ElBPXSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPDistSparse_s(*args)
      else:            lib.ElBPXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPDistSparse_d(*args)
      else:            lib.ElBPXDistSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  else: TypeExcept()

# ADMM
# ----
lib.ElBPADMM_s.argtypes = \
lib.ElBPADMM_d.argtypes = \
lib.ElBPADMM_c.argtypes = \
lib.ElBPADMM_z.argtypes = \
lib.ElBPADMMDist_s.argtypes = \
lib.ElBPADMMDist_d.argtypes = \
lib.ElBPADMMDist_c.argtypes = \
lib.ElBPADMMDist_z.argtypes = \
  [c_void_p,c_void_p,c_void_p,POINTER(iType)]
lib.ElBPADMM_s.restype = \
lib.ElBPADMM_d.restype = \
lib.ElBPADMM_c.restype = \
lib.ElBPADMM_z.restype = \
lib.ElBPADMMDist_s.restype = \
lib.ElBPADMMDist_d.restype = \
lib.ElBPADMMDist_c.restype = \
lib.ElBPADMMDist_z.restype = \
  c_uint
def BPADMM(A,b):
  if type(A) is not type(b):
    raise Exception('Types of A and b must match')
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  numIts = iType()
  if type(A) is Matrix:
    z = Matrix(A.tag)
    args = [A.obj,b.obj,z.obj,pointer(numIts)]
    if   A.tag == sTag: lib.ElBPADMM_s(*args)
    elif A.tag == dTag: lib.ElBPADMM_d(*args)
    elif A.tag == cTag: lib.ElBPADMM_c(*args)
    elif A.tag == zTag: lib.ElBPADMM_z(*args)
    else: DataExcept()
    return z, numIts
  elif type(A) is DistMatrix:
    z = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,z.obj,pointer(numIts)]
    if   A.tag == sTag: lib.ElBPADMMDist_s(*args)
    elif A.tag == dTag: lib.ElBPADMMDist_d(*args)
    elif A.tag == cTag: lib.ElBPADMMDist_c(*args)
    elif A.tag == zTag: lib.ElBPADMMDist_z(*args)
    else: DataExcept()
    return z, numIts
  else: TypeExcept()

# Chebyshev point
# ===============
lib.ElCP_s.argtypes = \
lib.ElCP_d.argtypes = \
lib.ElCPDist_s.argtypes = \
lib.ElCPDist_d.argtypes = \
lib.ElCPSparse_s.argtypes = \
lib.ElCPSparse_d.argtypes = \
lib.ElCPDistSparse_s.argtypes = \
lib.ElCPDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p]
lib.ElCP_s.restype = \
lib.ElCP_d.restype = \
lib.ElCPDist_s.restype = \
lib.ElCPDist_d.restype = \
lib.ElCPSparse_s.restype = \
lib.ElCPSparse_d.restype = \
lib.ElCPDistSparse_s.restype = \
lib.ElCPDistSparse_d.restype = \
  c_uint

lib.ElCPX_s.argtypes = \
lib.ElCPXDist_s.argtypes = \
lib.ElCPXSparse_s.argtypes = \
lib.ElCPXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   LPAffineCtrl_s]
lib.ElCPX_d.argtypes = \
lib.ElCPXDist_d.argtypes = \
lib.ElCPXSparse_d.argtypes = \
lib.ElCPXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   LPAffineCtrl_d]
lib.ElCPX_s.restype = \
lib.ElCPX_d.restype = \
lib.ElCPXDist_s.restype = \
lib.ElCPXDist_d.restype = \
lib.ElCPXSparse_s.restype = \
lib.ElCPXSparse_d.restype = \
lib.ElCPXDistSparse_s.restype = \
lib.ElCPXDistSparse_d.restype = \
  c_uint

def CP(A,b,ctrl=None):
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElCP_s(*args)
      else:            lib.ElCPX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElCP_d(*args)
      else:            lib.ElCPX_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElCPDist_s(*args)
      else:            lib.ElCPXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElCPDist_d(*args)
      else:            lib.ElCPXDist_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElCPSparse_s(*args)
      else:            lib.ElCPXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElCPSparse_d(*args)
      else:            lib.ElCPXSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElCPDistSparse_s(*args)
      else:            lib.ElCPXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElCPDistSparse_d(*args)
      else:            lib.ElCPXDistSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  else: TypeExcept()

# Dantzig selector
# ================
lib.ElDS_s.argtypes = \
lib.ElDSDist_s.argtypes = \
lib.ElDSSparse_s.argtypes = \
lib.ElDSDistSparse_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p]
lib.ElDS_d.argtypes = \
lib.ElDSDist_d.argtypes = \
lib.ElDSSparse_d.argtypes = \
lib.ElDSDistSparse_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p]
lib.ElDS_s.restype = \
lib.ElDS_d.restype = \
lib.ElDSDist_s.restype = \
lib.ElDSDist_d.restype = \
lib.ElDSSparse_s.restype = \
lib.ElDSSparse_d.restype = \
lib.ElDSDistSparse_s.restype = \
lib.ElDSDistSparse_d.restype = \
  c_uint

lib.ElDSX_s.argtypes = \
lib.ElDSXDist_s.argtypes = \
lib.ElDSXSparse_s.argtypes = \
lib.ElDSXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p,
   LPAffineCtrl_s]
lib.ElDSX_d.argtypes = \
lib.ElDSXDist_d.argtypes = \
lib.ElDSXSparse_d.argtypes = \
lib.ElDSXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p,
   LPAffineCtrl_d]
lib.ElDSX_s.restype = \
lib.ElDSX_d.restype = \
lib.ElDSXDist_s.restype = \
lib.ElDSXDist_d.restype = \
lib.ElDSXSparse_s.restype = \
lib.ElDSXSparse_d.restype = \
lib.ElDSXDistSparse_s.restype = \
lib.ElDSXDistSparse_d.restype = \
  c_uint

def DS(A,b,lambdaPre,ctrl=None):
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  lambd = TagToType(A.tag)(lambdaPre)
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElDS_s(*args)
      else:            lib.ElDSX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElDS_d(*args)
      else:            lib.ElDSX_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElDSDist_s(*args)
      else:            lib.ElDSXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElDSDist_d(*args)
      else:            lib.ElDSXDist_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElDSSparse_s(*args)
      else:            lib.ElDSXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElDSSparse_d(*args)
      else:            lib.ElDSXSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElDSDistSparse_s(*args)
      else:            lib.ElDSXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElDSDistSparse_d(*args)
      else:            lib.ElDSXDistSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  else: TypeExcept()

# Least Absolute Value regression
# ===============================
lib.ElLAV_s.argtypes = \
lib.ElLAV_d.argtypes = \
lib.ElLAVDist_s.argtypes = \
lib.ElLAVDist_d.argtypes = \
lib.ElLAVSparse_s.argtypes = \
lib.ElLAVSparse_d.argtypes = \
lib.ElLAVDistSparse_s.argtypes = \
lib.ElLAVDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p]
lib.ElLAV_s.restype = \
lib.ElLAV_d.restype = \
lib.ElLAVDist_s.restype = \
lib.ElLAVDist_d.restype = \
lib.ElLAVSparse_s.restype = \
lib.ElLAVSparse_d.restype = \
lib.ElLAVDistSparse_s.restype = \
lib.ElLAVDistSparse_d.restype = \
  c_uint

lib.ElLAVX_s.argtypes = \
lib.ElLAVXDist_s.argtypes = \
lib.ElLAVXSparse_s.argtypes = \
lib.ElLAVXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   LPAffineCtrl_s]
lib.ElLAVX_d.argtypes = \
lib.ElLAVXDist_d.argtypes = \
lib.ElLAVXSparse_d.argtypes = \
lib.ElLAVXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   LPAffineCtrl_d]
lib.ElLAVX_s.restype = \
lib.ElLAVX_d.restype = \
lib.ElLAVXDist_s.restype = \
lib.ElLAVXDist_d.restype = \
lib.ElLAVXSparse_s.restype = \
lib.ElLAVXSparse_d.restype = \
lib.ElLAVXDistSparse_s.restype = \
lib.ElLAVXDistSparse_d.restype = \
  c_uint

def LAV(A,b,ctrl=None):
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLAV_s(*args)
      else:            lib.ElLAVX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLAV_d(*args)
      else:            lib.ElLAVX_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLAVDist_s(*args)
      else:            lib.ElLAVXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLAVDist_d(*args)
      else:            lib.ElLAVXDist_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLAVSparse_s(*args)
      else:            lib.ElLAVXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLAVSparse_d(*args)
      else:            lib.ElLAVXSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,b.obj,x.obj]
    argsCtrl = [A.obj,b.obj,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElLAVDistSparse_s(*args)
      else:            lib.ElLAVXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElLAVDistSparse_d(*args)
      else:            lib.ElLAVXDistSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  else: TypeExcept()

# Logistic regression
# ===================
(NO_PENALTY,L1_PENALTY,L2_PENALTY)=(0,1,2)

lib.ElLogisticRegression_s.argtypes = \
lib.ElLogisticRegressionDist_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,sType,c_uint,POINTER(iType)]
lib.ElLogisticRegression_d.argtypes = \
lib.ElLogisticRegressionDist_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,dType,c_uint,POINTER(iType)]

lib.ElLogisticRegression_s.restype = \
lib.ElLogisticRegression_d.restype = \
lib.ElLogisticRegressionDist_s.restype = \
lib.ElLogisticRegressionDist_d.restype = \
  c_uint

def LogisticRegression(G,q,gamma,penalty=L1_PENALTY):
  if type(G) is not type(q):
    raise Exception('Types of G and q must match')
  if G.tag != q.tag:
    raise Exception('Datatypes of G and q must match')
  numIts = iType()
  if type(G) is Matrix:
    z = Matrix(G.tag)
    args = [G.obj,q.obj,z.obj,gamma,penalty,pointer(numIts)]
    if   G.tag == sTag: lib.ElLogisticRegression_s(*args)
    elif G.tag == dTag: lib.ElLogisticRegression_d(*args)
    else: DataExcept()
    return z, numIts
  elif type(G) is DistMatrix:
    z = DistMatrix(G.tag,MC,MR,G.Grid())
    args = [G.obj,q.obj,z.obj,gamma,penalty,pointer(numIts)]
    if   G.tag == sTag: lib.ElLogisticRegressionDist_s(*args)
    elif G.tag == dTag: lib.ElLogisticRegressionDist_d(*args)
    else: DataExcept()
    return z, numIts
  else: TypeExcept()

# Model fit
# =========
lib.ElModelFit_s.argtypes = \
lib.ElModelFitDist_s.argtypes = \
  [CFUNCTYPE(None,c_void_p,sType),CFUNCTYPE(None,c_void_p,sType),
   c_void_p,c_void_p,c_void_p,sType,POINTER(iType)]
lib.ElModelFit_d.argtypes = \
lib.ElModelFitDist_d.argtypes = \
  [CFUNCTYPE(None,c_void_p,dType),CFUNCTYPE(None,c_void_p,dType),
   c_void_p,c_void_p,c_void_p,dType,POINTER(iType)]
lib.ElModelFit_s.restype = \
lib.ElModelFit_d.restype = \
lib.ElModelFitDist_s.restype = \
lib.ElModelFitDist_d.restype = \
  c_uint

def ModelFit(lossProx,regProx,A,b,rho=1.2):
  if type(A) is not type(b):
    raise Exception('Types of A and b must match')
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  numIts = iType()
  cLoss = CFUNCTYPE(None,c_void_p,TagToType(A.tag))(lossProx)
  cReg = CFUNCTYPE(None,c_void_p,TagToType(A.tag))(regProx)
  if type(A) is Matrix:
    w = Matrix(A.tag)
    args = [cLoss,cReg,A.obj,b.obj,w.obj,rho,pointer(numIts)]
    if   A.tag == sTag: lib.ElModelFit_s(*args)
    elif A.tag == dTag: lib.ElModelFit_d(*args)
    else: DataExcept()
    return w, numIts
  elif type(A) is DistMatrix:
    w = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [cLoss,cReg,A.obj,b.obj,w.obj,rho,pointer(numIts)]
    if   A.tag == sTag: lib.ElModelFitDist_s(*args)
    elif A.tag == dTag: lib.ElModelFitDist_d(*args)
    else: DataExcept()
    return w, numIts
  else: TypeExcept()

# Non-negative matrix factorization
# =================================
lib.ElNMF_s.argtypes = \
lib.ElNMF_d.argtypes = \
lib.ElNMFDist_s.argtypes = \
lib.ElNMFDist_d.argtypes = \
  [c_void_p,c_void_p,c_void_p]
lib.ElNMF_s.restype = \
lib.ElNMF_d.restype = \
lib.ElNMFDist_s.restype = \
lib.ElNMFDist_d.restype = \
  c_uint

def NMF(A):
  args = [A.obj,X.obj,Y.obj]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElNMF_s(*args)
    elif A.tag == dTag: lib.ElNMF_d(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElNMFDist_s(*args)
    elif A.tag == dTag: lib.ElNMFDist_d(*args)
    else: DataExcept()
  else: TypeExcept()

# Non-negative least squares
# ==========================
lib.ElNNLS_s.argtypes = \
lib.ElNNLS_d.argtypes = \
lib.ElNNLSDist_s.argtypes = \
lib.ElNNLSDist_d.argtypes = \
lib.ElNNLSSparse_s.argtypes = \
lib.ElNNLSSparse_d.argtypes = \
lib.ElNNLSDistSparse_s.argtypes = \
lib.ElNNLSDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p]
lib.ElNNLS_s.restype = \
lib.ElNNLS_d.restype = \
lib.ElNNLSDist_s.restype = \
lib.ElNNLSDist_d.restype = \
lib.ElNNLSSparse_s.restype = \
lib.ElNNLSSparse_d.restype = \
lib.ElNNLSDistSparse_s.restype = \
lib.ElNNLSDistSparse_d.restype = \
  c_uint

def NNLS(A,b):
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    if   A.tag == sTag: lib.ElNNLS_s(*args)
    elif A.tag == dTag: lib.ElNNLS_d(*args)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,x.obj]
    if   A.tag == sTag: lib.ElNNLSDist_s(*args)
    elif A.tag == dTag: lib.ElNNLSDist_d(*args)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = SparseMatrix(A.tag)
    args = [A.obj,b.obj,x.obj]
    if   A.tag == sTag: lib.ElNNLSSparse_s(*args)
    elif A.tag == dTag: lib.ElNNLSSparse_d(*args)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,b.obj,x.obj]
    if   A.tag == sTag: lib.ElNNLSDistSparse_s(*args)
    elif A.tag == dTag: lib.ElNNLSDistSparse_d(*args)
    else: DataExcept()
    return x
  else: TypeExcept()

# ADMM
# ----
lib.ElNNLSADMM_s.argtypes = \
lib.ElNNLSADMM_d.argtypes = \
lib.ElNNLSADMMDist_s.argtypes = \
lib.ElNNLSADMMDist_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,POINTER(iType)]
lib.ElNNLSADMM_s.restype = \
lib.ElNNLSADMM_d.restype = \
lib.ElNNLSADMMDist_s.restype = \
lib.ElNNLSADMMDist_d.restype = \
  c_uint

def NNLSADMM(A,B):
  if type(A) is not type(B):
    raise Exception('Types of A and B must match')
  if A.tag != B.tag:
    raise Exception('Datatypes of A and B must match')
  numIts = iType()
  if type(A) is Matrix:
    X = Matrix(A.tag)
    args = [A.obj,B.obj,X.obj,pointer(numIts)]
    if   A.tag == sTag: lib.ElNNLSADMM_s(*args)
    elif A.tag == dTag: lib.ElNNLSADMM_d(*args)
    else: DataExcept()
    return X, numIts
  elif type(A) is DistMatrix:
    X = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,B.obj,X.obj,pointer(numIts)]
    if   A.tag == sTag: lib.ElNNLSADMMDist_s(*args)
    elif A.tag == dTag: lib.ElNNLSADMMDist_d(*args)
    else: DataExcept()
    return X, numIts
  else: TypeExcept()

# Quadratic program
# =================
(QP_ADMM,QP_IPF,QP_IPF_SELFDUAL,QP_MEHROTRA,QP_MEHROTRA_SELFDUAL)=(0,1,2,3,4)

lib.ElQPIPFLineSearchCtrlDefault_s.argtypes = \
lib.ElQPIPFLineSearchCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPIPFLineSearchCtrlDefault_s.restype = \
lib.ElQPIPFLineSearchCtrlDefault_d.restype = c_uint
class QPIPFLineSearchCtrl_s(ctypes.Structure):
  _fields_ = [("gamma",sType),("beta",sType),("psi",sType),
              ("stepRatio",sType),("progress",bType)]
  def __init__(self):
    lib.ElQPIPFLineSearchCtrlDefault_s(pointer(self))
class QPIPFLineSearchCtrl_d(ctypes.Structure):
  _fields_ = [("gamma",dType),("beta",dType),("psi",dType),
              ("stepRatio",dType),("progress",bType)]
  def __init__(self):
    lib.ElQPIPFLineSearchCtrlDefault_d(pointer(self))

# Direct conic form
# -----------------
(QP_DIRECT_FULL_KKT,QP_DIRECT_AUGMENTED_KKT) = (0,1)

lib.ElQPDirectIPFCtrlDefault_s.argtypes = \
lib.ElQPDirectIPFCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPDirectIPFCtrlDefault_s.restype = \
lib.ElQPDirectIPFCtrlDefault_d.restype = c_uint
class QPDirectIPFCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("centering",sType),
              ("system",c_uint),("lineSearchCtrl",QPIPFLineSearchCtrl_s),
              ("progress",bType)]
  def __init__(self):
    lib.ElQPDirectIPFCtrlDefault_s(pointer(self))
class QPDirectIPFCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("centering",dType),
              ("system",c_uint),("lineSearchCtrl",QPIPFLineSearchCtrl_d),
              ("progress",bType)]
  def __init__(self):
    lib.ElQPDirectIPFCtrlDefault_d(pointer(self))

lib.ElQPDirectMehrotraCtrlDefault_s.argtypes = \
lib.ElQPDirectMehrotraCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPDirectMehrotraCtrlDefault_s.restype = \
lib.ElQPDirectMehrotraCtrlDefault_d.restype = c_uint
class QPDirectMehrotraCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("maxStepRatio",sType),
              ("system",c_uint),("progress",bType)]
  def __init__(self):
    lib.ElQPDirectMehrotraCtrlDefault_s(pointer(self))
class QPDirectMehrotraCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("maxStepRatio",dType),
              ("system",c_uint),("progress",bType)]
  def __init__(self):
    lib.ElQPDirectMehrotraCtrlDefault_d(pointer(self))

lib.ElQPDirectCtrlDefault_s.argtypes = \
lib.ElQPDirectCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPDirectCtrlDefault_s.restype = \
lib.ElQPDirectCtrlDefault_d.restype = c_uint
class QPDirectCtrl_s(ctypes.Structure):
  _fields_ = [("approach",c_uint),
              ("ipfCtrl",QPDirectIPFCtrl_s),
              ("mehrotraCtrl",QPDirectMehrotraCtrl_s)]
  def __init__(self):
    lib.ElQPDirectCtrlDefault_s(pointer(self))
class QPDirectCtrl_d(ctypes.Structure):
  _fields_ = [("approach",c_uint),
              ("ipfCtrl",QPDirectIPFCtrl_d),
              ("mehrotraCtrl",QPDirectMehrotraCtrl_d)]
  def __init__(self):
    lib.ElQPDirectCtrlDefault_d(pointer(self))

lib.ElQPDirect_s.argtypes = \
lib.ElQPDirect_d.argtypes = \
lib.ElQPDirectDist_s.argtypes = \
lib.ElQPDirectDist_d.argtypes = \
lib.ElQPDirectSparse_s.argtypes = \
lib.ElQPDirectSparse_d.argtypes = \
lib.ElQPDirectDistSparse_s.argtypes = \
lib.ElQPDirectDistSparse_d.argtypes = \
  [c_void_p,c_void_p,
   c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p]
lib.ElQPDirect_s.restype = \
lib.ElQPDirect_d.restype = \
lib.ElQPDirectDist_s.restype = \
lib.ElQPDirectDist_d.restype = \
lib.ElQPDirectSparse_s.restype = \
lib.ElQPDirectSparse_d.restype = \
lib.ElQPDirectDistSparse_s.restype = \
lib.ElQPDirectDistSparse_d.restype = \
  c_uint

lib.ElQPDirectX_s.argtypes = \
lib.ElQPDirectXSparse_s.argtypes = \
lib.ElQPDirectXDist_s.argtypes = \
lib.ElQPDirectXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,
   c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   QPDirectCtrl_s]
lib.ElQPDirectX_d.argtypes = \
lib.ElQPDirectXSparse_d.argtypes = \
lib.ElQPDirectXDist_d.argtypes = \
lib.ElQPDirectXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,
   c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   QPDirectCtrl_d]
lib.ElQPDirectX_s.restype = \
lib.ElQPDirectX_d.restype = \
lib.ElQPDirectXSparse_s.restype = \
lib.ElQPDirectXSparse_d.restype = \
lib.ElQPDirectXDist_s.restype = \
lib.ElQPDirectXDist_d.restype = \
lib.ElQPDirectXDistSparse_s.restype = \
lib.ElQPDirectXDistSparse_d.restype = \
  c_uint

def QPDirect(Q,A,b,c,x,y,z,ctrl=None):
  if type(Q) is not type(A):
    raise Exception('A and Q must be of the same type')
  if type(b) is not type(c) or type(b) is not type(x) or \
     type(b) is not type(y) or type(b) is not type(z):
    raise Exception('{b,c,x,y,z} must be of the same type')
  args = [Q.obj,A.obj,b.obj,c.obj,x.obj,y.obj,z.obj]
  argsCtrl = [Q.obj,A.obj,b.obj,c.obj,x.obj,y.obj,z.obj,ctrl]
  if type(A) is Matrix:
    if type(b) is not Matrix: raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPDirect_s(*args)
      else:            lib.ElQPDirectX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPDirect_d(*args)
      else:            lib.ElQPDirectX_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix: raise Exception('b must be a DistMatrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPDirectDist_s(*args)
      else:            lib.ElQPDirectXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPDirectDist_d(*args)
      else:            lib.ElQPDirectXDist_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix: raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPDirectSparse_s(*args)
      else:            lib.ElQPDirectXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPDirectSparse_d(*args)
      else:            lib.ElQPDirectXSparse_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec: raise Exception('b must be a DistMultiVec')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPDirectDistSparse_s(*args)
      else:            lib.ElQPDirectXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPDirectDistSparse_d(*args)
      else:            lib.ElQPDirectXDistSparse_d(*argsCtrl)
    else: DataExcept()
  else: TypeExcept()

# Affine conic form
# -----------------
lib.ElQPAffineIPFCtrlDefault_s.argtypes = \
lib.ElQPAffineIPFCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPAffineIPFCtrlDefault_s.restype = \
lib.ElQPAffineIPFCtrlDefault_d.restype = c_uint
class QPAffineIPFCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("centering",sType),
              ("lineSearchCtrl",QPIPFLineSearchCtrl_s),
              ("progress",bType)]
  def __init__(self):
    lib.ElQPAffineIPFCtrlDefault_s(pointer(self))
class QPAffineIPFCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("centering",dType),
              ("lineSearchCtrl",QPIPFLineSearchCtrl_d),
              ("progress",bType)]
  def __init__(self):
    lib.ElQPAffineIPFCtrlDefault_d(pointer(self))

lib.ElQPAffineMehrotraCtrlDefault_s.argtypes = \
lib.ElQPAffineMehrotraCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPAffineMehrotraCtrlDefault_s.restype = \
lib.ElQPAffineMehrotraCtrlDefault_d.restype = c_uint
class QPAffineMehrotraCtrl_s(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",sType),("maxIts",iType),("maxStepRatio",sType),
              ("progress",bType)]
  def __init__(self):
    lib.ElQPAffineMehrotraCtrlDefault_s(pointer(self))
class QPAffineMehrotraCtrl_d(ctypes.Structure):
  _fields_ = [("primalInitialized",bType),("dualInitialized",bType),
              ("tol",dType),("maxIts",iType),("maxStepRatio",dType),
              ("progress",bType)]
  def __init__(self):
    lib.ElQPAffineMehrotraCtrlDefault_d(pointer(self))

lib.ElQPAffineCtrlDefault_s.argtypes = \
lib.ElQPAffineCtrlDefault_d.argtypes = [c_void_p]
lib.ElQPAffineCtrlDefault_s.restype = \
lib.ElQPAffineCtrlDefault_d.restype = c_uint
class QPAffineCtrl_s(ctypes.Structure):
  _fields_ = [("approach",c_uint),
              ("ipfCtrl",QPAffineIPFCtrl_s),
              ("mehrotraCtrl",QPAffineMehrotraCtrl_s)]
  def __init__(self):
    lib.ElQPAffineCtrlDefault_s(pointer(self))
class QPAffineCtrl_d(ctypes.Structure):
  _fields_ = [("approach",c_uint),
              ("ipfCtrl",QPAffineIPFCtrl_d),
              ("mehrotraCtrl",QPAffineMehrotraCtrl_d)]
  def __init__(self):
    lib.ElQPAffineCtrlDefault_d(pointer(self))

lib.ElQPAffine_s.argtypes = \
lib.ElQPAffine_d.argtypes = \
lib.ElQPAffineDist_s.argtypes = \
lib.ElQPAffineDist_d.argtypes = \
lib.ElQPAffineSparse_s.argtypes = \
lib.ElQPAffineSparse_d.argtypes = \
lib.ElQPAffineDistSparse_s.argtypes = \
lib.ElQPAffineDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,c_void_p]
lib.ElQPAffine_s.restype = \
lib.ElQPAffine_d.restype = \
lib.ElQPAffineDist_s.restype = \
lib.ElQPAffineDist_d.restype = \
lib.ElQPAffineSparse_s.restype = \
lib.ElQPAffineSparse_d.restype = \
lib.ElQPAffineDistSparse_s.restype = \
lib.ElQPAffineDistSparse_d.restype = \
  c_uint

lib.ElQPAffineX_s.argtypes = \
lib.ElQPAffineXDist_s.argtypes = \
lib.ElQPAffineXSparse_s.argtypes = \
lib.ElQPAffineXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,c_void_p,
   QPAffineCtrl_s]
lib.ElQPAffineX_d.argtypes = \
lib.ElQPAffineXDist_d.argtypes = \
lib.ElQPAffineXSparse_d.argtypes = \
lib.ElQPAffineXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,
   c_void_p,c_void_p,c_void_p,c_void_p,
   QPAffineCtrl_d]
lib.ElQPAffineX_s.restype = \
lib.ElQPAffineX_d.restype = \
lib.ElQPAffineXDist_s.restype = \
lib.ElQPAffineXDist_d.restype = \
lib.ElQPAffineXSparse_s.restype = \
lib.ElQPAffineXSparse_d.restype = \
lib.ElQPAffineXDistSparse_s.restype = \
lib.ElQPAffineXDistSparse_d.restype = \
  c_uint

def QPAffine(Q,A,G,b,c,h,x,y,z,s,ctrl=None):
  if type(Q) is not type(A) or type(A) is not type(G):
    raise Exception('{Q,A,G} must be of the same type')
  if type(b) is not type(c) or type(b) is not type(c) or \
     type(b) is not type(h) or type(b) is not type(x) or \
     type(b) is not type(y) or type(b) is not type(z) or \
     type(b) is not type(s):
    raise Exception('{b,c,h,x,y,z,s} must be of the same type')
  args = [Q.obj,A.obj,G.obj,b.obj,c.obj,h.obj,x.obj,y.obj,z.obj,s.obj]
  argsCtrl = [Q.obj,A.obj,G.obj,b.obj,c.obj,h.obj,x.obj,y.obj,z.obj,s.obj,ctrl]
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPAffine_s(*args)
      else:            lib.ElQPAffineX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPAffine_d(*args)
      else:            lib.ElQPAffineX_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPAffineDist_s(*args)
      else:            lib.ElQPAffineXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPAffineDist_d(*args)
      else:            lib.ElQPAffineXDist_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPAffineSparse_s(*args)
      else:            lib.ElQPAffineXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPAffineSparse_d(*args)
      else:            lib.ElQPAffineXSparse_d(*argsCtrl)
    else: DataExcept()
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    if   A.tag == sTag: 
      if ctrl == None: lib.ElQPAffineDistSparse_s(*args)
      else:            lib.ElQPAffineXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElQPAffineDistSparse_d(*args)
      else:            lib.ElQPAffineXDistSparse_d(*argsCtrl)
    else: DataExcept()
  else: TypeExcept()

# Box form
# --------
lib.ElQPBoxADMM_s.argtypes = \
lib.ElQPBoxADMMDist_s.argtypes = \
  [c_void_p,c_void_p,sType,sType,c_void_p,POINTER(iType)]
lib.ElQPBoxADMM_d.argtypes = \
lib.ElQPBoxADMMDist_d.argtypes = \
  [c_void_p,c_void_p,dType,dType,c_void_p,POINTER(iType)]
lib.ElQPBoxADMM_s.restype = \
lib.ElQPBoxADMM_d.restype = \
lib.ElQPBoxADMMDist_s.restype = \
lib.ElQPBoxADMMDist_d.restype = \
  c_uint

def QPBoxADMM(Q,C,lb,ub):
  if type(Q) is not type(C):
    raise Exception('Types of Q and C must match')
  if Q.tag != C.tag:
    raise Exception('Datatypes of Q and C must match')
  numIts = iType()
  if type(Q) is Matrix:
    Z = Matrix(Q.tag)
    args = [Q.obj,C.obj,lb,ub,Z.obj,pointer(numIts)]
    if   Q.tag == sTag: lib.ElQPBoxADMM_s(*args)
    elif Q.tag == dTag: lib.ElQPBoxADMM_d(*args)
    else: DataExcept()
    return Z, numIts
  elif type(Q) is DistMatrix:
    Z = DistMatrix(Q.tag,MC,MR,Q.Grid())
    args = [Q.obj,C.obj,lb,ub,Z.obj,pointer(numIts)]
    if   Q.tag == sTag: lib.ElQPBoxADMMDist_s(*args)
    elif Q.tag == dTag: lib.ElQPBoxADMMDist_d(*args)
    else: DataExcept()
    return Z, numIts
  else: TypeExcept()

# Basis pursuit denoising
# =======================
lib.ElBPDN_s.argtypes = \
lib.ElBPDNDist_s.argtypes = \
lib.ElBPDNSparse_s.argtypes = \
lib.ElBPDNDistSparse_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p]
lib.ElBPDN_d.argtypes = \
lib.ElBPDNDist_d.argtypes = \
lib.ElBPDNSparse_d.argtypes = \
lib.ElBPDNDistSparse_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p]

lib.ElBPDN_s.restype = \
lib.ElBPDN_d.restype = \
lib.ElBPDNDist_s.restype = \
lib.ElBPDNDist_d.restype = \
lib.ElBPDNSparse_s.restype = \
lib.ElBPDNSparse_d.restype = \
lib.ElBPDNDistSparse_s.restype = \
lib.ElBPDNDistSparse_d.restype = \
  c_uint

lib.ElBPDNX_s.argtypes = \
lib.ElBPDNXDist_s.argtypes = \
lib.ElBPDNXSparse_s.argtypes = \
lib.ElBPDNXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p,
   QPAffineCtrl_s]
lib.ElBPDNX_d.argtypes = \
lib.ElBPDNXDist_d.argtypes = \
lib.ElBPDNXSparse_d.argtypes = \
lib.ElBPDNXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p,
   QPAffineCtrl_d]
lib.ElBPDNX_s.restype = \
lib.ElBPDNX_d.restype = \
lib.ElBPDNXDist_s.restype = \
lib.ElBPDNXDist_d.restype = \
lib.ElBPDNXSparse_s.restype = \
lib.ElBPDNXSparse_d.restype = \
lib.ElBPDNXDistSparse_s.restype = \
lib.ElBPDNXDistSparse_d.restype = \
  c_uint

def BPDN(A,b,lambdPre,ctrl=None):
  if A.tag != b.tag:
    raise Exception('Datatypes of A and b must match')
  lambd = TagToType(A.tag)(lambdPre)
  if type(A) is Matrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPDN_s(*args)
      else:            lib.ElBPDNX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPDN_d(*args)
      else:            lib.ElBPDNX_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(b) is not DistMatrix:
      raise Exception('b must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPDNDist_s(*args)
      else:            lib.ElBPDNXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPDNDist_d(*args)
      else:            lib.ElBPDNXDist_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(b) is not Matrix:
      raise Exception('b must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPDNSparse_s(*args)
      else:            lib.ElBPDNXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPDNSparse_d(*args)
      else:            lib.ElBPDNXSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(b) is not DistMultiVec:
      raise Exception('b must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,b.obj,lambd,x.obj]
    argsCtrl = [A.obj,b.obj,lambd,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElBPDNDistSparse_s(*args)
      else:            lib.ElBPDNXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElBPDNDistSparse_d(*args)
      else:            lib.ElBPDNXDistSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  else: TypeExcept()

# ADMM
# ----
lib.ElBPDNADMM_s.argtypes = \
lib.ElBPDNADMM_c.argtypes = \
lib.ElBPDNADMMDist_s.argtypes = \
lib.ElBPDNADMMDist_c.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p,POINTER(iType)]
lib.ElBPDNADMM_d.argtypes = \
lib.ElBPDNADMM_z.argtypes = \
lib.ElBPDNADMMDist_d.argtypes = \
lib.ElBPDNADMMDist_z.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p,POINTER(iType)]

lib.ElBPDNADMM_s.restype = \
lib.ElBPDNADMM_d.restype = \
lib.ElBPDNADMM_c.restype = \
lib.ElBPDNADMM_z.restype = \
lib.ElBPDNADMMDist_s.restype = \
lib.ElBPDNADMMDist_d.restype = \
lib.ElBPDNADMMDist_c.restype = \
lib.ElBPDNADMMDist_z.restype = \
  c_uint

def BPDNADMM(A,b,lamb):
  if type(A) is not type(b): raise Exception('Types of A and b must match')
  if A.tag != b.tag: raise Exception('Datatypes of A and b must match')
  numIts = iType()
  if type(A) is Matrix:
    z = Matrix(A.tag)
    args = [A.obj,b.obj,lamb,z.obj,pointer(numIts)]
    if   A.tag == sTag: lib.ElBPDNADMM_s(*args)
    elif A.tag == dTag: lib.ElBPDNADMM_d(*args)
    elif A.tag == cTag: lib.ElBPDNADMM_c(*args)
    elif A.tag == zTag: lib.ElBPDNADMM_z(*args)
    else: DataExcept()
    return z, numIts
  elif type(A) is DistMatrix:
    z = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,b.obj,lamb,z.obj,pointer(numIts)]
    if   A.tag == sTag: lib.ElBPDNADMMDist_s(*args)
    elif A.tag == dTag: lib.ElBPDNADMMDist_d(*args)
    elif A.tag == cTag: lib.ElBPDNADMMDist_c(*args)
    elif A.tag == zTag: lib.ElBPDNADMMDist_z(*args)
    else: DataExcept()
    return z, numIts
  else: TypeExcept()

# Robust Principal Component Analysis
# ===================================
lib.ElRPCA_s.argtypes = \
lib.ElRPCA_d.argtypes = \
lib.ElRPCA_c.argtypes = \
lib.ElRPCA_z.argtypes = \
lib.ElRPCADist_s.argtypes = \
lib.ElRPCADist_d.argtypes = \
lib.ElRPCADist_c.argtypes = \
lib.ElRPCADist_z.argtypes = \
  [c_void_p,c_void_p,c_void_p]
lib.ElRPCA_s.restype = \
lib.ElRPCA_d.restype = \
lib.ElRPCA_c.restype = \
lib.ElRPCA_z.restype = \
lib.ElRPCADist_s.restype = \
lib.ElRPCADist_d.restype = \
lib.ElRPCADist_c.restype = \
lib.ElRPCADist_z.restype = \
  c_uint

def RPCA(M):
  if type(M) is Matrix:
    L = Matrix(M.tag)
    S = Matrix(M.tag)
    args = [M.obj,L.obj,S.obj]
    if   M.tag == sTag: lib.ElRPCA_s(*args)
    elif M.tag == dTag: lib.ElRPCA_d(*args)
    elif M.tag == cTag: lib.ElRPCA_c(*args)
    elif M.tag == zTag: lib.ElRPCA_z(*args)
    return L, S
  elif type(M) is DistMatrix:
    L = DistMatrix(M.tag,MC,MR,M.Grid())
    S = DistMatrix(M.tag,MC,MR,M.Grid())
    args = [M.obj,L.obj,S.obj]
    if   M.tag == sTag: lib.ElRPCADist_s(*args)
    elif M.tag == dTag: lib.ElRPCADist_d(*args)
    elif M.tag == cTag: lib.ElRPCADist_c(*args)
    elif M.tag == zTag: lib.ElRPCADist_z(*args)
    return L, S
  else: TypeExcept()

# Sparse inverse covariance selection
# ===================================
lib.ElSparseInvCov_s.argtypes = \
lib.ElSparseInvCov_c.argtypes = \
lib.ElSparseInvCovDist_s.argtypes = \
lib.ElSparseInvCovDist_c.argtypes = \
  [c_void_p,sType,c_void_p,POINTER(iType)]
lib.ElSparseInvCov_d.argtypes = \
lib.ElSparseInvCov_z.argtypes = \
lib.ElSparseInvCovDist_d.argtypes = \
lib.ElSparseInvCovDist_z.argtypes = \
  [c_void_p,dType,c_void_p,POINTER(iType)]

lib.ElSparseInvCov_s.restype = \
lib.ElSparseInvCov_d.restype = \
lib.ElSparseInvCov_c.restype = \
lib.ElSparseInvCov_z.restype = \
lib.ElSparseInvCovDist_s.restype = \
lib.ElSparseInvCovDist_d.restype = \
lib.ElSparseInvCovDist_c.restype = \
lib.ElSparseInvCovDist_z.restype = \
  c_uint

def SparseInvCov(D,lamb):
  numIts = iType()
  if type(D) is Matrix:
    Z = Matrix(D.tag)
    args = [D.obj,lamb,Z.obj,pointer(numIts)]
    if   D.tag == sTag: lib.ElSparseInvCov_s(*args)
    elif D.tag == dTag: lib.ElSparseInvCov_d(*args)
    elif D.tag == cTag: lib.ElSparseInvCov_c(*args)
    elif D.tag == zTag: lib.ElSparseInvCov_z(*args)
    else: DataExcept()
    return Z, numIts
  elif type(D) is DistMatrix:
    Z = DistMatrix(D.tag,MC,MR,D.Grid())
    args = [D.obj,lamb,Z.obj,pointer(numIts)]
    if   D.tag == sTag: lib.ElSparseInvCovDist_s(*args)
    elif D.tag == dTag: lib.ElSparseInvCovDist_d(*args)
    elif D.tag == cTag: lib.ElSparseInvCovDist_c(*args)
    elif D.tag == zTag: lib.ElSparseInvCovDist_z(*args)
    else: DataExcept()
    return Z, numIts
  else: TypeExcept()

# Support Vector Machine
# ======================
lib.ElSVM_s.argtypes = \
lib.ElSVMDist_s.argtypes = \
lib.ElSVMSparse_s.argtypes = \
lib.ElSVMDistSparse_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p]
lib.ElSVM_d.argtypes = \
lib.ElSVMDist_d.argtypes = \
lib.ElSVMSparse_d.argtypes = \
lib.ElSVMDistSparse_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p]

lib.ElSVM_s.restype = \
lib.ElSVM_d.restype = \
lib.ElSVMDist_s.restype = \
lib.ElSVMDist_d.restype = \
lib.ElSVMSparse_s.restype = \
lib.ElSVMSparse_d.restype = \
lib.ElSVMDistSparse_s.restype = \
lib.ElSVMDistSparse_d.restype = \
  c_uint

lib.ElSVMX_s.argtypes = \
lib.ElSVMXDist_s.argtypes = \
lib.ElSVMXSparse_s.argtypes = \
lib.ElSVMXDistSparse_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p,
   QPAffineCtrl_s]
lib.ElSVMX_d.argtypes = \
lib.ElSVMXDist_d.argtypes = \
lib.ElSVMXSparse_d.argtypes = \
lib.ElSVMXDistSparse_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p,
   QPAffineCtrl_d]
lib.ElSVMX_s.restype = \
lib.ElSVMX_d.restype = \
lib.ElSVMXDist_s.restype = \
lib.ElSVMXDist_d.restype = \
lib.ElSVMXSparse_s.restype = \
lib.ElSVMXSparse_d.restype = \
lib.ElSVMXDistSparse_s.restype = \
lib.ElSVMXDistSparse_d.restype = \
  c_uint

def SVM(A,d,lambdPre,ctrl=None):
  if A.tag != d.tag:
    raise Exception('Datatypes of A and d must match')
  lambd = TagToType(A.tag)(lambdPre)
  if type(A) is Matrix:
    if type(d) is not Matrix:
      raise Exception('d must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,d.obj,lambd,x.obj]
    argsCtrl = [A.obj,d.obj,lambd,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElSVM_s(*args)
      else:            lib.ElSVMX_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElSVM_d(*args)
      else:            lib.ElSVMX_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistMatrix:
    if type(d) is not DistMatrix:
      raise Exception('d must be a DistMatrix')
    x = DistMatrix(A.tag,MC,MR,A.Grid())
    args = [A.obj,d.obj,lambd,x.obj]
    argsCtrl = [A.obj,d.obj,lambd,x.obj,ctrl] 
    if   A.tag == sTag: 
      if ctrl == None: lib.ElSVMDist_s(*args)
      else:            lib.ElSVMXDist_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElSVMDist_d(*args)
      else:            lib.ElSVMXDist_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is SparseMatrix:
    if type(d) is not Matrix:
      raise Exception('d must be a Matrix')
    x = Matrix(A.tag)
    args = [A.obj,d.obj,lambd,x.obj]
    argsCtrl = [A.obj,d.obj,lambd,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElSVMSparse_s(*args)
      else:            lib.ElSVMXSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElSVMSparse_d(*args)
      else:            lib.ElSVMXSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  elif type(A) is DistSparseMatrix:
    if type(d) is not DistMultiVec:
      raise Exception('d must be a DistMultiVec')
    x = DistMultiVec(A.tag,A.Comm())
    args = [A.obj,d.obj,lambd,x.obj]
    argsCtrl = [A.obj,d.obj,lambd,x.obj,ctrl]
    if   A.tag == sTag: 
      if ctrl == None: lib.ElSVMDistSparse_s(*args)
      else:            lib.ElSVMXDistSparse_s(*argsCtrl)
    elif A.tag == dTag: 
      if ctrl == None: lib.ElSVMDistSparse_d(*args)
      else:            lib.ElSVMXDistSparse_d(*argsCtrl)
    else: DataExcept()
    return x
  else: TypeExcept()

# ADMM
# ----
lib.ElSVMADMM_s.argtypes = \
lib.ElSVMADMMDist_s.argtypes = \
  [c_void_p,c_void_p,sType,c_void_p,POINTER(iType)]
lib.ElSVMADMM_d.argtypes = \
lib.ElSVMADMMDist_d.argtypes = \
  [c_void_p,c_void_p,dType,c_void_p,POINTER(iType)]
lib.ElSVMADMM_s.restype = \
lib.ElSVMADMM_d.restype = \
lib.ElSVMADMMDist_s.restype = \
lib.ElSVMADMMDist_d.restype = \
  c_uint

def SVMADMM(G,q,gamma):
  if type(G) is not type(q):
    raise Exception('Types of G and q must match')
  if G.tag != q.tag:
    raise Exception('Datatypes of G and q must match')
  numIts = iType()
  if type(G) is Matrix:
    z = Matrix(G.tag)
    args = [G.obj,q.obj,gamma,z.obj,pointer(numIts)]
    if   G.tag == sTag: lib.ElSVMADMM_s(*args)
    elif G.tag == dTag: lib.ElSVMADMM_d(*args)
    else: DataExcept()
    return z, numIts
  elif type(G) is DistMatrix:
    z = DistMatrix(G.tag,MC,MR,G.Grid())
    args = [G.obj,q.obj,gamma,z.obj,pointer(numIts)]
    if   G.tag == sTag: lib.ElSVMADMMDist_s(*args)
    elif G.tag == dTag: lib.ElSVMADMMDist_d(*args)
    else: DataExcept()
    return z, numIts
  else: TypeExcept()

# Utilities
# =========

# Clipping
# --------
lib.ElLowerClip_s.argtypes = \
lib.ElLowerClipDist_s.argtypes = \
  [c_void_p,sType]
lib.ElLowerClip_d.argtypes = \
lib.ElLowerClipDist_d.argtypes = \
  [c_void_p,dType]
lib.ElLowerClip_s.restype = \
lib.ElLowerClip_d.restype = \
lib.ElLowerClipDist_s.restype = \
lib.ElLowerClipDist_d.restype = \
  c_uint

def LowerClip(X,lowerBound=0):
  args = [X.obj,lowerBound]
  if type(X) is Matrix:
    if   X.tag == sTag: lib.ElLowerClip_s(*args)
    elif X.tag == dTag: lib.ElLowerClip_d(*args)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == sTag: lib.ElLowerClipDist_s(*args)
    elif X.tag == dTag: lib.ElLowerClipDist_d(*args)
    else: DataExcept()
  else: TypeExcept()

lib.ElUpperClip_s.argtypes = \
lib.ElUpperClipDist_s.argtypes = \
  [c_void_p,sType]
lib.ElUpperClip_d.argtypes = \
lib.ElUpperClipDist_d.argtypes = \
  [c_void_p,dType]
lib.ElUpperClip_s.restype = \
lib.ElUpperClip_d.restype = \
lib.ElUpperClipDist_s.restype = \
lib.ElUpperClipDist_d.restype = \
  c_uint

def UpperClip(X,upperBound=1):
  args = [X.obj,upperBound]
  if type(X) is Matrix:
    if   X.tag == sTag: lib.ElUpperClip_s(*args)
    elif X.tag == dTag: lib.ElUpperClip_d(*args)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == sTag: lib.ElUpperClipDist_s(*args)
    elif X.tag == dTag: lib.ElUpperClipDist_d(*args)
    else: DataExcept()
  else: TypeExcept()

lib.ElClip_s.argtypes = \
lib.ElClipDist_s.argtypes = \
  [c_void_p,sType,sType]
lib.ElClip_d.argtypes = \
lib.ElClipDist_d.argtypes = \
  [c_void_p,dType,dType]
lib.ElClip_s.restype = \
lib.ElClip_d.restype = \
lib.ElClipDist_s.restype = \
lib.ElClipDist_d.restype = \
  c_uint

def Clip(X,lowerBound=0,upperBound=1):
  args = [X.obj,lowerBound,upperBound]
  if type(X) is Matrix:
    if   X.tag == sTag: lib.ElClip_s(*args)
    elif X.tag == dTag: lib.ElClip_d(*args)
    else: DataExcept()
  elif type(X) is DistMatrix:
    if   X.tag == sTag: lib.ElClipDist_s(*args)
    elif X.tag == dTag: lib.ElClipDist_d(*args)
    else: DataExcept()
  else: TypeExcept()

# Coherence
# ---------
lib.ElCoherence_s.argtypes = \
lib.ElCoherence_c.argtypes = \
lib.ElCoherenceDist_s.argtypes = \
lib.ElCoherenceDist_c.argtypes = \
  [c_void_p,POINTER(sType)]
lib.ElCoherence_d.argtypes = \
lib.ElCoherence_z.argtypes = \
lib.ElCoherenceDist_d.argtypes = \
lib.ElCoherenceDist_z.argtypes = \
  [c_void_p,POINTER(dType)]
lib.ElCoherence_s.restype = \
lib.ElCoherence_d.restype = \
lib.ElCoherence_c.restype = \
lib.ElCoherence_z.restype = \
lib.ElCoherenceDist_s.restype = \
lib.ElCoherenceDist_d.restype = \
lib.ElCoherenceDist_c.restype = \
lib.ElCoherenceDist_z.restype = \
  c_uint

def Coherence(A):
  value = TagToType(Base(A.tag))()
  args = [A.obj,pointer(value)]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElCoherence_s(*args)
    elif A.tag == dTag: lib.ElCoherence_d(*args)
    elif A.tag == cTag: lib.ElCoherence_c(*args)
    elif A.tag == zTag: lib.ElCoherence_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElCoherenceDist_s(*args)
    elif A.tag == dTag: lib.ElCoherenceDist_d(*args)
    elif A.tag == cTag: lib.ElCoherenceDist_c(*args)
    elif A.tag == zTag: lib.ElCoherenceDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
  return value

# Covariance
# ----------
lib.ElCovariance_s.argtypes = \
lib.ElCovariance_d.argtypes = \
lib.ElCovariance_c.argtypes = \
lib.ElCovariance_z.argtypes = \
lib.ElCovarianceDist_s.argtypes = \
lib.ElCovarianceDist_d.argtypes = \
lib.ElCovarianceDist_c.argtypes = \
lib.ElCovarianceDist_z.argtypes = \
  [c_void_p,c_void_p]

lib.ElCovariance_s.restype = \
lib.ElCovariance_d.restype = \
lib.ElCovariance_c.restype = \
lib.ElCovariance_z.restype = \
lib.ElCovarianceDist_s.restype = \
lib.ElCovarianceDist_d.restype = \
lib.ElCovarianceDist_c.restype = \
lib.ElCovarianceDist_z.restype = \
  c_uint

def Covariance(D):
  if type(D) is Matrix:
    S = Matrix(D.tag)
    args = [D.obj,S.obj]
    if   D.tag == sTag: lib.ElCovariance_s(*args)
    elif D.tag == dTag: lib.ElCovariance_d(*args)
    elif D.tag == cTag: lib.ElCovariance_c(*args)
    elif D.tag == zTag: lib.ElCovariance_z(*args)
    else: DataExcept()
    return S
  elif type(D) is DistMatrix:
    S = DistMatrix(D.tag,MC,MR,D.Grid())
    args = [D.obj,S.obj]
    if   D.tag == sTag: lib.ElCovarianceDist_s(*args)
    elif D.tag == dTag: lib.ElCovarianceDist_d(*args)
    elif D.tag == cTag: lib.ElCovarianceDist_c(*args)
    elif D.tag == zTag: lib.ElCovarianceDist_z(*args)
    else: DataExcept()
    return S
  else: TypeExcept()

# Frobenius-norm proximal map
# ---------------------------
lib.ElFrobeniusProx_s.argtypes = \
lib.ElFrobeniusProx_c.argtypes = \
lib.ElFrobeniusProxDist_s.argtypes = \
lib.ElFrobeniusProxDist_c.argtypes = \
  [c_void_p,sType]
lib.ElFrobeniusProx_d.argtypes = \
lib.ElFrobeniusProx_z.argtypes = \
lib.ElFrobeniusProxDist_d.argtypes = \
lib.ElFrobeniusProxDist_z.argtypes = \
  [c_void_p,dType]

lib.ElFrobeniusProx_s.restype = \
lib.ElFrobeniusProx_d.restype = \
lib.ElFrobeniusProx_c.restype = \
lib.ElFrobeniusProx_z.restype = \
lib.ElFrobeniusProxDist_s.restype = \
lib.ElFrobeniusProxDist_d.restype = \
lib.ElFrobeniusProxDist_c.restype = \
lib.ElFrobeniusProxDist_z.restype = \
  c_uint

def FrobeniusProx(A,rho):
  args = [A.obj,rho]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElFrobeniusProx_s(*args)
    elif A.tag == dTag: lib.ElFrobeniusProx_d(*args)
    elif A.tag == cTag: lib.ElFrobeniusProx_c(*args)
    elif A.tag == zTag: lib.ElFrobeniusProx_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElFrobeniusProxDist_s(*args)
    elif A.tag == dTag: lib.ElFrobeniusProxDist_d(*args)
    elif A.tag == cTag: lib.ElFrobeniusProxDist_c(*args)
    elif A.tag == zTag: lib.ElFrobeniusProxDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Hinge-loss proximal map
# -----------------------
lib.ElHingeLossProx_s.argtypes = \
lib.ElHingeLossProxDist_s.argtypes = \
  [c_void_p,sType]
lib.ElHingeLossProx_d.argtypes = \
lib.ElHingeLossProxDist_d.argtypes = \
  [c_void_p,dType]

lib.ElHingeLossProx_s.restype = \
lib.ElHingeLossProx_d.restype = \
lib.ElHingeLossProxDist_s.restype = \
lib.ElHingeLossProxDist_d.restype = \
  c_uint

def HingeLossProx(A,rho):
  args = [A.obj,rho]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElHingeLossProx_s(*args)
    elif A.tag == dTag: lib.ElHingeLossProx_d(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElHingeLossProxDist_s(*args)
    elif A.tag == dTag: lib.ElHingeLossProxDist_d(*args)
    else: DataExcept()
  else: TypeExcept()

# Log barrier
# -----------
lib.ElLogBarrier_s.argtypes = \
lib.ElLogBarrier_c.argtypes = \
lib.ElLogBarrierDist_s.argtypes = \
lib.ElLogBarrierDist_c.argtypes = \
  [c_uint,c_void_p,POINTER(sType)]
lib.ElLogBarrier_d.argtypes = \
lib.ElLogBarrier_z.argtypes = \
lib.ElLogBarrierDist_d.argtypes = \
lib.ElLogBarrierDist_z.argtypes = \
  [c_uint,c_void_p,POINTER(dType)]

lib.ElLogBarrier_s.restype = \
lib.ElLogBarrier_d.restype = \
lib.ElLogBarrier_c.restype = \
lib.ElLogBarrier_z.restype = \
lib.ElLogBarrierDist_s.restype = \
lib.ElLogBarrierDist_d.restype = \
lib.ElLogBarrierDist_c.restype = \
lib.ElLogBarrierDist_z.restype = \
  c_uint

def LogBarrier(uplo,A):
  barrier = TagToType(Base(A.tag))()
  args = [uplo,A.obj,pointer(barrier)]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElLogBarrier_s(*args)
    elif A.tag == dTag: lib.ElLogBarrier_d(*args)
    elif A.tag == cTag: lib.ElLogBarrier_c(*args)
    elif A.tag == zTag: lib.ElLogBarrier_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElLogBarrierDist_s(*args)
    elif A.tag == dTag: lib.ElLogBarrierDist_d(*args)
    elif A.tag == cTag: lib.ElLogBarrierDist_c(*args)
    elif A.tag == zTag: lib.ElLogBarrierDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
  return barrier

# Log-det divergence
# ------------------
lib.ElLogDetDiv_s.argtypes = \
lib.ElLogDetDiv_c.argtypes = \
lib.ElLogDetDivDist_s.argtypes = \
lib.ElLogDetDivDist_c.argtypes = \
  [c_uint,c_void_p,c_void_p,POINTER(sType)]
lib.ElLogDetDiv_d.argtypes = \
lib.ElLogDetDiv_z.argtypes = \
lib.ElLogDetDivDist_d.argtypes = \
lib.ElLogDetDivDist_z.argtypes = \
  [c_uint,c_void_p,c_void_p,POINTER(dType)]

lib.ElLogDetDiv_s.restype = \
lib.ElLogDetDiv_d.restype = \
lib.ElLogDetDiv_c.restype = \
lib.ElLogDetDiv_z.restype = \
lib.ElLogDetDivDist_s.restype = \
lib.ElLogDetDivDist_d.restype = \
lib.ElLogDetDivDist_c.restype = \
lib.ElLogDetDivDist_z.restype = \
  c_uint

def LogDetDiv(uplo,A,B):
  div = TagToType(Base(A.tag))()
  args = [uplo,A.obj,B.obj,pointer(div)]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElLogDetDiv_s(*args)
    elif A.tag == dTag: lib.ElLogDetDiv_d(*args)
    elif A.tag == cTag: lib.ElLogDetDiv_c(*args)
    elif A.tag == zTag: lib.ElLogDetDiv_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElLogDetDivDist_s(*args)
    elif A.tag == dTag: lib.ElLogDetDivDist_d(*args)
    elif A.tag == cTag: lib.ElLogDetDivDist_c(*args)
    elif A.tag == zTag: lib.ElLogDetDivDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
  return div

# Logistic proximal map
# ---------------------
lib.ElLogisticProx_s.argtypes = \
lib.ElLogisticProxDist_s.argtypes = \
  [c_void_p,sType]
lib.ElLogisticProx_d.argtypes = \
lib.ElLogisticProxDist_d.argtypes = \
  [c_void_p,dType]

lib.ElLogisticProx_s.restype = \
lib.ElLogisticProx_d.restype = \
lib.ElLogisticProxDist_s.restype = \
lib.ElLogisticProxDist_d.restype = \
  c_uint

def LogisticProx(A,rho):
  args = [A.obj,rho]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElLogisticProx_s(*args)
    elif A.tag == dTag: lib.ElLogisticProx_d(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElLogisticProxDist_s(*args)
    elif A.tag == dTag: lib.ElLogisticProxDist_d(*args)
    else: DataExcept()
  else: TypeExcept()

# Singular-value soft-thresholding
# --------------------------------
lib.ElSVT_s.argtypes = \
lib.ElSVT_c.argtypes = \
lib.ElSVTDist_s.argtypes = \
lib.ElSVTDist_c.argtypes = \
  [c_void_p,sType,bType]
lib.ElSVT_d.argtypes = \
lib.ElSVT_z.argtypes = \
lib.ElSVTDist_d.argtypes = \
lib.ElSVTDist_z.argtypes = \
  [c_void_p,dType,bType]

lib.ElSVT_s.restype = \
lib.ElSVT_d.restype = \
lib.ElSVT_c.restype = \
lib.ElSVT_z.restype = \
lib.ElSVTDist_s.restype = \
lib.ElSVTDist_d.restype = \
lib.ElSVTDist_c.restype = \
lib.ElSVTDist_z.restype = \
  c_uint

def SVT(A,rho,relative=False):
  args = [A.obj,rho,relative]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElSVT_s(*args)
    elif A.tag == dTag: lib.ElSVT_d(*args)
    elif A.tag == cTag: lib.ElSVT_c(*args)
    elif A.tag == zTag: lib.ElSVT_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElSVTDist_s(*args)
    elif A.tag == dTag: lib.ElSVTDist_d(*args)
    elif A.tag == cTag: lib.ElSVTDist_c(*args)
    elif A.tag == zTag: lib.ElSVTDist_z(*args)
    else: DataExcept()
  else: TypeExcept()

# Soft-thresholding
# -----------------
lib.ElSoftThreshold_s.argtypes = \
lib.ElSoftThreshold_c.argtypes = \
lib.ElSoftThresholdDist_s.argtypes = \
lib.ElSoftThresholdDist_c.argtypes = \
  [c_void_p,sType,bType]
lib.ElSoftThreshold_d.argtypes = \
lib.ElSoftThreshold_z.argtypes = \
lib.ElSoftThresholdDist_d.argtypes = \
lib.ElSoftThresholdDist_z.argtypes = \
  [c_void_p,dType,bType]

lib.ElSoftThreshold_s.restype = \
lib.ElSoftThreshold_d.restype = \
lib.ElSoftThreshold_c.restype = \
lib.ElSoftThreshold_z.restype = \
lib.ElSoftThresholdDist_s.restype = \
lib.ElSoftThresholdDist_d.restype = \
lib.ElSoftThresholdDist_c.restype = \
lib.ElSoftThresholdDist_z.restype = \
  c_uint

def SoftThreshold(A,rho,relative=False):
  args = [A.obj,rho,relative]
  if type(A) is Matrix:
    if   A.tag == sTag: lib.ElSoftThreshold_s(*args)
    elif A.tag == dTag: lib.ElSoftThreshold_d(*args)
    elif A.tag == cTag: lib.ElSoftThreshold_c(*args)
    elif A.tag == zTag: lib.ElSoftThreshold_z(*args)
    else: DataExcept()
  elif type(A) is DistMatrix:
    if   A.tag == sTag: lib.ElSoftThresholdDist_s(*args)
    elif A.tag == dTag: lib.ElSoftThresholdDist_d(*args)
    elif A.tag == cTag: lib.ElSoftThresholdDist_c(*args)
    elif A.tag == zTag: lib.ElSoftThresholdDist_z(*args)
    else: DataExcept()
  else: TypeExcept()
