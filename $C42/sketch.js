
function setup() {
  createCanvas(400,400);
 // createSprite(400, 200, 50, 50);
 angleMode(DEGREES);
}

function draw() {
  background("black"); 
  translate(200,200);
  rotate(-90);
  
 var hr =  hour();
 var mn= minute();
 var sc= second();

  strokeWeight(8);
 stroke(244, 4, 0);
 noFill();
 var secondA = map(sc,0,60,0,360);
 arc(0,0,300,300,0,secondA);

 stroke(15, 245, 4);
 var minuteA = map(mn,0,60,0,360);
 arc(0,0,280,280,0,minuteA);

 stroke(13, 0, 227);
 var hourA = map(hr%12,0,12,0,360);
 arc(0,0,260,260,0,hourA);

 push();
 rotate(secondA);
 stroke(244, 4, 0);
 line(0,0,100,0);
 pop();

 push();
 rotate(minuteA);
 stroke(15, 245, 4);
 line(0,0,75,0);
 pop();

 push();
 rotate(hourA);
 stroke(13, 0, 227);
 line(0,0,50,0);
 pop();
 
 stroke(255);
 point(0,0)
 
  
  drawSprites();
}