from mobileiron_api.client import MobileIronCloudAPI
import pytest, json


@pytest.fixture
def mobile_iron_client():
    return MobileIronCloudAPI("username", "password", "fqdn", 111)


@pytest.fixture
def get_device_profile_from_email():
    response = r"""
    {
        "errors": null,
        "result":
        {
            "totalCount": 1,
            "searchResults":
            [
                {
                    "id": 1844659,
                    "guid": "<guid>",
                    "mdmChannelId": "<mdmChannelId>",
                    "phoneNumber": null,
                    "deviceModel": "MacBookPro16,1",
                    "deviceName": "<deviceName>",
                    "platformType": "OSX",
                    "platformVersion": "12.4",
                    "osBuildVersion": "21F79",
                    "lastCheckin": "2022-08-02T18:10:53Z",
                    "registrationState": "ACTIVE",
                    "displayName": "<displayName>",
                    "firstName": "<firstName>",
                    "lastName": "<lastName>",
                    "uid": "<uid>",
                    "emailAddress": "<emailAddress>",
                    "clientVersion": "1.85.0 (3.1.85)",
                    "manufacturer": "Apple Inc.",
                    "imei": null,
                    "imei2": null,
                    "imsi": null,
                    "locatorServiceEnabled": false,
                    "meid": null,
                    "wifiMacAddress": "<MAC_ADDRESS>",
                    "wifiMacAddressForInventory": null,
                    "systemUpdateInformation": null,
                    "serialNumber": "<serialNumber>",
                    "altSerialNumber": null,
                    "cellularTechnology": null,
                    "currentCarrierNetwork": "UNKNOWN",
                    "subscriberCarrierNetwork": "UNKNOWN",
                    "locale": null,
                    "ownershipType": "COMPANY",
                    "complianceState": true,
                    "roaming": false,
                    "supervised": true,
                    "udid": "<udid>",
                    "clientLastCheckin": "2022-08-02T18:26:56Z",
                    "iccid": null,
                    "currentMcc": null,
                    "currentMnc": null,
                    "subscriberMcc": null,
                    "subscriberMnc": null,
                    "prettyModel": "MacBookPro16,1",
                    "policyViolationCount": 0,
                    "latitude": null,
                    "longitude": null,
                    "locationLastCapturedAt": null,
                    "lastRegistrationTime": "2022-02-09T12:17:58Z",
                    "lostModeEnabled": false,
                    "multiUser": false,
                    "maxResidentUsers": null,
                    "clientDeviceIdentifier": "<clientDeviceIdentifier>",
                    "availableCapacity": 414.0,
                    "totalCapacity": 499.0,
                    "totalRamMB": 0,
                    "clusterIdentifier": "CLOUD",
                    "deviceSource": "CLOUD",
                    "quarantined": false,
                    "jailbroken": false,
                    "passcodeCompliant": null,
                    "passcodeCompliantWithProfiles": null,
                    "blocked": false,
                    "locationStatusDetail": null,
                    "androidBuildFingerprint": null,
                    "androidBuildId": null,
                    "androidZebraPatchLevel": null,
                    "androidSystemUpdateStatus": null,
                    "salesCode": null,
                    "firmwareVersion": null,
                    "uptime": null,
                    "batteryLevel": null,
                    "batteryHealthStatus": null,
                    "batteryChargingStatus": null,
                    "batteryHealthPercentage": null,
                    "batteryManufacturedDate": null,
                    "batteryChargeCycles": null,
                    "userEnrolled": false,
                    "androidWorkContainerEnabled": false,
                    "androidWorkUid": null,
                    "androidManagedByGoogle": false,
                    "fcmEnabled": false,
                    "androidAospDeviceWithoutGms": false,
                    "androidEnrollmentSpecificId": null,
                    "androidNetworkSlicingEnabled": false,
                    "actionExceptionCodes":
                    [],
                    "violatedPolicies":
                    [],
                    "supportLockMessage": true,
                    "ownerId": 111111111,
                    "legalOwnerId": null,
                    "legalOwnerEmailAddress": null,
                    "kioskState": "NOT_CONFIGURED",
                    "customAttributes":
                    {
                        "attrs":
                        {}
                    },
                    "easDeviceIdentifiers":
                    [],
                    "appEasIdentifiers": null,
                    "androidDeviceOwnerModeEnabled": false,
                    "windowsDeviceType": null,
                    "secureAppsStatus": null,
                    "secureAppsEncryptionStatus": null,
                    "secureAppsEncryptionMode": null,
                    "tpmSpecificationVersion": null,
                    "bridgeVersion": null,
                    "bridgeDeviceDataLastCapturedAt": null,
                    "lastHotfixId": null,
                    "lastHotfixInstalledOn": null,
                    "mamOnly": false,
                    "authOnly": false,
                    "ipAddress": null,
                    "depEnrolled": false,
                    "depEligible": false,
                    "mobileThreatDefenseGeneralStatus": "NA",
                    "antiPhishingGeneralStatus": "NA",
                    "antiPhishingVpnGeneralStatus": "NA",
                    "samsungEfotaCapable": false,
                    "currentCountryName": null,
                    "currentCountryCode": null,
                    "homeCountryName": null,
                    "homeCountryCode": null,
                    "userPreferenceCSVHeader": null,
                    "dmPartitionId": 111111,
                    "dmPartitionName": "Default Space",
                    "entityName": "<entityName>",
                    "azureDeviceId": null,
                    "azureClientStatusCode": null,
                    "azureIntuneDeviceStatus": null,
                    "azureIntuneStatusUpdatedAt": null,
                    "azureUserUpn": null,
                    "androidSecurityPatchLevel": null,
                    "recoveryLockEnabled": false,
                    "serviceSubscriptions": null,
                    "assignedConfigs":
                    [
                        {
                            "id": null,
                            "dmPartitionId": 111111,
                            "name": "Cortex XDR - macOS Intel Profile",
                            "systemName": null,
                            "description": null,
                            "dmPartitionDistributionType": "NONE",
                            "policyType": "<policyType>",
                            "policyRuleType": "NONE",
                            "uuid": null,
                            "enabled": false,
                            "priority": null,
                            "cloneable": false,
                            "configurationMutable": false,
                            "distributionMutable": false,
                            "priorityMutable": false,
                            "deletable": false,
                            "totalDeviceCount": 0,
                            "installedDeviceCount": 0,
                            "violationDeviceCount": 0,
                            "modifiedAt": null,
                            "modifiedBy": null,
                            "actions": null,
                            "cloneableAcrossSpace": false,
                            "clonedFromDefaultSpace": false,
                            "resourceSupport":
                            {
                                "links":
                                []
                            },
                            "systemDefault": false
                        }
                    ],
                    "assignedPolicies": null,
                    "esimIdentifier": null
                }
            ],
            "offset": 0,
            "limit": 10,
            "queryTime": 92,
            "facetedResults":
            {
                "LAST_HOTFIX_ID":
                {},
                "SUBSCRIBERCARRIERNETWORK":
                {
                    "UNKNOWN": 1
                },
                "AUTHONLY":
                {},
                "DEVICEGROUP":
                {
                    "Win Test Group": null
                },
                "ANDROIDWORKPROFILEONCOMPANYOWNEDDEVICEENABLED":
                {},
                "PRETTYMODEL":
                {
                    "MacBookPro16,1": 1
                },
                "ANDROIDDEVICEOWNERMODEENABLED":
                {},
                "SERVICESUBSCRIPTIONS":
                {},
                "REGISTRATIONSTATE":
                {
                    "ACTIVE": 1
                },
                "ACCOUNTENABLED":
                {
                    "true": 1
                },
                "MULTIUSER":
                {},
                "DEVICESOURCE":
                {
                    "cloud": 1
                },
                "ANDROIDWORKPROFILEENABLED":
                {},
                "ISAPPLESILICON":
                {
                    "false": 1
                },
                "KIOSKSTATE":
                {},
                "ANDROIDSECURITYPATCHLEVEL":
                {},
                "JAILBROKEN":
                {},
                "PLATFORMTYPE":
                {
                    "OSX": 1
                },
                "OWNERSHIPTYPE":
                {
                    "COMPANY": 1
                },
                "ANDROIDSAFETYNETATTESTATIONTYPE":
                {},
                "ANDROIDWORKDEVICEOWNERWITHWORKPROFILEENABLED":
                {},
                "MOBILE_THREAT_DEFENSE_GENERAL_STATUS":
                {},
                "COMPLIANCESTATE":
                {
                    "true": 1
                },
                "SUPERVISED":
                {
                    "true": 1
                },
                "ANTIPHISHINGGENERALSTATUS":
                {},
                "SECUREAPPSSTATUS":
                {},
                "MAMONLY":
                {},
                "RECOVERY_LOCK_ENABLED":
                {
                    "false": 1
                },
                "ACCOUNTGROUP":
                {
                    "MDM all": 1
                },
                "ANDROIDMANAGEDBYGOOGLE":
                {},
                "ANDROIDWORKENABLED":
                {},
                "ANDROID_AOSP_DEVICE_WITHOUT_GMS":
                {},
                "OSBUILDVERSION":
                {
                    "21F79": 1
                },
                "ANTIPHISHINGVPNGENERALSTATUS":
                {},
                "ROAMING":
                {
                    "false": 1
                },
                "LOSTMODEENABLED":
                {},
                "ANTIPHISHINGANALYTICSSTATUS":
                {}
            },
            "totalUnfilteredResultCount": 0
        }
    }
    """

    return json.loads(response)

