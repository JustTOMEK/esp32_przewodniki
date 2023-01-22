#include <ArduinoBLE.h>

struct LocationData{
  BLEIntCharacteristic xCharacteristic, yCharacteristic;

  LocationData(int x, int y) :
    xCharacteristic(BLEIntCharacteristic("8eeec66e-71ce-11ed-a1eb-0242ac120002", BLERead | BLEBroadcast | BLEWrite)),
    yCharacteristic(BLEIntCharacteristic("74e7237c-71d0-11ed-a1eb-0242ac120002", BLERead | BLEBroadcast | BLEWrite)){
      xCharacteristic.setValue(x);
      yCharacteristic.setValue(y);
    }
};

LocationData location_data({{X}}, {{Y}});
BLEService locationSharingService("6951f9c0-2375-49f5-8da9-f45c9f067dcb");

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!BLE.begin()) {
    Serial.println("failed to initialize BLE!");
    while (1);
  }

  locationSharingService.addCharacteristic(location_data.xCharacteristic);
  locationSharingService.addCharacteristic(location_data.yCharacteristic);

  BLE.addService(locationSharingService);
  BLE.setAdvertisedService(locationSharingService);

  BLE.setDeviceName("LocationSharing");

  BLE.advertise();
  Serial.println("advertising ...");
}

void loop() {
  BLE.poll();
}
