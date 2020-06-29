# Copyright 2020 P&E Microcomputersystems. All rights reserved.
# Use of this source code in cycloneControlSDK.py is governed by a BSD-style license that can be found in the LICENSE.txt file.

import os.path
import ctypes
from cycloneControlSDKConstants import *

class cycloneControlSDK(object):

	# class constructor
	def __init__(self):
		self.__library_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "CycloneControlSDK.dll"))
		self.__library_loaded = False
		self.__loadLibrary()

	#private members
	def __loadLibrary(self):
		# Load the shared library into c types.
		try:
			self.__cycloneControlSDK = ctypes.CDLL(self.__library_path)
		except:
			print('Error while loading cycloneControlSDK.dll')
			sys.exit(1)
		if self.__cycloneControlSDK:
			self.__library_loaded = True
			
		# Define the arguments type and return type for each exported function starting here
		# Use None if there are no arguments and c_void_p for (void *)
		
		# DLL management calls
		self.__cycloneControlSDK.version.argtypes = None
		self.__cycloneControlSDK.version.restype = ctypes.c_char_p
		
		# Port and connection management calls
		self.__cycloneControlSDK.queryNumberOfAutodetectedCyclones.argtypes = None
		self.__cycloneControlSDK.queryNumberOfAutodetectedCyclones.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.queryInformationOfAutodetectedCyclone.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.queryInformationOfAutodetectedCyclone.restype = ctypes.c_char_p
		
		self.__cycloneControlSDK.enumerateAllPorts.argtypes = None
		self.__cycloneControlSDK.enumerateAllPorts.restype = None
		
		self.__cycloneControlSDK.connectToCyclone.argtypes = [ctypes.c_char_p]
		self.__cycloneControlSDK.connectToCyclone.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.connectToMultipleCyclones.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_void_p]
		self.__cycloneControlSDK.connectToMultipleCyclones.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.setLocalMachineIpNumber.argtypes = [ctypes.c_char_p]
		self.__cycloneControlSDK.setLocalMachineIpNumber.restype = None
		
		self.__cycloneControlSDK.disconnectFromAllCyclones.argtypes = None
		self.__cycloneControlSDK.disconnectFromAllCyclones.restype = None
		
		# Cyclone control and management calls
		self.__cycloneControlSDK.startImageExecution.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.startImageExecution.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.startDynamicDataProgram.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ushort, ctypes.c_char_p]
		self.__cycloneControlSDK.startDynamicDataProgram.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.checkCycloneExecutionStatus.argtypes = [ctypes.c_ulong]
		self.__cycloneControlSDK.checkCycloneExecutionStatus.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.dynamicReadBytes.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ushort, ctypes.c_char_p]
		self.__cycloneControlSDK.dynamicReadBytes.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.resetCyclone.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.resetCyclone.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.getFirmwareVersion.argtypes = [ctypes.c_ulong]
		self.__cycloneControlSDK.getFirmwareVersion.restype = ctypes.c_char_p		
		
		# Error management calls
		self.__cycloneControlSDK.getNumberOfErrors.argtypes = [ctypes.c_ulong]
		self.__cycloneControlSDK.getNumberOfErrors.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.getErrorCode.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.getErrorCode.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.getLastErrorAddr.argtypes = [ctypes.c_ulong]
		self.__cycloneControlSDK.getLastErrorAddr.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.getDescriptionOfErrorCode.argtypes = [ctypes.c_ulong, ctypes.c_long]
		self.__cycloneControlSDK.getDescriptionOfErrorCode.restype = ctypes.c_char_p
		
		# Image management calls
		self.__cycloneControlSDK.formatCycloneMemorySpace.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.formatCycloneMemorySpace.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.addCycloneImage.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_bool, ctypes.c_char_p]
		self.__cycloneControlSDK.addCycloneImage.restype = ctypes.c_ulong
		
		self.__cycloneControlSDK.eraseCycloneImage.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.eraseCycloneImage.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.getImageDescription.argtypes = [ctypes.c_ulong, ctypes.c_ulong]
		self.__cycloneControlSDK.getImageDescription.restype = ctypes.c_char_p
		
		self.__cycloneControlSDK.compareImageInCycloneWithFile.argtypes = [ctypes.c_ulong, ctypes.c_char_p, ctypes.c_ulong]
		self.__cycloneControlSDK.compareImageInCycloneWithFile.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.countCycloneImages.argtypes = [ctypes.c_ulong]
		self.__cycloneControlSDK.countCycloneImages.restype = ctypes.c_ulong
		
		#Property calls
		self.__cycloneControlSDK.getPropertyValue.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p, ctypes.c_char_p]
		self.__cycloneControlSDK.getPropertyValue.restype = ctypes.c_char_p
		
		self.__cycloneControlSDK.setPropertyValue.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
		self.__cycloneControlSDK.setPropertyValue.restype = ctypes.c_bool
		
		self.__cycloneControlSDK.getPropertyList.argtypes = [ctypes.c_ulong, ctypes.c_ulong, ctypes.c_char_p]
		self.__cycloneControlSDK.getPropertyList.restype = ctypes.c_char_p
		
		#Features Calls
		self.__cycloneControlSDK.cycloneSpecialFeatures.argtypes = [ctypes.c_ulong, ctypes.c_bool, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p]
		self.__cycloneControlSDK.cycloneSpecialFeatures.restype = ctypes.c_bool

	#public members
	def unloadLibrary(self):
		if self.__library_loaded:
			# Free the library from memory
			ctypes.windll.kernel32.FreeLibrary(self.__cycloneControlSDK._handle)
		# Delete the object
		del self.__cycloneControlSDK

	def version(self):
		if self.__library_loaded:
			versionStr = self.__cycloneControlSDK.version()
			return(versionStr.decode('UTF-8'))
		else:
			print('version() failed because cycloneControlSDK.dll not loaded')
			return None

	def queryNumberOfAutodetectedCyclones(self):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.queryNumberOfAutodetectedCyclones())
		else:
			print('queryNumberOfAutodetectedCyclones() failed because cycloneControlSDK.dll not loaded')
			return None

	def queryInformationOfAutodetectedCyclone(self, autodetectIndex, informationType):
		if self.__library_loaded:
			propertyValue = self.__cycloneControlSDK.queryInformationOfAutodetectedCyclone(autodetectIndex, informationType)
			return(propertyValue.decode('UTF-8'))
		else:
			print('queryInformationOfAutodetectedCyclone() failed because cycloneControlSDK.dll not loaded')
			return None

	def enumerateAllPorts(self):
		if self.__library_loaded:
			self.__cycloneControlSDK.enumerateAllPorts()
		else:
			print('enumerateAllPorts() failed because cycloneControlSDK.dll not loaded')

	def connectToCyclone(self, nameIpOrPortIdentifier):
		if self.__library_loaded:
			cycloneHandle = self.__cycloneControlSDK.connectToCyclone(nameIpOrPortIdentifier.encode('UTF-8'))
			return(cycloneHandle)
		else:
			print('connectToCyclone() failed because cycloneControlSDK.dll not loaded')
			return None

	def connectToMultipleCyclones(self, nameIpOrPortIdentifierArray, cycloneHandleArrayPointer, numberOfCycloneOpensAttempted):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.connectToMultipleCyclones(nameIpOrPortIdentifierArray.encode('UTF-8'), cycloneHandleArrayPointer, numberOfCycloneOpensAttempted))
		else:
			print('connectToMultipleCyclones() failed because cycloneControlSDK.dll not loaded')
			return None

	def setLocalMachineIpNumber(self, ipNumber):
		if self.__library_loaded:
			self.__cycloneControlSDK.setLocalMachineIpNumber(ipNumber.encode('UTF-8'))
		else:
			print('setLocalMachineIpNumber() failed because cycloneControlSDK.dll not loaded')

	def disconnectFromAllCyclones(self):
		if self.__library_loaded:
			self.__cycloneControlSDK.disconnectFromAllCyclones()
		else:
			print('disconnectFromAllCyclones() failed because cycloneControlSDK.dll not loaded')

	def startImageExecution(self, cycloneHandle, imageId):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.startImageExecution(cycloneHandle, imageId))
		else:
			print('startImageExecution() failed because cycloneControlSDK.dll not loaded')
			return None

	def startDynamicDataProgram(self, cycloneHandle, targetAddress, dataLength, buffer):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.startDynamicDataProgram(cycloneHandle, targetAddress, dataLength, buffer.encode('UTF-8')))
		else:
			print('startDynamicDataProgram() failed because cycloneControlSDK.dll not loaded')
			return None

	def checkCycloneExecutionStatus(self, cycloneHandle):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.checkCycloneExecutionStatus(cycloneHandle))
		else:
			print('checkCycloneExecutionStatus() failed because cycloneControlSDK.dll not loaded')
			return None

	def dynamicReadBytes(self, cycloneHandle, targetAddress, dataLength, buffer):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.dynamicReadBytes(cycloneHandle, targetAddress, dataLength, buffer))
		else:
			print('dynamicReadBytes() failed because cycloneControlSDK.dll not loaded')
			return None

	def resetCyclone(self, cycloneHandle, resetDelayInMs):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.resetCyclone(cycloneHandle, resetDelayInMs))
		else:
			print('resetCyclone() failed because cycloneControlSDK.dll not loaded')
			return None

	def getFirmwareVersion(self, cycloneHandle):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.getFirmwareVersion(cycloneHandle))
		else:
			print('getFirmwareVersion() failed because cycloneControlSDK.dll not loaded')
			return None

	def getNumberOfErrors(self, cycloneHandle):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.getNumberOfErrors(cycloneHandle))
		else:
			print('getNumberOfErrors() failed because cycloneControlSDK.dll not loaded')
			return None

	def getErrorCode(self, cycloneHandle, errorNum):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.getErrorCode(cycloneHandle, errorNum))
		else:
			print('getErrorCode() failed because cycloneControlSDK.dll not loaded')
			return None

	def getLastErrorAddr(self, cycloneHandle):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.getLastErrorAddr(cycloneHandle))
		else:
			print('getLastErrorAddr() failed because cycloneControlSDK.dll not loaded')
			return None

	def getDescriptionOfErrorCode(self, cycloneHandle, errorCode):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.getDescriptionOfErrorCode(cycloneHandle, errorCode).decode('UTF-8'))
		else:
			print('getDescriptionOfErrorCode() failed because cycloneControlSDK.dll not loaded')
			return None

	def formatCycloneMemorySpace(self, cycloneHandle, selectedMediaType):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.formatCycloneMemorySpace(cycloneHandle, selectedMediaType))
		else:
			print('formatCycloneMemorySpace() failed because cycloneControlSDK.dll not loaded')
			return None

	def addCycloneImage(self, cycloneHandle, selectedMediaType, replaceImageOfSameDescription, aFile):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.addCycloneImage(cycloneHandle, selectedMediaType, replaceImageOfSameDescription, aFile.encode('UTF-8')))
		else:
			print('addCycloneImage() failed because cycloneControlSDK.dll not loaded')
			return None

	def eraseCycloneImage(self, cycloneHandle, imageId):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.eraseCycloneImage(cycloneHandle, imageID))
		else:
			print('eraseCycloneImage() failed because cycloneControlSDK.dll not loaded')
			return None

	def getImageDescription(self, cycloneHandle, imageId):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.getImageDescription(cycloneHandle, imageID).decode('UTF-8'))
		else:
			print('getImageDescription() failed because cycloneControlSDK.dll not loaded')
			return None

	def compareImageInCycloneWithFile(self, cycloneHandle, aFile, imageId):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.compareImageInCycloneWithFile(cycloneHandle, aFile.encode('UTF-8'), imageID))
		else:
			print('compareImageInCycloneWithFile() failed because cycloneControlSDK.dll not loaded')
			return None

	def countCycloneImages(self, cycloneHandle):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.countCycloneImages(cycloneHandle))
		else:
			print('countCycloneImages() failed because cycloneControlSDK.dll not loaded')
			return None

	def getPropertyValue(self, cycloneHandle, resourceOrImageId, categoryName, propertyName):
		if self.__library_loaded:
			propertyValue = self.__cycloneControlSDK.getPropertyValue(cycloneHandle, resourceOrImageId, categoryName.encode('UTF-8'), propertyName.encode('UTF-8')) 
			return(propertyValue.decode('UTF-8'))
		else:
			print('getPropertyValue() failed because cycloneControlSDK.dll not loaded')
			return None

	def setPropertyValue(self, cycloneHandle, resourceOrImageId, categoryName, propertyName, newValue):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.setPropertyValue(cycloneHandle, resourceOrImageId, categoryName, propertyNam, newValue.encode('UTF-8'))) 
		else:
			print('setPropertyValue() failed because cycloneControlSDK.dll not loaded')
			return None

	def getPropertyList(self, cycloneHandle, resourceOrImageId, categoryName):
		if self.__library_loaded:
			propertyList = self.__cycloneControlSDK.getPropertyList(cycloneHandle, resourceOrImageId, categoryName) 
			return(propertyList.decode('UTF-8'))
		else:
			print('getPropertyList() failed because cycloneControlSDK.dll not loaded')
			return None

	def cycloneSpecialFeatures(self, featureNum, setFeature, paramValue1, paramValue2, paramValue3, paramReference1, paramReference2):
		if self.__library_loaded:
			return(self.__cycloneControlSDK.cycloneSpecialFeatures(featureNum, setFeature, paramValue1, paramValue2, paramValue3, paramReference1, paramReference2))
		else:
			print('cycloneSpecialFeatures() failed because cycloneControlSDK.dll not loaded')
			return None