# Copyright 2020 P&E Microcomputersystems. All rights reserved.
# Use of this source code in cycloneControlSDKConstants.py is governed by a BSD-style license that can be found in the LICENSE.txt file.

MEDIA_INTERNAL = 1;
MEDIA_EXTERNAL = 2;

#CATEGORY NAMES AND THEIR PROPERTIES
#A list of properties supported by the Cyclone can
#be retrieved with the getPropertyList() routine
CycloneProperties = 'cycloneProperties'
selectCyclonePropertyType = 'cycloneType'
selectCyclonePropertyFirmwareVersion = 'cycloneFirmwareVersion'
selectCyclonePropertyCycloneLogicVersion = 'cycloneLogicVersion'
selectCyclonePropertyName = 'cycloneName';
selectCyclonePropertyNumberOfInternalImages = 'numberOfInternalImages'
selectCyclonePropertyNumberOfExternalImages = 'numberOfExternalImages'
selectCyclonePropertyNumberOfImages = 'totalNumberOfImages'
currentImageSelected = 'currentImageSelected'

NetworkProperties = 'networkProperties'
selectNetworkPropertyCycloneIPAddress = 'cycloneIPAddress'
selectNetworkPropertyCycloneNetmask = 'cycloneNetworkMask'
selectNetworkPropertyCycloneGateway = 'cycloneNetworkGateway'
selectNetworkPropertyCycloneDNS = 'cycloneDNSAddress'

ImageProperties = 'imageProperties'
selectImagePropertyName = 'imageName'
selectImagePropertyMediaType = 'mediaType'
selectImagePropertyUniqueId = 'imageUniqueId'
selectImagePropertyCRC32 = 'imageCRC32'
selectImagePropertyVoltageSettings = 'imageVoltageSettings'
selectImagePropertyFirstObjectCrc = 'imageFirstObjectCrc'
selectImagePropertyFirstDeviceCrc = 'imageFirstDeviceCrc'
selectImagePropertySerialNumberCount = 'imageSerialNumberCount'
selectImagePropertyGetSerialNumber = 'imageSerialNumber' # Append index in decimal format, e.g. 'imageSerialNumber1', 'imageSerialNumber2'
selectImageEncryptionStatus = 'imageencryptionstatus'
selectImageKeyID = 'imagekeyid'
selectImageKeyDescription = 'imagekeydescription'

TargetProperties = 'targetProperties'
selectTargetPropertyTargetVoltageReading = 'targetVoltageReading'
selectTargetPropertyTargetCurrentReading = 'targetCurrentReading'
selectTargetPropertyTargetObjectCrc = 'targetObjectCrc'
selectTargetPropertyTargetDeviceCrc = 'targetDeviceCrc'

#Commands
PE_SET_FIRMWARE_UPDATE_PRINTF_CALLBACK = 0x58006001
PE_CYCLONE_SDK_SET_FIRMWARE_UPDATE_MODE = 0x58006002
PE_CYCLONE_SDK_ENABLE_DEBUG_OUT_FILE = 0x58006006

CYCLONE_GET_IMAGE_DESCRIPTION_FROM_FILE = 0xA5001001
CYCLONE_GET_IMAGE_CRC32_FROM_FILE = 0xA5001002
CYCLONE_GET_IMAGE_SETTINGS_FROM_FILE = 0xA5001003
CYCLONE_GET_IMAGE_COMMMAND_LINE_PARAMS_FROM_FILE = 0xA5001004
CYCLONE_GET_IMAGE_SCRIPT_FILE_FROM_FILE = 0xA5001005

CYCLONE_CHECK_IMAGE_FILE_ENCRYPTION_STATUS = 0xA5001018
CYCLONE_GET_IMAGE_ENCRYPTION_KEY_UNIQUE_ID = 0xA5001019
CYCLONE_GET_IMAGE_ENCRYPTION_KEY_DESCRIPTION = 0xA500101A
CYCLONE_GET_IMAGE_ENCRYPTION_KEY_ORIGINAL_FILE = 0xA500101B
CYCLONE_GET_IMAGE_ENCRYPTION_KEY_CURRENT_FILE = 0xA500101C
CYCLONE_SET_IMAGE_ENCRYPTION_KEY_CURRENT_FILE = 0xA500101D

PE_CYCLONE_GET_CYCLONE_SCREEN_BITMAP_BUFFER = 0xA5001101
PE_CYCLONE_SEND_DISPLAY_TOUCH = 0xA5001102
PE_CYCLONE_DOES_DISPLAY_NEED_UPDATE = 0xA5001103

CYCLONE_TOGGLE_POWER_NO_DEBUG = 0xA5002001
CYCLONE_SET_ACTIVE_SECURITY_CODE = 0xA5002002