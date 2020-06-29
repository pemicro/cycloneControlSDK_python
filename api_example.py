# Copyright 2020 P&E Microcomputersystems. All rights reserved.
# Use of this source code in api_example.py is governed by a BSD-style license that can be found in the LICENSE.txt file.

import sys
import ctypes
from time import sleep
from cycloneControlSDK import *

cycloneControlSDKObj = None

cyclone_info = {
  'opened_cyclone_identifier': '',
  'opened_cyclone_name': '',
  'opened_cyclone_handle': 0
}

def cmdOpen(cmdParam):
	print('Opening Cyclone ... ', end='')
	handle = cycloneControlSDKObj.connectToCyclone(cmdParam)
	print(cmdParam+' : ', end='')
	if handle != 0:
		cyclone_info['opened_cyclone_identifier'] = cmdParam
		cyclone_info['opened_cyclone_name'] = cycloneControlSDKObj.getPropertyValue(handle, 0, CycloneProperties, selectCyclonePropertyName)
		cyclone_info['opened_cyclone_handle'] = handle
		print('Opened Successfully. (Handle= '+str(cyclone_info['opened_cyclone_handle'])+', Name= '+str(cyclone_info['opened_cyclone_name'])+')')
		return(True)
	else:
		print('Can not establish a connection with specified Cyclone ... Failed.')
		return(False)

def cmdReplaceAllImages(cmdParam):
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Erasing all internal images ... ', end='')
	if cycloneControlSDKObj.formatCycloneMemorySpace(cyclone_info['opened_cyclone_handle'], MEDIA_INTERNAL):
		print('Erased.')
	else:
		print('Failed.')
		return(False)
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Adding internal image '+cmdParam+' ... ', end='')
	if cycloneControlSDKObj.addCycloneImage(cyclone_info['opened_cyclone_handle'], MEDIA_INTERNAL, True, cmdParam):
		print('Added.')
	else:
		print('Failed.')
		return(False)
	return(True)

def cmdListImages():
	print ('List of images on Cyclone \''+cyclone_info['opened_cyclone_name']+'\':')
	numimages = cycloneControlSDKObj.countCycloneImages(cyclone_info['opened_cyclone_handle'])
	if numimages > 0:
		for i in range(1, numimages+1):
			imageMediaType = cycloneControlSDKObj.getPropertyValue(cyclone_info['opened_cyclone_handle'], i, ImageProperties, selectImagePropertyMediaType)
			imageName = cycloneControlSDKObj.getPropertyValue(cyclone_info['opened_cyclone_handle'], i, ImageProperties, selectImagePropertyName)
			print('   Image '+str(i)+' ('+imageMediaType+') : '+imageName)
	else:
		print('   No Images')

def cmdLaunchImage(cmdParam):
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Attempting to launch Image '+cmdParam, end='')
	print(' ('+cycloneControlSDKObj.getPropertyValue(cyclone_info['opened_cyclone_handle'], 1, ImageProperties, selectImagePropertyName)+') ... ', end='')
	if not cycloneControlSDKObj.startImageExecution(cyclone_info['opened_cyclone_handle'], int(cmdParam)):
		print('Failed to execute.')
		return(False)
	else:
		print('Started.')
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Querying status of Image '+cmdParam, end='')
	print(' ('+cycloneControlSDKObj.getPropertyValue(cyclone_info['opened_cyclone_handle'], 1, ImageProperties, selectImagePropertyName)+') for completion ... ')
	while True:
		sleep(0.001)
		if cycloneControlSDKObj.checkCycloneExecutionStatus(cyclone_info['opened_cyclone_handle']) == 0:
			break
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : ', end='')
	if cycloneControlSDKObj.getNumberOfErrors(cyclone_info['opened_cyclone_handle']) == 0:
		print('Programming successful.')
		return(True)
	else:
		error = cycloneControlSDKObj.getErrorCode(cyclone_info['opened_cyclone_handle'], 1)
		if cycloneControlSDKObj.getLastErrorAddr(cyclone_info['opened_cyclone_handle']) != 0:
			print('Error '+hex(error)+' during programming.', end='')
			print('(Address='+hex(cycloneControlSDKObj.getLastErrorAddr(cyclone_info['opened_cyclone_handle']))+')')
		else:
			print('Error '+hex(error)+' during programming.')
	print(cycloneControlSDKObj.getDescriptionOfErrorCode(cyclone_info['opened_cyclone_handle'], error))
	return(False)

