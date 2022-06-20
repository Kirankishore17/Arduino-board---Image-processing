void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  // Setting baudrate to 9600
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  if(Serial.available() > 0){
      String s = Serial.readString(); // for incoming serial data
      Serial.println(s);
      digitalWrite(LED_BUILTIN, HIGH);
  }
}
