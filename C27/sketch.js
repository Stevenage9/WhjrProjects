const Constraint = Matter.Constraint;
const Engine = Matter.Engine;
const World = Matter.World;
const Bodies = Matter.Bodies;
const Body = Matter.Body;

function preload()
{
	
}

function setup() {
	createCanvas(800, 700);


	engine = Engine.create();
	world = engine.world;

	ball1 = new Ball(300,450,25);
	ball2 = new Ball(350,450,25);
	ball3 = new Ball(400,450,25);
	ball4 = new Ball(450,450,25);
	ball5 = new Ball(500,450,25);

	plank1 = new Plank(400,200,400,20);


	stringconstraint1 = new StringConstraint(ball1.body,{x:300, y:200});
	stringconstraint2 = new StringConstraint(ball2.body,{x:350, y:200});
	stringconstraint3 = new StringConstraint(ball3.body,{x:400, y:200});
	stringconstraint4 = new StringConstraint(ball4.body,{x:450, y:200});
	stringconstraint5 = new StringConstraint(ball5.body,{x:500, y:200});

	Engine.run(engine);
  
}


function draw() {
  rectMode(CENTER);
  //circMode(CENTER);
  background("white");

  stringconstraint1.display();
  stringconstraint2.display();
  stringconstraint3.display();
  stringconstraint4.display();
  stringconstraint5.display();

  ball1.display();
  ball2.display();
  ball3.display();
  ball4.display();
  ball5.display();

  plank1.display();
  drawSprites();
 
}

function keyPressed()
{
	if (keyCode === UP_ARROW)
	{
		Matter.Body.applyForce(ball1.body,ball1.body.position,{x:-50,y:-45});
	}
}