def cmdPutDynamicData(cmdParam):
	#Example: -putdynamicdata=0x4000,54,45,53,54,20,4e,55,4d,42,45,52
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Program and verify dynamic data ... Analyzing parameters ... ', end='')
	parameters = cmdParam.strip().split(',')
	if len(parameters) <= 1:
		print('Not enough parameters detected ... Failed.')
		print(parameters)
		return False
	print('Done.')
	try:
		address = int(parameters[0], 16)
	except:
		print(parameters[0]+' ... Invalid hex address parameter ... Failed.')
		return(False)
	print('[Address] = '+'0x{:08x}'.format(address))
	numberOfBytes = len(parameters)-1
	bufferList = []
	for i in range(1, numberOfBytes+1):
		try:
			data = int(parameters[i], 16)
		except ValueError:
			print(parameters[i]+' ... Invalid hex data parameter ... Failed.')
			print('Hex data must be in range(0, 256)')
			return(False)
		bufferList.append(chr(data))
		print('[Data] = '+'0x{:02x}'.format(data))
	bufferStr = ''.join(bufferList)
	print('[Data String] = '+bufferStr)
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Attempt to program and verify dynamic data ... ', end='')
	if not cycloneControlSDKObj.startDynamicDataProgram(cyclone_info['opened_cyclone_handle'], address, numberOfBytes, bufferStr):
		print('Failed to execute.')
		return(False)
	else:
		print('Started.')
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : Querying status of dynamic data operations ... ')
	while True:
		sleep(0.001)
		if cycloneControlSDKObj.checkCycloneExecutionStatus(cyclone_info['opened_cyclone_handle']) == 0:
			break
	print('Cyclone \''+cyclone_info['opened_cyclone_name']+'\' : ', end='')
	if cycloneControlSDKObj.getNumberOfErrors(cyclone_info['opened_cyclone_handle']) == 0:
		print('Programming successful.')
		return(True)
	else:
		error = cycloneControlSDKObj.getErrorCode(cyclone_info['opened_cyclone_handle'], 1)
		if cycloneControlSDKObj.getLastErrorAddr(cyclone_info['opened_cyclone_handle']) != 0:
			print('Error '+hex(error)+' during programming.', end='')
			print('(Address='+hex(cycloneControlSDKObj.getLastErrorAddr(cyclone_info['opened_cyclone_handle']))+')')
		else:
			print('Error '+hex(error)+' during programming.')
	print(cycloneControlSDKObj.getDescriptionOfErrorCode(cyclone_info['opened_cyclone_handle'], error))
	return(False)

def cmdGetImageCRC(cmdParam):
	SAPFile = ctypes.c_char_p(cmdParam.encode('UTF-8'))
	retValueCRC32 = ctypes.c_ulong()
	print('Getting CRC32 of '+SAPFile.value.decode('UTF-8')+' ... ', end='')
	if cycloneControlSDKObj.cycloneSpecialFeatures(CYCLONE_GET_IMAGE_CRC32_FROM_FILE, False, 0, 0, 0, ctypes.byref(retValueCRC32), SAPFile):
		print('Done')
		print('[Image File CRC32] = '+'0x{:08x}'.format(retValueCRC32.value))
		return(True)
	else:
		print('Failed')
		return(False)

def process_cmdparam():
	print('Executing commandline parameter(s) in order ...')
	for i in range(1, len(sys.argv)):
		iparamStr = (sys.argv[i]).upper()
		cmdParam = (iparamStr.partition('='))[-1]
		if iparamStr.find('-CYCLONE=') == 0:
			if not cmdOpen(cmdParam):
				print('Error occurred with parameter \'-cyclone=nnnnn\'.')
				return(False)
		elif iparamStr.find('-REPLACEALLIMAGES=') == 0:
			if not cmdReplaceAllImages(cmdParam):
				print('Error occurred with parameter \'-REPLACEALLIMAGES=\'.')
				return(False)
		elif iparamStr.find('-LISTIMAGES') == 0:
			print('')
			cmdListImages()
			print('')			
		elif iparamStr.find('-LAUNCHIMAGE=') == 0:
			if not cmdLaunchImage(cmdParam):
				print('Error occurred with parameter \'-LAUNCHIMAGE=\'.')
				return(False)
		elif iparamStr.find('-PUTDYNAMICDATA=') == 0:
			if not cmdPutDynamicData(cmdParam):
				print('Error occurred with parameter \'-PUTDYNAMICDATA=\'.')
				return(False)
		elif iparamStr.find('-GETIMAGECRC=') == 0:
			if not cmdGetImageCRC(cmdParam):
				print('Error occurred with parameter \'-GETIMAGECRC=\'.')
				return(False)				
		else:
			sys.exit('SystemExit: Unknown commandline parameters')
	return(True)

print('Cyclone API Example showing Python usage.')
if (len(sys.argv) < 2):
	print('List of valid parameters:')
	print(' -cyclone=nnnnn')
	print(' -replaceallimages=SAPfilename')
	print(' -listimages')
	print(' -launchimage=[image id]')
	print(' -putdynamicdata=[address],[data byte 1],[data byte 2],[data byte 3]...')
	print(' -getimagecrc=SAPfilename')
	print('')
	print('Parameter(s) are executed in the order specified on the commandline.')
else:
	cycloneControlSDKObj = cycloneControlSDK()
	print('cycloneControlSDK.dll Version '+cycloneControlSDKObj.version()+'\n')
	cycloneControlSDKObj.enumerateAllPorts()
	tresult = process_cmdparam()
	if tresult:
		print('Final Result: All commandline parameter(s) executed successfully.')
		code = 0
	else:
		print('Final Result: An error was encountered with a commandline parameter.')
		code = 1
	print('Disconnecting from all connected Cyclones ...')
	cycloneControlSDKObj.disconnectFromAllCyclones()
	cycloneControlSDKObj.unloadLibrary()
	sys.exit(code)	