@pytest.fixture
def get_device_profile_from_id():
    response = r"""
    {
        "errors": null,
        "result":
        {
            "totalCount": 1,
            "searchResults":
            [
                {
                    "id": 1844659,
                    "guid": "<guid>",
                    "mdmChannelId": "<mdmChannelId>",
                    "phoneNumber": null,
                    "deviceModel": "MacBookPro16,1",
                    "deviceName": "<deviceName>",
                    "platformType": "OSX",
                    "platformVersion": "12.4",
                    "osBuildVersion": "21F79",
                    "lastCheckin": "2022-08-02T18:10:53Z",
                    "registrationState": "ACTIVE",
                    "displayName": "<displayName>",
                    "firstName": "<firstName>",
                    "lastName": "<lastName>",
                    "uid": "<uid>",
                    "emailAddress": "<emailAddress>",
                    "clientVersion": "1.85.0 (3.1.85)",
                    "manufacturer": "Apple Inc.",
                    "imei": null,
                    "imei2": null,
                    "imsi": null,
                    "locatorServiceEnabled": false,
                    "meid": null,
                    "wifiMacAddress": "<MAC_ADDRESS>",
                    "wifiMacAddressForInventory": null,
                    "systemUpdateInformation": null,
                    "serialNumber": "<serialNumber>",
                    "altSerialNumber": null,
                    "cellularTechnology": null,
                    "currentCarrierNetwork": "UNKNOWN",
                    "subscriberCarrierNetwork": "UNKNOWN",
                    "locale": null,
                    "ownershipType": "COMPANY",
                    "complianceState": true,
                    "roaming": false,
                    "supervised": true,
                    "udid": "<udid>",
                    "clientLastCheckin": "2022-08-02T18:26:56Z",
                    "iccid": null,
                    "currentMcc": null,
                    "currentMnc": null,
                    "subscriberMcc": null,
                    "subscriberMnc": null,
                    "prettyModel": "MacBookPro16,1",
                    "policyViolationCount": 0,
                    "latitude": null,
                    "longitude": null,
                    "locationLastCapturedAt": null,
                    "lastRegistrationTime": "2022-02-09T12:17:58Z",
                    "lostModeEnabled": false,
                    "multiUser": false,
                    "maxResidentUsers": null,
                    "clientDeviceIdentifier": "<clientDeviceIdentifier>",
                    "availableCapacity": 414.0,
                    "totalCapacity": 499.0,
                    "totalRamMB": 0,
                    "clusterIdentifier": "CLOUD",
                    "deviceSource": "CLOUD",
                    "quarantined": false,
                    "jailbroken": false,
                    "passcodeCompliant": null,
                    "passcodeCompliantWithProfiles": null,
                    "blocked": false,
                    "locationStatusDetail": null,
                    "androidBuildFingerprint": null,
                    "androidBuildId": null,
                    "androidZebraPatchLevel": null,
                    "androidSystemUpdateStatus": null,
                    "salesCode": null,
                    "firmwareVersion": null,
                    "uptime": null,
                    "batteryLevel": null,
                    "batteryHealthStatus": null,
                    "batteryChargingStatus": null,
                    "batteryHealthPercentage": null,
                    "batteryManufacturedDate": null,
                    "batteryChargeCycles": null,
                    "userEnrolled": false,
                    "androidWorkContainerEnabled": false,
                    "androidWorkUid": null,
                    "androidManagedByGoogle": false,
                    "fcmEnabled": false,
                    "androidAospDeviceWithoutGms": false,
                    "androidEnrollmentSpecificId": null,
                    "androidNetworkSlicingEnabled": false,
                    "actionExceptionCodes":
                    [],
                    "violatedPolicies":
                    [],
                    "supportLockMessage": true,
                    "ownerId": 111111111,
                    "legalOwnerId": null,
                    "legalOwnerEmailAddress": null,
                    "kioskState": "NOT_CONFIGURED",
                    "customAttributes":
                    {
                        "attrs":
                        {}
                    },
                    "easDeviceIdentifiers":
                    [],
                    "appEasIdentifiers": null,
                    "androidDeviceOwnerModeEnabled": false,
                    "windowsDeviceType": null,
                    "secureAppsStatus": null,
                    "secureAppsEncryptionStatus": null,
                    "secureAppsEncryptionMode": null,
                    "tpmSpecificationVersion": null,
                    "bridgeVersion": null,
                    "bridgeDeviceDataLastCapturedAt": null,
                    "lastHotfixId": null,
                    "lastHotfixInstalledOn": null,
                    "mamOnly": false,
                    "authOnly": false,
                    "ipAddress": null,
                    "depEnrolled": false,
                    "depEligible": false,
                    "mobileThreatDefenseGeneralStatus": "NA",
                    "antiPhishingGeneralStatus": "NA",
                    "antiPhishingVpnGeneralStatus": "NA",
                    "samsungEfotaCapable": false,
                    "currentCountryName": null,
                    "currentCountryCode": null,
                    "homeCountryName": null,
                    "homeCountryCode": null,
                    "userPreferenceCSVHeader": null,
                    "dmPartitionId": 111111,
                    "dmPartitionName": "Default Space",
                    "entityName": "<entityName>",
                    "azureDeviceId": null,
                    "azureClientStatusCode": null,
                    "azureIntuneDeviceStatus": null,
                    "azureIntuneStatusUpdatedAt": null,
                    "azureUserUpn": null,
                    "androidSecurityPatchLevel": null,
                    "recoveryLockEnabled": false,
                    "serviceSubscriptions": null,
                    "assignedConfigs":
                    [
                        {
                            "id": null,
                            "dmPartitionId": 111111,
                            "name": "Cortex XDR - macOS Intel Profile",
                            "systemName": null,
                            "description": null,
                            "dmPartitionDistributionType": "NONE",
                            "policyType": "<policyType>",
                            "policyRuleType": "NONE",
                            "uuid": null,
                            "enabled": false,
                            "priority": null,
                            "cloneable": false,
                            "configurationMutable": false,
                            "distributionMutable": false,
                            "priorityMutable": false,
                            "deletable": false,
                            "totalDeviceCount": 0,
                            "installedDeviceCount": 0,
                            "violationDeviceCount": 0,
                            "modifiedAt": null,
                            "modifiedBy": null,
                            "actions": null,
                            "cloneableAcrossSpace": false,
                            "clonedFromDefaultSpace": false,
                            "resourceSupport":
                            {
                                "links":
                                []
                            },
                            "systemDefault": false
                        }
                    ],
                    "assignedPolicies": null,
                    "esimIdentifier": null
                }
            ],
            "offset": 0,
            "limit": 10,
            "queryTime": 92,
            "facetedResults":
            {
                "LAST_HOTFIX_ID":
                {},
                "SUBSCRIBERCARRIERNETWORK":
                {
                    "UNKNOWN": 1
                },
                "AUTHONLY":
                {},
                "DEVICEGROUP":
                {
                    "Win Test Group": null
                },
                "ANDROIDWORKPROFILEONCOMPANYOWNEDDEVICEENABLED":
                {},
                "PRETTYMODEL":
                {
                    "MacBookPro16,1": 1
                },
                "ANDROIDDEVICEOWNERMODEENABLED":
                {},
                "SERVICESUBSCRIPTIONS":
                {},
                "REGISTRATIONSTATE":
                {
                    "ACTIVE": 1
                },
                "ACCOUNTENABLED":
                {
                    "true": 1
                },
                "MULTIUSER":
                {},
                "DEVICESOURCE":
                {
                    "cloud": 1
                },
                "ANDROIDWORKPROFILEENABLED":
                {},
                "ISAPPLESILICON":
                {
                    "false": 1
                },
                "KIOSKSTATE":
                {},
                "ANDROIDSECURITYPATCHLEVEL":
                {},
                "JAILBROKEN":
                {},
                "PLATFORMTYPE":
                {
                    "OSX": 1
                },
                "OWNERSHIPTYPE":
                {
                    "COMPANY": 1
                },
                "ANDROIDSAFETYNETATTESTATIONTYPE":
                {},
                "ANDROIDWORKDEVICEOWNERWITHWORKPROFILEENABLED":
                {},
                "MOBILE_THREAT_DEFENSE_GENERAL_STATUS":
                {},
                "COMPLIANCESTATE":
                {
                    "true": 1
                },
                "SUPERVISED":
                {
                    "true": 1
                },
                "ANTIPHISHINGGENERALSTATUS":
                {},
                "SECUREAPPSSTATUS":
                {},
                "MAMONLY":
                {},
                "RECOVERY_LOCK_ENABLED":
                {
                    "false": 1
                },
                "ACCOUNTGROUP":
                {
                    "MDM all": 1
                },
                "ANDROIDMANAGEDBYGOOGLE":
                {},
                "ANDROIDWORKENABLED":
                {},
                "ANDROID_AOSP_DEVICE_WITHOUT_GMS":
                {},
                "OSBUILDVERSION":
                {
                    "21F79": 1
                },
                "ANTIPHISHINGVPNGENERALSTATUS":
                {},
                "ROAMING":
                {
                    "false": 1
                },
                "LOSTMODEENABLED":
                {},
                "ANTIPHISHINGANALYTICSSTATUS":
                {}
            },
            "totalUnfilteredResultCount": 0
        }
    }
    """

    return json.loads(response)

