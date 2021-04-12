class Plank
{
    constructor(x,y,w,h)
    {
        this.body = Bodies.rectangle(x,y,w,h);
        this.body.position.x = x;
        this.body.position.y = y;
        this.width = w;
        this.height = h;
    }

    display()
    {
        rectMode(CENTER);
        rect(this.body.position.x,this.body.position.y,this.width,this.height);
    }
}