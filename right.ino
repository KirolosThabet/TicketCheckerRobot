// This alternate version of the code does not require
// atomic.h. Instead, interrupts() and noInterrupts()
// are used. Please use this code if your
// platform does not support ATOMIC_BLOCK.
#include <ros.h>
#include <std_msgs/Float32.h>
ros::NodeHandle  nh;
float state=0;
// Pins
#define ENCA 3
#define ENCB 2
#define PWM 10
#define IN1 9
#define IN2 8

// globals
long prevT = 0;
int posPrev = 0;
// Use the "volatile" directive for variables
// used in an interrupt
volatile int pos_i = 0;
volatile float velocity_i = 0;
volatile long prevT_i = 0;

float v1Filt = 0;
float v1Prev = 0;
float v2Filt = 0;
float v2Prev = 0;
float eprev = 0;

float eintegral = 0;
void MotorState(const std_msgs::Float32 msg){
  state=msg.data;
}

ros::Subscriber<std_msgs::Float32> subscriber("/Motor/cmd",&MotorState);
void setup() {
  Serial.begin(9600);

  pinMode(ENCA, INPUT);
  pinMode(ENCB, INPUT);
  pinMode(PWM, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
nh.initNode();
nh.subscribe(subscriber);
  attachInterrupt(digitalPinToInterrupt(ENCA),readEncoder, RISING);

  delay(1350);
}

void loop() {
while(state ==00.0 || state==3.0)
{nh.spinOnce();}
  // read the position and velocity
  int pos = 0;
  float velocity2 = 0;
  noInterrupts();  // disable interrupts temporarily while reading
  pos = pos_i;
  velocity2 = velocity_i;
  interrupts();  // turn interrupts back on

  // Compute velocity with method 1
  long currT = micros();
  float deltaT = ((float)(currT - prevT)) / 1.0e6;
  float velocity1 = (pos - posPrev) / deltaT;
  posPrev = pos;
  prevT = currT;

  // Convert count/s to RPM
  float v1 = velocity1 / 374.0 * 60.0;
  float v2 = velocity2 / 374.0 * 60.0;

  // Low-pass filter (25 Hz cutoff)
  v1Filt = 0.854 * v1Filt + 0.0728 * v1 + 0.0728 * v1Prev;
  v1Prev = v1;
  v2Filt = 0.854 * v2Filt + 0.0728 * v2 + 0.0728 * v2Prev;
  v2Prev = v2;

  // Set a target
  float vt = 70;
  //  float vt = 100*(sin(currT/1e6)>0);

  // Compute the control signal u
  float kp = 2.18; //7.6  //6.4  //8.53            //2.6
  float ki = 0.312; //6.8  //0.312  //0.69
  float kd = 0; //26.3


  float e = (vt - v1Filt);
  eintegral = eintegral + e * deltaT;
  float dedt = (e - eprev) / deltaT;

  eprev = e;

  /* if (v1Filt<=75 && v1Filt>=65){
    v1Filt= 70;
    }*/

  float u = kp * e + ki * eintegral + dedt * kd;


  // Set the motor speed and direction
  int dir = 1;
  if (u < 0) {
    dir = -1;
  }
  int pwr = (int) fabs((u + 19.28) / 0.8209);

  if (pwr > 150) {
    pwr = 150;
  }



  setMotor(dir, pwr, PWM, IN1, IN2);

//  Serial.print(vt);
//  Serial.print(" ");
//  Serial.print(v1Filt);
//  Serial.println();
  delay(1);

nh.spinOnce();  
}

void setMotor(int dir, int pwmVal, int pwm, int in1, int in2) {
  analogWrite(pwm,  pwmVal);  // Motor speed
  if (dir == 1) {
    // Turn one way
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  } else if (dir == -1) {
    // Turn the other way
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  } else {
    // Or dont turn
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
  }
}

void readEncoder() {
  // Read encoder B when ENCA rises
  int b = digitalRead(ENCB);
  int increment = 0;
  if (b > 0) {
    // If B is high, increment forward
    increment = 1;
  } else {
    // Otherwise, increment backward
    increment = -1;
  }
  pos_i = pos_i + increment;

  // Compute velocity with method 2
  long currT = micros();
  float deltaT = ((float)(currT - prevT_i)) / 1.0e6;
  velocity_i = increment / deltaT;
  prevT_i = currT;
}
