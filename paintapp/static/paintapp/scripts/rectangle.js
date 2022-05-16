class Rectangle extends Figure{
    constructor(canvas, x, y, filled = false, height=0, width=0) {
        super(canvas, x, y, filled);
        this.lenY = height;
        this.lenX = width;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.strokeRect(this.startX, this.startY, this.lenX, this.lenY);
        if (this.fill) {
            this.ctx.fillRect(this.startX, this.startY, this.lenX, this.lenY);
        }
        this.ctx.closePath();
    }

    redraw(new_x, new_y) {
        this.reset();
        this.lenX = new_x - this.startX;
        this.lenY = new_y - this.startY;
        this.draw();
    }

    get_json() {
        let res = super.get_json();
        res['type'] = 'Rectangle';
        res['height'] = this.lenY;
        res['width'] = this.lenX;
        return res;
    }
}