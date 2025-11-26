/* Plant watering system with new Blynk update + I2C Fix */

#define BLYNK_TEMPLATE_ID   "TMPL6uDCkEtHt"
#define BLYNK_TEMPLATE_NAME "plant watering system"
#define BLYNK_AUTH_TOKEN    "XyNBHy_Bp2TWyPgcf2Sac_V0jZ2cUHoZ"

// Include the library files
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

// Initialize the LCD display (Change address if needed: 0x27 or 0x3F)
LiquidCrystal_I2C lcd(0x27, 16, 2);

char auth[] = BLYNK_AUTH_TOKEN;   // Blynk Auth token
char ssid[] = "blue_whale";       // WiFi name
char pass[] = "soponabdullah";    // WiFi password

BlynkTimer timer;
bool Relay = 0;

// Define component pins
#define sensor A0
#define waterPump D3

// Function declaration
void soilMoistureSensor();

void setup() {
  Serial.begin(9600);

  // Initialize I2C for ESP8266
  Wire.begin(D2, D1);  // SDA=D2, SCL=D1

  // Initialize LCD
  lcd.init();
  lcd.backlight();

  // Pump setup
  pinMode(waterPump, OUTPUT);
  digitalWrite(waterPump, HIGH); // Pump OFF initially (Relay is active LOW)

  // Connect to Blynk
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);

  // Loading animation
  lcd.setCursor(0, 0);
  lcd.print("System Loading");
  for (int a = 0; a <= 15; a++) {
    lcd.setCursor(a, 1);
    lcd.print(".");
    delay(200);
  }
  lcd.clear();

  // Call the soil moisture function every 1s
  timer.setInterval(1000L, soilMoistureSensor);
}

// Get the button value from Blynk app
BLYNK_WRITE(V1) {
  Relay = param.asInt();

  if (Relay == 1) {
    digitalWrite(waterPump, LOW);  // Relay ON
    lcd.setCursor(0, 1);
    lcd.print("Motor is ON ");
  } else {
    digitalWrite(waterPump, HIGH); // Relay OFF
    lcd.setCursor(0, 1);
    lcd.print("Motor is OFF");
  }
}

// Get the soil moisture values
void soilMoistureSensor() {
  int value = analogRead(sensor);                  // Raw value (0-1023)
  int percent = map(value, 0, 1023, 100, 0);       // Dry=0%, Wet=100%

  // Debugging on Serial
  Serial.print("Raw Value: ");
  Serial.print(value);
  Serial.print(" | Moisture: ");
  Serial.print(percent);
  Serial.println("%");

  // Send data to Blynk app
  Blynk.virtualWrite(V0, percent);

  // Show on LCD
  lcd.setCursor(0, 0);
  lcd.print("Moisture:");
  lcd.print(percent);
  lcd.print("%   "); // Extra spaces to clear old digits
}

void loop() {
  Blynk.run();  // Run the Blynk library
  timer.run();  // Run the Blynk timer
}
