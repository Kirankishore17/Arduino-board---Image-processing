void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(7, OUTPUT);
  // Setting baudrate to 9600
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  if(Serial.available() > 0){
      String s = Serial.readString(); // for incoming serial data
      s.trim();
      if(s.equals("1")){
        Serial.println("Face present: " + s);
        digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(7, HIGH);
      }
      if(s.equals("0")){
        Serial.println("Face absent: " + s);
        digitalWrite(LED_BUILTIN, LOW);
        digitalWrite(7, HIGH);
      }
  }
  delay(2000);
}