@pytest.fixture
def get_device_profile_from_mac():
    response = r"""
    {
        "errors": null,
        "result":
        {
            "totalCount": 1,
            "searchResults":
            [
                {
                    "id": 1844659,
                    "guid": "<guid>",
                    "mdmChannelId": "<mdmChannelId>",
                    "phoneNumber": null,
                    "deviceModel": "MacBookPro16,1",
                    "deviceName": "<deviceName>",
                    "platformType": "OSX",
                    "platformVersion": "12.4",
                    "osBuildVersion": "21F79",
                    "lastCheckin": "2022-08-02T18:10:53Z",
                    "registrationState": "ACTIVE",
                    "displayName": "<displayName>",
                    "firstName": "<firstName>",
                    "lastName": "<lastName>",
                    "uid": "<uid>",
                    "emailAddress": "<emailAddress>",
                    "clientVersion": "1.85.0 (3.1.85)",
                    "manufacturer": "Apple Inc.",
                    "imei": null,
                    "imei2": null,
                    "imsi": null,
                    "locatorServiceEnabled": false,
                    "meid": null,
                    "wifiMacAddress": "<MAC_ADDRESS>",
                    "wifiMacAddressForInventory": null,
                    "systemUpdateInformation": null,
                    "serialNumber": "<serialNumber>",
                    "altSerialNumber": null,
                    "cellularTechnology": null,
                    "currentCarrierNetwork": "UNKNOWN",
                    "subscriberCarrierNetwork": "UNKNOWN",
                    "locale": null,
                    "ownershipType": "COMPANY",
                    "complianceState": true,
                    "roaming": false,
                    "supervised": true,
                    "udid": "<udid>",
                    "clientLastCheckin": "2022-08-02T18:26:56Z",
                    "iccid": null,
                    "currentMcc": null,
                    "currentMnc": null,
                    "subscriberMcc": null,
                    "subscriberMnc": null,
                    "prettyModel": "MacBookPro16,1",
                    "policyViolationCount": 0,
                    "latitude": null,
                    "longitude": null,
                    "locationLastCapturedAt": null,
                    "lastRegistrationTime": "2022-02-09T12:17:58Z",
                    "lostModeEnabled": false,
                    "multiUser": false,
                    "maxResidentUsers": null,
                    "clientDeviceIdentifier": "<clientDeviceIdentifier>",
                    "availableCapacity": 414.0,
                    "totalCapacity": 499.0,
                    "totalRamMB": 0,
                    "clusterIdentifier": "CLOUD",
                    "deviceSource": "CLOUD",
                    "quarantined": false,
                    "jailbroken": false,
                    "passcodeCompliant": null,
                    "passcodeCompliantWithProfiles": null,
                    "blocked": false,
                    "locationStatusDetail": null,
                    "androidBuildFingerprint": null,
                    "androidBuildId": null,
                    "androidZebraPatchLevel": null,
                    "androidSystemUpdateStatus": null,
                    "salesCode": null,
                    "firmwareVersion": null,
                    "uptime": null,
                    "batteryLevel": null,
                    "batteryHealthStatus": null,
                    "batteryChargingStatus": null,
                    "batteryHealthPercentage": null,
                    "batteryManufacturedDate": null,
                    "batteryChargeCycles": null,
                    "userEnrolled": false,
                    "androidWorkContainerEnabled": false,
                    "androidWorkUid": null,
                    "androidManagedByGoogle": false,
                    "fcmEnabled": false,
                    "androidAospDeviceWithoutGms": false,
                    "androidEnrollmentSpecificId": null,
                    "androidNetworkSlicingEnabled": false,
                    "actionExceptionCodes":
                    [],
                    "violatedPolicies":
                    [],
                    "supportLockMessage": true,
                    "ownerId": 111111111,
                    "legalOwnerId": null,
                    "legalOwnerEmailAddress": null,
                    "kioskState": "NOT_CONFIGURED",
                    "customAttributes":
                    {
                        "attrs":
                        {}
                    },
                    "easDeviceIdentifiers":
                    [],
                    "appEasIdentifiers": null,
                    "androidDeviceOwnerModeEnabled": false,
                    "windowsDeviceType": null,
                    "secureAppsStatus": null,
                    "secureAppsEncryptionStatus": null,
                    "secureAppsEncryptionMode": null,
                    "tpmSpecificationVersion": null,
                    "bridgeVersion": null,
                    "bridgeDeviceDataLastCapturedAt": null,
                    "lastHotfixId": null,
                    "lastHotfixInstalledOn": null,
                    "mamOnly": false,
                    "authOnly": false,
                    "ipAddress": null,
                    "depEnrolled": false,
                    "depEligible": false,
                    "mobileThreatDefenseGeneralStatus": "NA",
                    "antiPhishingGeneralStatus": "NA",
                    "antiPhishingVpnGeneralStatus": "NA",
                    "samsungEfotaCapable": false,
                    "currentCountryName": null,
                    "currentCountryCode": null,
                    "homeCountryName": null,
                    "homeCountryCode": null,
                    "userPreferenceCSVHeader": null,
                    "dmPartitionId": 111111,
                    "dmPartitionName": "Default Space",
                    "entityName": "<entityName>",
                    "azureDeviceId": null,
                    "azureClientStatusCode": null,
                    "azureIntuneDeviceStatus": null,
                    "azureIntuneStatusUpdatedAt": null,
                    "azureUserUpn": null,
                    "androidSecurityPatchLevel": null,
                    "recoveryLockEnabled": false,
                    "serviceSubscriptions": null,
                    "assignedConfigs":
                    [
                        {
                            "id": null,
                            "dmPartitionId": 111111,
                            "name": "Cortex XDR - macOS Intel Profile",
                            "systemName": null,
                            "description": null,
                            "dmPartitionDistributionType": "NONE",
                            "policyType": "<policyType>",
                            "policyRuleType": "NONE",
                            "uuid": null,
                            "enabled": false,
                            "priority": null,
                            "cloneable": false,
                            "configurationMutable": false,
                            "distributionMutable": false,
                            "priorityMutable": false,
                            "deletable": false,
                            "totalDeviceCount": 0,
                            "installedDeviceCount": 0,
                            "violationDeviceCount": 0,
                            "modifiedAt": null,
                            "modifiedBy": null,
                            "actions": null,
                            "cloneableAcrossSpace": false,
                            "clonedFromDefaultSpace": false,
                            "resourceSupport":
                            {
                                "links":
                                []
                            },
                            "systemDefault": false
                        }
                    ],
                    "assignedPolicies": null,
                    "esimIdentifier": null
                }
            ],
            "offset": 0,
            "limit": 10,
            "queryTime": 92,
            "facetedResults":
            {
                "LAST_HOTFIX_ID":
                {},
                "SUBSCRIBERCARRIERNETWORK":
                {
                    "UNKNOWN": 1
                },
                "AUTHONLY":
                {},
                "DEVICEGROUP":
                {
                    "Win Test Group": null
                },
                "ANDROIDWORKPROFILEONCOMPANYOWNEDDEVICEENABLED":
                {},
                "PRETTYMODEL":
                {
                    "MacBookPro16,1": 1
                },
                "ANDROIDDEVICEOWNERMODEENABLED":
                {},
                "SERVICESUBSCRIPTIONS":
                {},
                "REGISTRATIONSTATE":
                {
                    "ACTIVE": 1
                },
                "ACCOUNTENABLED":
                {
                    "true": 1
                },
                "MULTIUSER":
                {},
                "DEVICESOURCE":
                {
                    "cloud": 1
                },
                "ANDROIDWORKPROFILEENABLED":
                {},
                "ISAPPLESILICON":
                {
                    "false": 1
                },
                "KIOSKSTATE":
                {},
                "ANDROIDSECURITYPATCHLEVEL":
                {},
                "JAILBROKEN":
                {},
                "PLATFORMTYPE":
                {
                    "OSX": 1
                },
                "OWNERSHIPTYPE":
                {
                    "COMPANY": 1
                },
                "ANDROIDSAFETYNETATTESTATIONTYPE":
                {},
                "ANDROIDWORKDEVICEOWNERWITHWORKPROFILEENABLED":
                {},
                "MOBILE_THREAT_DEFENSE_GENERAL_STATUS":
                {},
                "COMPLIANCESTATE":
                {
                    "true": 1
                },
                "SUPERVISED":
                {
                    "true": 1
                },
                "ANTIPHISHINGGENERALSTATUS":
                {},
                "SECUREAPPSSTATUS":
                {},
                "MAMONLY":
                {},
                "RECOVERY_LOCK_ENABLED":
                {
                    "false": 1
                },
                "ACCOUNTGROUP":
                {
                    "MDM all": 1
                },
                "ANDROIDMANAGEDBYGOOGLE":
                {},
                "ANDROIDWORKENABLED":
                {},
                "ANDROID_AOSP_DEVICE_WITHOUT_GMS":
                {},
                "OSBUILDVERSION":
                {
                    "21F79": 1
                },
                "ANTIPHISHINGVPNGENERALSTATUS":
                {},
                "ROAMING":
                {
                    "false": 1
                },
                "LOSTMODEENABLED":
                {},
                "ANTIPHISHINGANALYTICSSTATUS":
                {}
            },
            "totalUnfilteredResultCount": 0
        }
    }
    """

    return json.loads(response)


