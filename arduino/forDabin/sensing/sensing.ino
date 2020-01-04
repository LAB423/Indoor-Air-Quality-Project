#include <AdafruitSensor.h>
#include <SoftwareSerial.h>        //RX, TX 통신 라이브러리 추가
#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT22 
DHT dht(DHTPIN, DHTTYPE);

SoftwareSerial Serial1(4,3);          //TX ,RX 핀을 4, 3번 핀으로 지정
int touchSensor = 5;                  // 터치센서 5번 핀으로 지정

char buf[50];
void setup() {

  Serial.begin(9600);   // 시리얼 통신을 시작, 통신 속도는 9600
  dht.begin();
  Serial1.begin(9600);        //RX, TX 통신 시작
  pinMode(touchSensor, INPUT);  //touchsenseor 통신 시작
}


void loop() {
 
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  int a1 = analogRead(A0);   // flame 1
  int a2 = analogRead(A1);   // flame 2                            
  
  int sensorValue;
  sensorValue=analogRead(A2);

  int touchValue = digitalRead(touchSensor); // touchsensor pin number = digit 2;
  
  float Vol, ppm;
  Vol=sensorValue*4.95/1023;
  ppm = map(Vol, 0, 4.95, 1, 50); // Concentration Range: 1~50 ppm 
  
  int count = 0;
  unsigned char c;
  unsigned char high;

  long pmcf10=0;
  long pmcf25=0;
  long pmcf100=0;

  long pmat10=0;
  long pmat25=0;
  long pmat100=0;

  
  
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");        //습도
  Serial.print(h);
  Serial.print(" % ");
  Serial.print(",");

  Serial.print("Temperature: ");     //온도
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(",");

  Serial.print("Flame1:");              //Flame 1
  Serial.print(a1);  
  Serial.print(" nm "); 
  Serial.print(",");            

  Serial.print("Flame2:");              //Flame 2
  Serial.print(a2);  
  Serial.print(" nm ");
  Serial.print(",");                                 

  Serial.print("Sensor Value: ");    //VOCs
  Serial.print(sensorValue);
  Serial.print(" voc ");
  Serial.print(",");

  Serial.print("Vol: ");
  Serial.print(Vol);
  Serial.print(" vol ");
  Serial.print(",");

  Serial.print("ppm: ");
  Serial.print(ppm);
  Serial.print(" ppm ");
  Serial.print(",");
    


 while (Serial1.available()) {               //FineDust

    c = Serial1.read();           //RX, TX 통신을 통한 값을 c로 저장

    if((count==0 && c!=0x42) || (count==1 && c!=0x4d)){

      Serial.println("check failed");
      break;

    }
    else if(count == 4 || count == 6 || count == 8 || count == 10 || count == 12 || count == 14) {

      high = c;
    }

    else if(count == 5){             //pm1.0의 수치값 계산

      pmcf10 = 256*high + c;

      Serial.print("PM 1.0: ");
      Serial.print(pmcf10);
      Serial.print(" ug/m3 ");
      Serial.print(",");

    }

    else if(count == 7){           //pm2.5의 수치값 계산

      pmcf25 = 256*high + c;

      Serial.print("PM 2.5: ");
      Serial.print(pmcf25);
      Serial.print(" ug/m3 ");
      Serial.print(",");
    }

    else if(count == 9){           //pm 10의 수치값 계산

      pmcf100 = 256*high + c;

      Serial.print("PM 10: ");
      Serial.print(pmcf100);
      Serial.print(" ug/m3 ");
      Serial.print(",");

    }

    count++;
 }

  while(Serial1.available()) Serial1.read();


  if (touchValue == HIGH){      // 터치됨
    Serial.print("touchSensor: ");
    Serial.print("1 touch");
    Serial.print(",");
  } 
  else {                      //터치 안됨
    Serial.print("touchSensor: ");
    Serial.print("0 touch");
    Serial.println(",");
  }

  delay(10000);     //10초
}

