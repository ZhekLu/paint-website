class Line extends Figure{
    constructor(canvas, x, y, endX=0, endY=0) {
        super(canvas, x, y, false);
        this.endX = endX;
        this.endY = endY;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.moveTo(this.startX, this.startY);
        this.ctx.lineTo(this.endX, this.endY);
        this.ctx.stroke();
        this.ctx.closePath();
    }

    redraw(x, y) {
        this.reset();
        this.endX = x;
        this.endY = y;
        this.draw();
    }
}