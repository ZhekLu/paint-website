class Rectangle extends Figure{
    constructor(canvas, x, y, filled = false, height=0, width=0) {
        super(canvas, x, y, filled);
        this.height = height;
        this.width = width;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.strokeRect(this.startX, this.startY, this.width, this.height);
        if (this.fill) {
            this.ctx.fillRect(this.startX, this.startY, this.width, this.height);
        }
        this.ctx.closePath();
    }

    redraw(new_x, new_y) {
        this.reset();
        this.width = new_x - this.startX;
        this.height = new_y - this.startY;
        this.draw();
    }
}