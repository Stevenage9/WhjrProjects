class Ball
{
    constructor(x,y,radius)
    {   
        var options =
        {
            isStatic : false,
            'restitution' : 1,
            'density' : 0.8,
           'friction' : 0
        }

        this.body = Bodies.circle(x,y,radius,options)
        this.body.position.x = x;
        this.body.position.y = y;
        this.radius = radius;
        World.add(world, this.body);

       
    }

    display()
    {
        circle(this.body.position.x,this.body.position.y,this.radius);
    }
}