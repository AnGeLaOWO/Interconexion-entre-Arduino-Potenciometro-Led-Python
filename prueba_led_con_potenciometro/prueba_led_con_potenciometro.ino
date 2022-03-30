int led = 9;
int valor = 0;
int estado = 0;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  estado = analogRead(A0);
  if(estado < (1023/2)){
    digitalWrite(led, LOW);
    valor = map(estado,0,1023,0,100);
    float voltaje = estado * (5.0/1023.0);
    Serial.println(voltaje);
  }
  else{
    if((estado >= (1023/2)) && estado < 1023){
    valor = map(estado,0,1023,0,100);
    float voltaje = estado * (5.0/1023.0);
    digitalWrite(led, valor);
    Serial.println(voltaje);
    }
    else{
      valor = map(estado,0,1023,0,100);
      float voltaje = estado * (5.0/1023.0);
      digitalWrite(led, valor);
      Serial.println(voltaje);
      delay(10);
      digitalWrite(led, LOW);
    }
  }
  delay(100);
}
