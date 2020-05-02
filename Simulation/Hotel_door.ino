
/*
    The circuit:
 * LCD RS pin to digital pin 12
 * LCD Enable pin to digital pin 11
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * LCD VSS pin to ground
 * LCD VCC pin to 5V
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)*/

#include <LiquidCrystal.h>
#include <Servo.h>


// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
Servo myservo; // create servo object to control a servo
int potpin = 0; // analog pin used to connect the potentiometer
int val; // variable to read the value from the analog pin
int pirPin = 6  ;       // PIR Out pin 
int pirStat = 0;   

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  myservo.attach(9);
  // Print a message to the LCD.
  pinMode(pirPin, INPUT);     
  Serial.begin(9600);
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  
  // print the number of seconds since reset:
 
  val = analogRead(potpin);
  pirStat = digitalRead(pirPin); 
  if (pirStat == HIGH)
  {
    lcd.setCursor(0, 1);
    lcd.print("access granted");
    val = map(val, 0, 1023, 0, 120);
   // scale it to use it with the servo (value between 0 and 180)
    myservo.write(val); // sets the servo position according to the scaled value
  }
  else
  {
    lcd.setCursor(0, 1);
    lcd.print("invalid       ");
    val = map(val, 0, 1023, 0, 0);
   // scale it to use it with the servo (value between 0 and 180)
    myservo.write(val); 
  }
}
 
