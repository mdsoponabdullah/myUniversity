/*
 * IoT Smart Irrigation System - Corrected Version
 * ESP8266 + ThingSpeak + Relay Control
 * Sensors: Soil Moisture + Temperature Only
 */

// Include required libraries
#include <ESP8266WiFi.h>
#include <ThingSpeak.h>
#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// WiFi credentials - REPLACE WITH YOUR ACTUAL CREDENTIALS
const char* ssid = "EEE lab";           // Replace with your WiFi name
const char* password = "soponabdullah";    // Replace with your WiFi password

// ThingSpeak settings - REPLACE WITH YOUR ACTUAL CREDENTIALS
unsigned long channelID = 3149661;              // Replace with your Channel ID
const char* writeAPIKey = "1RMGP8SWKKFB48VT"; // Replace with your Write API Key

// Pin definitions
#define MOISTURE_PIN A0      // Soil moisture sensor
#define DHT_PIN 14           // DHT sensor (D5)
#define RELAY_PIN 12         // Relay module (D6)
#define DHT_TYPE DHT22       // DHT11 or DHT22

// Sensor objects
DHT dht(DHT_PIN, DHT_TYPE);
WiFiClient client;
LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address - try 0x3F if 0x27 doesn't work

// Threshold values - CALIBRATE THESE FOR YOUR SOIL
const int DRY_SOIL_THRESHOLD = 700;  // Moisture value above this = dry soil
const int WET_SOIL_THRESHOLD = 400;  // Moisture value below this = wet soil

// Timing variables
unsigned long lastUpdate = 0;
const unsigned long updateInterval = 20000; // Update every 20 seconds

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  delay(100);
  
  Serial.println("\n\n=== IoT Smart Irrigation System ===");
  Serial.println("Initializing...");
  
  // Initialize pins
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); // Pump OFF initially
  
  // Initialize DHT sensor
  dht.begin();
  delay(1000); // Give sensor time to initialize
  
   // Initialize I2C manually for ESP8266
  Wire.begin(D2, D1);  // SDA = D2, SCL = D1
  delay(100);

  // Initialize LCD
  lcd.init();
  lcd.backlight();
  lcd.clear();
  delay(100);

  lcd.setCursor(0, 0);
  lcd.print("Smart Irrigation");
  lcd.setCursor(0, 1);
  lcd.print("Initializing...");
  
  delay(2000);
  
  // Connect to WiFi
  connectWiFi();
  
  // Initialize ThingSpeak
  ThingSpeak.begin(client);
  
  Serial.println("System initialization complete!");
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("System Ready");
  delay(2000);
}

void loop() {
  // Read sensors
  int moistureValue = readMoisture();
  float temperature = dht.readTemperature();
  
  // Check if temperature reading is valid
  if (isnan(temperature)) {
    Serial.println("ERROR: Failed to read from DHT sensor!");
    temperature = -99.9; // Error value
    // Try to reinitialize DHT sensor
    dht.begin();
  }
  
  // Display on Serial Monitor
  Serial.println("\n--- Sensor Readings ---");
  Serial.print("Moisture: "); Serial.println(moistureValue);
  Serial.print("Temperature: "); Serial.print(temperature); Serial.println(" °C");
  
  // Display on LCD
  displayLCD(moistureValue, temperature);
  
  // Control pump based on moisture (only if sensors are working)
  if (moistureValue > 0 && temperature != -99.9) {
    bool pumpStatus = controlPump(moistureValue);
    
    // Send data to ThingSpeak (every 20 seconds)
    if (millis() - lastUpdate >= updateInterval) {
      sendToThingSpeak(moistureValue, temperature, pumpStatus);
      lastUpdate = millis();
    }
  } else {
    Serial.println("ERROR: Sensor readings invalid, skipping pump control");
    digitalWrite(RELAY_PIN, LOW); // Ensure pump is OFF
  }
  
  delay(2000); // Wait 2 seconds before next reading
}

// Function to connect to WiFi
void connectWiFi() {
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  WiFi.mode(WIFI_STA);
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 30) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("\nWiFi Connected!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("\nWiFi Connection Failed!");
    Serial.println("Please check your credentials and try again.");
  }
}

// Function to read soil moisture
int readMoisture() {
  int total = 0;
  int validReadings = 0;
  
  // Take 10 readings and average, skip outliers
  for (int i = 0; i < 10; i++) {
    int reading = analogRead(MOISTURE_PIN);
    if (reading >= 0 && reading <= 1023) { // Valid ADC range
      total += reading;
      validReadings++;
    }
    delay(10);
  }
  
  if (validReadings == 0) {
    Serial.println("ERROR: No valid moisture readings!");
    return 0;
  }
  
  return total / validReadings;
}

// Function to control water pump
bool controlPump(int moisture) {
  static bool pumpState = false;
  
  if (moisture > DRY_SOIL_THRESHOLD) {
    // Soil is dry, turn pump ON
    digitalWrite(RELAY_PIN, HIGH);
    pumpState = true;
    Serial.println(">>> PUMP ON - Soil is DRY");
  } else if (moisture < WET_SOIL_THRESHOLD) {
    // Soil is wet enough, turn pump OFF
    digitalWrite(RELAY_PIN, LOW);
    pumpState = false;
    Serial.println(">>> PUMP OFF - Soil is WET");
  } else {
    // Maintain current state (hysteresis)
    Serial.println(pumpState ? "PUMP: ON (Maintaining)" : "PUMP: OFF (Maintaining)");
  }
  
  return pumpState;
}

// Function to display data on LCD
void displayLCD(int moisture, float temp) {
  lcd.clear();
  
  // Line 1: Moisture
  lcd.setCursor(0, 0);
  lcd.print("Mois:");
  lcd.print(moisture*100/1023);
    lcd.print("%");

  
  // Line 1: Temperature
  lcd.setCursor(8, 0);
  lcd.print("Tmp:");
  if (temp == -99.9) {
    lcd.print("ERR");
  } else {
    lcd.print((int)temp);
    lcd.print("C");
  }
  
  // Line 2: Pump Status
  lcd.setCursor(0, 1);
  if (digitalRead(RELAY_PIN) == HIGH) {
    lcd.print("PUMP: OFF ");
  } else {
    lcd.print("PUMP: ON");
  }
  
  // Line 2: WiFi Status
  lcd.setCursor(9, 1);
  if (WiFi.status() == WL_CONNECTED) {
    lcd.print("W:OK");
  } else {
    lcd.print("W:NO");
  }
}

// Function to send data to ThingSpeak
void sendToThingSpeak(int moisture, float temp, bool pump) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi not connected. Attempting to reconnect...");
    connectWiFi();
    if (WiFi.status() != WL_CONNECTED) {
      Serial.println("Failed to reconnect. Skipping ThingSpeak update.");
      return;
    }
  }
  
  // Set fields
  ThingSpeak.setField(1, moisture);
  ThingSpeak.setField(2, temp);
  ThingSpeak.setField(3, pump ? 1 : 0);
  
  // Write to ThingSpeak
  int response = ThingSpeak.writeFields(channelID, writeAPIKey);
  
  if (response == 200) {
    Serial.println("Data sent to ThingSpeak successfully!");
  } else {
    Serial.print("Error sending data to ThingSpeak. HTTP code: ");
    Serial.println(response);
  }
}