@pytest.fixture
def get_user_profile_from_email():
    response = r"""
    {
        "errors": null,
        "result":
        {
            "totalCount": 1,
            "searchResults":
            [
                {
                    "id": 646053305,
                    "createdAt": "2021-10-06T12:35:24Z",
                    "displayName": "<displayName>",
                    "firstName": "<firstName>",
                    "lastName": "<lastName>",
                    "uid": "<uid>",
                    "emailAddress": "<emailAddress>",
                    "accountSource": "AAD",
                    "inviteState": "Completed",
                    "inviteResendCount": 0,
                    "accountType": "USER",
                    "enabled": true,
                    "locked": false,
                    "superUser": false,
                    "termsAccepted": false,
                    "bypassSaml": false,
                    "passwordExpiresAt": "2022-10-06T12:35:24Z",
                    "accountSettings": "null",
                    "mutable": true,
                    "loginFailureCount": 0,
                    "passwordHistory": "{}",
                    "androidWorkEmail": "<androidWorkEmail>",
                    "androidWorkUserStatus": "ENABLED",
                    "androidWorkRetryCount": 0,
                    "androidWorkDeviceAccountEnabled": false,
                    "idpUserDeleted": false,
                    "passwordNeverExpire": false,
                    "registrationPin":
                    {
                        "createdAt": null,
                        "expiresAt": null,
                        "pin": null,
                        "used": false,
                        "ppkgPinStatus": "NOT_GENERATED"
                    },
                    "groups":
                    [
                        "MDM all"
                    ],
                    "assignedConfigs":
                    [
                        {
                            "id": null,
                            "dmPartitionId": 111111,
                            "name": "Password rotation policy for Laptops",
                            "systemName": null,
                            "description": null,
                            "dmPartitionDistributionType": "NONE",
                            "policyType": "PASSCODE",
                            "policyRuleType": "NONE",
                            "uuid": null,
                            "enabled": false,
                            "priority": null,
                            "cloneable": false,
                            "configurationMutable": false,
                            "distributionMutable": false,
                            "priorityMutable": false,
                            "deletable": false,
                            "totalDeviceCount": 0,
                            "installedDeviceCount": 0,
                            "violationDeviceCount": 0,
                            "modifiedAt": null,
                            "modifiedBy": null,
                            "actions": null,
                            "cloneableAcrossSpace": false,
                            "clonedFromDefaultSpace": false,
                            "resourceSupport":
                            {
                                "links":
                                []
                            },
                            "systemDefault": false
                        }
                    ],
                    "deviceCount": 1
                }
            ],
            "offset": 0,
            "limit": 10,
            "queryTime": 125,
            "facetedResults":
            {
                "PASSWORDEXPIRATION":
                {
                    "false": 1,
                    "true": 0
                },
                "ACCOUNTSOURCE":
                {
                    "AAD": 1,
                    "LDAP": 0,
                    "ROSTER": 0,
                    "SALESFORCE": 0,
                    "SCIM_AAD": 0,
                    "LOCAL": 0,
                    "SCIM_OKTA": 0
                },
                "TERMSACCEPTED":
                {
                    "false": 1,
                    "true": 0
                },
                "INVITESTATE":
                {
                    "Completed": 1,
                    "Expired": 0,
                    "None": 0,
                    "Pending": 0
                },
                "ACCOUNTTYPE":
                {
                    "SUPPORT": 0,
                    "API": 0,
                    "PARTNER_USER": 0,
                    "USER": 1
                },
                "ANDROIDWORKSTATUS":
                {
                    "ENABLED": 1,
                    "ERROR": 0,
                    "NONE": 0,
                    "DELETED": 0
                },
                "ACCOUNTGROUP":
                {
                    "MDM all": 1
                }
            },
            "totalUnfilteredResultCount": 0
        }
    }
    """

    return json.loads(response)

