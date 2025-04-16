float cf = 0.516; // calibration factor
int ffs1 = A0; // FlexiForce sensor is connected analog pin A0 of arduino or mega.
int ffsdata = 0;
float vout; // voltage represents force


void setup()
{
  Serial.begin(9600); // baud rate in bits per second
  pinMode(ffs1, INPUT); // pin name and status  
}


void loop()
{
  ffsdata = analogRead(ffs1);
  vout = (ffsdata * 5.0) / 1023.0; // translate voltage
  vout = vout * cf ; // calibrate the voltage output
  Serial.println(vout, 3);
  delay(100);
}
