class Ellipse extends Figure{
    constructor(canvas, x, y, filled = false, radiusX=0, radiusY=0) {
        super(canvas, x, y, filled, 'Ellipse');
        this.radX = radiusX;
        this.radY = radiusY;
    }

    draw() {
        this.ctx.beginPath();
        this.ctx.ellipse(
            this.startX + this.radX,
            this.startY + this.radY,
            Math.abs(this.radX),
            Math.abs(this.radY),
            0, 0, 2 * Math.PI);
        this.ctx.stroke();
        if(this.fill) {
            this.ctx.fill();
        }
        this.ctx.closePath();
    }

    redraw(x, y) {
        this.reset();
        this.radX = (x - this.startX) / 2;
        this.radY = (y - this.startY) / 2;
        this.draw();
    }

    get_json() {
        let res = super.get_json();
        res['type'] = 'Ellipse';
        res['radX'] = this.radX;
        res['radY'] = this.radY;
        return res;
    }
}