@pytest.fixture
def get_user_profiles_bulk():
    response = r"""
    {
        "errors": null,
        "result":
        {
            "totalCount": 9586,
            "searchResults":
            [
                {
                    "id": 646053305,
                    "createdAt": "2021-10-06T12:35:24Z",
                    "displayName": "<displayName>",
                    "firstName": "<firstName>",
                    "lastName": "<lastName>",
                    "uid": "<uid>",
                    "emailAddress": "<emailAddress>",
                    "accountSource": "AAD",
                    "inviteState": "Completed",
                    "inviteResendCount": 0,
                    "accountType": "USER",
                    "enabled": true,
                    "locked": false,
                    "superUser": false,
                    "termsAccepted": false,
                    "bypassSaml": false,
                    "passwordExpiresAt": "2022-10-06T12:35:24Z",
                    "accountSettings": "null",
                    "mutable": true,
                    "loginFailureCount": 0,
                    "passwordHistory": "{}",
                    "androidWorkEmail": "<androidWorkEmail>",
                    "androidWorkUserStatus": "ENABLED",
                    "androidWorkRetryCount": 0,
                    "androidWorkDeviceAccountEnabled": false,
                    "idpUserDeleted": false,
                    "passwordNeverExpire": false,
                    "registrationPin":
                    {
                        "createdAt": null,
                        "expiresAt": null,
                        "pin": null,
                        "used": false,
                        "ppkgPinStatus": "NOT_GENERATED"
                    },
                    "groups":
                    [
                        "All Users"
                    ],
                    "deviceCount": 0
                }
            ],
            "offset": 0,
            "limit": 1,
            "queryTime": 231,
            "facetedResults":
            {
                "PASSWORDEXPIRATION":
                {
                    "true": 4,
                    "false": 9582
                },
                "ACCOUNTSOURCE":
                {
                    "AAD": 9548,
                    "LDAP": 0,
                    "ROSTER": 0,
                    "SALESFORCE": 0,
                    "SCIM_AAD": 0,
                    "LOCAL": 38,
                    "SCIM_OKTA": 0
                },
                "TERMSACCEPTED":
                {
                    "true": 68,
                    "false": 9518
                },
                "INVITESTATE":
                {
                    "Completed": 4750,
                    "Expired": 0,
                    "None": 2482,
                    "Pending": 2354
                },
                "ACCOUNTTYPE":
                {
                    "SUPPORT": 3,
                    "API": 2,
                    "PARTNER_USER": 0,
                    "USER": 9581
                },
                "ANDROIDWORKSTATUS":
                {
                    "ERROR": 2505,
                    "ENABLED": 7081,
                    "NONE": 0,
                    "DELETED": 0
                },
                "ACCOUNTGROUP":
                {
                    "MDM all": 5361,
                    "MDM Staff": 3638
                }
            },
            "totalUnfilteredResultCount": 0
        }
    }
    """

    return json.loads(response)
